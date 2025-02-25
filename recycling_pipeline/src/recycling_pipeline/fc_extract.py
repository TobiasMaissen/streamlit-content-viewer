from firecrawl import FirecrawlApp
import json
from pathlib import Path
import re
from config import FIRECRAWL_API_KEY


def crawl_blog_posts(limit=5):
    app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
    
    # Crawle die Blogposts
    crawl_result = app.crawl_url(
        url='https://blog.dinotronic.ch',
        params={
            'limit': limit,
            'maxDepth': 3,  # Erhöht auf 3, um auch die Artikel von den Pagination-Seiten zu erreichen
            'includePaths': [
                "/*",
                "/page/*"  # Explizit die Pagination-Seiten einschließen
            ],
            'excludePaths': [
                "/kundenstimmen/*", 
                "/author/*", 
                "/en/*", 
                "/tag/*"
            ],
            'allowBackwardLinks': False,
            'allowExternalLinks': False,
            'scrapeOptions': {
                'formats': ['markdown'],
                'onlyMainContent': True,
            }
        }
    )
    
    # Speichere die kompletten Rohdaten als JSON
    raw_output_path = Path("firecrawl_output/raw_crawl_result.json")
    raw_output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(raw_output_path, 'w', encoding='utf-8') as f:
        json.dump(crawl_result, f, ensure_ascii=False, indent=2)
        
    return crawl_result


def extract_blog_posts(crawl_result):
    blog_posts = []
    seen_urls = set()  # Um Duplikate zu vermeiden
    
    # Speichere die kompletten Rohdaten als JSON
    raw_output_path = Path("firecrawl_output/raw_crawl_result.json")
    raw_output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(raw_output_path, 'w', encoding='utf-8') as f:
        json.dump(crawl_result, f, ensure_ascii=False, indent=2)
    
    for i, page in enumerate(crawl_result.get('data', [])):
        url = page.get('metadata', {}).get('url', '')
        
        # Überspringe Übersichtsseiten und Tag-Seiten
        if (url == 'https://blog.dinotronic.ch/' or 
            '/page/' in url or 
            '/tag/' in url):
            continue
            
        # Verhindere Duplikate
        if url in seen_urls:
            continue
        seen_urls.add(url)
            
        markdown_content = page.get('markdown', '')
        metadata = page.get('metadata', {})
        
        # Speichere den kompletten, unbearbeiteten Blogbeitrag als Markdown
        raw_output_path = Path("firecrawl_output/raw_posts")
        raw_output_path.mkdir(parents=True, exist_ok=True)
        
        # Nutze den Titel aus den Metadaten für den Dateinamen
        title = metadata.get('title', f'post_{i}')
        safe_title = re.sub(r'[^a-zA-Z0-9]', '_', title)
        
        # Speichere Rohdaten als Markdown
        with open(raw_output_path / f"{safe_title}.md", 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        # Extrahiere den Content bis zum Avatar-Bild
        content_parts = markdown_content.split('![avatar]')
        main_content = content_parts[0] if len(content_parts) > 0 else markdown_content
        
        # Extrahiere das Datum aus dem Markdown
        date_match = re.search(r'\] ([A-Z][a-z]+ \d+, \d{4} \d+:\d+:\d+ [AP]M)', markdown_content)
        
        blog_post = {
            "title": metadata.get('title', 'Unbekannter Titel'),
            "date": date_match.group(1) if date_match else 'Unbekanntes Datum',
            "content": main_content.strip(),
            "url": url
        }
        
        blog_posts.append(blog_post)
    
    # Speichere die extrahierten Blogposts als JSON
    output = {
        "blog_posts": blog_posts,
        "total_posts": len(blog_posts)
    }
    
    output_path = Path("firecrawl_output/blog_posts.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
        
    return output



if __name__ == "__main__":
    # Erst crawlen
    crawl_result_dinotronic = crawl_blog_posts(limit=300)

    # Dann extrahieren und als JSON speichern
    blog_posts = extract_blog_posts(crawl_result_dinotronic)
    print(f"Extrahierte {blog_posts['total_posts']} Blogposts")