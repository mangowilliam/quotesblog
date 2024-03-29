import unittest

from app.user import Blog, Quote, User,Comment


class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote(1, 'mango', 'try me even now',
                               'http://quotes.stormconsultancy.co.uk/quotes/7')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote, Quote,))


class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password='banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)


class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.new_blog = Blog(1, "blog1", "power is power", "", 'come on')

    def test_password_setter(self):
        self.assertTrue(self.new_blog is not None)
        
class CommentsModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_comment = Comment(1, "blog1", "1", 'come all')

    def test_password_setter(self):
        self.assertTrue(self.new_comment is not None)

if __name__ == '__main__':
    unittest.main()
