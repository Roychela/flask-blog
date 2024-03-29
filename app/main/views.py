from flask import render_template, request,redirect,url_for,abort 
from ..models import Post, User, Comments
from . import main
from ..request import get_quote
from .. import db, photos
from .forms import UpdateProfile, PostForm, CommentsForm
from flask_login import login_required,current_user
from datetime import datetime


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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)  

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    

@main.route('/post/<int:id>', methods = ['GET','POST'])
def post(id):
    post = Post.get_post(id)
    posted = post.posted.strftime('%b %d, %Y')
    if request.args.get("upvote"):
        post.upvotes += 1

        db.session.add(post)
        db.session.commit()

        return redirect("/post/{post_id}".format(post_id=post.id)) 

    elif request.args.get("downvote"):
        post.downvotes+=1

        db.session.add(post)
        db.session.commit()

        return redirect("/post/{post_id}".format(post_id=post.id))

    comment_form = CommentsForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comments(comment = comment,user = current_user,post_id = post)

        new_comment.save_comment()
    comments = Comments.get_comments(post)

    return render_template("post.html", post = post, comment_form = comment_form, comments = comments, date = posted)   
@main.route('/post/new/', methods = ['GET','POST'])
@login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data 
        post = form.post.data
        category = form.category.data
        new_post = Post(title = title,post_content=post,post_category=category,user=current_user, upvotes=0, downvotes=0)
        new_post.save_post()
        return redirect(url_for('.index'))

    title = 'Flask Blog Post'
    return render_template('new_post.html',title = title, post_form=form)

@main.route('/user/<uname>/posts')
def user_profile_posts(uname):
    user = User.query.filter_by(username=uname).first()
    posts = Post.query.filter_by(user_id = user.id).all()

    return render_template("profile/posts.html", user=user,posts=posts)

@main.route("/post/<int:id>/update", methods=['GET', 'POST'])
@login_required
def update_post(id):
    post = Post.get_post(id)
    if post.user != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.post_category = form.category.data
        post.post_content = form.post.data
        db.session.commit()
        #flash('Your post has been updated!', 'success')
        return redirect(url_for('.post',id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.category.data = post.post_category
        form.post.data = post.post_content
    return render_template('new_post.html', title='Update Post',
                           post_form=form, legend='Update Post')


@main.route("/post/<int:id>/delete", methods=['POST'])
@login_required
def delete_post(id):
    post = Post.get_post(id)
    if post.user != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    #flash('Your post has been deleted!', 'success')
    return redirect(url_for('.index'))


@main.route('/quote/')
def quote():

    '''
    View function for random quote
    '''
    quote = get_quote()
    return render_template('quote.html',quote = quote)  