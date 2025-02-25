import json
import re
from crewai.flow.flow import Flow, start
from crews.content_crew.content_crew import BlogRewriterCrew
from tools.custom_tool import load_blog_posts, clean_blog_content, save_content
from dotenv import load_dotenv

load_dotenv()



class ContentFlow(Flow):
    def __init__(self):
        super().__init__()
        self.content_crew = BlogRewriterCrew()
        self.results = []

    @start()
    def process_blog_posts(self):
        json_path = "/Users/tobiasmaissen/Desktop/temp-streamlit-project/recycling_pipeline/src/recycling_pipeline/firecrawl_output/blog_posts.json"
        posts = load_blog_posts(json_path)
        
        for post in posts:
            cleaned_content = clean_blog_content(post['content'])
            
            actual_word_count = len(cleaned_content.split())
            actual_word_count = int(actual_word_count * 0.9)
            allowed_word_count = int(actual_word_count * 0.8)
            
            inputs = {
                'title': post['title'],
                'date': post['date'],
                'content': cleaned_content,
                'word_count': actual_word_count,
                'allowed_word_count': allowed_word_count,
                'url': post.get('url', '')
            }
            
            result = self.content_crew.crew().kickoff(inputs=inputs)
            
            blog_content = result.tasks_output[0].raw
            linkedin_content = result.tasks_output[1].raw if len(result.tasks_output) > 1 else None
            whitepaper_content = result.tasks_output[2].raw if len(result.tasks_output) > 2 else None
            
            content_post = {
                'title': post['title'],
                'date': post['date'],
                # Blog
                'content': blog_content,
                'original_word_count': actual_word_count,
                'allowed_word_count': allowed_word_count,
                'new_word_count': len(blog_content.split()),
                # LinkedIn
                'linkedin_content': linkedin_content,
                'linkedin_word_count': len(linkedin_content.split()) if linkedin_content else 0,
                # Whitepaper
                'whitepaper_content': whitepaper_content,
                'whitepaper_word_count': len(whitepaper_content.split()) if whitepaper_content else 0,
                # URL                
                'url': post.get('url', '')
            }
            self.results.append(content_post)

        save_content(self.results, "updated_content_flow.json")
        
        return self.results

def kickoff():
    content_flow = ContentFlow()
    content_flow.kickoff()  # Ruft automatisch process_blog_posts() auf
    
    print(f"\nBlog-Posts wurden in 'updated_content_flow.json' gespeichert.")


def plot():
    content_flow = ContentFlow()
    content_flow.plot()

if __name__ == "__main__":
    kickoff()
