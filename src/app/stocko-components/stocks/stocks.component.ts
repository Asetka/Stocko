import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import * as Highcharts from 'highcharts';
@Component({
  selector: 'app-stocks',
  templateUrl: './stocks.component.html',
  styleUrls: ['./stocks.component.sass']
})
export class StocksComponent implements OnInit {
  ticker: string = "";
  stockObject: any;
  searched: boolean = false;
  stockPrices: number[] = []
  highcharts = Highcharts;
  chartOptions: Highcharts.Options = {};

  constructor(
    private http: HttpClient,
  ) { }
  
  ngOnInit(): void {

  }
  onSearch(){
    const base = `https://stocko-flask-api-dev.herokuapp.com/stock-page/`
    const url = `${base}/${this.ticker}`;
    this.http.get<any>(url).subscribe(data => {
      console.log(data)
      this.stockObject = JSON.parse(JSON.stringify(data))
      if(this.stockObject != null){
        this.searched = true;
      }
      console.log(this.stockObject.chart_data.week_ending)
      const stockData = this.stockObject.chart_data.end_of_week_price;
      const stockDates = this.stockObject.chart_data.week_ending;

      console.log(stockData)

      var stockPrices = new Array;
      var stockPrices = new Array;

      for(var i in stockData){
        console.log(stockData[i]);
        stockPrices.push(Number(stockData[i]))
      }
      console.log(stockPrices)
      this.highcharts = Highcharts;
      this.chartOptions = {
        title: {
          text: this.stockObject.ticker
        },
        xAxis: {
          title: {
            text: 'Date'
          },
          categories: this.stockObject.chart_data.week_ending
        },
        yAxis: {
          title: {
            text: "Price"
          }
        },
        series: [{
          data: stockPrices,
          type: 'spline'
        }]
      }
    })
    console.log(this.searched)

  }
}
