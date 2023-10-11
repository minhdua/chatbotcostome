import { Injector } from '@angular/core';
import { IProduct } from '@common/interfaces/IProduct';
import { TableHelper } from './helpers/TableHelper';
import { ConfirmDialogService } from '@common/services/confirmDialog.service';
import { LoadingService } from '@common/services/loading.service';

export abstract class ComponentBase {
  tableHelperBase = TableHelper;
  confirmDialog: ConfirmDialogService;
  loadingService: LoadingService;

  constructor(injector: Injector) {
    this.confirmDialog = injector.get(ConfirmDialogService);
    this.loadingService = injector.get(LoadingService);
  }

  getCart() {
    return localStorage.getItem('CART')
      ? JSON.parse(localStorage.getItem('CART') || '')
      : [];
  }

  deleteCart() {
    localStorage.removeItem('CART');
  }

  setCart(cart: IProduct[]) {
    localStorage.setItem('CART', JSON.stringify(cart));
  }

  addToCart(product: IProduct) {
    const cart = this.getCart();
    const productIndex = cart.findIndex(
      (item: IProduct) => item.id === product.id && item.size === product.size && item.color === product.color
    );
    if (productIndex != -1) {
      cart[productIndex].quantityInCart = product.quantityInCart + cart[productIndex].quantityInCart;
    } else {
      cart.push(product);
    }
    // if (productIndex != -1) {
    //   cart[productIndex].quantityInCart = quantityInCart
    //     ? quantityInCart
    //     : cart[productIndex].quantityInCart + 1;
    // } else {
    //   product.quantityInCart = quantityInCart ? quantityInCart : 1;
    //   cart.push(product);
    // }
    this.setCart(cart);
  }

  uuid() {
    var d = new Date().getTime();//Timestamp
    var d2 = ((typeof performance !== 'undefined') && performance.now && (performance.now()*1000)) || 0;//Time in microseconds since page-load or 0 if unsupported
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16;//random number between 0 and 16
        if(d > 0){//Use timestamp until depleted
            r = (d + r)%16 | 0;
            d = Math.floor(d/16);
        } else {//Use microseconds since page-load if supported
            r = (d2 + r)%16 | 0;
            d2 = Math.floor(d2/16);
        }
        return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
  }

  getUuid() {
    return localStorage.getItem('UUID') && JSON.parse(localStorage.getItem('UUID') || '');
  }

  setUuid() {
    localStorage.setItem('UUID', JSON.stringify(this.uuid()));
  }

  showLoading(): void {
    this.loadingService.toggleLoading(true);
  }

  hideLoading(): void {
    this.loadingService.toggleLoading(false);
  }
}
