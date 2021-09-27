import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-evaluations',
  templateUrl: './evaluations.component.html',
  styleUrls: ['./evaluations.component.sass']
})
export class EvaluationsComponent implements OnInit {

  ticker = ''
  
  constructor() { }

  ngOnInit(): void {
  }

  onSearch(){
    console.log(this.ticker)
  }

}
