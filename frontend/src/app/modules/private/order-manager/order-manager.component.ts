import { Inject, Injector } from '@angular/core';
import { Component } from '@angular/core';
import { ComponentBase } from '@common/componens/ComponentBase';
import { ITableHelper } from '@common/componens/helpers/TableHelper';
import { OrderService } from '@common/services/public/order.service';
import { PageEvent } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { OrderEnum } from '@common/enum/order';

@Component({
  selector: 'app-order-manager',
  templateUrl: './order-manager.component.html',
  styleUrls: ['./order-manager.component.scss'],
})
export class OrderManagerComponent extends ComponentBase {
  displayedColumns: string[] = [
    'id',
    'fullname',
    'email',
    'address',
    'phone',
    'status',
    'action',
  ];

  filterValues: any = {};
  filterSelectObj: any = [];
  dataSource = new MatTableDataSource();
  tableHelper: ITableHelper = new this.tableHelperBase();
  cachedOrderStatusOptions = Object.values(OrderEnum);

  constructor(
    injector: Injector, 
    public _orderService: OrderService,
  ) {
    super(injector);

    // Object to create Filter for
    this.filterSelectObj = [
      {
        name: 'STATUS',
        columnProp: 'status',
        options: this.cachedOrderStatusOptions,
        modelValue: ''
      }
    ]
  }

  ngOnInit() {
    this.getOrders();

    // Overrride default filter behaviour of Material Datatable
    this.dataSource.filterPredicate = this.createFilter();
  }

  // Called on Filter change
  filterChange(filter: any, event: any) {
    this.filterValues[filter.columnProp] = event.value.trim().toLowerCase();
    this.dataSource.filter = JSON.stringify(this.filterValues);
    this.getOrders();
  }

  // When load page in the first time
  // When you click filterChange() for status or anything else .... 
  createFilter() {
    let filterFunction = function (data: any, filter: string): boolean {
      let searchTerms = JSON.parse(filter);
      let isFilterSet = false;

      for (const col in searchTerms) {
        if (searchTerms[col].toString() !== '') {
          isFilterSet = true;
        } else {
          delete searchTerms[col];
        }
      }

      let nameSearch = () => {
        let found = false;
        if (isFilterSet) {
          for (const col in searchTerms) {
            searchTerms[col].trim().toLowerCase().split(' ').forEach((word: any) => {
              if (data[col].toString().toLowerCase().indexOf(word) != -1 && isFilterSet) {
                found = true;
              }
            });
          }
          return found;
        } else {
          return true;
        }
      }
      
      return nameSearch();
    }
    return filterFunction;
  }

  getOrders() {
    this.showLoading();
    // Input curentPage and pageSize of Orders page admin
    const param = {
      page: this.tableHelper.table.currentPage + 1,
      per_page: this.tableHelper.table.pageSize,
      status: this.filterSelectObj[0].modelValue,
    };

    this._orderService.getOrders(param).subscribe(
      (res) => {
        this.hideLoading();
        // Get data into dataSource and order by id
        this.dataSource.data = res.data.sort((a: any, b: any) => {
          return a.id - b.id;
        });

        this.tableHelper.table.totalRecordsCount = res.total;
      },
      (error) => {
        this.hideLoading();
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
    this.getOrders();
  }

  openDialogDelete(id: number){
    this.confirmDialog.confirm('Are you sure want to delele this?').subscribe((data) => {
      if (data) {
        this.deleteOrder(id);
      }
    });
  }

  deleteOrder(id: number){
    this.showLoading();
    let param = {
      order_id : id,
      status: OrderEnum.CANCELLED,
    }
    this._orderService.deleteOrderById(param).subscribe((res) => {
      window.location.reload();
      this.hideLoading();
    }, 
    (error) => {
      this.hideLoading();
    })
  }
}
