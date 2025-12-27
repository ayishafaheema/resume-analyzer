from extension import db

class Analysis(db.Model):
    __tablename__="analysis"

    id=db.Column(db.Integer,primary_key=True)
    resume_id=db.Column(db.Integer,db.ForeignKey("resume.id"),nullable=False)
    jd_id=db.Column(db.Integer,db.ForeignKey("jd.id"),nullable=False)
    matching_skill=db.Column(db.Text)
    missing_skill=db.Column(db.Text)
    fit_score=db.Column(db.Integer,nullable=False)
    time=db.Column(db.DateTime,nullable=False)

    resume = db.relationship("Resume", backref=db.backref("analyses", lazy=True))
    jd = db.relationship("Jd", backref=db.backref("analyses", lazy=True))

    __table_args__=(
    db.UniqueConstraint("resume_id","jd_id",name="unique_resume_jd",))


