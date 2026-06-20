from flask import Flask
from api.routes.livro_routes import bp

app = Flask(__name__)

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)