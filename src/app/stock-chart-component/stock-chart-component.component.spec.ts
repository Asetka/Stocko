import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StockChartComponentComponent } from './stock-chart-component.component';

describe('StockChartComponentComponent', () => {
  let component: StockChartComponentComponent;
  let fixture: ComponentFixture<StockChartComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StockChartComponentComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StockChartComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
