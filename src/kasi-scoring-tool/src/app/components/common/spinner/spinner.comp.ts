import { OverlayConfig, OverlayRef } from '@angular/cdk/overlay';
import { Component, Input, TemplateRef, ViewChild, ViewContainerRef } from '@angular/core';
import { ProgressSpinnerMode, ThemePalette } from '@angular/material';
import { OverlayService } from 'src/app/services/overlay.service';


@Component({
    selector: 'spinner',
    templateUrl: 'spinner.html',
    styleUrls: ['spinner.scss']
})
export class SpinnerComponent {
    @Input() color?: ThemePalette;
    @Input() diameter?: number = 100;
    @Input() mode?: ProgressSpinnerMode = "indeterminate";
    @Input() strokeWidth?: number;
    @Input() value?: number;
    @Input() backdropEnabled = true;
    @Input() positionGloballyCenter = true;
    @Input() display: boolean;

    @ViewChild('spinnerRef', { static: false })
    private spinnerRef: TemplateRef<any>;
    private spinnerOverlayConfig: OverlayConfig;
    private overlayRef: OverlayRef;

    constructor(private vcRef: ViewContainerRef, private overlayService: OverlayService) { }

    ngOnInit() {
        // Config for Overlay Service
        this.spinnerOverlayConfig = {
            hasBackdrop: this.backdropEnabled
        };
        if (this.positionGloballyCenter) {
            this.spinnerOverlayConfig['positionStrategy'] = this.overlayService.positionGloballyCenter();
        }
        // Create Overlay for the spinner
        this.overlayRef = this.overlayService.createOverlay(this.spinnerOverlayConfig);
    }
    ngDoCheck() {
        // Based on status of displayProgressSpinner attach/detach overlay to progress spinner template
        if (this.display && !this.overlayRef.hasAttached()) {
            this.overlayService.attachTemplatePortal(this.overlayRef, this.spinnerRef, this.vcRef);
        } else if (!this.display && this.overlayRef.hasAttached()) {
            this.overlayRef.detach();
        }
    }
}