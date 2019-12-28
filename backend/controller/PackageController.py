from app import app

from flask import flash, request

from service.PackageService import PackageService

packageService = PackageService()


@app.route('/createPackage', methods=['POST'])
def createPackage():
    print(request.json)
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = packageService.createPackage(request.headers, request.json)

    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1

    return wsResponse


@app.route('/getAllPackages', methods=['POST'])
def getAllPackages():
    print(request.json)
    wsResponse = {"resultSet": None, "operationStatus": None}
    responseData = packageService.getAllPackages(request.headers)

    wsResponse['resultSet'] = responseData
    wsResponse['operationStatus'] = 1

    return wsResponse
