import { AllEmployeesComponent } from './employee-dashboard/all-employees/all-employees.component';
import { EmployeeDashboardComponent } from './employee-dashboard/employee-dashboard.component';
import { CustomerLoginComponent } from './customer-login/customer-login.component';
import { LoginComponent } from './login/login.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CreateEmployeeComponent } from './employee-dashboard/create-employee/create-employee.component';


const routes: Routes = [
  { path: 'employee-login', component: LoginComponent },
  { path: 'customer-login', component: CustomerLoginComponent },
  { path: 'employee-dashboard', component: EmployeeDashboardComponent,
    children:[
      {
        path: 'create-employee',
        component: CreateEmployeeComponent
      },
      {
        path: 'all-employees',
        component: AllEmployeesComponent
      }
    ]

  }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
