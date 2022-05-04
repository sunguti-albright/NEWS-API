import urllib.request
import json
from .models import Article, Source
api_key = None
base_url = None


def configure_request(app):
    global api_key, base_url
    # Getting API key
    api_key = app.config['NEWS_API_KEY']

    # Getting the news base url
    base_url = app.config["NEWS_API_BASE_URL"]
    # print(base_url)


def get_articles(endpoint, category):
    """ 
    function that gets the headlines on request 
    """

    get_articles_url = base_url.format(endpoint, category, '', api_key)
    print(get_articles_url)
    # print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results(articles_results_list)

    return articles_results


def process_results(articles_list):
    """
    Function that processes api results and transforms them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain article details
    Returns:
        headlines_results: A list of headlines objects
    """
    article_results = []
    for article in articles_list:
        source = article.get('source')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        image_url = article.get('urlToImage')
        publish_time = article.get('publishedAt')

        article_object = Article(
            source, author, title, description, url, image_url, publish_time)
        article_results.append(article_object)

    return article_results


def get_sources(endpoint, category):
    """ 
    function that gets the sources on request 
    """

    get_sources_url = base_url.format(endpoint, category, '', api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        articles_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            articles_results = process_sources(sources_results_list)

    return articles_results


def process_sources(sources_list):
    """
    Function that processes api results and transforms them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain article details
    Returns:
        results: A list of headlines objects
    """
    source_results = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')

        source_object = Source(id, name, description, url, category, country)
        source_results.append(source_object)

    return source_results
   
