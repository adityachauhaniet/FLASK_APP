from flask import Flask
from routes.auth import auth_bp#login blueprint

def create_app():
    app = Flask(__name__)

    app.secret_key = "my-secret-key"

    app.register_blueprint(auth_bp)

    return app

# create_app():-->Ye function app ko create karega, aur jb bhi hume new app ki need padegi hum bus simply es function
# ko call kr denge.Ye app bna ke de dega.
# return app-->Yeapp ko chala dega
# app.secrete_key-->ager hum session,flash use karte hain yo eski need padegi
# app.register_blueprint(auth_bp)-->ye line humare login blueprint ko main app se connect kr degi.

# __init__.py-->Es line me humne app ka initialization code likha hai.Es line me humne Flask app create kiya hai,uske
# bad secret key set kiya hai,aur finally login blueprint ko register kiya hai.   
# #Note:Blueprints Flask me ek tarah ka component hota hai jo humare application ke different functionalities ko
# modularize krne me help krta hai.
# #Isse hum apne application ko chote-chote parts me divide kr sakte hain,jise alag-alag files me rakh sakte hain,
# aur fir unhe main application me import kr sakte hain.
# #Isse humare code ka structure better hota hai,aur maintain krna bhi easy ho jata hai.
# #Yahan humne auth blueprint ko import kiya hai jo routes/auth.py file me defined hai,aur fir usse main app me register
# kiya hai. 
# #Isse humare application me authentication related routes aur functionalities add ho jayengi.
# #Jab bhi hum create_app function ko call karenge,ye ek naya Flask app create karega,jisme authentication
# functionalities included hongi.
# #Is tarah se hum apne Flask application ko modular aur organized bana sakte hain.
# Es line ka matlbab file tabhi chalegi jb ye file directly run(execute) ki jayegi na ki import ki jayegi.