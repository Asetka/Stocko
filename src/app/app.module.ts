import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CommonModule } from '@angular/common';

// Import the module from the SDK
import { AuthModule } from '@auth0/auth0-angular';
import { AuthButtonComponentComponent } from './auth-button-component/auth-button-component.component';
import { UserProfileComponentComponent } from './user-profile-component/user-profile-component.component';
import { WikiComponent } from './wiki/wiki.component';
import { HomeComponent } from './home/home.component';
import { MainComponent } from './stocko-components/main/main.component';
import { DeliverablesComponent } from './wiki/deliverables/deliverables.component';
import { BiosComponent } from './wiki/bios/bios.component';
import { AboutComponent } from './wiki/about/about.component';
import { ContactDevsComponent } from './contact-devs/contact-devs.component';
import { PositionsComponent } from './stocko-components/positions/positions.component';
import { EvaluationsComponent } from './stocko-components/evaluations/evaluations.component';
import { StockForecasterComponent } from './stocko-components/stock-forecaster/stock-forecaster.component';
import { StocksComponent } from './stocko-components/stocks/stocks.component';
import { StockChartComponentComponent } from './stock-chart-component/stock-chart-component.component';
import { HighchartsChartModule } from 'highcharts-angular';


@NgModule({
  declarations: [
    AppComponent,
    AuthButtonComponentComponent,
    UserProfileComponentComponent,
    WikiComponent,
    HomeComponent,
    MainComponent,
    DeliverablesComponent,
    BiosComponent,
    AboutComponent,
    ContactDevsComponent,
    PositionsComponent,
    EvaluationsComponent,
    StockForecasterComponent,
    StocksComponent,
    StockChartComponentComponent,
  ],
  imports: [
    BrowserModule,
    HighchartsChartModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
    CommonModule,
    AuthModule.forRoot({
      domain: 'dev-919y6k1x.us.auth0.com',
      clientId: 'XcZirvnmcn3RDRti4CnGvaUmlELKeXHl'
    }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
