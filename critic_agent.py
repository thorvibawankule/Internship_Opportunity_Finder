from crewai import Agent

critic_agent = Agent(
    role="Reviewer",
    goal="Check email quality",
    backstory="Gives feedback on email",
    verbose=True,
    allow_delegation=False
)