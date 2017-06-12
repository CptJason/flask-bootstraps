def test_can_import_package():
    import flask_bootstraps


def test_can_initialize_app_and_extesion():
    from flask import Flask
    from flask_bootstraps import Bootstrap

    app = Flask(__name__)
    Bootstrap(app)
