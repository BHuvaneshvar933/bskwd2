from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from data_loader import load_data
from recommender import recommend_jobs

app = Flask(__name__)
CORS(app)

# Load job data once when the server starts
jobs_df = load_data('./datasets/indeed.csv')

@app.route('/api/recommend-jobs', methods=['POST'])
def get_job_recommendations():
    data = request.json
    user_skills = data.get('skills', '').split(',')
    user_role = data.get('role', '')

    recommended_jobs = recommend_jobs(jobs_df, user_skills, user_role)
    
    # Convert DataFrame to list of dictionaries for JSON serialization
    results = recommended_jobs.to_dict('records')
    
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
