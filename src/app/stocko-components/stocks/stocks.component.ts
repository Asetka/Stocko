import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-stocks',
  templateUrl: './stocks.component.html',
  styleUrls: ['./stocks.component.sass']
})
export class StocksComponent implements OnInit {
  ticker: string = "";
  stockObject: any;

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
      console.log(this.stockObject)
    })

  }
}