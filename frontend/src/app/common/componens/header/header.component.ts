import { Component, Injector } from '@angular/core';
import { Router } from '@angular/router';
import { ComponentBase } from '../ComponentBase';
import { IProduct } from '@common/interfaces/IProduct';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent extends ComponentBase {

  screens = [
    {
      name: 'Home',
      link: 'home'
    },
    {
      name: 'Shop',
      link: 'shop'
    },
  ];
  
  public href: string = "";

  constructor(
    private router: Router,
    injector: Injector
  ) {
    super(injector);
  }

  ngOnInit() {
    this.href = this.router.url.slice(1);
  }

  getTotalProduct() {
    const cart = this.getCart();
    let quantity = 0;
    cart.map((product: IProduct) => quantity += (product.quantityInCart || 0));
    return quantity;
  }

  getTotalPrice() {
    const cart = this.getCart();
    let price = 0;
    cart.map((product: IProduct) => price += ((product?.price || 0) * (product?.quantityInCart || 0)));
    return price;
  }

  goToShoppingCart() {
    const cart = this.getCart();
    cart.length > 0 && this.router.navigate(['shopping-cart']);
  }
}
