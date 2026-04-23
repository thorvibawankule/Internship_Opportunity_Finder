import requests

def judge_internships(listings):
    results = []

    for job in listings:

        prompt = f"""
You are an LLM-as-a-Judge for internship quality.

Evaluate this internship strictly and return in this format:

Score: (0 to 10)
Reason: (1-2 lines why this score)

Internship:
Title: {job.get('title')}
Description: {job.get('content')}
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        output = response.json()["response"]

        job["llm_judge_output"] = output
        results.append(job)

    return results