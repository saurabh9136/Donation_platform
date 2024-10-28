export class Notification {  
    type: NotificationType | undefined;  
    message: string | undefined;  
}  
export enum NotificationType {  
    Success,  
    Error,  
    Info,  
    Warning  
} 