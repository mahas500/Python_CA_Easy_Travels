import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { CustomerLoginComponent } from './customer-login/customer-login.component';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { EmployeeDashboardComponent } from './employee-dashboard/employee-dashboard.component';
import { CreateEmployeeComponent } from './employee-dashboard/create-employee/create-employee.component';
import { AllEmployeesComponent } from './employee-dashboard/all-employees/all-employees.component';
import { CreatePackageComponent } from './employee-dashboard/create-package/create-package.component';




@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    CustomerLoginComponent,
    EmployeeDashboardComponent,
    CreateEmployeeComponent,
    AllEmployeesComponent,
    CreatePackageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }
