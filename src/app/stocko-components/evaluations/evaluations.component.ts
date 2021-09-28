import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { UpperCasePipe } from '@angular/common';

@Component({
  selector: 'app-evaluations',
  templateUrl: './evaluations.component.html',
  styleUrls: ['./evaluations.component.sass']
})
export class EvaluationsComponent implements OnInit {

  peRatio = null;                       //  Float
  profitMargin = null;                  //  Percent
  profitGrowth = null;                  //  Percent
  revenueGrowth = null;                 //  Percent
  currentAssetsVsLiabilities = null;    //  INt
  totalAssetsVsLiabilities= null;       //  Int
  changeInSharesOutstanding= null;      //  Percent
  freeCashFlowGrowth= null;             //  Percent
  freeCashFlowDesiredSharePrice= null;  //  Float
  freeCashFlowDesiredMarketCap = null;  //  Float
  evEbitdaRatio = null;                 //  Float
  priceToBookRatio = null;              //  Float
  historyError = false;

  waitText = '';
  
  ticker = ''
  curTicker = "Awaiting search";
  endpoint = 'http://127.0.0.1:5000/stock-evaluation/'
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  json: any;

  constructor(
    private http: HttpClient,
  ) { }
  ngOnInit(): void {
  }

  onSearch(){
    this.curTicker = this.ticker;
    this.http.get<any>(this.endpoint+this.ticker)
      .subscribe(data => { 
        console.log(data)
        this.peRatio = data.pe_ratio;
        this.profitMargin = data.profit_margin;
        this.profitGrowth = data.profit_growth;
        this.revenueGrowth = data.revenue_growth;
        this.currentAssetsVsLiabilities = data.current_assets_vs_liabilities;
        this.totalAssetsVsLiabilities = data.total_assets_vs_liabilities;
        this.changeInSharesOutstanding = data.change_in_shares_ourstanding;
        this.freeCashFlowGrowth = data.fcf_growth;
        this.freeCashFlowDesiredSharePrice = data.fcf_desired_price;
        this.freeCashFlowDesiredMarketCap = data.fcf_desired_marketcap;
        this.evEbitdaRatio = data.ev_ebitda_ratio;
        this.priceToBookRatio = data.price_to_book_ratio;
        this.historyError = data.years_of_history_error;
      })
  }
}