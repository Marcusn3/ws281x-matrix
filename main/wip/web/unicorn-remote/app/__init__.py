from flask import Flask, request
from flask_restful import Api
import atexit

from app.state import state
from app.views import index
from app.api import SetProgram, StopProgram


def create_app():
    state.set_model()

    app = Flask(__name__)
    app.register_blueprint(index)

    app.config['ERROR_404_HELP'] = False

    api = Api(app)
    api.add_resource(SetProgram, '/api/program/<string:program>')
    api.add_resource(StopProgram, '/api/stop')

    atexit.register(state.stop_program)

    return app
