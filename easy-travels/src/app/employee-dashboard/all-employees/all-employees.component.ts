import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ServerendpointsService } from 'src/app/service/serverendpoints.service';

@Component({
  selector: 'app-all-employees',
  templateUrl: './all-employees.component.html',
  styleUrls: ['./all-employees.component.css']
})
export class AllEmployeesComponent implements OnInit {
   employees=[]
  constructor(public httpClient: HttpClient,
    public serverEndpoints: ServerendpointsService) { }

  ngOnInit() {
    this.getAllEmployees()
  }



  getAllEmployees() {

    let postBody = {

    }
    let header = {

    }
    this.httpClient.post(this.serverEndpoints.SERVERURL + this.serverEndpoints.getAllEmployees, postBody, { headers: header }).subscribe((response: any) => {

      if (response.operationStatus == this.serverEndpoints.OPERATION_SUCESSESULL) {
        this.employees=response.resultSet
        console.log(this.employees)
      } else {
        //this.customhttpService.getSpecificError(response.operationStatus);
      }

    }, (error: Response) => {

      if (error.status === 404) {
        console.log('Wrong url');
      } else if (error.status === 400) {
      }
    });
  }
  role
  assigneRole(role,empId){
    alert(this.role)
    let postBody = {
      "employeeId":empId,
      "roleId":role
    }
    let header = {
      "sessionId":localStorage.getItem(this.serverEndpoints.LOGGED_IN_EMPLOYEE_SEESION_ID)
    }
    this.httpClient.post(this.serverEndpoints.SERVERURL + this.serverEndpoints.assignRoleToEmployee, postBody, { headers: header }).subscribe((response: any) => {

      if (response.operationStatus == this.serverEndpoints.OPERATION_SUCESSESULL) {
        this.getAllEmployees();
      } else {
        //this.customhttpService.getSpecificError(response.operationStatus);
      }

    }, (error: Response) => {

      if (error.status === 404) {
        console.log('Wrong url');
      } else if (error.status === 400) {
      }
    });
  }
}
