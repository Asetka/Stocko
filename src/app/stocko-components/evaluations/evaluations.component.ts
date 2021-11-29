import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

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

  peRatio: number = 0;                       
  profitMargin: number = 0;                  
  profitGrowth: number = 0;                  
  revenueGrowth: number = 0;                 
  currentAssetsVsLiabilities: number = 0;    
  totalAssetsVsLiabilities: number= 0;       
  changeInSharesOutstanding: number= 0;      
  freeCashFlowGrowth: number= 0;             
  freeCashFlowDesiredSharePrice: number= 0;  
  freeCashFlowDesiredMarketCap: number = 0;  
  evEbitdaRatio: number = 0;                 
  priceToBookRatio: number = 0;   
  stockPrice: number = 0; 
  marketCap: number = 0; 


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

  constructor(
    private http: HttpClient,
  ) { }

  ngOnInit(): void {
  }

  onSearch(){
    this.curTicker = this.ticker;
    this.http.get<any>(this.endpoint+this.ticker)
      .subscribe(data => { 
        this.stockPrice = data.stock_price;
        this.marketCap = data.market_cap;
        this.historyError = data.years_of_history_error;

        this.peRatio = data.pe_ratio;
        
        this.peRatioS = this.checkOneReverse(data.pe_ratio, 20);

        this.profitMargin = data.profit_margin;
        this.profitMarginS = this.checkProfitMargin(data.profit_margin, 10);

        this.profitGrowth = data.profit_growth;
        this.profitGrowthS = this.checkOne(data.profit_growth, 0);

        this.revenueGrowth = data.revenue_growth;
        this.revenueGrowthS = this.checkOne(data.revenue_growth, 0);

        this.currentAssetsVsLiabilities = data.current_assets_vs_liabilities;
        this.currentAssetsVsLiabilitiesS = this.checkOne(data.current_assets_vs_liabilities, 0);

        this.totalAssetsVsLiabilities = data.total_assets_vs_liabilities;
        this.totalAssetsVsLiabilitiesS = this.checkOne(data.total_assets_vs_liabilities, 0);

        this.changeInSharesOutstanding = data.change_in_shares_ourstanding;
        this.changeInSharesOutstandingS = this.checkOneReverse(data.change_in_shares_ourstanding, 0);

        this.freeCashFlowGrowth = data.fcf_growth;
        this.freeCashFlowGrowthS = this.checkOne(data.fcf_growth, 0);

        this.freeCashFlowDesiredSharePrice = data.fcf_desired_price;
        this.freeCashFlowDesiredSharePriceS = this.checkOneReverse(data.fcf_desired_price, data.stock_price);

        this.freeCashFlowDesiredMarketCap = data.fcf_desired_marketcap;
        this.freeCashFlowDesiredMarketCapS = this.checkOne(data.fcf_desired_marketcap, data.market_cap);

        this.evEbitdaRatio = data.ev_ebitda_ratio;
        this.evEbitdaRatioS = this.checkOneReverse(data.ev_ebitda_ratio, 10)

        this.priceToBookRatio = data.price_to_book_ratio;
        this.priceToBookRatioS = this.checkOneReverse(data.price_to_book_ratio, 3)


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
