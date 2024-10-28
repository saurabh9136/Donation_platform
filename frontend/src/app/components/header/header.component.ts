import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { StorageDataService } from '../../services/storage-data.service';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterModule, CommonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
  constructor(private storage : StorageDataService){}

  public loggedIn = false;
  public userLoggedin : any ;
  
  logout(){

  }
}
