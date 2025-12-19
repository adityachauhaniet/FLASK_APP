# Mannual Form Handling Via Flask
from flask import Flask, render_template,request,redirect,flash,url_for

app = Flask(__name__)
#flask session ke liye secrete key bnana padeag
app.secret_key = "my-secrete-key"

#home page pe hi form bna dete hain
@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "POST": #tabhi hum name lenge
        name = request.form.get("name")
        if not name:
            flash("Name cannot be empty!")
            #esko pgir se form pe hi redirect kr denge
            return redirect( url_for("form")) #dosare page pe leke jana h,to bus name likhna padeag, BUT ager external site pe jana h to esme pura https adress ayega
        #ager name mil gya ho to
        flash(f"Thankyou { name }, your feedback was successfully saved")
        #ab esko thankyou wale html page pe redirect kara denge
        return redirect(url_for("thankyou")) #koi task complete hone per, new page pe jane ke liye redirect use karte hain, aur esme route name pass karte hain
    #ager ye sb complete ho gya ya nhi to wapas se form bhar sake eske liye wapas form pe jan padega
    return render_template("form.html") #task complete hone per same route pe leke jana h,url pass kar sakte hain
#thankyou wala bhi route bna lete hain
@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


# @app.route('/base')
# def base():
#     return render_template("base.html")

# @app.route('/feedback',methods=["POST","GET"])
# def feedback():
#     if request.method == "POST":
#         name = request.form.get("username")
#         message = request.form.get("message")
#         return render_template("thankyou.html", user=name, message=message)
    
#     return render_template("feedback.html")




if __name__ == '__main__':
    app.run(debug=True)

# 3:11:07