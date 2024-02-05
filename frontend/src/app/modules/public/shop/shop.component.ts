/*
  1. Khai báo các biến để lưu danh sách sản phẩm, danh sách danh mục, danh sách kích thước, danh sách màu sắc, và các biến liên quan đến việc lọc sản phẩm.

  2. Trong hàm ngOnInit(), bạn gọi hàm mainJs() để thực hiện một tác vụ JavaScript tùy chỉnh. Sau đó, bạn gọi các hàm getParam(), getCategories(), và getProducts() để lấy thông tin từ URL, danh mục sản phẩm và danh sách sản phẩm.

  3. Hàm getParam() được sử dụng để lấy các tham số từ URL, chẳng hạn như danh mục, kích thước, màu sắc, thuộc tính dự đoán và danh mục dự đoán.

  4. Hàm getCategories() sử dụng dịch vụ CategoryService để lấy danh sách danh mục sản phẩm từ máy chủ.

  5. Hàm getProducts() sử dụng dịch vụ ProductService để lấy danh sách sản phẩm dựa trên các bộ lọc được áp dụng.

  6. Hàm chooseFillterType() được gọi khi người dùng chọn một loại lọc (danh mục, màu sắc, kích thước) và nó thay đổi các biến liên quan đến việc lọc sản phẩm và sau đó gọi lại hàm getProducts() để cập nhật danh sách sản phẩm dựa trên lựa chọn của người dùng.
*/

import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ICategory } from '@common/interfaces/ICategory';
import { IProduct } from '@common/interfaces/IProduct';
import { CategoryService } from '@common/services/public/category.service';
import { ProductService } from '@common/services/public/products.service';
declare function mainJs(): any;

@Component({
  selector: 'app-shop',
  templateUrl: './shop.component.html',
  styleUrls: ['./shop.component.scss'],
})
export class ShopComponent {
  // Danh sách sản phẩm
  products: IProduct[] = [];

  // Danh sách danh mục sản phẩm
  categories: ICategory[] = [];

  // Danh sách kích thước sản phẩm
  sizes = ['S', 'M', 'L', 'XL', 'XXL'];

  // Danh sách màu sắc sản phẩm
  colors = ['WHITE', 'BLUE' ,'GREEN' , 'YELLOW', 'ORANGE', 'PINK', 'GREY', 'RED', 'BLACK', 'BROWN', 'PURPLE'];

  // Màu sắc được chọn
  color = '';

  // Kích thước được chọn
  size = '';

  // Giá nhỏ
  price_min = '';

  // Giá lớn
  price_max = '';

  // Thuộc tính dự đoán
  attributes_predict = '';

  // Danh mục dự đoán
  categories_predict = '';

  // Sản phẩm dự đoán
  products_predict = '';

  // Danh sách danh mục được lọc
  filterCategories: string[] = [];

  // Biến kiểm tra xem đang tải dữ liệu hay không
  isLoading = false;

  constructor(
    private _categoryService: CategoryService,
    private _productService: ProductService,
    private _route: ActivatedRoute
  ) {}

  ngOnInit() {
    // Gọi hàm JavaScript tùy chỉnh
    mainJs();

    // Lấy tham số từ URL
    this.getParam();

    // Lấy danh mục sản phẩm
    this.getCategories();

    // Lấy danh sách sản phẩm
    this.getProducts();
  }

  // Lấy tham số từ URL
  getParam() {
    this._route.queryParams.subscribe((params) => {
      const { 
        category, 
        size, 
        color, 
        price_min, 
        price_max, 
        attributes_predict, 
        categories_predict, 
        products_predict 
      } = params;

      if (category) {
        this.filterCategories = category && category.split(',');
      }

      this.size = size || '';
      this.color = color || '';
      this.price_min = price_min || '';
      this.price_max = price_max || '';
      this.attributes_predict = attributes_predict || '';
      this.categories_predict = categories_predict || '';
      this.products_predict = products_predict || '';
    });
  }

  // Lấy danh mục sản phẩm
  getCategories() {
    this._categoryService.getCategories().subscribe(
      (res) => {
        this.categories = res.data;
      },
      (error) => {
        console.log(error);
      }
    );
  }

  // Lấy danh sách sản phẩm
  getProducts() {
    this.isLoading = true;
    const param = {
      page: 1,
      per_page: 200,
      category: this.filterCategories.toString(),
      color: this.color,
      size: this.size,
      price_min: this.price_min,
      price_max: this.price_max,
      attributes_predict: this.attributes_predict,
      categories_predict: this.categories_predict,
      products_predict: this.products_predict,
    };
   
    this._productService.getProducts(param).subscribe(
      (res) => {
        this.products = res.data;
        this.isLoading = false;
      },
      (error) => {
        console.log(error);
        this.isLoading = false;
      }
    );
  }

  // Chọn loại lọc (danh mục, màu sắc, kích thước)
  chooseFillterType(name: string | number | undefined, type: string) {
    if (name) {
      const stringValue = name.toString();
      if (type === 'category' && name) {
        const index = this.filterCategories.findIndex(
          (item) => item === stringValue
        );
      }
      if (type === 'color') {
        this.color = this.color === stringValue ? '' : stringValue;
      }
      if (type === 'size') {
        this.size = this.size === stringValue ? '' : stringValue;
      }
      // Lấy lại danh sách sản phẩm sau khi áp dụng bộ lọc
      this.getProducts();
    }
  }

  //Lọc giá từ giá nhỏ nhất
  onChangePriceMin(value_min: string): void {
    this.price_min = value_min;
    this.getProducts();
  }

  // Lọc giá đến giá cao nhất
  onChangePriceMax(value_max: string): void {
    this.price_max = value_max;
    this.getProducts();
  }

}