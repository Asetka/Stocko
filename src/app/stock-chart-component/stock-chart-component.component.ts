import { Component, OnInit, Input } from '@angular/core';
import * as Highcharts from 'highcharts';

@Component({
  selector: 'app-stock-chart-component',
  templateUrl: './stock-chart-component.component.html',
  styleUrls: ['./stock-chart-component.component.sass']
})
export class StockChartComponentComponent implements OnInit {
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
          text: 'Month'
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
