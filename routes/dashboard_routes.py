from flask import Flask,render_template,Blueprint,request,redirect,url_for,flash,session


dash_bp=Blueprint("dash",__name__)

@dash_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.signin"))

    return render_template("dashboard.html")

@dash_bp.route("/upload-cv")
def upload_cv():
    if "user_id" not in session:
        return redirect(url_for("auth.signin"))

    return render_template("upload_cv.html")

@dash_bp.route("/upload-jd")
def upload_jd():
    if "user_id" not in session:
        return redirect(url_for("auth.signin"))

    return render_template("upload_jd.html")

@dash_bp.route("/analysis")
def analysis():
    if "user_id" not in session:
        return redirect(url_for("auth.signin"))

    return render_template("analysis.html")

@dash_bp.route("/settings")
def settings():
    if "user_id" not in session:
        return redirect(url_for("auth.signin"))

    return render_template("settings.html")


