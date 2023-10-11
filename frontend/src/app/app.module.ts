import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { AuthGuard } from '@common/services/auth/author-guard.service';
import { SharedModule } from '@common/shared.module';

const routes: Routes = [
  {
    path: '',
    redirectTo: '/chatbot',
    pathMatch: 'full',
  },
  {
    path: 'admin',
    loadChildren: () =>
      import('./modules/private/private.module').then((x) => x.PrivateModule),
    canActivate: [AuthGuard],
    data: { preload: true },
  },
  {
    path: 'auth',
    loadChildren: () =>
      import('./modules/auth/auth.module').then((x) => x.AuthModule)
  },
  {
    path: '',
    loadChildren: () =>
      import('./modules/public/public.module').then((x) => x.PublicModule),
  },
];

@NgModule({
  declarations: [AppComponent],
  imports: [
    HttpClientModule,
    BrowserModule,
    SharedModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(routes),
    ReactiveFormsModule,
  ],
  providers: [AuthGuard],
  bootstrap: [AppComponent],
})
export class AppModule {}
