# What is Flask?

Flask is a web (micro)framework based in python--ie you can make websites with it! It's relatively easy to use, and great for building small websites. Flask makes it easy to develop website and add common features like login or forms via integrations. This also imposes some limitations in terms of what you can do--it is pretty common to trade customizability for easy of use. That said, there's usually a way around these limitations, it just might not be the intended use case for flask.

Today you'll be building your own website!

If you want to see an example flask page, you can check out this [website](https://www.dayzerodiagnostics.com/) that I built this past summer.

# Setup

First, you'll need to install the python module for flask. You can do this in pip with
<br>
`pip install Flask`
<br>
Now clone this repo (or if you are reading this locally you can skip this step). We've made a small flask website here for you to play around with and so that we can explain many of the underlying concepts of flask. Now you're ready to run the flask application with
<br>
`FLASK_APP=web.py flask run`
<br>
Navigate to `localhost:5000` in a browser (just paste this into the URL bar) to see the website!

# Structure

## Architecture

Flask works on a system of HTML templates.

If you're interested in learning about the architectures for other common web frameworks, I would recommend learning about Django's MVT (Models, Views, and Templates) architecture.

## Jinja

Jinja is a template engine based in python, and it's what Flask uses for templating. One of the main features of templates is that they can be extended (if you've learned an object-oriented language, you could analogize this to inheritance between classes).

If you continue doing web development, you will almost certainly use Jinja or similar implementation of placeholders and templates. This is a common trend in programming--even accross different SDKs or frameworks, there will often be shared concepts!

## Debugging

Normally flask won't update the website when you change the code. You might wonder why this--you should ask yourself why you think this is?. However, you can change this by setting what are called environmental variables. These just tell flask what environment it should be run in (e.g. a development or debuggin one). If you paste this in before you run flask, then the site will automatically reload when you make changes, so you won't have to reboot the site every time.
<br>
```
export FLASK_DEBUG=1
```
<br>
You might notice some similarities between the `FLASK_ENV=development` and the initial code you used to run flask--`FLASK_APP=web.py`. This is because `FLASK_APP` is also an environmental variable! What environment do you think it is setting?
<br>
There are some files that if changed still require restarting the site--try to figure out which ones these are.

