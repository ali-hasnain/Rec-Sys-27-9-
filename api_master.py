import sql_update
import rec_int_ghn
from flask import Flask, request,jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)

class getRec(Resource):
    def get(self, User_Id ):
        return {'data': rec_int_ghn.recommend(User_Id)}
        #return jsonify(ghn_rec_collab.api_rec(userId))
        #return ghn.hybrid( userId)

class Upd(Resource):
    def get( self, personId,contentId,eventType ):
        sql_update.update_csv( personId,contentId,eventType )
        return {'data': 'SUCCESS'}
        #return jsonify(ghn_rec_collab.api_rec( userId))
        #return ghn.hybrid( userId)
        
api.add_resource(Upd, '/ghnupdate/<personId>/<contentId>/<eventType>')
api.add_resource(getRec, '/ghnrec/<User_Id>')

if __name__ == '__main__':
    app.run()
