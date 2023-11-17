import { Injector } from '@angular/core';
import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ComponentBase } from '@common/componens/ComponentBase';
import { IPayment } from '@common/interfaces/IPayment';
import { OrderService } from '@common/services/public/order.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-get-order-detail',
  templateUrl: './get-order-detail.component.html',
  styleUrls: ['./get-order-detail.component.scss'],
})
export class GetOrderDetailComponent extends ComponentBase {
  constructor(
    injector: Injector, 
    public _orderService: OrderService, 
    private route: ActivatedRoute,
    private location: Location
  ){ 
    super(injector);
  }

  idOrder!: number;
  userOrderInfo: IPayment = {};
  orderStatus: string[] = [];
  currentStatus!: string | undefined;
  
  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    this.idOrder = +id!;

    if(id) {
       this.getOrderStatus();
       this.getOrderById(+id);
    }
  }

  getOrderById(id: number) {
    this.showLoading();
    this._orderService.getOrderById(id).subscribe(
      (res) => {
        this.hideLoading();
        this.userOrderInfo = res.data;
        this.currentStatus = this.userOrderInfo?.status;
      },
      (error) => {
        this.hideLoading();
      }
    );
  }

  getOrderStatus(){
    this._orderService.getOrdersStatus().subscribe(
      (res) => {
        this.orderStatus = res.data;
      },
      (error) => {
        console.log(error);
      }
    );
  }

  getTotalPrice() {
    let price = 0;
    this.userOrderInfo?.products?.map(
      (product: any) =>
        (price += (product?.price || 0) * (product?.quantity || 0))
    );
    return price;
  }

  // Update status of Billing
  handleBilling(){
    let param = {
      order_id : this.idOrder,
      status: this.currentStatus,
    }
    
    this._orderService.updateStatusOrder(param).subscribe(
      () => {
        window.location.reload();
      },
      (error) => {
        console.log(error);
      }
    );
  }

  checkChangeStatus() {
    return this.currentStatus == this.userOrderInfo?.status ? true : false
  }

  goBack(): void {
    this.location.back();
  }
  
}
