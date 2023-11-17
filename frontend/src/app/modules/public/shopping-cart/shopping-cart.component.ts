import { Component, Injector } from '@angular/core';
import { ComponentBase } from '@common/componens/ComponentBase';
import { IProduct } from '@common/interfaces/IProduct';
declare function mainJs(): any;

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.scss'],
})
export class ShoppingCartComponent extends ComponentBase {
  cart: IProduct[] = this.getCart() || [];

  constructor(injector: Injector) {
    super(injector);
  }

  ngOnInit() {
    mainJs()
  }

  getImg(img: string | undefined) {
    return `${img}`;
  }

  changeQuality(quantity: number, index: number) {
    this.cart[index].quantityInCart = +quantity;
    this.setCart(this.cart);
  }

  getTotalPrice() {
    let price = 0;
    this.cart.map(
      (product: IProduct) =>
        (price += (product?.price || 0) * (product?.quantityInCart || 0))
    );
    return price;
  }

  removeItemFromCart(index: number) {
    this.cart.splice(index, 1);
    this.setCart(this.cart);
  }
}
