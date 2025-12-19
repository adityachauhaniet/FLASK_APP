from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key ="supersecrete" 


#homepage login page
@app.route("/", methods=["GET","POST"])
def login():
    if request.method== "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        #ager ye user admin hua to, user ka data session me save kr lenge
        if username == "admin" and password == "123":
            session["user"] = username #store in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentail. Try again", mimetype="text/plan")
    
    return '''
            <h2>Login Page</h2>
            <form method="POST">
            username: <input type="text" name="username"><br>
            password: <input type="text" name="password"><br>
            <input type="submit" value="login">
            </form> 
    '''
#welcomer page after login 
@app.route('/welcome')
def welcome():
    if "user" in session: #ager user session pape me aa gya h tb
        return f''' #f-->forword string
        <h2>Welcome, {session["user"]}!</h2>
        <a href={url_for('logout')}>Logout</a>

    '''
    return redirect(url_for("login")) #ager logout ho gye ho to wapas se login pe aa jao

#logout page
@app.route('/logout')
def logout(): # user key ko session me se remove karna padega
    session.pop("user",None) #None-->ager kuchh reson se session me nhi h to None error se bachayega
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)