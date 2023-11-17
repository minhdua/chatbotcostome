import { Component, OnInit } from '@angular/core';
import { LoadingService } from '@common/services/loading.service';

@Component({
  selector: 'app-private',
  templateUrl: './private.component.html',
  styleUrls: ['./private.component.scss']
})
export class PrivateComponent implements OnInit {

  isFetchData = false;
  isFirstLoad = false;
  isLoading: boolean = false;

  constructor(
    public loadingService: LoadingService
    ) {}

  ngOnInit() {}

}
