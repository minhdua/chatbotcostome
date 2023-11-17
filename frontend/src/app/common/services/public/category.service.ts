import { Injectable } from '@angular/core';
import { BaseService } from '@common/services/base.service';
import { environment } from '@env/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class CategoryService {
  constructor(private _base: BaseService) {}

  /**
   * getCategories - get list categories
   * @method GET /categories
   * @return array: list categories
   */
  getCategories(): Observable<any> {
    const url = `${environment.apiUrl}/categories`;
    return this._base.get(url);
  }
}
