from crewai import Agent

shortlist_agent = Agent(
    role="Shortlister",
    goal="Select best internships",
    backstory="Filters relevant internships",
    verbose=True,
    allow_delegation=False
)