import { Component, inject } from '@angular/core';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';
import { Router } from '@angular/router';

const ELEMENT_DATA: any[] = [
  { id: 1, name: 'Products', link: 'admin/products' },
  { id: 2, name: 'NLP', link: 'admin/nlp' },
  { id: 3, name: 'CNN', link: 'admin/CNN' },
  { id: 4, name: 'Orders', link: 'admin/orders' },
];

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss'],
})
export class NavigationComponent {
  private breakpointObserver = inject(BreakpointObserver);

  isHandset$: Observable<boolean> = this.breakpointObserver
    .observe(Breakpoints.Handset)
    .pipe(
      map((result) => result.matches),
      shareReplay()
    );
  
  public href: string = "";

  screens = ELEMENT_DATA;
  screen = '';

  constructor(
    private router: Router
  ) {}

  ngOnInit() {
    this.href = this.router.url.slice(1);
    const index = this.screens.findIndex((item: any) => item.link === this.href);
    if(index != -1) {
      this.screen = this.screens[index].name;
    }
    console.log(this.href);
    
  }

  clickScreen(screen: any) {
    this.href = screen?.link;
    this.screen = screen?.name;
    this.router.navigate([screen?.link]);
  }
}
