import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { SharedModule } from 'src/app/common/shared.module';
import { ShopDetailComponent } from './shop-detail.component';

const routes: Routes = [
  {
    path: '',
    component: ShopDetailComponent,
  },
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    RouterModule.forChild(routes),
  ],
})
export class ShopDetailModule {}
