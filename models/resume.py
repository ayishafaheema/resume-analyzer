from extension import db

class Resume(db.Model):
    __tablename__="resume"

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    text=db.Column(db.Text,nullable=False)
    time=db.Column(db.DateTime,nullable=False)

    user = db.relationship("User", backref=db.backref("resumes", lazy=True))









