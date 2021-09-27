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

{
  "change_in_shares_ourstanding": "WORKING IN PROGRESS",
  "current_assets_vs_liabilities": "-4367757000",
  "ev_ebitda_ratio": "0",
  "fcf_desired_marketcap": "6642884000.0",
  "fcf_desired_price": "28.153062435369307",
  "fcf_growth": "-53.355085032383386",
  "pe_ratio": "5.17",
  "price_to_book_ratio": "0.986",
  "profit_growth": "-52.53388176976217",
  "profit_margin": "65.0",
  "revenue_growth": "-41.225751166861144",
  "total_assets_vs_liabilities": "3779386000",
  "years_of_history_error": false
}

export interface PillarData {
  peRatio : number;
  ProfitMargin : number;
  ProfitGrowth : number;



}