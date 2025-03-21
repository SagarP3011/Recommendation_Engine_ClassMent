# Recommendation_Engine_ClassMent

## Overview  
This project recommends similar job roles based on skill similarity. It uses a predefined dataset of job roles and required skills, computes similarity using cosine similarity, and suggests the top 3 most relevant roles.  

## Approach  
1. **Data Representation:**  
   - Job roles and their required skills are stored in a dictionary.  
   - Skills are converted into feature vectors using CountVectorizer.  
   
2. **Similarity Calculation:**  
   - Cosine similarity is used to measure the closeness between roles.  
   - The top 3 most similar job roles are recommended.  

3. **Implementation:**  
   - The project is implemented as a **Streamlit app** for an interactive UI.  
   - The UI allows users to select a job role and get recommendations instantly.  

## Why Cosine Similarity?  
- Handles text-based data efficiently.  
- Works well for high-dimensional representations.  
- Captures relationships between skills more effectively than Jaccard similarity.

## Screenshots  
- Includes Screen Shots to demonstrate the Streamlit UI made for the task.
 
