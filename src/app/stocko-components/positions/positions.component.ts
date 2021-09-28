import { Component, OnInit } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
@Component({
  selector: 'app-positions',
  templateUrl: './positions.component.html',
  styleUrls: ['./positions.component.sass']
})
export class PositionsComponent implements OnInit {


  constructor(public auth: AuthService) { }

  ngOnInit(): void {
    this.auth.user$.subscribe(data => {
      console.log(data?.nickname)
      
    })
  }
}
