from google import genai
from google.genai import Client
import streamlit as st
advisor = genai.Client(api_key="AIzaSyAWCq2P4YUFjQsBM2hgTF1_hEWG9nNBg74")
st.title("Your Personalized AI Career Advisor")
age = st.text_input("what is your age ?")
qualification = st.text_input("what is your qualification")
designation = st.text_input("what is your current designation")
salary = st.text_input("what is your current salary")
skills = st.text_input("what are your skills")
experience = st.text_input("Mention your past experience")
Interest = st.text_input("what are the fields you are interested in")
goals = st.text_input("what are your career goals")
location = st.text_input("what is your prefferred location")
language = st.text_input("what are the languages you know")
citizenship = st.text_input("what is your nationality")

prompt = f"""
You are an expert career advisor with 20+ years of experience helping professionals across different industries. 
Your role is to carefully analyze the user’s profile and provide practical, realistic, and actionable career advice.

User Profile:
- Age: {age}
- Qualification: {qualification}
- Current Designation: {designation}
- Skills: {skills}
- Work Experience: {experience}
- Interests: {Interest}
- Future Career Goals: {goals}
- Preferred Location: {location}
- Languages Spoken: {language}
- Nationality: {citizenship}

Instructions for your response:
1. Start with a short personalized career summary for the user.
2. Suggest 2–3 suitable career paths aligned with their skills, interests, and goals.
3. Recommend specific industries, roles, or companies in {location} (or globally if applicable).
4. Highlight skill gaps (if any) and suggest learning resources, certifications, or projects.
5. Provide networking, portfolio-building, and job-search strategies tailored to their profile.
6. End with a motivational note that encourages the user to take action.

Your advice should be clear, professional, and tailored specifically to the user’s profile.
"""


if st.button("SUBMIT"):
    response = advisor.models.generate_content(
        model="models/gemini-1.5-flash",
        contents=prompt,
    )
    st.write(response.text)
