import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { HomeComponent } from './home.component';
import { SharedModule } from 'src/app/common/shared.module';

const routes: Routes = [
  {
    path: '/home',
    component: HomeComponent,
  }
];

@NgModule({
  declarations: [
    HomeComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    RouterModule.forChild(routes),
  ]
})
export class HomeModule { }
