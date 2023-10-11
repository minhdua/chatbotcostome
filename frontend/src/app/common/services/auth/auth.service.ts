import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})

export class AuthService {

  isLoggedIn = false;

  constructor(
    private _http: HttpClient,
  ) {
    if(this.getToken()) {
      this.isLoggedIn = true
    }
  }

  getToken() {
    return localStorage.getItem('TOKEN');
  }

  setToken() {
    localStorage.setItem('TOKEN', 'TOKEN');
  }
}
