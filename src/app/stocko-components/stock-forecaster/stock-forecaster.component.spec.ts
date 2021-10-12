import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StockForecasterComponent } from './stock-forecaster.component';

describe('StockForecasterComponent', () => {
  let component: StockForecasterComponent;
  let fixture: ComponentFixture<StockForecasterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StockForecasterComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StockForecasterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
