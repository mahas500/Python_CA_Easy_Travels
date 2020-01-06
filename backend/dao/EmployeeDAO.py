import uuid

import pymysql
from sqlalchemy.dialects.mssql.information_schema import columns
from sqlalchemy.engine import result

from dbconfig import mysql
from flask import jsonify


class EmployeeDAO:

    @classmethod
    def employeeLogin(cls, username, password):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(
                "SELECT * FROM employee e LEFT JOIN employee_role_mapping erm on e.employee_id = erm.employee_id where e.username = %s and e.password = %s",
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
            cursor.execute(
                "select * from employee e LEFT JOIN employee_role_mapping erm on e.employee_id = erm.employee_id where e.employee_id = %s ",
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

    @classmethod
    def getAllEmployees(cls):
        try:
            sessionId = str(uuid.uuid4())

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "SELECT * from employee e LEFT JOIN employee_role_mapping erm on e.employee_id = erm.employee_id LEFT JOIN employee_role er on er.role_id=erm.role_id ORDER BY e.created_on DESC")
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def createEmployee(cls, employee_id, name, username, password, email, contact_no):
        try:
            sessionId = str(uuid.uuid4())

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                "insert into employee (employee_id,name ,username,password,email,contact_no) VALUES (%s, %s, %s, %s, %s, %s)",
                (employee_id, name, username, password, email, contact_no))
            conn.commit()

            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def searchEmployee(cls, searchText):
        try:
            sessionId = str(uuid.uuid4())

            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "SELECT * FROM employee WHERE MATCH (name, email) AGAINST ('*" + searchText + "*' IN BOOLEAN MODE) ORDER BY created_on"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def checkIfEmployeeExistWithEmailId(cls, emailId):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("Select * from employee e where e.email=%s", emailId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def updateOTP(cls, employeeId, OTP):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sessionId = str(uuid.uuid4())
            print("---------", OTP, employeeId)
            cursor.execute("update employee e set otp = %s where employee_id = %s ",
                           (OTP, employeeId))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def changePassword(cls, email_id, otp, password):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("update employee e set password = %s where email = %s and otp= %s ",
                           (password, email_id, otp))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
