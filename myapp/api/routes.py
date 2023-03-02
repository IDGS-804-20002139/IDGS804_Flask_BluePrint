#Aqui van todos las rutas para que el api funcione

from flask import Blueprint

api=Blueprint('api',__name__,url_prefix='/api')

@api.route("/getdata")
def getdat():
    return {'key':'value'}


