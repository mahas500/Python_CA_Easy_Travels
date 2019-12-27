import uuid

import pymysql
from sqlalchemy.dialects.mssql.information_schema import columns
from sqlalchemy.engine import result

from dbconfig import mysql
from flask import jsonify
from models.employee import Employee


class EmployeeDAO:

    @classmethod
    def employeeLogin(cls, username, password):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM employee e where e.username = %s and e.password = %s",
                           (username, password))
            rows = cursor.fetchone()

            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def updateEmployeeSessionToken(cls, employeeId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sessionId = str(uuid.uuid4())

            cursor.execute("update employee e set session_id = %s where employee_id = %s ",
                           (sessionId, employeeId))
            conn.commit()
            cursor.execute("select * from employee e where e.employee_id = %s ",
                           employeeId)
            d = cursor.fetchone()

            return d
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getEmployeeFromSessionId(cls, sessionId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from employee e WHERE e.session_id = %s ",
                           sessionId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def checkIfEmployeeHasARole(cls, employeeId, roleId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("SELECT * from employee_role_mapping e WHERE e.employee_id = %s and e.role_id= %s",
                           (employeeId, int(roleId)))
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def assignRoleToEmployee(cls, employeeId, roleId):
        try:
            sessionId = str(uuid.uuid4())

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute("insert into employee_role_mapping (mapping_id, employee_id, role_id) value (%s, %s, %s)",
                           (sessionId, employeeId, int(roleId)))
            conn.commit()

            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
