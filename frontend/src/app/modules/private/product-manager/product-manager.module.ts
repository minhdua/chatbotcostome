import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ProductManagerComponent } from './product-manager.component';
import { SharedModule } from '@common/shared.module';
import { CreateProductComponent } from './create-product/create-product.component';
import { EditProductComponent } from './edit-product/edit-product.component';

const routes: Routes = [
  {
    path: '',
    component: ProductManagerComponent,
  },
  {
    path: 'create-product',
    component: CreateProductComponent,
  },
  {
    path: ':id',
    component: EditProductComponent,
  },
];

@NgModule({
  declarations: [
    ProductManagerComponent,
    CreateProductComponent,
    EditProductComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    RouterModule.forChild(routes)
  ],
})
export class ProductManagerModule {}
