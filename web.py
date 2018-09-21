from flask import Flask, render_template, request, abort, send_file
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/projects')
def projects_page():
	return render_template('projects.html')

if __name__ == '__main__':
	app.run(debug=True)