import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-stocks',
  templateUrl: './stocks.component.html',
  styleUrls: ['./stocks.component.sass']
})
export class StocksComponent implements OnInit {
  test = "cim"
  constructor(
    private http: HttpClient,
  ) { }

  ngOnInit(): void {
    
  }
  stockStringObject: any;
  stockObject: any;
  onSearch(ticker: string){
    const base = `https://stocko-flask-api-dev.herokuapp.com/stock-page/`
    const url = `${base}/${ticker}`;
    this.http.get<any>(url).subscribe(data => {
      console.log(data)
      this.stockStringObject = JSON.stringify(data)
      this.stockObject = JSON.parse(this.stockStringObject)
      console.log(this.stockObject.ticker)
    })

  }
}