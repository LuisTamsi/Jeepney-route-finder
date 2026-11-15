from flask import Flask
from get import bp as get_bp
from post import bp as post_bp
from put import bp as put_bp
from delete import bp as delete_bp

app = Flask(__name__)

app.register_blueprint(get_bp)
app.register_blueprint(post_bp)
app.register_blueprint(put_bp)
app.register_blueprint(delete_bp)
if __name__ == '__main__':
    app.run()
