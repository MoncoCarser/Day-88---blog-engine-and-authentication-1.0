from flask import Flask, redirect, render_template, session, request
from replit import db
import os

app = Flask(__name__)

def panties_for_yoshi():
    entry = ""
    f = open("./templates/template.html", "r")
    entry = f.read()
    f.close()
    keys = db.keys()
    keys = list(keys)
    content = ""
    for key in reversed(sorted(keys)):
        thisEntry = entry
        if key != "userid":
            thisEntry = thisEntry.replace("{title}", db[key]["title"])
            thisEntry = thisEntry.replace("{date}", db[key]["date"])
            thisEntry = thisEntry.replace("{body}", db[key]["body"])
            content += thisEntry
    return content

@app.route('/') 
def index():  
    page = ""
    f = open("./templates/mainpage.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{blog_printer}", panties_for_yoshi())
    return page


@app.route('/blog_writer') 
def blog_writer():  
    if request.headers["X-Replit-User-Id"] != db["userid"]:
        return redirect("/")
    return render_template("blogging.html")

@app.route('/log_in') 
def log_in():  
#to save userid on first usage in possible future version
#userid = request.headers["X-Replit-User-Id"]
# db["userid"] = userid
    if request.headers["X-Replit-User-Id"] == db["userid"]:
        return redirect("/blog_writer")
    return render_template("loggin.html")
    

@app.route("/blog_saved", methods=["POST"])
def blog_saved():
    form = request.form
    entry = {"title": form["blog_title"], "date" : form["date"], "body": form["blog_text"]}
    db[form["date"]] = entry
    return redirect("/blog_writer")


app.run(host='0.0.0.0', port=81)



