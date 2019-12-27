from app import app
from service import adminservice
from flask import jsonify
from flask import flash, request

from service.adminservice import AdminService

adminService = AdminService()


@app.route('/employeeLogin', methods=['POST'])
def employeeLogin():

    responseData = adminService.employeeLogin(request.headers, request.json)
    return responseData
