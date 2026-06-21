from flask import Flask
from api.routes.livro_routes import bp
from api.routes.usuario_routes import bp_usuario

app = Flask(__name__)

app.register_blueprint(bp)
app.register_blueprint(bp_usuario)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)