import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NgoRegistrationComponent } from './ngo-registration.component';

describe('NgoRegistrationComponent', () => {
  let component: NgoRegistrationComponent;
  let fixture: ComponentFixture<NgoRegistrationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NgoRegistrationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NgoRegistrationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
