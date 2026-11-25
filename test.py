from src.tools.tools import web_search,scrape_url
from src.pipelines.pipline import run_research_pipeline

# output=web_search("what is the capital of france")


topic="the impact of AI on the job market in 2026"

run_research_pipeline(topic)

