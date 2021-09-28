import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WikiComponent } from './wiki/wiki.component';
import { HomeComponent } from './home/home.component';
import { MainComponent } from './stocko-components/main/main.component';
import { BiosComponent } from './wiki/bios/bios.component';
import { AboutComponent } from './wiki/about/about.component';
import { DeliverablesComponent } from './wiki/deliverables/deliverables.component';
import { StocksComponent } from './stocko-components/stocks/stocks.component';
import { PositionsComponent } from './stocko-components/positions/positions.component';
import { EvaluationsComponent } from './stocko-components/evaluations/evaluations.component';
import { StockForecasterComponent } from './stocko-components/stock-forecaster/stock-forecaster.component';
import { NlpComponent } from './stocko-components/nlp/nlp.component';
import { BackTestingComponent } from './stocko-components/back-testing/back-testing.component';
import { AuthGuard } from '@auth0/auth0-angular';

const routes: Routes = [
  { 
    path: '', 
    component: HomeComponent 
  },
  { 
    path: 'wiki', 
    component: WikiComponent,
    children: [
      {
        path: 'bios',
        component: BiosComponent,
      },
      {
        path: 'about',
        component: AboutComponent,
      },
      {
        path: 'deliverables',
        component: DeliverablesComponent,
      },
    ]
  
  },
  { 
    path: 'app', 
    component: MainComponent,
    canActivate: [AuthGuard],
    children: [
      {
        path: 'stocks',
        component: StocksComponent,
      },
      {
        path: 'positions',
        component: PositionsComponent,
      },
      {
        path: 'evaluations',
        component: EvaluationsComponent,
      },
      {
        path: 'stockForecaster',
        component: StockForecasterComponent,
      },
      {
        path: 'nlp',
        component: NlpComponent,
      },
      {
        path: 'backTesting',
        component: BackTestingComponent,
      },
    ]
  },
  {
    path : '**',
    component: HomeComponent
  }


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
