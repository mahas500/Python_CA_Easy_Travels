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


