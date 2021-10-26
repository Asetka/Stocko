import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-stock-forecaster',
  templateUrl: './stock-forecaster.component.html',
  styleUrls: ['./stock-forecaster.component.sass']
})
export class StockForecasterComponent implements OnInit {
  url = 'https://stocko-flask-api-dev.herokuapp.com/forecast-page/'
  ticker = ""
  pFcf: number = 0;
  pEarning: number = 0;

  annualReturn: any;

  revenueCagr: any;
  fcfMarginAvg: any;
  peRatio: any;
  priceToFcf: any;
  profitMarginAvg: any;
  stockPrice: any;
  shareChangeAvg: any;
  ufcRevenueTtm:any;
  ufcSharesTtm:any;

  revenueCagrAssumption: any;
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

  onSearch(){
    console.log(this.ticker)
    this.http.get<any>(this.url+this.ticker).subscribe(data => {
      console.log(data);
      this.revenueCagr = data.revenue_cagr
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

  updateVariables(){
    const revenue_year_one = this.ufcRevenueTtm * Math.pow((1 + this.profitMarginAvgAssumption), 1);
    const revenue_year_two = this.ufcRevenueTtm * Math.pow((1 + this.profitMarginAvgAssumption), 2);
    const revenue_year_three = this.ufcRevenueTtm * Math.pow((1 + this.profitMarginAvgAssumption), 3);
    const revenue_year_four = this.ufcRevenueTtm * Math.pow((1 + this.profitMarginAvgAssumption), 4);
    const revenue_year_five = this.ufcRevenueTtm * Math.pow((1 + this.profitMarginAvgAssumption), 5);
    const revenue_year_six = this.ufcRevenueTtm * Math.pow((1 + this.profitMarginAvgAssumption), 6);
    const revenue_year_seven = this.ufcRevenueTtm * Math.pow((1 + this.profitMarginAvgAssumption), 7);

    // multiple of earnings
    const margin_year_one = revenue_year_one * this.profitMarginAvgAssumption;
    const margin_year_two = revenue_year_two * this.profitMarginAvgAssumption;
    const margin_year_three = revenue_year_three * this.profitMarginAvgAssumption;
    const margin_year_four = revenue_year_four * this.profitMarginAvgAssumption;
    const margin_year_five = revenue_year_five * this.profitMarginAvgAssumption;
    const margin_year_six = revenue_year_six * this.profitMarginAvgAssumption;
    const margin_year_seven = revenue_year_seven * this.profitMarginAvgAssumption;
    const margin_terminal = margin_year_seven * this.peRatioAssumption;

    const dcf_year_one = margin_year_one / Math.pow((1 + this.annualReturn), 1);
    const dcf_year_two = margin_year_two / Math.pow((1 + this.annualReturn), 2);
    const dcf_year_three = margin_year_three / Math.pow((1 + this.annualReturn), 3);
    const dcf_year_four = margin_year_four / Math.pow((1 + this.annualReturn), 4);
    const dcf_year_five = margin_year_five / Math.pow((1 + this.annualReturn), 5);
    const dcf_year_six = margin_year_six / Math.pow((1 + this.annualReturn), 6);
    const dcf_year_seven = margin_year_seven / Math.pow((1 + this.annualReturn), 7);
    const dcf_terminal = dcf_year_seven * this.peRatioAssumption;

    const shares_after_seven_years = this.ufcSharesTtm * Math.pow((1 + this.shareChangeAvgAssumption), 7)

    const dcf_sum = dcf_year_one + dcf_year_two + dcf_year_three + dcf_year_four + dcf_year_five + dcf_year_six + dcf_year_seven + dcf_terminal;
    // THIS IS FIRST PRICE
    const multiple_earnings_price = dcf_sum / shares_after_seven_years


    // this is discounted free cash flow
    const dcf_to_revenue_one = revenue_year_one
    const dcf_to_revenue_two = revenue_year_two
    const dcf_to_revenue_three = revenue_year_three
    const dcf_to_revenue_four = revenue_year_four
    const dcf_to_revenue_five = revenue_year_five
    const dcf_to_revenue_six = revenue_year_six
    const dcf_to_revenue_seven = revenue_year_seven
    const dcf_to_revenue_terminal = dcf_to_revenue_seven



    this.pFcf = this.fcfMarginAvgAssumption;
    this.pEarning = this.fcfMarginAvgAssumption;
  }
}
