""" This module handles all API endpoints """


from models import storage
from flask import Flask, jsonify
from models.api_data import resource_data

app = Flask(__name__)

@app.route('/api/v1/resources/<title>', strict_slashes=True)
def resources(title):
    if storage.all_resources():
        # Read from database
        res = storage.all_resources()
        dict = {}

        for res_item in res.keys():
            if title.lower() in res_item.lower():
                dict[res_item] = res[res_item]
        if dict:
            # title has no match in db
            resource_data(title)
            res_2 = storage.all_resources()

            for res_item in res_2.keys():
                if title.lower() in res_item.lower():
                    dict[res_item] = res_2[res_item]
            if not dict:
                return '{ "error": "Topic not found" }'
            return jsonify(dict)
        return jsonify(dict)

    resource_data(title)
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
