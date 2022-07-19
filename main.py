from scrap import getAlbumDetails,getTrackDetails
from flask import Flask
from flask_restful import Api, Resource

class Album(Resource):
    def get(self,album):
        details= getAlbumDetails(album)
        return details

class Track(Resource):
    def get(self,track):
        details= getTrackDetails(track)
        return details

app= Flask(__name__)
api=Api(app)

api.add_resource(Album,"/albums/<string:album>")
api.add_resource(Track,"/tracks/<string:track>")

if __name__== "__main__":
    app.run()

