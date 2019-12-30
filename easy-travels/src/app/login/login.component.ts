import { ServerendpointsService } from './../service/serverendpoints.service';
import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { NgModule } from '@angular/core';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username
  password

  constructor(public httpClient: HttpClient,
    public serverEndpoints:ServerendpointsService) { }

  ngOnInit() {
  }

loginEmployee(){
  let postBody = {
    "username":this.username,
	  "password":this.password
  }
  let header={}
  this.httpClient.post(this.serverEndpoints.SERVERURL + this.serverEndpoints.employeeLogin, postBody, header).subscribe((response: any) => {

    if (response.operationStatus == this.serverEndpoints.OPERATION_SUCESSESULL) {
      //this.loggedInUser = response.resultSet.appUser;
      //this.loggedInUserSession = response.resultSet.session;
      let employee=response.resultSet;
      localStorage.setItem(this.serverEndpoints.LOGGED_IN_EMPLOYEE_SEESION_ID,employee.session_id)
      localStorage.setItem(this.serverEndpoints.LOGGED_IN_EMPLOYEE_NAME,employee.name)
      localStorage.setItem(this.serverEndpoints.LOGGED_IN_EMPLOYEE_ID,employee.employee_id)
      localStorage.setItem(this.serverEndpoints.LOGGED_IN_EMPLOYEE_ROLE,employee.role_id)
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


