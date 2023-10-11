import { Injectable } from '@angular/core';
import { BaseService } from '@common/services/base.service';
import { environment } from '@env/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ProductDetailsService {
  constructor(private _base: BaseService) {}

  /**
   * getProductDetail
   * @method GET /product
   * @param product_id ID của sản phẩm
   * @return Observable<any>: chi tiết sản phẩm
   */
  getProductDetails(product_id: number): Observable<any> {
    const url = `${environment.apiUrl}/products/${product_id}`;
    return this._base.get(url);
  }
}
