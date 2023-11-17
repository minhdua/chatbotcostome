import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { SharedModule } from '@common/shared.module';
import { NlpManagementComponent } from './nlp-management.component';
import { NlpCreateOrEditComponent } from './nlp-create-or-edit/nlp-create-or-edit.component';

const routes: Routes = [
  {
    path: '',
    component: NlpManagementComponent,
  },
  {
    path: 'nlp-detail/:id',
    component: NlpCreateOrEditComponent,
  }
];

@NgModule({
  declarations: [NlpManagementComponent, NlpCreateOrEditComponent],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    RouterModule.forChild(routes),
  ]
})
export class NlpManagementModule { }
