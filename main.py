from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG']=True  # displays runtime errors in the browser, too

@app.route("/validate", methods=["POST", "GET"])
def login():

    title = "Validation"
    title2 = "Welcome!"

    username = ""
    password = ""
    verify_password = ""
    email = ""
    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        verify_password = request.form["verify_password"]
        email = request.form["email"]
    
    
    if not username:
        username_error = "Please enter a username."
        username = ""
    
    for char in username:
        if char.isspace():
            username_error = "Username cannot contain a space."
            username = ""
        else:
            if (len(username) < 3) or (len(username) > 20):
                username_error = "Username needs to be at least 3 characters but less than 20 characters."
                username = ""

    if not password:
        password_error = "Please enter a password."
        password = ""
    else:
        for char in password:
            if char.isspace():
                password_error = "Password cannot contain a space."
                password = ""
            else:
                if (len(password) < 3) or (len(password) > 20):
                    password_error = "Password needs to be at least 3 characters but less than 20 characters."
                    password = ""

    if not verify_password:
        verify_password_error = "Please re-enter password."
        verify_password = ""
    else:
        if password != verify_password:
            verify_password_error = "Passwords do not match."
            verify_password = ""

     
    at_count = 0 
    period_count = 0   
    
    if email:
        for char in email:
            if char.isspace():
                email_error = "Email cannot contain a space."
                email = ""
            elif char == ("@"):
                at_count += 1
            elif char == ("."):
                period_count += 1
            elif (len(email) < 3) or (len(email) > 20):
                email_error = "Email needs to be at least 3 characters but less than 20 characters.."
                email = ""
    
        if at_count > 1:
            email_error = "Email must contain only 1 @ symbol."
            email = ""
        if at_count < 1:
            email_error = "Email must contain at least 1 @ symbol."
            email = ""

        if period_count > 1:
            email_error = "Email must contain only 1 dot(.)."
            email = ""
        if period_count < 1:
            email_error = "Email must contain at least 1 dot(.)."
            email = ""

    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template("welcome.html", title = title2, username = username)

    else:
        return render_template("index.html", 
            title = title, 
            username=username, 
            password=password, 
            verify_password=verify_password, 
            email=email, 
            username_error=username_error,
            password_error=password_error,
            verify_password_error=verify_password_error,
            email_error=email_error) 

@app.route("/")
def index():
    title = "User Signup"
    return render_template("index.html", title = title)
    

app.run()