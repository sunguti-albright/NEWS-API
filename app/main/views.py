from flask import render_template
# from app import app

from . import main
from ..requests import get_articles, get_sources
from ..models import Article, Source

@main.route('/')
def index():
    """ View root page function that returns the index page and it's data """

    # Getting popular headlines
    headlines = get_articles('top-headlines', 'business')
    all_sources = get_sources('sources', '')
    print(headlines)
    title = "Up to date news headlines"
    return render_template('index.html', title = title, headlines = headlines, all_sources = all_sources)