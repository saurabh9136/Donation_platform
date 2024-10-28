import { Component } from '@angular/core';
import { NotificationService } from './toastr-notification.service';
import { Notification, NotificationType } from "./toastr-notification.model";
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-toastr-notification',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './toastr-notification.component.html',
  styleUrl: './toastr-notification.component.css'
})
export class ToastrNotificationComponent {
  notifications: Notification[] = [];

  constructor(public _notificationService: NotificationService) { }

  ngOnInit() {
      this._notificationService.getAlert().subscribe((alert: Notification) => {
          this.notifications = [];
          if (!alert) {
              this.notifications = [];
              return;
          }
          this.notifications.push(alert);
          setTimeout(() => {
              this.notifications = this.notifications.filter(x => x !== alert);
          }, 10000);
      });
  }

  removeNotification(notification: Notification) {
      this.notifications = this.notifications.filter(x => x !== notification);
  }

  /**Set css class for Alert -- Called from alert component**/
  cssClass(notification: Notification) {
      if (!notification) {
          return '';
      }
      switch (notification.type) {
          case NotificationType.Success:
              return 'toast-success';
          case NotificationType.Error:
              return 'toast-error';
          case NotificationType.Info:
              return 'toast-info';
          case NotificationType.Warning:
              return 'toast-warning';
      }
  }
}
