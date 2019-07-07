from flask import render_template
from ..models import Post

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting posts from the different categories
    tech_posts = Post.get_posts('tech')
    entertainment_posts = Post.get_posts('entertainment')
    fashion_posts = Post.get_posts('fashion')
    automobiles_posts = Post.get_posts('automobiles')
    title = 'Home - Welcome to Blogout Online Website'
    
    return render_template('index.html', title = title, tech=tech_posts, entertainment=entertainment_posts, fashion=fashion_posts, automobiles=automobiles_posts)