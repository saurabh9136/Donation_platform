# Danadiksha

Danadiksha is a donation platform where users can connect with NGOs, make donations, and receive transparency through tax relief certificates and video proof of their contributions. It includes JWT-based authentication and utilizes Django Rest Framework (DRF) for the backend and Angular for the frontend.

---
## Notes

- **Frontend Development**: The frontend component is under development. It will include user and NGO portals for donation management, donation tracking, and transparency features.
- **AWS Configuration**: AWS configuration is pending to securely store and manage NGO images, terms and conditions certificates, proof videos, and tax relief certificates.
## Project Flow

1. **User Registration and Login**  
   - Users and NGOs can independently register on the platform. 
   - Users receive a confirmation upon successful registration.
   - NGOs are registered to manage donation activities and update proofs.

2. **User Donation Process**
   - Users select an NGO and choose an amount to donate.
   - Upon donation, the platform deducts a platform commission and confirms the donation.
   - A tax relief certificate is generated and made available for download.

3. **NGO Proof and Certificate Upload**
   - NGOs upload proof of distribution (e.g., video, images) and necessary documentation.
   - The platform stores these files (to be configured on AWS).
   - Donors are notified once the proof is uploaded.

4. **Admin Management**
   - Admins have control over user and NGO accounts.
   - They manage homepage banners and control platform content as needed.

5. **User Dashboard and Donation History**
   - Users can view their donation history, download receipts, and check NGO updates.
   - Real-time updates will be implemented to keep users informed of NGO activities.

## Features

- **User and NGO Registration**: Users and NGOs can register and create accounts independently.
- **JWT Authentication**: Secures API endpoints with JWT-based token authentication.
- **Donation Management**: Users can donate to NGOs, who can then record proof of fund usage and upload tax certificates.
- **Transparency**: NGOs provide video evidence and tax certificates post-donation.
- **Role-Based Access**: Ensures secure access for users and NGOs.

---

## Tech Stack

- **Backend**: Django Rest Framework (DRF)
- **Frontend**: Angular with standalone components
- **Database**: SQLite

---

## API Endpoints

### 1. **User Registration** - `POST /api/users/register`
Registers a new user with the provided details.

**Request**:
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe@example.com",
  "password": "password123",
  "mobile_number": "1234567890",
  "city": "New York",
  "address": "1234 Elm Street",
  "country_region": "USA"
}
**Response**:
```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "email": "johndoe@example.com",
  "status": "Active"
}


### 2. **NGO Registration** - `POST /api/ngos/register`
Registers a new NGO with the provided details.

**Request**:
```json
{
  "ngo_name": "Animal Welfare",
  "email": "contact@animalwelfare.org",
  "password": "securepassword",
  "registration_number": "12345",
  "mobile_number": "1234567890",
  "city": "San Francisco",
  "address": "5678 Oak Street",
  "country_region": "USA"
}
**Response**:
```json
{
  "ngo_id": "123e4567-e89b-12d3-a456-426614174000",
  "email": "contact@animalwelfare.org",
  "status": "Active"
}

### 3. **User Login** - `POST /api/login`
Authenticates the user and returns a JWT token.

**Request**:
```json
{
  "email": "johndoe@example.com",
  "password": "password123"
}

**Response**:
```json
{
  "access": "<JWT Access Token>",
  "refresh": "<JWT Refresh Token>",
  User : 1 // indicating whether the user is Donator or NGO
}
### 4. **Create Donation** - `POST /api/donations/`
Creates a donation from a user to an NGO.

**Request**:
```json
{
  "user": "123e4567-e89b-12d3-a456-426614174000",
  "ngo": "987e6543-e89b-12d3-a456-426614174111",
  "amount": 100,
  "message": "For a better cause",
  "payment_method": "Credit Card"
}


**Response**:
```json
{
  "donation_id": "789e4567-e89b-12d3-a456-426614174333",
  "status": "Initialized",
  "amount": 100,
  "message": "For a better cause"
}

### 5. **Upload Tax Certificate and Video Proof** - `POST /api/donations/<donation_id>/upload_proof/`
Allows NGOs to upload tax certificates and video proofs for donations.

**Request**:
tax_certificate: (File)
video_proof: (File)

**Response**:
```json
{
  "status": "Success",
  "message": "Tax certificate and video proof uploaded successfully."
}


## Future Improvements

- **Email Notifications**: Integrate automated email notifications for users and NGOs upon donation, certificate upload, and registration.
- **Donation History & Reporting**: Add a history view for users to track past donations with downloadable reports.
- **Multiple Payment Methods**: Support additional payment options like PayPal and Stripe for flexible donations.
- **Real-Time Updates**: Enable real-time updates using WebSockets or similar technology to notify users of NGO activities.
- **Analytics Dashboard**: Provide NGOs with a dashboard for tracking donations, viewing reports, and analyzing donation trends.
- **Enhanced Security**: Add features like two-factor authentication (2FA) for better account security.


