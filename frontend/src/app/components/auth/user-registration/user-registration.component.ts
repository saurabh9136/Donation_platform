import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-user-registration',
  standalone: true,
  imports: [FormsModule , CommonModule],
  templateUrl: './user-registration.component.html',
  styleUrl: './user-registration.component.css'
})
export class UserRegistrationComponent {
  user = {
    firstName: '',
    lastName: '',
    email: '',
    mobileNumber: '',
    password: '',
    confirmPassword: '',
    preferredCause: '',
    address: '',
    country: '',
    city:''
  };

  apiErrorMessage: string = '';
  onSubmit(){
    
  }
}
