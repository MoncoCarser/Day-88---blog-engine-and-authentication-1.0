# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*
```html
<html>
  <head>
    <title>My Website</title>
  </head>

  <body>
    <h1>Here's my site</h1>
    <p>Everyone can read this.</p>
</html>
```


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
  page += f"""<img src="{request.headers["X-Replit-User-Profile"]}" width="200">"""
  return page

app.run(host='0.0.0.0', port=81)
```

<details> <summary> 👀 Answer </summary>
The script and button code were missing from the HTML page.
  
```html
<html>
  <head>
    <title>My Website</title>
    <script src="https://replit.com/public/js/repl-auth-v2.js"></script>
  </head>

  <body>
    <h1>Here's my site</h1>
    <p>Everyone can read this.</p>
 
    <button onclick="LoginWithReplit()"> Login </button>
  </body>
</html>
```

In the Flask code, I had tried to access a dictionary key (in square brackets) that did not exist. It's `X-Replit-User-Profile-Image` not `X-Replit-User-Profile`.
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
  page += f"""<img src="{request.headers["X-Replit-User-Profile-Image"]}" width="200">"""
  return page

app.run(host='0.0.0.0', port=81)
```
</details>