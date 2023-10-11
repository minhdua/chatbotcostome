import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map } from 'rxjs/operators';
import { AuthService } from './auth/auth.service';

@Injectable({
  providedIn: 'root'
})
export class BaseService {

  headers: HttpHeaders;
  headersForm: HttpHeaders;

  constructor(
    private _http: HttpClient,
    private _auth: AuthService
  ) {
    this.headers = this.setHeaders();
    this.headersForm = this.setHeadersForm(); // for form
  }

  setHeaders(): HttpHeaders {
    const header = new HttpHeaders();
    return header.set('Content-Type', 'application/json');
  }

  setHeadersForm(): HttpHeaders { // for form
    const header = new HttpHeaders();
    return header.set('consumes', `multipart/form-data`);
  }

  updateHeader() {
    this.headers = this.setHeaders();
    this.headersForm = this.setHeadersForm(); // for form
    console.log('update header');
  }

  get(url: string) {
    return this._http.get(url, { headers: this.setHeaders() })
    .pipe(
      map(data => {
        return data;
      })
    );
  }

  post(url: string, obj: object, isForm: boolean) {
    return this._http.post(url, obj, { headers: isForm ? this.setHeadersForm() : this.setHeaders() })
    .pipe(
      map(data => {
        return data;
      })
    );
  }

  put(url: string, obj: object, isForm: boolean) {
    return this._http.put(url, obj, { headers: isForm ? this.setHeadersForm() : this.setHeaders() })
    .pipe(
      map(data => {
        return data;
      })
    );
  }

   delete(url: string) {
    return this._http.delete(url, { headers: this.setHeadersForm() })
    .pipe(
      map(data => {
        return data;
      })
    );
  }

  postNotify(url: string, obj: object) {
    return this._http.post(url, obj, { headers: this.setHeaders() })
    .pipe(
      map(data => {
        return data;
      })
    );
  }

  delete_with_body(url: string, obj: object) {
    const options = {
      headers: this.headers,
      body: obj
    };
    return this._http.delete(url, options)
      .pipe(
        map(data => {
          return data;
        })
      );
  }

  get_arraybuffer(url: string, isForm: boolean) {
    return this._http.get<any[]>(url, { headers: isForm ? this.setHeadersForm() : this.setHeaders(), responseType: 'arraybuffer' as 'json' })
      .pipe(
        map(data => {
          return data;
        })
      );
  }

}
