# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## What's My Line?

👉 What's the problem here?


```html
<html>
  <head>
    <title>My Website</title>
  </head>


  <body>
    <h1>Here's my site</h1>
    <p>Everyone can read this.</p>
 
    <button onclick="LoginWithReplit()"> Login </button>
  </body>
</html>

```

<details> <summary> 👀 Answer </summary>
  
The `script` code **must** be included in every page where you want a login function.

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

</details>

