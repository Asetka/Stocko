import { Component, OnInit } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.sass']
})
export class MainComponent implements OnInit {

  constructor(public auth: AuthService) { }

  name : any | undefined;

  ngOnInit(): void {
    this.auth.user$.subscribe(data => {
      this.name = data?.nickname
    })
  }

}
