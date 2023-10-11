import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { SharedModule } from 'src/app/common/shared.module';
import { ShoppingCartComponent } from './shopping-cart.component';

const routes: Routes = [
  {
    path: '',
    component: ShoppingCartComponent,
  }
];

@NgModule({
  declarations: [
    ShoppingCartComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    RouterModule.forChild(routes),
  ]
})
export class ShoppingCartModule { }
