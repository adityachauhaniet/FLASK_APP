from flask import Flask, render_template, redirect, request, url_for,flash
from forms import RegistrationForm #forms.py se RegistrationForm ko import ke lete hain(Basically property inherite kr rhe h)

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/", methods=["POST", "GET"])
def register():
    form = RegistrationForm() #Registration form ko call kr lete hian
#check kr lete hain ki form ke rgistration form store hua ki nhi, matlab submithua h ki nhi
    if form.validate_on_submit():
        #ager yes to form me se details read kr lenge
        name = form.name.data
        email = form.email.data
        #Jb ye ho jayega to ek flash msg show kara denge
        flash(f"Welcome {name}! You registered successully", "success") #success-->ye ek msg h
        #ab jb ye ho jayega esko success page pe leke jayenge
        return redirect( url_for("success")) #success-->ye success.html ka route name h
    #ab jb ye task complete ho jaye tb esko wapas se registration page pe bhej denge,
    #aur uspe form ko hi show karayenge
    return render_template("register.html", form = form)


#Route for success.html
@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)


    # 3:38:36