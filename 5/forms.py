from flask_wtf import FlaskForm 
#FlaskForm -->Ye ek base calss hota h koi bhi form create karne ke liye use karte hain
#wtform ke features ko bhi import kr lete hain
from wtforms import StringField, PasswordField, SubmitField
#Form ke data ko validate karne ke liye validatorm bhi i,port kr lete hain
from wtforms.validators import DataRequired, Email, Length
#DataRequired-->Ye ensure karega ki input empty to nhi ja rha h na
#Email-->Ye ensure karega ki user ka email valid h ki nhi, like, @ symbol, .com, @gmail etc
#StringField-->Ye input text ke liye hota h, PasswordField-->Ye password ke liye hota h, SubmitField-->Ye Register karne ke liye hota h

#Ab ek registration form name se class create karte hain, aur usme FlaskForm ko import kar lete hain
#Means FlaskForm ki property ko inherite karenge usme
class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")

#StringFiled-->Input text ke liye like name, email
#Password-->YE password lene ke liye use karte hain
#SubmitField-->Eska use registration form ko submit karne ke liye karte hain
#DataRequired()-->Eska matlab ye box empty nhi hona chahiye
#Email()-->Ye email ko validate karega , ki wo valid h ki nhi
#Length(min=6)-->Eska matlab password ka length minimum 6 hona hi chahiye