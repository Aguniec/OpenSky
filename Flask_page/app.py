from flask import Flask
from flask_restful import Api, Resource
import requests
import json
import sqlite3
import collections
from Flask_page import rest_api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        rest_api.input_data()
        return rest_api.make_country_dict()
        # print(resposne.json())
    #    print(dict(freq))
    #    for key, value in freq.items():
    #        print("{} : {}".format(key, value))
    #    return freq.items()

    #    data_to_database()
    # input_data()


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
