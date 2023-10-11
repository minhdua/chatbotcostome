import { Injectable } from '@angular/core';
import { BaseService } from '@common/services/base.service';
import { environment } from '@env/environment';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class ProductService {
  constructor(private _base: BaseService, private http: HttpClient) {}

  /**
   * getProducts - get list products
   * @method GET /products
   * @return array: list products
   */
  getProducts(param: any): Observable<any> {
    console.log(param);
    let url = `${environment.apiUrl}/products?page=${param.page}&per_page=${param.per_page}`;
    if (param.category) {
      url += `&category=${param.category}`;
    }
    if (param.color) {
      url += `&color=${param.color}`;
    }
    if (param.size) {
      url += `&size=${param.size}`;
    }
    if (param.attributes_predict) {
      url += `&attributes_predict=${param.attributes_predict}`;
    }
    if (param.categories_predict) {
      url += `&categories_predict=${param.categories_predict}`;
    }
    return this._base.get(url);
  }

  getColors(): Observable<any> {
    const url = `${environment.apiUrl}/colors`;
    return this._base.get(url);
  }

  getSizes(): Observable<any> {
    const url = `${environment.apiUrl}/sizes`;
    return this._base.get(url);
  }

  postProduct(data: any): Observable<any> {
    const url = `${environment.apiUrl}/products`;
    return this._base.post(url, data, false);
  }

  updateProduct(product_id: any, data: any): Observable<any> {
    const url = `${environment.apiUrl}/products/${product_id}`;
    return this._base.put(url, data, false);
  }

  postImg(product_id: any, data: any): Observable<any> {
    const url = `${environment.apiUrl}/products/${product_id}`;
    return this.http.post(url, data);
  }

  getProductDetails(product_id: number): Observable<any> {
    const url = `${environment.apiUrl}/products/${product_id}`;
    return this._base.get(url);
  }

  deleteProduct(product_id: number): Observable<any> {
    const url = `${environment.apiUrl}/products/${product_id}`;
    return this._base.delete(url);
  }
}
