import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class LoadingService {

  loading$ = new BehaviorSubject(false);

  constructor(private _base: BaseService) { }

  toggleLoading(isShow: boolean) {
    this.loading$.next(isShow);
  }

}
