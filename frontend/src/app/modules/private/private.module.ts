import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { SharedModule } from 'src/app/common/shared.module';
import { PrivateComponent } from './private.component';

const routes: Routes = [
  {
    path: '',
    component: PrivateComponent,
    children: [
      {
        path: '',
        redirectTo: '/admin/products',
        pathMatch: 'full',
      },
      {
        path: 'products',
        loadChildren: () => import('./product-manager/product-manager.module').then(x => x.ProductManagerModule),
        data: { preload: true }
      },
      {
        path: 'orders',
        loadChildren: () => import('./order-manager/order-manager.module').then(x => x.OrderManagerModule),
        data: { preload: true }
      },
      {
        path: 'nlp',
        loadChildren: () => import('./nlp-management/nlp-management.module').then(x => x.NlpManagementModule),
        data: { preload: true }
      }
    ]
  }
];

@NgModule({
  declarations: [
    PrivateComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    RouterModule.forChild(routes)
  ]
})
export class PrivateModule { }
