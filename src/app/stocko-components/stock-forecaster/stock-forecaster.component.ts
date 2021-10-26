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

  annualReturn: number = 0;

  revenueCagr: number = 0;
  fcfMarginAvg: number = 0;
  peRatio: number = 0;
  priceToFcf: number = 0;
  profitMarginAvg: number = 0;
  stockPrice: number = 0;
  shareChangeAvg: number = 0;
  ufcRevenueTtm:number = 0;
  ufcSharesTtm:number = 0;

  revenueCagrAssumption: number = 0;
  shareChangeAvgAssumption: number = 0;
  profitMarginAvgAssumption: number = 0;
  fcfMarginAvgAssumption: number = 0;
  peRatioAssumption: number = 0;
  priceToFcfAssumption: number = 0;

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
    this.revenueCagrAssumption = this.revenueCagrAssumption / 100;
    this.shareChangeAvgAssumption = this.shareChangeAvgAssumption / 100;
    this.profitMarginAvgAssumption = this.profitMarginAvgAssumption / 100;
    this.fcfMarginAvgAssumption = this.fcfMarginAvgAssumption / 100;
    this.annualReturn = this.annualReturn / 100;

    const revenue_year_one = this.ufcRevenueTtm * Math.pow((1 + this.revenueCagrAssumption), 1);
    const revenue_year_two = this.ufcRevenueTtm * Math.pow((1 + this.revenueCagrAssumption), 2);
    const revenue_year_three = this.ufcRevenueTtm * Math.pow((1 + this.revenueCagrAssumption), 3);
    const revenue_year_four = this.ufcRevenueTtm * Math.pow((1 + this.revenueCagrAssumption), 4);
    const revenue_year_five = this.ufcRevenueTtm * Math.pow((1 + this.revenueCagrAssumption), 5);
    const revenue_year_six = this.ufcRevenueTtm * Math.pow((1 + this.revenueCagrAssumption), 6);
    const revenue_year_seven = this.ufcRevenueTtm * Math.pow((1 + this.revenueCagrAssumption), 7);

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

    const shares_after_seven_years = this.ufcSharesTtm * Math.pow((1 + this.shareChangeAvgAssumption), 7);

    const dcf_sum = dcf_year_one + dcf_year_two + dcf_year_three + dcf_year_four + dcf_year_five + dcf_year_six + dcf_year_seven + dcf_terminal;
    // THIS IS FIRST PRICE
    const multiple_earnings_price = dcf_sum / shares_after_seven_years;


    // this is discounted free cash flow
    const fcf_to_revenue_one = revenue_year_one * this.fcfMarginAvgAssumption;
    const fcf_to_revenue_two = revenue_year_two * this.fcfMarginAvgAssumption;
    const fcf_to_revenue_three = revenue_year_three * this.fcfMarginAvgAssumption;
    const fcf_to_revenue_four = revenue_year_four * this.fcfMarginAvgAssumption;
    const fcf_to_revenue_five = revenue_year_five * this.fcfMarginAvgAssumption;
    const fcf_to_revenue_six = revenue_year_six * this.fcfMarginAvgAssumption;
    const fcf_to_revenue_seven = revenue_year_seven * this.fcfMarginAvgAssumption;
    const fcf_to_revenue_terminal = fcf_to_revenue_seven * this.priceToFcfAssumption;

    const dcf2_year_one = fcf_to_revenue_one / (Math.pow((1 + this.annualReturn), 1));
    const dcf2_year_two = fcf_to_revenue_two / (Math.pow((1 + this.annualReturn), 2));
    const dcf2_year_three = fcf_to_revenue_three / (Math.pow((1 + this.annualReturn), 3));
    const dcf2_year_four = fcf_to_revenue_four / (Math.pow((1 + this.annualReturn), 4));
    const dcf2_year_five = fcf_to_revenue_five / (Math.pow((1 + this.annualReturn), 5));
    const dcf2_year_six = fcf_to_revenue_six / (Math.pow((1 + this.annualReturn), 6));
    const dcf2_year_seven = fcf_to_revenue_seven / (Math.pow((1 + this.annualReturn), 7));
    const dcf2_terminal = dcf_year_seven * this.priceToFcfAssumption;
    const dcf2_sum = dcf2_year_one + dcf2_year_two + dcf2_year_three + dcf2_year_four + dcf2_year_five + dcf2_year_six + dcf2_year_seven + dcf2_terminal;

    // THIS IS SECOND PRICE
    const discounted_fcf_price = dcf2_sum / shares_after_seven_years;

    this.pFcf = discounted_fcf_price;
    this.pEarning = multiple_earnings_price;
  }
}
