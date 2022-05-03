from app import app
import urllib.request, json
from .models import sources
from .models import articles

Source = sources.Source
Article = articles.Article

#getting apiKey from config.py
apiKey = app.config['NEWS_API_KEY']
#getting base url from config.py
base_url = app.config['NEWS_BASE_URL']


#############SOURCES####################

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(apiKey)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
    source_results =None
    if get_sources_response["sources"]:
        source_results_list = get_sources_response["sources"]
        source_results = process_sources(source_results_list)
    return source_results

def process_sources(source_list):
    '''
    Function that processes the source results and turns them into a list of objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        
       
        source_object = Source(id,name,description,url,category)
        source_results.append(source_object)
    return source_results


#############ARTICLES####################
def get_article(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,apiKey)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(news):
    '''
    A function that processes the json files of news articles from api
    '''
    article_source_results = []
    for article in news:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get ('publishedAt')

        if url:
            article_objects = articles.Article(author,title,description,url,urlToImage,publishedAt)
            article_source_results.append(article_objects)

    return article_source_results

    
