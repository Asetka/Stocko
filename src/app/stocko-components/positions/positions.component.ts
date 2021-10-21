import { APP_INITIALIZER, Component, OnInit } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, findIndex, map, tap } from 'rxjs/operators';
import { THIS_EXPR } from '@angular/compiler/src/output/output_ast';

@Component({
  selector: 'app-positions',
  templateUrl: './positions.component.html',
  styleUrls: ['./positions.component.sass']
})
export class PositionsComponent implements OnInit {

  d : any;
  userName : string | undefined;
  myArr : Position[] = []
  newTicker : string = "";
  newAvgCost : number = 0;
  newQty : number = 0;


  addOpen: boolean =  false;
  editOpen: boolean = false;
  emptyPositions: boolean = false;
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(public auth: AuthService, private http: HttpClient,) { }
  
  ngOnInit(): void {
    this.auth.user$.subscribe(data => {
      this.getPositions(data?.nickname).subscribe(data => this.d = data)
      this.userName = data?.nickname;
    })
  }

  getPositions(uid: string | undefined): Observable<any[]> {
    const base = `https://stocko-flask-api-dev.herokuapp.com/personal-portfolio`
    const url = `${base}/${uid}`;
    return this.http.get<any[]>(url)
      .pipe(tap(x => {
        this.d = x;
        this.myArr = this.d.response;
        if(this.myArr.length == 0){
          this.emptyPositions = true;
        }
      }))
  }

  addPosition(ticker: string, avgPrice: number, quantity: number){
    const base = `https://stocko-flask-api-dev.herokuapp.com/personal-portfolio`
    const url = `${base}/${this.userName}`;
    console.log(this.userName);
    console.log(url)
    const formData = new FormData()
    formData.set("ticker", ticker.toUpperCase())
    formData.set("avg_price", avgPrice.toString());
    formData.set("qty", quantity.toString());
    this.http.post<any>(url,formData).subscribe();
    this.myArr.push()
  }

  editPosition(val: Position){
    const base = `https://stocko-flask-api-dev.herokuapp.com/personal-portfolio`
    const url = `${base}/${this.userName}`;
    console.log(this.userName);
    console.log(url)
    const formData = new FormData()
    formData.set("ticker", val.ticker)
    this.http.post<any>(url,formData).subscribe();
  }

  deletePosition(val: Position){
    const base = `https://stocko-flask-api-dev.herokuapp.com/personal-portfolio`
    const url = `${base}/${this.userName}`;
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
  qty : number;
  ticker : string;
}