import numpy as np

from fit_predictor import load_fit_model, predict_fit_score

def recommend_jobs(jobs_df, user_skills, user_role):
    # Load the model
    model = load_fit_model()

    # Prepare the recommendations
    recommended_jobs = []
    for index, row in jobs_df.iterrows():
        title_match_score = 1 if user_role.lower() in row['job_title'].lower() else 0

        matched_skills = set(user_skills).intersection(set(row['skills'].split(',')))
        missing_skills = set(row['skills'].split(',')) - matched_skills
        
        fit_score = predict_fit_score(model, len(matched_skills), len(missing_skills), title_match_score)

        if fit_score > 0:  # Assuming fit_score should be greater than 0 to recommend
            recommended_jobs.append({
                'job_title': row['job_title'],
                'description': row['description_text'][:150] + '...',  # Minimized description
                'salary': row['salary_formatted'],
                'fit_score': fit_score,
                'matched_skills': ', '.join(matched_skills),
                'missing_skills': ', '.join(missing_skills)
            })

    # Sort jobs by fit score in descending order
    recommended_jobs = sorted(recommended_jobs, key=lambda x: x['fit_score'], reverse=True)

    return recommended_jobs


def predict_fit_score(model, matched_count, missing_count, title_match):
    features = np.array([[matched_count, missing_count, title_match]])
    return model.predict(features)[0]
