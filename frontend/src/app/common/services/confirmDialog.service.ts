import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ComfirmDialogComponent } from '@common/componens/comfirm-dialog/comfirm-dialog.component';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root',
})
export class ConfirmDialogService {

    constructor(
        private _dialog: MatDialog,
    ) {
    }

    confirm(detail: string, title?: string, closeBtn?: string, submitBtn?: string): Observable<any> {
        return this._dialog.open(ComfirmDialogComponent, {
            panelClass: 'loyalty-modal',
            data: { type: 'warning', title: title || 'Warning', detail, closeBtn, submitBtn }
        }).afterClosed();
    }

    success(detail: string): Observable<any> {
        return this._dialog.open(ComfirmDialogComponent, {
            panelClass: 'loyalty-modal',
            data: { type: 'success', title: 'Congratulations', detail }
        }).afterClosed();
    }

    error(detail: string): Observable<any> {
        return this._dialog.open(ComfirmDialogComponent, {
            panelClass: 'loyalty-modal',
            data: { type: 'error', title: '', detail }
        }).afterClosed();
    }

    info(title: string, detail: string) {
        return this._dialog.open(ComfirmDialogComponent, {
            panelClass: 'loyalty-modal',
            data: { type: 'info', title, detail }
        }).afterClosed();
    }
}
