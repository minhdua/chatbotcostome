import { Injectable } from '@angular/core';
import { BaseService } from '@common/services/base.service';
import { environment } from '@env/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NlpService {

  constructor(private _base: BaseService) { }

  /**
   * createOrEditNlp
   * @method POST /categories
   */
  createOrEditNlp(params: any): Observable<any> {
    const url = `${environment.apiUrl}/create_or_edit_intent`;
    return this._base.post(url, params, false);
  }

  /**
   * getNlpList
   * @method GET /get_intents
   */
  getNlpList(param: any): Observable<any> {
    const url = `${environment.apiUrl}/get_intents?page=${param.page}&per_page=${param.per_page}`;
    return this._base.get(url);
  }

  /**
   * getNlpDetails
   * @method GET /get_detail_intent
   */
  getNlpDetails(id: number): Observable<any> {
    const url = `${environment.apiUrl}/get_detail_intent/${id}`;
    return this._base.get(url);
  }

  /**
   * deleteNlp
   * @method DELETE /get_detail_intent/id
   */
  deleteNlp(id: number): Observable<any> {
    const url = `${environment.apiUrl}/delete_intent/${id}`;
    return this._base.delete(url);
  }

  /**
   * getNlpDetails
   * @method GET /train_chatbot
   */
  trainChatbot(): Observable<any> {
    const url = `${environment.apiUrl}/train_chatbot`;
    return this._base.get(url);
  }
}
