from extension import db

class Jd(db.Model):
    __tablename__="jd"

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    text=db.Column(db.Text,nullable=False)
    time=db.Column(db.DateTime,nullable=False)

    user = db.relationship("User", backref=db.backref("jds", lazy=True))










