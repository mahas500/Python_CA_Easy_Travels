import pymysql
from app import app
from dbconfig import mysql
from flask import jsonify
from flask import flash, request
from controller import EmployeeController
from controller import CustomerController
from controller import PackageController


if __name__ == "__main__":
    app.run()



