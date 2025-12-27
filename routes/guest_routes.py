from flask import Flask,render_template,Blueprint,request,redirect,url_for,flash
from services import user_service
from services.guest_service import GuestResumeAnalyzer


guest_bp=Blueprint("guest",__name__)

@guest_bp.route("/guest",methods=["GET","POST"])
def guest_analyze():
    if request.method=="POST":
        job_description=request.form.get("job_description")
        resume=request.form.get("resume")
        
        job_file = request.files.get("job_file")
        resume_file = request.files.get("resume_file")
        
        analyzer=GuestResumeAnalyzer(
            job_description=job_description,
            resume=resume,
            job_file=job_file,
            resume_file=resume_file
        )
        
        result=analyzer.analyze()
        return render_template(
            "guest_result.html",
            result=result
        )
    return render_template("guest.html")    
        
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    