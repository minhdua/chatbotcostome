import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { SharedModule } from 'src/app/common/shared.module';
import { ReactiveFormsModule } from '@angular/forms';
import { PaymentComponent } from './payment.component';

const routes: Routes = [
  {
    path: '',
    component: PaymentComponent,
  }
];

@NgModule({
  declarations: [
    PaymentComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    ReactiveFormsModule,
    RouterModule.forChild(routes),
  ]
})
export class PaymentModule { }
