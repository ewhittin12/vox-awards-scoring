
import streamlit as st
import re
import math

st.title("VOX Awards Submission Scoring")

st.markdown("""
Paste the campaign text below. The algorithm will parse and score it based on:
- Research (20 pts)
- Planning (30 pts)
- Implementation (20 pts)
- Evaluation (20 pts)
- Creativity Bonus (10 pts)
""")

submission = st.text_area("Paste the campaign submission here:")
budget = st.number_input("Budget (USD)", min_value=0.0)
team_size = st.number_input("Team size", min_value=1, value=1)

if st.button("Score Submission"):
    def contains_keywords(text, keywords):
        return any(kw.lower() in text.lower() for kw in keywords)

    def count_smart_objectives(text):
        smart_patterns = [
            r"(?i)specific",
            r"(?i)measurable",
            r"(?i)attainable|achievable",
            r"(?i)relevant",
            r"(?i)time[- ]?bound"
        ]
        return sum(1 for pattern in smart_patterns if re.search(pattern, text))

    score = 0
    log = []

    # Research (20 pts)
    research_score = 0
    if contains_keywords(submission, ["research", "survey", "focus group", "secondary data"]):
        research_score += 10
        if contains_keywords(submission, ["primary research", "original research"]):
            research_score += 5
        if contains_keywords(submission, ["used to guide", "informed our plan"]):
            research_score += 5
    log.append(f"Research Score: {research_score}/20")

    # Planning (30 pts)
    planning_score = 0
    smart_score = count_smart_objectives(submission)
    if smart_score >= 3:
        planning_score += 15
    if contains_keywords(submission, ["budget", "$", "timeline"]):
        planning_score += 5
    if contains_keywords(submission, ["audience", "target group"]):
        planning_score += 5
    if contains_keywords(submission, ["goal", "objective"]):
        planning_score += 5
    log.append(f"Planning Score: {planning_score}/30")

    # Implementation (20 pts)
    implementation_score = 0
    if contains_keywords(submission, ["implemented", "executed", "launched", "carried out"]):
        implementation_score += 10
    if contains_keywords(submission, ["channels", "tactics", "activities"]):
        implementation_score += 5
    if contains_keywords(submission, ["adjusted", "adapted", "pivoted"]):
        implementation_score += 5
    log.append(f"Implementation Score: {implementation_score}/20")

    # Evaluation (20 pts)
    evaluation_score = 0
    if contains_keywords(submission, ["results", "measured", "outcomes", "evaluation"]):
        evaluation_score += 10
    if contains_keywords(submission, ["return on investment", "ROI", "impact"]):
        evaluation_score += 5
    if contains_keywords(submission, ["learned", "insights for next time"]):
        evaluation_score += 5
    log.append(f"Evaluation Score: {evaluation_score}/20")

    # Creativity Bonus (10 pts)
    creativity_score = 0
    if contains_keywords(submission, ["unexpected", "creative", "innovative", "surprise"]):
        creativity_score += 5
    if len(submission.split()) > 500 and not contains_keywords(submission, ["form letter"]):
        creativity_score += 5
    log.append(f"Creativity Score: {creativity_score}/10")

    # Normalize based on budget/team size
    base_score = research_score + planning_score + implementation_score + evaluation_score + creativity_score
    efficiency_factor = min(1.2, max(0.8, (5 / team_size) * (10000 / (budget + 1))))
    normalized_score = round(base_score * efficiency_factor, 2)

    st.markdown("## Score Summary")
    for line in log:
        st.write(line)
    st.write(f"Normalized Score (Adjusted for Budget and Team Size): **{normalized_score}/100**")
