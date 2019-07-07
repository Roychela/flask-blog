import unittest
from app.models import Post, User, Comments
from app import db


class CommentsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Comments class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_James = User(
            username='James', password='potato', email='james@ms.com')
        self.new_post = Post(id=12,title='Hard work', post_content='Hard work pays off',
                               post_category="interview pitch", user=self.user_James)
        self.new_comment = Comments(
            id=15, comment='good work', user=self.user_James)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id, 15)
        self.assertEquals(self.new_comment.comment, 'good work')
        self.assertEquals(self.new_comment.user, self.user_James)
