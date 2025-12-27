import string
from lemmatization import lemmatize_text,similarity
from utils.skill_loader import load_skills


SKILLS = load_skills()

def analyze_resume(job_description,resume):
    
    lemmatized_job=lemmatize_text(job_description)
    lemmatized_resume=lemmatize_text(resume)

    job_words=[
        word.strip(string.punctuation).lower()
        for word in lemmatized_job.split()
    ]
    resume_words=[
        word.strip(string.punctuation).lower()
        for word in lemmatized_resume.split()
    ]

    stop_words={
        "a", "an", "the",
        "and", "or", "but", "so", "because", "although", "while",
        "to", "of", "in", "on", "at", "for", "with", "by", "from",
        "about", "into", "over", "after", "before", "between", "under", "without",
        "i", "me", "my", "we", "our", "you", "your", "he", "his",
        "she", "her", "it", "its", "they", "them", "their",
        "is", "am", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did",
        "can", "could", "may", "might", "must", "shall", "should", "will", "would",
        "this", "that", "these", "those", "there", "here",
        "such", "very", "more", "most", "less", "many", "much",
        "each", "every", "some", "any", "all",
        "responsible", "responsibilities", "experience", "experiences",
        "knowledge", "skills", "skill", "ability", "abilities",
        "role", "position", "candidate", "work", "working",
        "team", "company", "organization",
        "etc", "per", "via"
    }
    
    job_words=[w for w in job_words if w not in stop_words]
    resume_words=[w for w in resume_words if w not in stop_words]
    
    

    job_lines = {
        line.strip().lower()
        for line in job_description.splitlines()
        if line.strip()
    }

    resume_lines = {
        line.strip().lower()
        for line in resume.splitlines()
        if line.strip()
    }

    job_skills = [skill for skill in SKILLS if skill in job_lines]
    resume_skills = [skill for skill in SKILLS if skill in resume_lines]

    
    matches=set(job_skills)&set(resume_skills)
    
    threshold=0.60
    for jw in job_skills:
        for rw in resume_skills:
            if similarity(jw,rw)>=threshold:
                matches.add(jw)
                
                
    missing_words = set(job_skills) - matches
    
    return sorted(matches), sorted(missing_words)
            
                
                
