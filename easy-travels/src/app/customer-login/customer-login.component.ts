import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ServerendpointsService } from '../service/serverendpoints.service';

@Component({
  selector: 'app-customer-login',
  templateUrl: './customer-login.component.html',
  styleUrls: ['./customer-login.component.css']
})
export class CustomerLoginComponent implements OnInit {
  username
  password

  constructor(public httpClient: HttpClient,
    public serverEndpoints:ServerendpointsService) { }

  ngOnInit() {
  }

customerLogin(){
  let postBody = {
    "username":this.username,
	  "password":this.password
  }
  let header={}
  this.httpClient.post(this.serverEndpoints.SERVERURL + this.serverEndpoints.customerLogin, postBody, header).subscribe((response: any) => {

    if (response.operationStatus == this.serverEndpoints.OPERATION_SUCESSESULL) {
      //this.loggedInUser = response.resultSet.appUser;
      //this.loggedInUserSession = response.resultSet.session;
      let customer=response.resultSet;
      localStorage.setItem(this.serverEndpoints.LOGGED_IN_CUSTOMER_SEESION_ID,customer.session_id)
      localStorage.setItem(this.serverEndpoints.LOGGED_IN_CUSTOMER_NAME,customer.name)
      localStorage.setItem(this.serverEndpoints.LOGGED_IN_CUSTOMER_ID,customer.customer_id)

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
