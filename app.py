from flask import  Flask
from routes.main_routes import main_bp
from routes.usuario_routes import user_bp


app = Flask(__name__)
app.secret_key = 'jhow'

# registrar os bluerprints
app.register_blueprint(main_bp)
app.register_blueprint(user_bp, url_prefix='/usuario')


if __name__ == '__main__':
    app.run(debug=True)