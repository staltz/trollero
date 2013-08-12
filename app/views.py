
from flask import render_template
from app import app
from app.logic import generate_response

@app.route('/')
def index():
	context = {
		'reply_text': generate_response(),
	}
	return render_template('index.html', **context)
