class Article:
    """ Article class to define Article Objects"""

    def __init__(self, source, author, title, description, url, image_url, publish_time):

        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url
        self.publish_time = publish_time

class Source:
    """ Source class to define source objects"""

    def __init__(self, id, name, description, url, category, country):

        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country