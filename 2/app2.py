from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/submit', methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username == "aditya123" and password == "pass":
    #     return render_template("welcome.html", name=username)
    #ager credential ek se jyada hon tb
    #ek dictionary bna denge sabke, phir usme se match karayenge
    valid_users ={
        'admin':'123',
        'aditya123':'pass',
        'vishnu': 'lier'
    }
    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html", name=username)
    
    else:
        return "Invalid credential"


# @app.route('/form')
# def form():
#     return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)
