import { Injectable } from '@angular/core';
import { IQuestion } from '@common/interfaces/IQuestion';
import { BaseService } from '@common/services/base.service';
import { environment } from '@env/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ChatbotService {
  constructor(private _base: BaseService) {}

  /**
   * sendQuestionByText
   * @method POST /chatbot
   * @return object: conversation
   */
  sendQuestionByText(question: IQuestion): Observable<any> {
    const url = `${environment.apiUrl}/chatbot`;
    return this._base.post(url, question, false);
  }

  /**
   * sendQuestionByImage
   * @method POST /upload_file
   * @body file_image: file
   * @return object: conversation
   */
  sendQuestionByImage(question: any): Observable<any> {
    const url = `${environment.apiUrl}/upload_file`;
    return this._base.post(url, question, true);
  }

  /**
   * getChatHistory
   * @method POST /get_histories
   * @body session_user: string
   * @body user_say: string
   * @return array: conversation
   */
  addHistory(body: any): Observable<any> {
    const url = `${environment.apiUrl}/add_history`;
    return this._base.post(url, body, true);
  }

  /**
   * getChatHistory
   * @method POST /get_history_by_session
   * @body session_user: string
   * @return array: conversation
   */
  getChatHistory(body: any): Observable<any> {
    const url = `${environment.apiUrl}/get_history_by_session`;
    return this._base.post(url, body, true);
  }
}
