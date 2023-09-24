from Busqueda import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import random


app = create_app('default')
app_context = app.app_context()
app_context.push()
api = Api(app)
api.init_app(app)
failsService = True

class VistaBusqueda(Resource):

    def get(self):

        random_fail = random.randint(0, 10)
        app.logger.info(random_fail)
        if failsService:
            if random_fail >= 9:
                return {
                    "result": "fallo en el proceso",
                }, 404
            else:
                return {
                    "result": "busqueda procesada",
                }, 200
        else:
            return {
                "result": "Busqueda procesada",
            }, 200


api.add_resource(VistaBusqueda, '/busquedaprocesada')
