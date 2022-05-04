from app import app
import urllib.request,json
from app.models.models import Source,Article


# Getting api key
apiKey = app.config['NEWS_API_KEY']

# Getting base url
base_url = app.config['NEWS_API_BASE_URL']

def get_sources():
    """
    A function that gets the json files from our url request
    """
    get_sources_url = base_url.format(apiKey)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results= None

        if get_sources_response["sources"]:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    """
    A function that processes the news sources results
   
    """
    source_results=[]
    for source_item in source_list:
        id = source_item.get("id")
        name = source_item.get("name")
        description = source_item.get("description")
        url = source_item.get("url")
        category = source_item.get("category")


        source_object = source.Source(id,name,description,url,category)
        source_results.append(source_object)

    return source_results


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
            article_objects = article.Article(author,title,description,url,urlToImage,publishedAt)
            article_source_results.append(article_objects)

    return 