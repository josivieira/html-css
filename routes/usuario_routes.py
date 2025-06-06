from flask import blueprint, render_template

user_bp = blueprint('user', __name__)


@user_bp.route('/login')
def login():
    return render_template('login.html')

@user_bp.route('/register')
def register():
    return render_template('register.html')
