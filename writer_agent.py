import requests

def writer_agent(data):
    data = str(data)[:1000]

    prompt = f"""
Write a professional internship application email.

Use this data:
{data}

Keep it formal and short.
"""

    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    return res.json()["response"]