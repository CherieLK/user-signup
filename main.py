from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route("/add", methods=['POST'])
def add_name():
    
    new_person_name = request.form['username']
    new_password = request.form['password']    
    verify_password = request.form['vpassword']
    new_email = request.form['oemail']

    username_error = ""
    password_error = ""
    vpassword_error = ""
    email_error = ""

    # if the user typed nothing at all
    if (not new_person_name) or (new_person_name.strip() == ""):
        username_error += "Please enter your name. "
        
    # field is too short or too long
    if len(new_person_name) < 3 or len(new_person_name) > 20:
        username_error += "Username has to be 3 to 20 characters. "
            
    # no space
    if ' ' in  new_person_name:
         username_error += "Username cannot have a space."
         
    # if the user typed nothing at all
    if (not new_password) or (new_password.strip() == ""):
            password_error += "Please enter a password. "
           
        
    # field is too short or too long
    if len(new_password) < 3 or len(new_password) > 20:
        password_error += "Password has to be 3 to 20 characters. "
        
    # no space
    if ' ' in  new_password:
        password_error += "Password cannot have a space."
        
    # passwords do not match
    if verify_password != new_password:
        password_error += "Passwords do not match."
        
    # field is too short or too long
    if new_email != "":
        if len(new_email) < 3 or len(new_email) > 20:
            email_error += "Email has to be 3 to 20 characters."
        
    # no space
    if new_email != "":
        if ' ' in new_email:
            email_error += "Email cannot have a space. "
            
    if new_email != "":
        app = "@"
        dot = "."
        if new_email.count(dot) > 1:
            email_error += "Email cannot have more than 1 dot or 1 @."


    if username_error == "" and password_error == "" and vpassword_error == "" and email_error == "":
        return render_template('welcome.html', username=new_person_name)
    else:
        return render_template('index.html', username_error=username_error, password_error=password_error, vpassword_error=vpassword_error,
         email_error=email_error)
            
    


if __name__ == "__main__":
    app.run()
