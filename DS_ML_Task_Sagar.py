# Solution to the DS/ML Intern Task by SAGAR PURSWANI(sagarpurswani0@gmail.com) for submission at ClassMent

# Basic Recommendation Engine Task
# Objective:
# Create a simple recommendation engine that, given a Data Science or ML job role, 
# recommends the three closest roles based on the similarity of required skills.

# Steps followed(Plan): -
# 1.Preparing Data: Define job roles and their required skills.
# 2.Convert to Vectors: Use a text-based similarity method.
# 3.Compute Similarity: Using cosine similarity.
# 4.Recommend Roles: Return top 3 similar roles.
# 5.Deliverables: A Python file and  Streamlit UI with a short explanation.

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1
roles = {
    "Data Scientist": ["Python", "Machine Learning", "Statistics", "Deep Learning"],
    "ML Engineer": ["Python", "TensorFlow", "Machine Learning", "Deployment"],
    "Data Analyst": ["SQL", "Excel", "Python", "Statistics"],
    "AI Researcher": ["Deep Learning", "NLP", "Computer Vision", "Python"],
    "Data Engineer": ["SQL", "Big Data", "Python", "ETL"],
}
df = pd.DataFrame(roles.items(), columns=["Job Role", "Skills"])
df["Skills"] = df["Skills"].apply(lambda x: " ".join(x))

# Step 2
vectorizer = CountVectorizer()
skill_matrix = vectorizer.fit_transform(df["Skills"])  

# Step 3
cosine_sim = cosine_similarity(skill_matrix)

# Step 4
def recommend_roles(job_role, df, sim_matrix):
    idx = df[df["Job Role"] == job_role].index[0]  
    sim_scores = list(enumerate(sim_matrix[idx]))  
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]  
    return [df["Job Role"][i] for i, _ in sim_scores]

# Testing for a sample input manually 

# input_role = "Data Scientist"
# recommendations = recommend_roles(input_role, df, cosine_sim)
# print(f"Recommended roles for {input_role}: {recommendations}")

# input_role = "Data Analyst"
# recommendations = recommend_roles(input_role, df, cosine_sim)
# print(f"Recommended roles for {input_role}: {recommendations}")

# Step 5
import streamlit as st

st.title("Job Role Recommendation Engine")
input_role = st.selectbox("Select a job role", df["Job Role"])
if st.button("Recommend"):
    recommendations = recommend_roles(input_role, df, cosine_sim)
    st.write(f"Top 3 similar roles: {', '.join(recommendations)}")
