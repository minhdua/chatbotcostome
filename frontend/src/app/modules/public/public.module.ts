import { PaymentModule } from './payment/payment.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { SharedModule } from 'src/app/common/shared.module';
import { PublicComponent } from './public.component';
import { ShopDetailComponent } from './shop-detail/shop-detail.component';

const routes: Routes = [
  {
    path: '',
    component: PublicComponent,
    children: [
      {
        path: 'chatbot',
        loadChildren: () =>
          import('./chat-box/chat-box.module').then((x) => x.ChatBoxModule),
        data: { preload: true },
      },
      {
        path: 'home',
        loadChildren: () =>
          import('./home/home.module').then((x) => x.HomeModule),
        data: { preload: true },
      },
      {
        path: 'shop',
        loadChildren: () =>
          import('./shop/shop.module').then((x) => x.ShopModule),
        data: { preload: true },
      },
      {
        path: 'shopping-cart',
        loadChildren: () =>
          import('./shopping-cart/shopping-cart.module').then(
            (x) => x.ShoppingCartModule
          ),
        data: { preload: true },
      },
      {
        path: 'shop-detail/:id',
        loadChildren: () =>
          import('./shop-detail/shop-detail.module').then(
            (x) => x.ShopDetailModule
          ),
        data: { preload: true },
      },
      {
        path: 'shopping-cart/payment',
        loadChildren: () =>
          import('./payment/payment.module').then((x) => x.PaymentModule),
        data: { preload: true },
      },
    ],
  },
];

@NgModule({
  declarations: [PublicComponent, ShopDetailComponent],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    RouterModule.forChild(routes),
  ],
})
export class PublicModule {}
