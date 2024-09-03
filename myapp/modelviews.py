from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, request
from wtforms.fields import PasswordField

# customize for user model

class UserAdminView (ModelView):

    # customize the displayed columns
    Column_list = ('full_name', 'email', 'subscription')
    # set columns that can be edited
    edit_rules = ('full_name', 'email', 'subscription')

    # Add password field as a hidden field

    form_extra_rules = {
        'password': PasswordField('password')
    }
     # Customize how the password field is saved
    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    
    # Restrict access to the view
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    # Redirect users who are not allowed access
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))
