import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BackTestingComponent } from './back-testing.component';

describe('BackTestingComponent', () => {
  let component: BackTestingComponent;
  let fixture: ComponentFixture<BackTestingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BackTestingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BackTestingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
