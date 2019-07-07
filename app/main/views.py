from flask import render_template,request,redirect,url_for,abort
from . import main
from app.request import get_quote
from flask_login import login_required,login_user,logout_user,current_user
from ..user import User,Blog,Comment
from .forms import UpdateProfile,BlogForm
from .. import db,photos






@main.route('/', methods = ['GET','POST'])
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    title ='my blogquote'
    quote=get_quote()
    blog=Blog.query.all()
    return render_template('index.html',title=title,quote=quote,blog=blog)

@main.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_blogs():
    """
    view blog function to create a new blog
    """
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        title = blog_form.title.data
        content = blog_form.content.data
        print(current_user._get_current_object().id)
        new_blog = Blog(user_id = current_user._get_current_object().id, content=content, title=title)
       
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect(url_for('main.index'))

    return render_template('new_blog.html',  blog_form=blog_form)

@main.route('/user/<uname>')
@login_required
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