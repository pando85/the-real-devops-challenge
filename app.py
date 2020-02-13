from os import environ

from flask import Flask, jsonify
from flask_pymongo import PyMongo

from src.mongoflask import MongoJSONEncoder, ObjectIdConverter, find_restaurants


app = Flask(__name__)
app.config["MONGO_URI"] = environ.get("MONGO_URI")
app.json_encoder = MongoJSONEncoder
app.url_map.converters["objectid"] = ObjectIdConverter
mongo = PyMongo(app)


@app.route("/api/v1/restaurant")
def restaurants():
    restaurants = find_restaurants(mongo)
    return jsonify(restaurants)


@app.route("/api/v1/restaurant/<id>")
def restaurant(_id):
    restaurants = find_restaurants(mongo, _id)
    if len(restaurants) > 0:
        return jsonify(restaurants[0])
    return '', 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8080)
