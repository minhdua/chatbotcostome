import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, CanActivateChild, CanLoad, Route, Router, RouterStateSnapshot } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable()
export class AuthGuard implements CanActivate, CanActivateChild, CanLoad {
  constructor(private _auth: AuthService, private router: Router) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    const url: string = state.url;

    return this.checkLogin(url);
  }

  canActivateChild(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    return this.canActivate(route, state);
  }

  // #docregion, canLoad
  canLoad(route: Route): boolean {
    const url = `/${route.path}`;

    return this.checkLogin(url);
  }
  // #enddocregion canLoad
  checkLogin(url: string): boolean {

    if (this._auth.isLoggedIn) { return true; }

    // Navigate to the login page with extras
    this.router.navigate(['/auth/login']);
    return false;
  }
  // #docregion admin-can-load
}
