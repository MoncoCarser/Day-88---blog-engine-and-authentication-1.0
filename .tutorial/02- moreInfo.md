# What's the Best Key?

User name might not be the best piece of info to use to identify a user because the user can change this. The thing that's unique that never changes is their **user ID** - this would be a good piece of info to use as a key because it's unique and permanent for every user.

We can also get information about:
- What teams a user belongs to.
- Roles (teacher, student, Replit staff etc)
- Profile pic

## Display The Pic

Yeah, that would be *great*, wouldn't it. Like a book of faces, a picture book, a face novel....Ok, I'll stop now.

Anyway, let's add the user's profile pic to the `hi` page:

👉 Here's the whole code:

```python
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  if request.headers["X-Replit-User-Name"]:
    return redirect("/hi")

  page = ""
  f = open("page.html", "r")
  page = f.read()
  f.close()
  return page

@app.route("/hi")
def hi():
  if not request.headers["X-Replit-User-Name"]:
    return redirect("/")
  
  page = ""
  page += f"""<h1>{request.headers["X-Replit-User-Name"]}</h1>"""

  ###### The new bit ##################
  page += f"""<img src="{request.headers["X-Replit-User-Profile-Image"]}" width="200">"""
  
  return page

app.run(host='0.0.0.0', port=81)
```

## Try it out!