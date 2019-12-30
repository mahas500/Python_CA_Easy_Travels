import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ServerendpointsService {

  constructor() { }

  SERVERURL="http://localhost:5000/";

  employeeLogin= "employeeLogin";
  customerLogin="customerLogin";
  createEmployee="createEmployee";


  OPERATION_SUCESSESULL = 1


  //localstorage variables
  LOGGED_IN_EMPLOYEE_SEESION_ID="LOGGED_IN_EMPLOYEE_SEESION_ID";
  LOGGED_IN_EMPLOYEE_ID="LOGGED_IN_EMPLOYEE_ID";
  LOGGED_IN_EMPLOYEE_NAME="LOGGED_IN_EMPLOYEE_NAME";
  LOGGED_IN_EMPLOYEE_ROLE="LOGGED_IN_EMPLOYEE_ROLE";
  LOGGED_IN_CUSTOMER_SEESION_ID="LOGGED_IN_CUSTOMER_SEESION_ID";
  LOGGED_IN_CUSTOMER_ID="LOGGED_IN_CUSTOMER_ID";
  LOGGED_IN_CUSTOMER_NAME="LOGGED_IN_CUSTOMER_NAME";
}
