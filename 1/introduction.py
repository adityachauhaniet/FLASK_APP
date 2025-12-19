from flask import Flask,request #Flask package ko import kr rjhe hain

app = Flask(__name__)#HUmne ek object bnaya app name ka aur usme pass karenge name, ab ye objeck humari website ko rpresent karega,and
#__name__ --> ye humare flask ko btayega ki jis website per kaam kar rhe hain ye us website ka main file h 

#ab ek routescreate karenge decorator ki help se, jisase koi user aye to yha se ek home page show kara saken
@app.route("/")
def home():
    return "Hello Babe!"

@app.route('/register')
def register():
    return "Register here Babe."

@app.route('/login')
def login():
    return "Login here Babe."


#GET, POST Methods
@app.route('/submit', methods=["GET","POST"])
def submit():
    if request.method == "POST":
        return "You are sending the data."
    else:
        return "You are just viewing the form"


if __name__ == '__main__':
   app.run(debug=True)