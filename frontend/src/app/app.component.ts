import { Component, Injector } from '@angular/core';
import { ComponentBase } from '@common/componens/ComponentBase';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent extends ComponentBase {
  
  isLoading: boolean = false;
  
  constructor(
    injector: Injector,
  ) {
    super(injector);
    if(!this.getUuid()) {
      this.setUuid();
    }
  }

  ngOnInit() {
    this.loadingService.loading$.subscribe((res: boolean) => {
      if (res) {
        this.isLoading = res;
      } else {
        this.isLoading = res;
      };
    });
  }
}
