import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { UserRegistrationComponent } from './components/auth/user-registration/user-registration.component';
import { NgoRegistrationComponent } from './components/auth/ngo-registration/ngo-registration.component';
import { LoginComponent } from './components/auth/login/login.component';

export const routes: Routes = [
    {path: '',  component: HomeComponent},
    {path: 'home', component: HomeComponent},
    {path: 'user_signup', component: UserRegistrationComponent},
    {path: 'ngo_singup', component:NgoRegistrationComponent},
    {path: 'login', component:LoginComponent}

];
