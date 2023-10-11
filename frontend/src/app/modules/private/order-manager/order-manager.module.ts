import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { OrderManagerComponent } from './order-manager.component';
import { SharedModule } from '@common/shared.module';
import { GetOrderDetailComponent } from './get-order-detail/get-order-detail.component';

const routes: Routes = [
  {
    path: '',
    component: OrderManagerComponent,
  },
  {
    path: ':id',
    component: GetOrderDetailComponent,
  },
];

@NgModule({
  declarations: [OrderManagerComponent, GetOrderDetailComponent],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    RouterModule.forChild(routes),
  ],
})
export class OrderManagerModule {}
