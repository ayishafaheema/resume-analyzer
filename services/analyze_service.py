from utils.skill_loader import load_skills

# Load skills once
SKILLS = load_skills()

def extract_skills_resume(resume_text):
    """
    Extract skills from CV text.
    Return a list of skills found in resume_text.
    """
    text = resume_text.lower()  # lowercase for matching

    # simple matching: if skill appears anywhere in text
    found_skills = [skill for skill in SKILLS if skill.lower() in text]

    # return sorted unique skills
    return sorted(set(found_skills))

def extract_skills_jd(jd_text):
    """
    Extract skills from CV text.
    Return a list of skills found in resume_text.
    """
    text = jd_text.lower()  # lowercase for matching

    # simple matching: if skill appears anywhere in text
    found_skills = [skill for skill in SKILLS if skill.lower() in text]

    # return sorted unique skills
    return sorted(set(found_skills))
