from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()

"""Models for Blogly."""
default_img_url = "https://cdn.vectorstock.com/i/preview-1x/61/88/user-icon-human-person-symbol-avatar-login-sign-vector-28996188.jpg"

class User(db.Model):
    """User."""
    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key =True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                           nullable=False)
    last_name = db.Column(db.String(50),
                          nullable= True)
    image_url = db.Column(db.String,
                          nullable= False)
    def greet(self):
        return f"Hi My first_name is {self.first_name} and my last name is {self.last_name}"
    
    