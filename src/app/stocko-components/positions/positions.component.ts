import { Component, OnInit } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, findIndex, map, tap } from 'rxjs/operators';

@Component({
  selector: 'app-positions',
  templateUrl: './positions.component.html',
  styleUrls: ['./positions.component.sass']
})
export class PositionsComponent implements OnInit {
  base = `https://stocko-flask-api-dev.herokuapp.com`
  priceHelper : any;
  d : any;
  userName : string | undefined;
  myArr : Position[] = [];

  newTicker : string = "";
  newAvgCost : number = 0;
  newQty : number = 0;

  editTicker : string = "";
  editAvgCost : number = 0;
  editQty : number = 0;

  addOpen: boolean =  false;
  emptyPositions: boolean = false;

  constructor(public auth: AuthService, private http: HttpClient,) { }
  
  ngOnInit(): void {
    this.auth.user$.subscribe(data => {
      this.getPositions(data?.nickname).subscribe(data => this.d = data)
      this.userName = data?.nickname;
    })
  }

  getPositions(uid: string | undefined) {
    const url = `${this.base}/personal-portfolio/${uid}`;
    return this.http.get<any[]>(url)
      .pipe(tap(x => {
        this.d = x;
        this.myArr = this.d.response;
      }))
  }

  getPrice(ticker: string){
    const url = `${this.base}/stock-price/${ticker}`
    this.http.get<any>(url).subscribe(data => {
      console.log(data.price)
      return data.price;
    })
  }

  addPosition(ticker: string, avgPrice: number, quantity: number){
    const url = `${this.base}/personal-portfolio/${this.userName}`;
    const formData = new FormData()
    formData.set("ticker", ticker.toUpperCase())
    formData.set("avg_price", avgPrice.toString());
    formData.set("qty", quantity.toString());
    this.http.post<any>(url,formData).subscribe();
    location.reload();
  }

  editPosition(ticker: string, avgPrice: number, quantity: number){
    const url = `${this.base}/personal-portfolio/${this.userName}`;
    const formData = new FormData()
    formData.set("ticker", ticker.toUpperCase())
    formData.set("avg_price", avgPrice.toString());
    formData.set("qty", quantity.toString());
    this.http.put<any>(url,formData).subscribe();
    location.reload();
  }

  deletePosition(val: Position){
    const url = `${this.base}/personal-portfolio/${this.userName}`;
    console.log(this.userName);
    console.log(url)
    const formData = new FormData()
    formData.set("ticker", val.ticker)
    this.http.delete<any>(url, {body: formData}).subscribe();
    this.myArr.splice(this.myArr.indexOf(val),1);
  }
}

export interface Position {
  avg_price : number;
  pct_change: number;
  price: number;
  profit: number;
  qty : number;
  ticker : string;
}