import { Component, Injector, Inject } from '@angular/core';
import { ComponentBase } from '@common/componens/ComponentBase';
import { IProduct } from '@common/interfaces/IProduct';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { PaymentService } from '@common/services/public/payment.service';
import { IPayment } from '@common/interfaces/IPayment';
import { Router } from '@angular/router';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.scss'],
})
export class PaymentComponent extends ComponentBase {
  
    constructor(
        injector: Injector,
        private _paymentService: PaymentService,
        private formBuilder: FormBuilder,
        private _router: Router
    ) {
        super(injector);
    }

    products: IProduct[] = this.getCart() || []

    paymentForm!: FormGroup;

    ngOnInit() {
      this.paymentForm = this.formBuilder.group({
        fullName: ['', Validators.required],
        email: ['', [Validators.required, Validators.email]],
        address: ['', Validators.required],
        phone: ['', [Validators.required, Validators.pattern(/^\d{10,11}$/)]],
        note: ['']
      });
    }

    onPhoneInput(event: any) {
      // Loại bỏ tất cả các ký tự không phải số từ giá trị nhập liệu
      const inputValue = event.target.value;
      const numericValue = inputValue.replace(/[^0-9]/g, '');

      // Cập nhật giá trị trường phone với giá trị số mới
      this.paymentForm.get('phone')?.setValue(numericValue);

      // Kiểm tra chiều dài của số điện thoại
      if (numericValue.length < 10 || numericValue.length > 11) {
        this.paymentForm.get('phone')?.setErrors({ 'phoneLength': true });
      } else {
        this.paymentForm.get('phone')?.setErrors(null);
      }
    }

    sendPayment() {
      this.showLoading();
      const productsList: any[] = this.products.map(item => {
        return {
          order_color: item.color,
          order_size: item.size,
          product_id: item.id,
          quantity: item.quantityInCart
        };
      });

      let infomartionUser: IPayment = {
        fullname: this.paymentForm.get('fullName')?.value,
        email: this.paymentForm.get('email')?.value,
        address: this.paymentForm.get('address')?.value,
        phone: this.paymentForm.get('phone')?.value,
        // note: this.paymentForm.get('note')?.value,
        products: productsList,
        status: "Pending",
      };

      this._paymentService.sendOrderForUser(infomartionUser).subscribe(
        (res) => {
          this.deleteCart();

          this.hideLoading();
          this.confirmDialog.success('Order successfully').subscribe(item => this._router.navigate(['home']))
        },
        (error) => {
          this.hideLoading();
        }
      );
    }

    getTotalPrice() {
        let price = 0;
        this.products?.map((product: IProduct) => price += (product?.price || 0) * (product?.quantityInCart || 0));
        return price;
      }

    checkCart()
    {
      return this.products.length > 0 ? false : true;
    }
}