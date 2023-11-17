import { Component, Inject, OnInit } from "@angular/core";
import { MatDialogRef, MAT_DIALOG_DATA } from "@angular/material/dialog";

@Component({
  selector: "lib-comfirm-dialog",
  templateUrl: "./comfirm-dialog.component.html",
  styleUrls: ["./comfirm-dialog.component.scss"],
})
export class ComfirmDialogComponent implements OnInit {
  constructor(
    public dialogRef: MatDialogRef<ComfirmDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
  ) {
  }

  ngOnInit(): void { }

  close(flag: boolean): void {
    this.dialogRef.close(flag);
  }

  getClassOfType(isIcon: boolean) {
    let result = '';
    switch (this.data.type) {
      case "warning":
        result = isIcon ? 'fa fa-warning text-warning' : 'text-warning';
        break;
      case "error":
        result = isIcon ? 'fa fa-times text-danger' : 'text-danger';
        break;
      case "success":
        result = isIcon ? 'fa fa-check text-success' : 'text-success';
        break;
      case "info":
        result = isIcon ? 'fa fa-info text-info' : 'text-info';
        break;
      default:
        break;
    }
    return result;
  }
}
