import { Component, OnInit } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

@Component({
  selector: 'app-positions',
  templateUrl: './positions.component.html',
  styleUrls: ['./positions.component.sass']
})
export class PositionsComponent implements OnInit {

  d : any;
  userName : string | undefined;
  myArr : Position[] = []


  emptyPositions: boolean = false;

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(public auth: AuthService, private http: HttpClient,) { }
  ngOnInit(): void {
    this.auth.user$.subscribe(data => {
      this.getPositions(data?.nickname).subscribe(data => this.d = data)
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
}

export interface Position {
  avg_price : number;
  qty : number;
  ticker : string;
}