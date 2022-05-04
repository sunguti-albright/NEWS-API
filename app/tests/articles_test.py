import unittest
from app.models.models import articles
Article = articles.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''
    
    def setUp(self):
            '''
            Set up method that will run before every test   
            '''
            self.new_article = Article("John Doe", "Match made in heaven", "The NBA all star game. The Grizzlies vs The Calves go head to head", "https://newsapi.org/register/success", "https://newsapi.org/register", "7th June")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()