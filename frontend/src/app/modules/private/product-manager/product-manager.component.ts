import { Injector } from '@angular/core';
import { Component } from '@angular/core';
import { PageEvent } from '@angular/material/paginator';

import { ComponentBase } from '@common/componens/ComponentBase';
import { ITableHelper } from '@common/componens/helpers/TableHelper';
import { ProductService } from '@common/services/public/products.service';
import { CategoryService } from '@common/services/public/category.service';
import { ICategory } from '@common/interfaces/ICategory';
import { Router } from '@angular/router';

@Component({
  selector: 'app-product-manager',
  templateUrl: './product-manager.component.html',
  styleUrls: ['./product-manager.component.scss'],
})
export class ProductManagerComponent extends ComponentBase {

  // Các cột hiển thị trong bảng sản phẩm
  displayedColumns: string[] = ['id', 'img', 'name', 'price', 'action'];
  // Dữ liệu cho bảng
  dataSource = [];
  // Đối tượng trợ giúp quản lý bảng
  tableHelper: ITableHelper = new this.tableHelperBase();
  // Danh sách danh mục sản phẩm
  categories: ICategory[] = [];

  animal?: string;
  name?: string;

  constructor(
    injector: Injector,
    public _productService: ProductService,
    private _categoryService: CategoryService,
    private _router: Router,
  ) {
    super(injector);
    this.getProducts();
    this.getCategories();
  }

  // Hàm lấy danh sách danh mục sản phẩm
  getCategories() {
    this._categoryService.getCategories().subscribe(
      (res) => {
        this.categories = res.data;
        console.log(res.data);
      },
      (error) => {
        console.log(error);
      }
    );
  }

  // Hàm lấy danh sách sản phẩm
  getProducts() {
    // hiển thị loading
    this.showLoading();
    const param = {
      page: this.tableHelper.table.currentPage + 1,
      per_page: this.tableHelper.table.pageSize,
    };
    // call api trên backend để lấy dữ liệu về
    this._productService.getProducts(param).subscribe(
      (res) => {
        // thành công ẩn loading
        this.hideLoading();
        // gán data vào bảng
        this.dataSource = res.data;
        this.tableHelper.table.totalRecordsCount = res.total;
      },
      (error) => {
        // lỗi ẩn loading
        this.hideLoading();
        console.log(error);
      }
    );
  }

  // Hàm thay đổi trang trong bảng sản phẩm
  changePage(e: PageEvent) {
    if (e.pageSize != this.tableHelper.table.pageSize) {
      this.tableHelper.table.currentPage = 0;
    } else {
      this.tableHelper.table.currentPage = e.pageIndex;
    }
    this.tableHelper.table.pageSize = e.pageSize;
    this.getProducts();
  }

  // Hàm xử lý xóa sản phẩm
  onDelele = (id: number) => {
    this.confirmDialog.confirm('Are you sure want to delele this?').subscribe((data) => {
      if (data) {
        this.showLoading();
        this._productService.deleteProduct(id).subscribe(
          (res) => {
            this.hideLoading();
            this.confirmDialog
              .success('Product delete successfully.')
              .subscribe((res) => {
                this._router.routeReuseStrategy.shouldReuseRoute = () => false;
                this._router.onSameUrlNavigation = 'reload';
                this._router.navigate([this._router.url]);
              });
          },
          (error) => {
            console.log(error);
            this.hideLoading();
          }
        );
      }
    });
  };
}
