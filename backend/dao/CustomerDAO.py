import uuid

import pymysql
from sqlalchemy.dialects.mssql.information_schema import columns
from sqlalchemy.engine import result

from dbconfig import mysql
from flask import jsonify
#from models.employee import Employee


class CustomerDAO:

    @classmethod