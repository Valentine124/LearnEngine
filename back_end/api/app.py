""" This module handles all API endpoints """


from models import storage
from api.views import app_views
from flask import Flask

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close():
    storage.close()

if __name__ = '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
