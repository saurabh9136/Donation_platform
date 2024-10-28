import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiRouteService } from '../utility/app.refrence';

@Injectable({
  providedIn: 'root'
})
export class CommonService {
  constructor(private httpClientService: HttpClient, private apiPath: ApiRouteService) {}

  login(payload: any) {
    return this.httpClientService.post(this.apiPath.login, payload);
  }

  userRegistration(payload : any){
    return this.httpClientService.post(this.apiPath.user, payload);
  }

  ngoRegistration(payload : any){
    return this.httpClientService.post(this.apiPath.ngo, payload);
  }
  logout(){
    
  }
}
