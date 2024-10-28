import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StorageDataService {

  constructor() { }
  
  setStorageData(storageName: string, data: any, isJson: boolean) {
    if (isJson)
      localStorage.setItem(storageName, JSON.stringify(data));
    else
      localStorage.setItem(storageName, data);
  }

  getStorageData(storageName: string, isJson: boolean) {
    let data: any = localStorage.getItem(storageName);
    if (isJson)
      return JSON.parse(data);
    else
      return data;
  }

  getStorageDataModel(storageName: string, isJson: boolean, model: any) {
    let data: any = localStorage.getItem(storageName);
    if (isJson)
      return JSON.parse(data, model);
    else
      return data;
  }

  clearStorageData(storageName: string) {
    localStorage.removeItem(storageName);
  }

  cleanAll() {
    localStorage.clear();
  }

  getLocalStorageData(storageName: string, isJson: boolean) {
    let data: any = localStorage.getItem(storageName);
    if (isJson)
      return JSON.parse(data);
    else
      return data;
  }

  clearLocalStorageData(storageName: string) {
    localStorage.removeItem(storageName);
  }

  cleanLocalStorageAll() {
    localStorage.clear();
  }

  setSessionStorageData(storageName: string, data: any, isJson: boolean) {
    if (isJson)
      sessionStorage.setItem(storageName, JSON.stringify(data));
    else
      sessionStorage.setItem(storageName, data);
  }

  getSessionStorageData(storageName: string, isJson: boolean) {
    let data: any = sessionStorage.getItem(storageName);
    if (isJson)
      return JSON.parse(data);
    else
      return data;
  }

  cleanSessionStorageAll() {
    sessionStorage.clear();
  }
}
