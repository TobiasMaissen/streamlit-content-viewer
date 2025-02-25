# src/blogRewriter/crew.py
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource


# Create a JSON knowledge source
json_seo = JSONKnowledgeSource(
    file_paths=["../knowledge/seo_output.json"]
)



@CrewBase
class BlogRewriterCrew():
    """Crew zum Neufassen von Blogbeiträgen."""

    @agent
    def blog_rewriter(self) -> Agent:
        """
        Definiert den Blog Rewriter-Agenten.
        Dieser Agent verwendet die Konfiguration aus agents.yaml und arbeitet im verbose-Modus,
        um detaillierte Logs zu liefern.
        """
        return Agent(
            config=self.agents_config['blog_rewriter'],
            verbose=True,
        )
        
    @agent
    def linkedin_post_creator(self) -> Agent:
        """
        Definiert den LinkedIn Post Creator-Agenten.
        Dieser Agent verwendet die Konfiguration aus agents.yaml und arbeitet im verbose-Modus,
        um detaillierte Logs zu liefern.
        """ 
        return Agent(
            config=self.agents_config['linkedin_post_creator'],
            verbose=True,
        )

    @agent
    def whitepaper_creator(self) -> Agent:
        """
        Definiert den Whitepaper Creator-Agenten.
        Dieser Agent verwendet die Konfiguration aus agents.yaml und arbeitet im verbose-Modus,
        um detaillierte Logs zu liefern.
        """
        return Agent(
            config=self.agents_config['whitepaper_creator'],
            verbose=True,
        )

    @task
    def rewrite_blog_task(self) -> Task:
        """
        Definiert die Rewrite-Task.
        Diese Task übernimmt den Input (den Originaltext) und fordert den Agenten auf,
        den Text neu zu verfassen, wie in der Beschreibung definiert.
        """
        return Task(
            config=self.tasks_config['rewrite_blog_task'],
            # Optional: output_file kann hier angegeben werden, wenn die Task direkt in eine Datei schreibt.
        )
    
    @task
    def create_linkedin_post_task(self) -> Task:
        """
        Definiert die Create LinkedIn Post-Task.
        Diese Task übernimmt den Input (den Originaltext) und fordert den Agenten auf,
        einen LinkedIn Post zu erstellen, wie in der Beschreibung definiert.    
        """
        return Task(
            config=self.tasks_config['create_linkedin_post_task'],
        )
    
    @task
    def create_whitepaper_task(self) -> Task:
        """
        Definiert die Create Whitepaper-Task.
        Diese Task übernimmt den Input (den Originaltext) und fordert den Agenten auf,
        ein Whitepaper zu erstellen, wie in der Beschreibung definiert.
        """
        return Task(
            config=self.tasks_config['create_whitepaper_task'],
        )
    
    @crew
    def crew(self) -> Crew:
        """
        Stellt die Crew zusammen, die automatisch alle mit @agent und @task dekorierten Methoden sammelt.
        Der hier definierte sequentielle Prozess sorgt dafür, dass die Task in der richtigen Reihenfolge
        ausgeführt wird.
        """
        return Crew(
            agents=self.agents,  # Automatisch durch den @agent-Dekorator
            tasks=self.tasks,    # Automatisch durch den @task-Dekorator
            process=Process.sequential,
            knowledge_sources=[json_seo],
            verbose=True,
        )
