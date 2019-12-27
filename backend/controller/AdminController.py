from app import app
from service import adminservice
from flask import jsonify
from flask import flash, request

		
adminserviceObj=adminservice.AdminService

@app.route('/adminlogin',methods=['POST'])
def index():
    print(request.json.get('name'))
    return "akjshajksh"