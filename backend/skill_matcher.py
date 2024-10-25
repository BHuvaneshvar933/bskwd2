def match_skills(user_skills, job_skills):
    """
    Compares user skills with job skills and returns matching skills and missing skills.
    """
    user_skills = {skill.strip().lower() for skill in user_skills}
    job_skills = {skill.strip().lower() for skill in job_skills.split(',')}
    
    matched_skills = user_skills.intersection(job_skills)
    missing_skills = job_skills - user_skills
    return matched_skills, missing_skills
