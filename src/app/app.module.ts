import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

// Import the module from the SDK
import { AuthModule } from '@auth0/auth0-angular';
import { AuthButtonComponentComponent } from './auth-button-component/auth-button-component.component';
import { UserProfileComponentComponent } from './user-profile-component/user-profile-component.component';


@NgModule({
  declarations: [
    AppComponent,
    AuthButtonComponentComponent,
    UserProfileComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AuthModule.forRoot({
      domain: 'dev-919y6k1x.us.auth0.com',
      clientId: 'XcZirvnmcn3RDRti4CnGvaUmlELKeXHl'
    }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
