import pandas as pd
import re

# Define a list of common skills to match within Job Descriptions
COMMON_SKILLS = [
    'python', 'machine learning', 'data analysis', 'sql', 'deep learning',
    'statistics', 'data visualization', 'nlp', 'big data', 'java', 'c++',
    'excel', 'r', 'cloud computing', 'data mining', 'tableau', 'power bi',
    'data engineering', 'pandas', 'numpy', 'tensorflow', 'keras'
]

def load_data(file_path):
    """
    Loads the job data from a CSV file and performs initial preprocessing.
    """
    jobs_df = pd.read_csv(file_path)
    jobs_df = jobs_df[['job_title', 'description_text', 'salary_formatted']]
    jobs_df.dropna(inplace=True)  # Drop rows with missing values
    
    # Extract skills from the Job Descriptions
    jobs_df['skills'] = jobs_df['description_text'].apply(extract_skills)
    return jobs_df

def extract_skills(description):
    """
    Extracts a list of common skills found in the Job Description.
    """
    description = description.lower()
    skills_found = [skill for skill in COMMON_SKILLS if re.search(r'\b' + skill + r'\b', description)]
    return ', '.join(skills_found) if skills_found else ''
