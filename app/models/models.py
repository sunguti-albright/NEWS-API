class Source:
    """
    Source class to define source objects
    """

def __init__(self, id, title, description, url, category):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.category = category

class Article:
    """
    A class that generates new instances of news articles within news sources
    """
    
    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

