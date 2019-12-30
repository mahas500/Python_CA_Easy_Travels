import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ServerendpointsService {

  constructor() { }

  SERVERURL="http://localhost:5000/";

  employeeLogin= "employeeLogin";



  OPERATION_SUCESSESULL = 1
}
