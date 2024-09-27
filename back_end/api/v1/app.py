""" This module handles all API endpoints """


from models import storage
from flask import Flask, jsonify
from models.api_data import resource_data

app = Flask(__name__)

@app.route('/api/v1/resources/<title>', strict_slashes=True)
def resources(title):
    """ 
    Search the parameter in the databese and return
    a json string to the client.
    """

    # Call the function that request all the apis
    # and save the result to the database
    resource_data(title)
    # Get all resources from the database
    res = storage.all_resources()
    new_dict = {}

    for key in res.keys():
        if title.lower() in key.lower():
            new_dict[key] = res[key]

    return jsonify(new_dict)

@app.teardown_request
def close(exception):
    storage.close()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
