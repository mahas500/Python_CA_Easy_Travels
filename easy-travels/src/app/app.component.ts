import { Component } from '@angular/core';
import { Routes, RouterModule, Router } from '@angular/router';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'easy-travels';

  constructor(public router:Router){

  }

  ngOnInit() {
    console.log(this.router.url)
  }

}
