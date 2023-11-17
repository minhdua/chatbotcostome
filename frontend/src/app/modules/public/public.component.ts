import { Component, OnInit } from '@angular/core';
import {MatDialog} from '@angular/material/dialog';
import { ChatBoxComponent } from '@common/componens/chat-box/chat-box.component';

@Component({
  selector: 'app-public',
  templateUrl: './public.component.html',
  styleUrls: ['./public.component.scss']
})
export class PublicComponent implements OnInit {

  isFetchData = false;
  isFirstLoad = false;

  constructor(public dialog: MatDialog) {}

  ngOnInit() {}

  openDialog() {
    const dialogRef = this.dialog.open(ChatBoxComponent, {
      panelClass: 'chatBox-panel',
      backdropClass: 'chatBox-backdrop'
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

}
