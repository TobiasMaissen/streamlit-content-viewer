import os
from dotenv import load_dotenv

# Lade .env nur in Entwicklung
if not os.environ.get("K_SERVICE"):
    load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')
LANGTRACE_API_KEY = os.getenv('LANGTRACE_API_KEY')