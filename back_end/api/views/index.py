from api.views import app_views

@app_views.route('/status')
def status():
    return '{ "status": "200" }'
