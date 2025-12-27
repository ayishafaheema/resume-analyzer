import os

def load_skills():
    """
    Reads skills from data/skills.txt and returns them as a Python set.
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    skill_file = os.path.join(base_dir,"skills.txt")

    skills = set()

    with open(skill_file, "r", encoding="utf-8") as f:
        for line in f:
            skill = line.strip().lower()
            if skill:
                skills.add(skill)

    return skills
