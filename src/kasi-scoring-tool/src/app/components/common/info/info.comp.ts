import { Component, Inject } from '@angular/core';
import { MatDialogRef, MatDialog, MAT_DIALOG_DATA } from '@angular/material';
import { AppName } from 'types/definitions';

@Component({
    selector: 'info',
    templateUrl: 'info.html',
    styleUrls: ['info.scss'],
})
export class InfoComponent {
    AppNameRef = AppName;

    constructor(@Inject(MAT_DIALOG_DATA) public data: any) { }
}
