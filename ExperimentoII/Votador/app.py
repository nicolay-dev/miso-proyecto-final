import sys
from urllib import response
import urllib3
import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

cors = CORS(app)

urlServiceTest = 'https://jsonplaceholder.typicode.com/todos/1'
# urlServiceOne = urlServiceTest
# urlServiceTwo = urlServiceTest
# urlServiceThree = urlServiceTest
urlServiceOne = 'http://127.0.0.1:8100/busquedaprocesada'
urlServiceTwo = 'http://127.0.0.1:8200/busquedaprocesada'
urlServiceThree = 'http://127.0.0.1:8300/busquedaprocesada'
retryHU = True
voteTactic = True
amountOfRetries = 7

@app.route('/sendBusqueda')
def sendBusquedaRequest():
    resStatus = 404
    count = 0
    if retryHU:
        while count <= 7 and resStatus == 404:
            count = count + 1
            processing = procesBusqueda()
            response = processing[0]
            resStatus = processing[1]
    else:
        processing = procesBusqueda()
        response = processing[0]
        resStatus = processing[1]

    return json.dumps(response), resStatus

def procesBusqueda():
    if voteTactic:
        response1 = sendBusqueda(urlServiceOne)
        response2 = sendBusqueda(urlServiceTwo)
        response3 = sendBusqueda(urlServiceThree)
    else:
        response1 = sendBusqueda(urlServiceOne)
        response2 = response1
        response3 = response1
    status = compareResult(response1, response2, response3)
    resStatus = 200

    if (status != 'ok'):
        if ((response3[1] == 404) & (response2[1] == 404) & (response1[1] == 404)):
            resStatus = 404
            response = buildResponse(status, '', '{} {} {}'.format(urlServiceOne, urlServiceTwo, urlServiceThree))
        if (response3[1] == response1[1] != response2[1]):
            response = buildResponse(status, response3[0], urlServiceTwo)
        if (response3[1] != response1[1] == response2[1]):
            response = buildResponse(status, response1[0], urlServiceThree)
        if (response1[1] != response3[1] == response2[1]):
            response = buildResponse(status, response2[0], urlServiceOne)
    else:
        response = buildResponse(status, response1, '') 
    return [response, resStatus]

def sendBusqueda(url):
    http = urllib3.PoolManager()
    req = http.request('GET', url)
    result = [json.loads(req.data), req.status]
    return result

def compareResult(data1, data2, data3):
    if (data1[1] == 200 and data2[1] == 200 and data3[1] == 200):
        status = 'ok'
    else:
        status = 'fail'
    return status

def buildResponse(status, data, serviceFail):
    response = {
        "status": status,
        "data": data,
        "serviceFail": 'none'
    }
    if (status != 'ok'):
        response['serviceFail'] = serviceFail
    return response