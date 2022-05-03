from flask import render_template
from app import app
from .request import get_sources, get_article

@app.route('/')
def index():
    source = get_sources()
    title = "Home! Welcome to NewsSnooze"
    return render_template('index.html', title=title, sources=source)

@app.route('/article/<id>')
def article(id):
    
    
    articles = get_article(id)
    return render_template('article.html', articles=articles,id=id )
    