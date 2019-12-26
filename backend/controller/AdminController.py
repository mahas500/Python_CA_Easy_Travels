from app import app
from models.Admin import Admin
from service import adminservice
from flask import jsonify
from flask import flash, request

from service.adminservice import AdminService

adminService = AdminService()


@app.route('/adminlogin', methods=['POST'])
def adminlogin():

    responseData = adminService.adminlogin(request.headers, request.json)
    return responseData
