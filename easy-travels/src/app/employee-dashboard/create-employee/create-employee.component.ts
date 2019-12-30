import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ServerendpointsService } from 'src/app/service/serverendpoints.service';

@Component({
  selector: 'app-create-employee',
  templateUrl: './create-employee.component.html',
  styleUrls: ['./create-employee.component.css']
})
export class CreateEmployeeComponent implements OnInit {
  name
  contact_no
	username
	password
	email

  constructor(public httpClient: HttpClient,
    public serverEndpoints:ServerendpointsService) { }

  ngOnInit() {
  }

  createEmployee(){
    debugger
    let postBody = {
      "contact_no":this.contact_no,
      "name":this.name,
      "username":this.username,
      "password":this.password,
      "email":this.email
    }
    let header={
      "sessionId":localStorage.getItem(this.serverEndpoints.LOGGED_IN_EMPLOYEE_SEESION_ID)
    }
    this.httpClient.post(this.serverEndpoints.SERVERURL + this.serverEndpoints.createEmployee, postBody, {headers:header}).subscribe((response: any) => {

      if (response.operationStatus == this.serverEndpoints.OPERATION_SUCESSESULL) {
        //this.loggedInUser = response.resultSet.appUser;
        //this.loggedInUserSession = response.resultSet.session;
        alert("Employee Registered Succesfully")

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
