print("START")

from tools.tavily_tool import search_internships
from agents.writer_agent import writer_agent

print("IMPORTS DONE")

# STEP 1
listings = search_internships("AI internships India")
print("TAVILY OK")

# STEP 2 (VERY IMPORTANT)
listings = listings[:2]

print("GENERATING EMAIL...")

# STEP 3
email = writer_agent(listings)

# STEP 4
print("\nFINAL OUTPUT:\n")
print(email)