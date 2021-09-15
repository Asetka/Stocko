import { Component, OnInit, Inject } from '@angular/core';
// Import the AuthService type from the SDK
import { AuthService } from '@auth0/auth0-angular';
import { DOCUMENT } from '@angular/common';

@Component({
  selector: 'app-auth-button-component',
  templateUrl: './auth-button-component.component.html',
  styleUrls: ['./auth-button-component.component.sass']
})
export class AuthButtonComponentComponent implements OnInit {

  constructor(@Inject(DOCUMENT) public document: Document, public auth: AuthService) {}

  ngOnInit(): void {
  }

}
