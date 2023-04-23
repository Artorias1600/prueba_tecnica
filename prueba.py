from flask import Flask, request
from flask_restful import Resource, Api
import requests
app = Flask(__name__)
api = Api (app)

endpoint = "https://api.chucknorris.io/jokes/random"

class Endpoint(Resource):
    def get(self):
        resultados = []
        for _ in range(25):
            response = requests.get(endpoint)
            if response.status_code == 200:
                datos = response.json()
                id = datos['id']
                resultados.append(id)
            else:
                return{"error":"no hay datos"}, response.status_code
        return {"ids":resultados}

api.add_resource(Endpoint, "/resultado")

if __name__ == "__main__":
    app.run(debug=True)
