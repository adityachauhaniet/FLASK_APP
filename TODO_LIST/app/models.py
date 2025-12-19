from app import db #importing the SQLAlchemy database instance(object of SQLAlchemy)
from datetime import datetime



# --------------------------------------- User Model ---------------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)#primary key column of user
    username = db.Column(db.String(50), nullable=False) #user ka username , duplicate ho skte hian
    email = db.Column(db.String(100), unique=True, nullable=False)#user ka email unique hona chahiye
    password = db.Column(db.String(100), nullable=False)#user ka password , hashed password

    #Relationship: Ek user ke multiple tasks ho sakte hain
    tasks = db.relationship('Task', backref='user', lazy=True)
    # 'Task' = related model ka naam
    # backref='user' => task.user se user object mil jayega


# --------------------------------------- Task Model ---------------------------------------

 #defining the User model(with the help of db.Model)

class Task(db.Model): #esase Task class table me convert ho jayega in database
    #ab hum table ke columns define karenge as class attributes
    id = db.Column(db.Integer, primary_key=True) #primary key column
    title = db.Column(db.String(50), nullable=True) #Task title column
    status = db.Column(db.String(20), nullable=False, default='Pending') #Task status column
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #Task creation timestamp column
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #Foreign key column to link task to a user

    # Foreign Key(Relationship): Ye user table ke id column ko point karega
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # user.id = 'user' table la 'id' column h
    # table ka naam by default jo class name hota h uska lower case hota h, User-->user.
