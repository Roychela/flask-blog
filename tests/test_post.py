import unittest
from app.models import Post, User
from app import db

class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_post = Post(id=12,title='Hard work',post_content='Hard work pays off',post_category="interview pitch",user = self.user_James)
    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.id,12)
        self.assertEquals(self.new_post.title,'Hard work')
        self.assertEquals(self.new_post.post_content,'Hard work pays off')
        self.assertEquals(self.new_post.post_category,"interview pitch")
        self.assertEquals(self.new_post.user,self.user_James)
    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

    def test_get_post_by_id(self):
        self.new_post.save_post()
        got_post = Post.get_post(12)
        self.assertTrue(got_post is not None)
