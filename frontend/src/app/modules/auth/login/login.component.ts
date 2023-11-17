import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '@common/services/auth/auth.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;

  constructor(
    private _auth: AuthService,
    private _router: Router,
    private formBuilder: FormBuilder,
  ) {}

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      fullName: ['admin', Validators.required],
      password: ['admin', Validators.required],
    });
  }

  login() {
    this._auth.isLoggedIn = true;
    this._auth.setToken();
    this._router.navigate(['admin']);
  }
}
