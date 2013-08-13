
from flask import render_template, request
from app import app
from app.logic import generate_text

@app.route('/')
def index():
	context = {
		'troll_text': generate_text(),
	}
	return render_template('index.html', **context)

@app.route('/_get_text')
def get_troll_text():
	subject = request.args.get('subject')
	# Clean the string
	if isinstance(subject, basestring):
		subject = subject.strip()
		if len(subject) <= 0:
			subject = None
	return generate_text(subject)
