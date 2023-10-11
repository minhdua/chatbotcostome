import { Injectable } from '@angular/core';
import { BaseService } from '@common/services/base.service';
import { environment } from '@env/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PaymentService {

  constructor(private _base: BaseService) { }

  /**
   * sendOrderForUser
   * @method POST /orders
   * @return object: isPayment
   */
  sendOrderForUser(infomartionUser: any): Observable<any> {
    const url = `${environment.apiUrl}/orders`;
    return this._base.post(url, infomartionUser, false);
  }
}
