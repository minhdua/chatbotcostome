import { Injectable } from '@angular/core';
import { BaseService } from '@common/services/base.service';
import { environment } from '@env/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class OrderService {
  constructor(private _base: BaseService) {}

  /**
   * getOrdersStatus - get list orders statuses
   * @method GET /order-statuses
   * @return array: list orders statuses
   */
  getOrdersStatus(): Observable<any> {
    let url = `${environment.apiUrl}/order-statuses`;
    return this._base.get(url);
  }

  /**
   * getOrders - get list orders
   * @method GET /orders
   * @return array: list orders
   */
  getOrders(param: any): Observable<any> {
    let url = `${environment.apiUrl}/orders?page=${param.page}&per_page=${param.per_page}&status=${param.status}`;
    return this._base.get(url);
  }

  /**
   * getOrderById - get detail order
   * @method GET /orders/{order_id}
   * @return Single(): list order detail
   */
    getOrderById(id: number): Observable<any> {
      let url = `${environment.apiUrl}/orders/${id}`;
      return this._base.get(url);
    }

    /**
   * updateStatusOrder - update status billing
   * @method PUT /update_status_order
   * @return Single(): update status for billing order
   */
    updateStatusOrder(param: any): Observable<any> {
      let url = `${environment.apiUrl}/update_status_order`;
      return this._base.put(url, param, false);
    }

    /**
   * deleteOrderById - delete order bill
   * @method PUT /update_status_order
   * @return Single(): update status cancel for billing order
   */
    deleteOrderById(param: any): Observable<any> {
      let url = `${environment.apiUrl}/update_status_order`;
      return this._base.put(url, param, false);
    }
}
