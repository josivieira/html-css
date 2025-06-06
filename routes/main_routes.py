from flask import blueprint, render_template

main_bp = blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')


