from flask import render_template,Blueprint,request,session,redirect,url_for
from services.analyze_service import extract_skills_resume
from services.analyze_service import extract_skills_jd
from datetime import datetime
from models.resume import Resume
from models.jd import Jd
from extension import db


analyze_bp=Blueprint("analyze",__name__)

@analyze_bp.route("/analyze-cv",methods=["POST"])
def analyze_cv():
        resume_text=request.form.get("resume_text")
        
        user_id = session.get("user_id")  # real user
        if not user_id:
            return redirect(url_for('auth.signin'))

        resume = Resume(
        user_id=user_id,
        text=resume_text,
        time=datetime.utcnow()
        )
        
        db.session.add(resume)
        db.session.commit()
        
        skills = extract_skills_resume(resume_text)

        return render_template(
        "upload_cv.html",
        skills=skills
        )
        
@analyze_bp.route("/analyze-jd",methods=["POST"])
def analyze_jd():
        jd_text=request.form.get("jd_text")
        
        user_id = session.get("user_id")  # real user
        if not user_id:
            return redirect(url_for('auth.signin'))

        jd = Jd(
        user_id=user_id,
        text=jd_text,
        time=datetime.utcnow()
        )
        
        db.session.add(jd)
        db.session.commit()
        
        skills = extract_skills_jd(jd_text)

        return render_template(
        "upload_jd.html",
        skills=skills
        )        


