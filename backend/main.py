import pymysql
from app import app
from dbconfig import mysql
from flask import jsonify
from flask import flash, request
import user	
		
if __name__ == "__main__":
    app.run()