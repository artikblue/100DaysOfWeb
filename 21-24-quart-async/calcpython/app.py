import quart
from views import sw
from views import home
from config import settings
import services.starwars

app = quart.Quart(__name__)
is_debug = True

app.register_blueprint(home.blueprint)
app.register_blueprint(sw.blueprint)


def configure_app():
    mode = 'dev' if is_debug else 'prod'
    data = settings.load(mode)


def run_web_app():
    app.run(debug=is_debug, port=5001)


configure_app()

if __name__ == '__main__':
    run_web_app()
