import unittest
from models import articles
Article = articles.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''
    
    def setUp(self):
            '''
            Set up method that will run before every test   
            '''
            self.new_article = Article('Growing Religious Fervor on the Right and the Illusions Shattered by Putin’s War','Five articles from around The Times, narrated just for you','null','https://www.nytimes.com/2022/04/15/podcasts/religious-right-ukraine-war-narrated-articles.html','article_image')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()