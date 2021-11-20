import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import * as Highcharts from 'highcharts/highstock';

import HStockTools from "highcharts/modules/stock-tools";



HStockTools(Highcharts);
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

  balanceSheet: any = [];
  balanceSheetOpen: boolean = false;
  cashFlowOpen: boolean = false;
  incomeStatementOpen: boolean = false;


  constructor(
    private http: HttpClient,
  ) { }
  
  ngOnInit(): void {

  }
  onSearch(){
    const base = `https://stocko-flask-api-dev.herokuapp.com/stock-page/`
    const url = `${base}/${this.ticker}`;
    this.http.get<any>(url).subscribe(data => {
      this.stockObject = JSON.parse(JSON.stringify(data))

      if(this.stockObject != null){
        this.searched = true;
      }

      const stockDate = this.stockObject.chart_data.week_ending;
      const stockData = this.stockObject.chart_data.end_of_week_price;
      const stockStart = this.stockObject.chart_data.start_of_week_price;
      const stockHigh = this.stockObject.chart_data.high_of_week_price;
      const stockLow = this.stockObject.chart_data.low_of_week_price;
      const stockVol = this.stockObject.chart_data.volume_of_week;
      var ohlc = new Array;
      var volume = new Array;
    

      this.balanceSheet = this.stockObject.balance_sheet_dict;

      for(var i in stockData){
        var tdate = new Date(stockDate[i])
        ohlc.push( [tdate.getTime(),Number(stockStart[i]),Number(stockHigh[i]),Number(stockLow[i]),Number(stockData[i])])
        volume.push([tdate.getTime(),Number(stockVol[i])])
      }

      this.highcharts = Highcharts;
      this.chartOptions = {
        title: {
          text: this.stockObject.ticker
        },
        xAxis: {
          title: {
            text: 'Date'
          },
          categories: stockDate.reverse()
        },
        yAxis: [{
          labels: {
            align: 'right',
            x: -3
          },
          title: {
            text: "OHLC"
          },
          height: '60%',
          lineWidth: 2,
          resize: {
            enabled: true
          }
        }, {
          labels: {
            align: 'right',
            x: -3
          },
          title: {
            text: "Volume"
          },
          top: '65%',
          height: '35%',
          offset: 0,
          lineWidth: 2,
        }],
        tooltip: {
          split: true
        },

        series: [{
          type: "candlestick",
          data: ohlc.reverse(),
          name: 'Price (in USD)'
        }, {
          type: "column",
          name: "Volume",
          data: volume.reverse(),
          yAxis: 1
        }]
      }

    })
  }


  openBalanceSheet(){
    this.balanceSheetOpen = true;
    this.cashFlowOpen = false;
    this.incomeStatementOpen = false;
  }
  openCashFlow(){
    this.balanceSheetOpen = false;
    this.cashFlowOpen = true;
    this.incomeStatementOpen = false;
  }
  openIncomeStatement(){
    this.balanceSheetOpen = false;
    this.cashFlowOpen = false;
    this.incomeStatementOpen = true;
  }

}
