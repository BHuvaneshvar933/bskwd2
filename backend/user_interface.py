def display_results(recommended_jobs):
    print("\nTop Job Recommendations:\n")
    for job in recommended_jobs:
        print(f"Job Title: {job['job_title']}")
        print(f"Description: {job['description']}")
        print(f"Salary: {job['salary']}")
        print(f"Fit Score: {job['fit_score']}")
        print(f"Matched Skills: {job['matched_skills']}")
        print(f"Missing Skills: {job['missing_skills']}\n")
