import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-stock-forecaster',
  templateUrl: './stock-forecaster.component.html',
  styleUrls: ['./stock-forecaster.component.sass']
})
export class StockForecasterComponent implements OnInit, OnChanges {
  url = 'https://stocko-flask-api-dev.herokuapp.com/forecast-page/'
  ticker = ""
  @Input() pFcf: number = 0;
  @Input() pEarning: number = 0;

  annualReturn: any;

  fcfMarginAvg: any;
  peRatio: any;
  priceToFcf: any;
  profitMarginAvg: any;
  stockPrice: any;
  shareChangeAvg: any;
  ufcRevenueTtm:any;
  ufcSharesTtm:any;

  fcfMarginAvgAssumption: any;
  peRatioAssumption: any;
  priceToFcfAssumption: any;
  profitMarginAvgAssumption: any;
  stockPriceAssumption: any;
  shareChangeAvgAssumption: any;
  ufcRevenueTtmAssumption:any;
  ufcSharesTtmAssumption:any;
  yearsOfHistoryError:boolean=true;

  constructor(
    private http: HttpClient,
  ) { }

  ngOnInit(): void {
  }

  ngOnChanges(changes: SimpleChanges){
    changes.pFcf = (this.peRatioAssumption + this.fcfMarginAvgAssumption);
    changes.pFcf = (this.peRatioAssumption + this.fcfMarginAvgAssumption);
  }

  onSearch(){
    console.log(this.ticker)
    this.http.get<any>(this.url+this.ticker).subscribe(data => {
      console.log(data);
      this.fcfMarginAvg = data.fcf_margin_avg;
      this.peRatio = data.pe_ratio;
      this.priceToFcf = data.price_to_fcf;
      this.profitMarginAvg = data.profit_margin_avg;
      this.stockPrice = data.stock_price;
      this.shareChangeAvg = data.share_change_avg;
      this.ufcRevenueTtm = data.ufc_revenue_ttm;
      this.ufcSharesTtm = data.ufc_shares_ttm;
      this.yearsOfHistoryError = data.years_of_history_error;

    });

  }
}
