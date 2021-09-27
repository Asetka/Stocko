import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WikiComponent } from './wiki/wiki.component';
import { HomeComponent } from './home/home.component';
import { MainComponent } from './stocko-components/main/main.component';
import { BiosComponent } from './wiki/bios/bios.component';
import { AboutComponent } from './wiki/about/about.component';
import { DeliverablesComponent } from './wiki/deliverables/deliverables.component';

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
    component: MainComponent 
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
