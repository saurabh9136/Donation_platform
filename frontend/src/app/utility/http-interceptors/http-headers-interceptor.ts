import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { CommonService } from "../../services/common.service";
import { StorageDataService } from "../../services/storage-data.service";


@Injectable()
export class HttpHeadersInterceptor implements HttpInterceptor {

    constructor(private storage: StorageDataService, private commonService : CommonService){}

    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        throw new Error("Method not implemented.");
    }

}