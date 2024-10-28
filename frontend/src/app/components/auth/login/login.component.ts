import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common'; // Import CommonModule
import { CommonService } from '../../../services/common.service';
import { HttpClientModule } from '@angular/common/http';
import { StorageDataService } from '../../../services/storage-data.service';
import { NotificationService } from '../../../utility/toastr-notification/toastr-notification.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, CommonModule, HttpClientModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  providers: [NotificationService]
})
export class LoginComponent {

  email: string = '';
  password: string = '';
  apiErrorMessage: string | null = null;

  constructor(private commonService : CommonService, private storage : StorageDataService, private notify : NotificationService){}

  onSubmit() {
    if (!this.email || !this.password) {
      return;
    }
    const payload = {
      email: this.email,
      password: this.password
    };

    this.commonService.login(payload).subscribe(
      (res : any) => {
        if(res.user == 1){
          this.storage.setStorageData("user", 1, true);
        }else {
          this.storage.setStorageData("user", 0, true);
        }
       
        let token : string = res.access;
        this.storage.setStorageData("token", token, false);
        console.log(this.storage.getStorageData('user', true));
        console.log(this.storage.getStorageData('token', false));
        this.notify.success("Welcome : Successfully Logged in")
      },
      (error) => {
        this.notify.error(error)
      }
    )
  }
}
function jwtDecode(token: string) {
  throw new Error('Function not implemented.');
}

