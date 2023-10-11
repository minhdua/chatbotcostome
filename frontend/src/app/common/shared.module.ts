import { NgModule } from '@angular/core';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatCardModule } from '@angular/material/card';
import { MatMenuModule } from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatPaginatorModule } from '@angular/material/paginator';

import { HeaderComponent } from './componens/header/header.component';
import { DashboardComponent } from './componens/dashboard/dashboard.component';
import { CommonModule } from '@angular/common';
import { NavigationComponent } from './componens/navigation/navigation.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { ProductComponent } from './componens/product/product.component';
import { RouterModule } from '@angular/router';
import { MatTableModule } from '@angular/material/table';
import { ChatBoxComponent } from './componens/chat-box/chat-box.component';
import { MatDialogModule } from '@angular/material/dialog';
import { ReactiveFormsModule } from '@angular/forms';
import { FooterComponent } from './componens/footer/footer.component';
import { MatSortModule } from '@angular/material/sort';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatRadioModule } from '@angular/material/radio';
import { MatChipsModule } from '@angular/material/chips';
import { MatOptionModule } from '@angular/material/core';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { ComfirmDialogComponent } from './componens/comfirm-dialog/comfirm-dialog.component';
import { LoadingComponent } from './componens/loading/loading.component';

@NgModule({
  declarations: [
    HeaderComponent,
    DashboardComponent,
    NavigationComponent,
    ProductComponent,
    ChatBoxComponent,
    FooterComponent,
    ComfirmDialogComponent,
    LoadingComponent
  ],
  imports: [
    RouterModule,
    CommonModule,
    MatGridListModule,
    MatCardModule,
    MatMenuModule,
    MatIconModule,
    MatButtonModule,
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatTableModule,
    MatDialogModule,
    ReactiveFormsModule,
    MatPaginatorModule,
    MatSortModule,
    MatInputModule,
    MatSelectModule,
    MatRadioModule,
    MatChipsModule,
    MatOptionModule,
    MatSelectModule,
    MatChipsModule,
    MatTooltipModule,
    MatSnackBarModule
  ],
  exports: [
    HeaderComponent,
    DashboardComponent,
    NavigationComponent,
    ProductComponent,
    ChatBoxComponent,
    FooterComponent,
    ComfirmDialogComponent,  
    LoadingComponent,

    ReactiveFormsModule,
    MatGridListModule,
    MatCardModule,
    MatMenuModule,
    MatIconModule,
    MatButtonModule,
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatTableModule,
    MatDialogModule,
    MatPaginatorModule,
    MatInputModule,
    MatSelectModule,
    MatRadioModule,
    MatChipsModule,
    MatOptionModule,
    MatSelectModule,
    MatChipsModule,
    MatTooltipModule,
    MatSnackBarModule
  ],
})
export class SharedModule {}
