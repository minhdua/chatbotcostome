import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NavigateService {


  toggleSidebar$ = new BehaviorSubject<any>({});

  constructor(private _router: Router) { }

  getURLs() {
    this.urls = this._router.url;
  }

  get urls() {
    return JSON.parse(localStorage.getItem('URLS') || '') || {};
  }

  set urls(url) {
    localStorage.setItem('URLS', JSON.stringify(url));
  }
}
