import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContactDevsComponent } from './contact-devs.component';

describe('ContactDevsComponent', () => {
  let component: ContactDevsComponent;
  let fixture: ComponentFixture<ContactDevsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ContactDevsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ContactDevsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
