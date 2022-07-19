from scrap import getAlbumDetails
from flask import Flask
from flask_restful import Api, Resource, reqparse
import requests

class Album(Resource):
    def get(self,album):
        details= getAlbumDetails(album)
        return details


app= Flask(__name__)
api=Api(app)

api.add_resource(Album,"/albums/<string:album>")




if __name__== "__main__":
    app.run()

