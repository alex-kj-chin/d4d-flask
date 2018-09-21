# What is Flask?

Flask is a web framework based in python--ie you can make websites with it! It's relatively easy to use (compared to a web framework like Django), and great for building small websites. Today you'll be building your own website!

If you want to see an example flask page, you can check out this [website](https://www.dayzerodiagnostics.com/) that I built this past summer.

# Setup

First, you'll need to install the python module for flask. You can do this in pip with
<br>
```pip install Flask```

Now clone this repo (or if you are reading this locally you can skip this step). We've made a small flask website here for you to play around with and so that we can explain many of the underlying concepts of flask. Now you're ready to run the flask application with

```FLASK_APP=hello.py flask run```

Navigate to `localhost:5000` in a browser (just paste this into the URL bar) to see the website!

# Structure

Flask works on a system of templates.