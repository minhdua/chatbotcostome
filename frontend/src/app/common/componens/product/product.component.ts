import { Component, Injector, Input } from '@angular/core';
import { ComponentBase } from '../ComponentBase';
import { IProduct } from '@common/interfaces/IProduct';
import { Router } from '@angular/router';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss'],
})
export class ProductComponent extends ComponentBase {
  constructor(injector: Injector, private router: Router) {
    super(injector);
    // const img = document.querySelector('.product__item__pic') as any;
    // img.style?.backgroundImage = 'ff';
  }

  @Input() product: IProduct = {
    id: 0,
    name: '',
    image_url: '',
    price: 0,
  };
  // @Input() isNew = false;
  // @Input() isSale = false;

  getImg() {
    return `url(${this.product?.image_url})`;
  }

  addProductToCart() {
    this.addToCart(this.product);
  }

  goToShopDetail(shopId: any): void {
    this.router.navigate(['/shop-detail', shopId]);
  }
}
