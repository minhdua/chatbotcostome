import { Injector } from '@angular/core';
import { Component } from '@angular/core';
import { PageEvent } from '@angular/material/paginator';

import { ComponentBase } from '@common/componens/ComponentBase';
import { ITableHelper } from '@common/componens/helpers/TableHelper';
import { INlp } from '@common/interfaces/INlp';
import { NlpService } from '@common/services/public/nlp.service';

@Component({
  selector: 'app-nlp-management',
  templateUrl: './nlp-management.component.html',
  styleUrls: ['./nlp-management.component.scss'],
})
export class NlpManagementComponent extends ComponentBase {
  displayedColumns: string[] = ['id', 'tag', 'patterns', 'responses', 'action'];
  dataSource: INlp[] = [];
  tableHelper: ITableHelper = new this.tableHelperBase();

  constructor(injector: Injector, public _nlp: NlpService) {
    super(injector);
  }

  ngOnInit() {
    this.getNlpList();
  }

  getNlpList() {
    this.showLoading();
    const param = {
      page: this.tableHelper.table.currentPage + 1,
      per_page: this.tableHelper.table.pageSize,
    };
    this._nlp.getNlpList(param).subscribe(
      (res) => {
        this.dataSource = res.data;
        this.tableHelper.table.totalRecordsCount = res.total_records;
        this.hideLoading();
      },
      (error) => {
        this.hideLoading();
        console.log(error);
      }
    );
  }

  changePage(e: PageEvent) {
    if(e.pageSize != this.tableHelper.table.pageSize) {
      this.tableHelper.table.currentPage = 0;
    } else {
      this.tableHelper.table.currentPage = e.pageIndex;
    }
    this.tableHelper.table.pageSize = e.pageSize;
    this.getNlpList();
  }

  formatData(data: string) {
    return `${data.length > 0 ? data.slice(0, 15) : ''} ${
      data.length > 15 ? '...' : ''
    }`;
  }

  retrain() {
    this.showLoading();
    this._nlp.trainChatbot().subscribe(
      (res) => {
        this.confirmDialog.success('Retrain successfully');
        this.hideLoading();
      },
      (error) => {
        this.hideLoading();
        console.log(error);
      }
    );
  }

  deleteNlp(id: number) {
    this.confirmDialog.confirm('Are you sure want to delele this?').subscribe((data) => {
      if (data) {
        this.showLoading();
        this._nlp.deleteNlp(id).subscribe(
          (res) => {
            this.confirmDialog.success('Delete successfully');
            this.hideLoading();
            this.getNlpList();
          },
          (error) => {
            this.hideLoading();
            console.log(error);
          }
        );
      }
    });
  }
}
