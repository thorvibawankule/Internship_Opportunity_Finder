from crewai import Agent

listing_agent = Agent(
    role="Internship Finder",
    goal="Collect internship data",
    backstory="Fetches and passes internship listings",
    verbose=True,
    allow_delegation=False
)