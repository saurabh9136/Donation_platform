import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class ApiRouteService {
    private baseUrl: string = environment.apiBaseUrl;

  user: string = `${this.baseUrl}users/`;
  ngo: string = `${this.baseUrl}ngos/`;
  donation: string = `${this.baseUrl}donations/`;
  admin: string = `${this.baseUrl}admin/`;
  login: string = `${this.baseUrl}login/`;
  
}
