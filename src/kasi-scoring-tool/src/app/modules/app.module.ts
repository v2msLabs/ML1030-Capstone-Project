import { HttpClientModule } from '@angular/common/http';
import { ErrorHandler, NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatNativeDateModule } from '@angular/material/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from 'components/app.comp';
import { CountrySelectorComponent } from 'components/common/country/country-selector.comp';
import { MultiChoiceStepComponent } from 'components/common/multi-choice-step/multi-choice-step.comp';
import { ScoreComponent } from 'components/common/score/score.comp';
import { SpinnerComponent } from 'components/common/spinner/spinner.comp';
import { EnvSurveyComponent } from 'components/env-survey/env-survey.comp';
import { LenderSurveyComponent } from 'components/lender-survey/lender-survey.comp';
import { AppErrorHandler } from '../services/app-error-handler.service';
import { ModelService } from '../services/model.service';
import { OverlayService } from '../services/overlay.service';
import { AppRoutingModule } from './app-routing.module';
import { MaterialModule } from './material-module';


@NgModule({
  declarations: [
    AppComponent, ScoreComponent, EnvSurveyComponent, MultiChoiceStepComponent,
    CountrySelectorComponent, LenderSurveyComponent, SpinnerComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule,
    MatNativeDateModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule
  ],
  providers: [ModelService, OverlayService, { provide: ErrorHandler, useClass: AppErrorHandler }],
  entryComponents: [AppComponent],
  bootstrap: [AppComponent],
})
export class AppModule { }
