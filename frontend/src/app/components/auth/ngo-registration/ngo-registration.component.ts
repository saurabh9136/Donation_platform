import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-ngo-registration',
  standalone: true,
  imports: [FormsModule , CommonModule],
  templateUrl: './ngo-registration.component.html',
  styleUrl: './ngo-registration.component.css'
})
export class NgoRegistrationComponent {
  ngo = {
    ngo_name: '',
    registration_number: '',
    email: '',
    mobileNumber: '',
    password: '',
    confirmPassword: '',
    contact_person: '',
    details : '',
    terms_conditions_path : '',
    address: '',
    country: '',
    city:''
  };

  apiErrorMessage: string = '';

  constructor(private http: HttpClient) {}

  onSubmit() {
    if (this.ngo.password !== this.ngo.confirmPassword) {
      this.apiErrorMessage = 'Passwords do not match.';
      return;
    }

    // Make an API call to register the user
    this.http.post('https://your-api-url/register', this.ngo)
      .pipe(
        // catchError(error => {
        //   this.apiErrorMessage = error.error.message || 'An error occurred during registration.';
        //   return throwError(error);
        // })
      )
      .subscribe(response => {
        // Handle successful response
        console.log('User registered successfully', response);
        this.apiErrorMessage = ''; // Clear error message on success
        // Redirect user or perform other actions
      });
  }
}
