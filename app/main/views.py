from flask import render_template, request,redirect,url_for,abort 
from ..models import Post, User
from .. import db, photos
from .forms import UpdateProfile

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