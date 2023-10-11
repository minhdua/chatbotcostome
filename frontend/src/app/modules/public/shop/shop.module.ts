/*
  1.Trong mảng routes, bạn đã định nghĩa một tuyến đường cho trang cửa hàng. Nó sẽ hiển thị ShopComponent khi đường dẫn (path) rỗng ('') được truy cập.

  2. Trong phần imports, bạn đã nhập các module cần thiết cho ShopModule:

  CommonModule: Đây là module cơ bản của Angular chứa các hàm và directive phổ biến. Nó được sử dụng để chia sẻ các phần tử giao diện người dùng cơ bản.

  FormsModule: Module này chứa các đối tượng và hàm hỗ trợ cho việc xử lý biểu mẫu (forms) trong ứng dụng.

  SharedModule: Đây có thể là một module tự tạo dựa trên các thành phần và chức năng chung của ứng dụng.

  RouterModule.forChild(routes): Bạn đã đăng ký các tuyến đường của module này bằng cách sử dụng RouterModule.forChild(). Điều này cho phép bạn xác định cách tuyến đường của ShopComponent sẽ được quản lý trong module này.

  declarations: Trong phần này, bạn đã khai báo ShopComponent là thành phần của module. Điều này có nghĩa là bạn có thể sử dụng ShopComponent trong module và trang web của bạn.
*/

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { SharedModule } from 'src/app/common/shared.module';
import { ShopComponent } from './shop.component';

// Định nghĩa các tuyến đường (routes) cho module cửa hàng
const routes: Routes = [
  {
    path: '',
    component: ShopComponent,
  }
];

@NgModule({
  declarations: [
    ShopComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    RouterModule.forChild(routes),
  ]
})
export class ShopModule { }
