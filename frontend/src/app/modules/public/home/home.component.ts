import { Component } from '@angular/core';
import { IProduct } from '@common/interfaces/IProduct';
import { ProductService } from '@common/services/public/products.service';
declare function mainJs(): any;

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  
  constructor(
    public _productService: ProductService
  ) {}

  ngOnInit() {
    mainJs();
    this.getProducts();
  }

  products: IProduct[] = [];

  getProducts() {
    const param = {
      page: 1,
      per_page: 8
    }
    this._productService.getProducts(param).subscribe(
      (res) => {
        res.data.map((item: any) => {
          item.color = "";
          item.size = "";
        })
        this.products = res.data;
      },
      (error) => {
        console.log(error);
      }
    );
  }
}
