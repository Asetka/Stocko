import { Component, OnInit } from '@angular/core';
import * as Highcharts from 'highcharts';
@Component({
  selector: 'app-stocks',
  templateUrl: './stocks.component.html',
  styleUrls: ['./stocks.component.sass']
})
export class StocksComponent implements OnInit {
  highcharts = Highcharts;
  chartOptions: Highcharts.Options = {};
  constructor() { }

  ngOnInit(): void {
    this.highcharts = Highcharts;
    this.chartOptions = {
      title: {
        text: "Apple"
      },
      xAxis: {
        title: {
          text: 'Date'
        },
        categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
      },
      yAxis: {
        title: {
          text: "Price"
        }
      },
      series: [{
        data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 24.4, 19.3, 16.0, 18.4, 17.9],
        type: 'spline'
      }]
    }
  }

}
