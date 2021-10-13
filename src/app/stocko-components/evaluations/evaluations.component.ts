import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-evaluations',
  templateUrl: './evaluations.component.html',
  styleUrls: ['./evaluations.component.sass']
})

export class EvaluationsComponent implements OnInit {

  good = "bg-success";
  medium = "bg-warning";
  bad = "bg-danger";
  error = "bg-info";

  peRatio = null;                       
  profitMargin = null;                  
  profitGrowth = null;                  
  revenueGrowth = null;                 
  currentAssetsVsLiabilities = null;    
  totalAssetsVsLiabilities= null;       
  changeInSharesOutstanding= null;      
  freeCashFlowGrowth= null;             
  freeCashFlowDesiredSharePrice= null;  
  freeCashFlowDesiredMarketCap = null;  
  evEbitdaRatio = null;                 
  priceToBookRatio = null;   
  stockPrice = null; 

  peRatioS = "";                       
  profitMarginS = "";                  
  profitGrowthS = "";                  
  revenueGrowthS = "";                 
  currentAssetsVsLiabilitiesS = "";    
  totalAssetsVsLiabilitiesS= "";       
  changeInSharesOutstandingS= "";      
  freeCashFlowGrowthS= "";             
  freeCashFlowDesiredSharePriceS= "";  
  freeCashFlowDesiredMarketCapS = "";  
  evEbitdaRatioS = "";                 
  priceToBookRatioS = "";    

  historyError = null;

  waitText = '';
  
  ticker = ''
  curTicker = "Awaiting search";
  endpoint = 'https://stocko-flask-api-dev.herokuapp.com/stock-evaluation/'
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

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
        this.stockPrice = data.stock_price;
        this.historyError = data.years_of_history_error;

        this.peRatio = data.pe_ratio;
        this.peRatioS = this.checkOneReverse(data.pe_ratio, 20)

        this.profitMargin = data.profit_margin;
        this.profitMarginS = this.checkOne(data.profit_margin, 10)

        this.profitGrowth = data.profit_growth;
        this.profitGrowthS = this.checkOne(data.profit_growth, 0)

        this.revenueGrowth = data.revenue_growth;
        this.revenueGrowthS = this.checkOne(data.revenue_growth, 0)

        this.currentAssetsVsLiabilities = data.current_assets_vs_liabilities;
        this.currentAssetsVsLiabilitiesS = this.checkOne(data.current_assets_vs_liabilities, 0)

        this.totalAssetsVsLiabilities = data.total_assets_vs_liabilities;
        this.totalAssetsVsLiabilitiesS = this.checkOne(data.total_assets_vs_liabilities, 0)

        this.changeInSharesOutstanding = data.change_in_shares_ourstanding;
        this.changeInSharesOutstandingS = this.checkOne(data.change_in_shares_ourstanding, 0)

        this.freeCashFlowGrowth = data.fcf_growth;
        this.freeCashFlowGrowthS = this.checkOne(data.fcf_growth, 0)

        this.freeCashFlowDesiredSharePrice = data.fcf_desired_price;
        this.freeCashFlowDesiredSharePriceS = this.checkOne(data.fcf_desired_price, data.stock_price)

        this.freeCashFlowDesiredMarketCap = data.fcf_desired_marketcap;
        this.freeCashFlowDesiredMarketCapS = this.checkOne(data.fcf_desired_marketcap, 20)

        this.evEbitdaRatio = data.ev_ebitda_ratio;
        this.evEbitdaRatioS = this.checkOneReverse(data.ev_ebitda_ratio, 10)

        this.priceToBookRatio = data.price_to_book_ratio;
        this.priceToBookRatioS = this.checkOne(data.price_to_book_ratio, 20)


      })
  }



  checkProfitMargin(v: number, check: number){
    if(v >= check)
      return this.good;
    else if(v < check)
      return this.bad;
    else
      return this.error;
  }
  checkOne(v: number, check: number){
    if(v == check)
      return this.medium;
    else if(v > check)
      return this.good;
    else if(v < check)
      return this.bad;
    else
      return this.error;
  }

  checkOneReverse(v: number, check: number){
    if(v == check)
      return this.medium;
    else if(v < check)
      return this.good;
    else if(v > check)
      return this.bad;
    else
      return this.error;
  }
  
}
