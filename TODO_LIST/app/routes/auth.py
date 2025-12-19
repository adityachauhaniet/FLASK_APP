from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash #importing password hashing functions
from app import db
from app.models import User
from app.forms import RegistrationForm, LoginForm


#ek blueprint object create krte hai for auth routes
auth_bp = Blueprint('auth', __name__) #name of the blueprint and module name
#------------------ASSIGNMENT: Create the features for that user can register with username, email and password, and Login by username ,password or by email,password, or by google account and can logout .----------------------------

# ------------------------------ Register Route -------------------------
@auth_bp.route('/register', methods=["POST", "GET"])
def register():
    #ager user already login h to usko direct tasks pe bhejdenghe
    if 'user_id' in session: 
        return redirect(url_for('tasks.view_tasks'))
    
    form = RegistrationForm()

    if form.validate_on_submit(): #method== POST + validation ok
        username = form.username.data
        email = form.email.data
        password = form.password.data

        #check if username ya email already exist
        existing_user_by_username = User.query.filter_by(username=username).first()
        existing_user_by_email = User.query.filter_by(email=email).first()

        if existing_user_by_username:
            flash("Username already taken, choose another one.", 'danger')
            return render_template('register.html', form=form)
        
        if existing_user_by_email:
            flash("Email already registered. Please login.", 'danger')
            return render_template('register.html', form=form) # yha per ko login.html page pe jna chaiyte tha?
        
        #Password hash karte hain
        hashed_password = generate_password_hash(password) #ye unique password dega

        #naya User object create karte hi9an
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration susccessgul! Please login now.", 'success')
        return redirect(url_for('auth.login'))
    
    #GET request ya validation error ke ;liye
    return render_template('register.html', form=form)



# ------------------------------ Login Route -------------------------

@auth_bp.route('/login', methods=["POST", "GET"])
def login():
    #ager user already logged in h
    if 'user_id' in session: #eska matlab user already login h
        return redirect(url_for('tasks.view_tasks'))
    
    form = LoginForm() #login form ko unherate kr lete hian

    if form.validate_on_submit(): #method = POST + validation okk then
        identifier = form.email_or_username.data # email ya username dono me se kuchh bhi
        password = form.password.data #form me se data read kr rhe hain

        #pahle email se search kr lete hain
        user = User.query.filter_by(email=identifier).first()
        #ager email se nhi mila to username se search lro
        if not user:
            user = User.query.filter_by(username=identifier).first()

        if user and check_password_hash(user.password, password): #user ka pass aur hashed pass dono match hon tabhi
            # Yahan DB user ka (id+username) session me daal dete hain
            session['user_id'] = user.id
            session['username'] = user.username # optional, displaye ke liye bus
            flash("Login successfull!", "success")
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash("Invalid email/password or password", "danger")
            

    return render_template('login.html', form=form) #ager ,match nhi hua to phir se login page pe bhej do




# ------------------------------ Logot Route -------------------------

@auth_bp.route('/logout')
def logout():
    # remove the user from the session for log them out
    session.pop('user_id', None) #ab logout ka flash message show karte hain
    session.pop('username', None)
    session.pop('user', None) #accrding to old code
    flash('You have been logged out', 'info') #flash message with category info
    #ab esko phir se login page pe redirect kra dete hain
    return redirect(url_for('auth.login')) #why auth.login--> because login route is in auth blueprint 

