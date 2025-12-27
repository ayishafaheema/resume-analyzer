from flask import Flask,render_template
from extension import db
from routes.auth_routes import auth_bp 
from routes.guest_routes import guest_bp
import os
from routes.dashboard_routes import dash_bp
from routes.analyze_routes import analyze_bp 

app=Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))  # ensures project folder
db_path = os.path.join(basedir, "database.db")

app.secret_key = "my_super_secret_key_123"




app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


from models.user import User

app.register_blueprint(auth_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(dash_bp)
app.register_blueprint(analyze_bp)


with app.app_context():
    db.create_all()
    print("db.create_all() executed")

@app.route("/")
def welcome():
    return render_template("welcome.html")



if __name__=="__main__":
    app.run(debug=True, port=5013)
