import { Component, OnInit } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';

@Component({
  selector: 'app-positions',
  templateUrl: './positions.component.html',
  styleUrls: ['./positions.component.sass']
})
export class PositionsComponent implements OnInit {

  portfolioGain: number = 0;
  portfolioProfit: number = 0;

  base = `https://stocko-flask-api-dev.herokuapp.com/personal-portfolio`
  priceHelper : any;
  d : any;
  userName : string | undefined;
  myArr : Position[] = [];

  newTicker : string = "";
  newAvgCost : string = "";
  newQty : string = "";

  editTicker : string = "";
  editAvgCost : string ="";
  editQty : string = "";

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
    const url = `${this.base}/${uid}`;
    return this.http.get<any[]>(url)
      .pipe(tap(x => {
        this.d = x;
        this.myArr = this.d.response;
        if(this.myArr.length == 0) this.emptyPositions = true;
        this.portfolioProfit = this.d.data.portfolio_profit;
        this.portfolioGain = this.d.data.portfolio_pct_chage;

      }))
  }
  addPosition(ticker: string, avgPrice: string, quantity: string){
    const url = `${this.base}/${this.userName}`;
    const formData = new FormData()
    formData.set("ticker", ticker.toUpperCase())
    formData.set("avg_price", avgPrice.toString());
    formData.set("qty", quantity.toString());
    this.http.post<any>(url, formData).subscribe();
  }

  editPosition(ticker: string, avgPrice: string, quantity: string){
    const url = `${this.base}/${this.userName}`;
    const formData = new FormData()
    formData.set("ticker", ticker.toUpperCase())
    formData.set("avg_price", avgPrice);
    formData.set("qty", quantity);
    this.http.put<Position>(url, formData).subscribe();
  }

  deletePosition(val: Position){
    const url = `${this.base}/${this.userName}`;
    const formData = new FormData()
    formData.set("ticker", val.ticker)
    this.http.delete<any>(url, {body: formData}).subscribe();
    this.myArr.splice(this.myArr.indexOf(val),1);
  }
  
  getPortfolioSum(arr: Position[]): number{
    arr.forEach(element => {
      this.portfolioProfit = this.portfolioProfit + element.profit;
    });
    return this.portfolioProfit;
  }

  getTotalPercentChange(arr: Position[]): number{
    var initalCosts: number = 0;
    for(var x in arr){
      initalCosts = Number(initalCosts) + Number(arr[x].avg_price)
    }
    var portfolioGrowth = this.portfolioProfit/initalCosts;

    return portfolioGrowth;
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