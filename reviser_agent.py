from crewai import Agent

reviser_agent = Agent(
    role="Editor",
    goal="Improve email",
    backstory="Fixes and improves email",
    verbose=True,
    allow_delegation=False
)