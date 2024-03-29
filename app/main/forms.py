from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField('Blog Post Title',validators=[Required()])
    post = TextAreaField('Post:',validators = [Required()])
    category = SelectField('Type',choices=[('tech','Tech Blog Post'),('entertainment','Entertainment Blog Post'),('fashion','Fashion Blog Post'),('automobiles','Automobiles Blog Post')],validators=[Required()])
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')