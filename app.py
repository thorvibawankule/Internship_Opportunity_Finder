import streamlit as st

from tools.tavily_tool import search_internships
from agents.judge_agent import judge_internships

st.set_page_config(page_title="AI Internship Finder", layout="centered")

st.title("🤖 AI Internship Opportunity Finder")

query = st.text_input("Search internships", "AI internships India")

if st.button("Find & Rank Opportunities"):

    # STEP 1: SEARCH
    with st.spinner("Searching internships..."):
        listings = search_internships(query)

    listings = listings[:5]

    st.success("Internships fetched!")

    # STEP 2: LLM JUDGE
    with st.spinner("LLM-as-a-Judge evaluating internships..."):
        ranked_listings = judge_internships(listings)

    st.success("AI Ranking completed!")

    # STEP 3: SHOW RESULTS
    st.subheader("🏆 Ranked Internship Opportunities")

    for i, job in enumerate(ranked_listings):

        st.markdown("---")

        st.write(f"### {i+1}. {job.get('title', 'No Title')}")

        st.write("🔗 Link:", job.get("url", "No URL"))

        st.write("📄 Description:")
        st.write(job.get("content", "")[:300] + "...")

        # ⭐ SCORE (if available)
        if "score" in job:
            st.write("⭐ AI Score:", job["score"])

        # 🤖 LLM-AS-A-JUDGE OUTPUT (IMPORTANT PART)
        st.markdown("### 🤖 LLM-as-a-Judge Evaluation")

        st.info(job.get("llm_judge_output", "No LLM output"))