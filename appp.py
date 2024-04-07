from flask import Flask
from database import db
 
# Creating Flask App
app = Flask(__name__)
# Database Name
db_name = 'vehicle.db'
# Configuring SQLite Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
# Suppresses warning while tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialising SQLAlchemy with Flask App
db.init_app(app)


""" app.py file """

 
""" Creating Database with App Context"""
def create_db():
    with app.app_context():
        db.create_all()
 
if __name__ == "__main__":
    from models import Vehicle
    create_db()