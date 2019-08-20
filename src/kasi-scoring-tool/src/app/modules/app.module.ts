import { NgModule } from '@angular/core';
import { AppComponent } from 'components/app.comp';
import { EnvSurveyComponent } from 'components/env-survey/env-survey.comp';
import { MaterialModule } from './material-module';
import { MatNativeDateModule } from '@angular/material/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MultiChoiceStepComponent } from 'components/common/multi-choice-step/multi-choice-step.comp';
import { CountrySelectorComponent } from 'components/common/country/country-selector.comp';
import { AppRoutingModule } from './app-routing.module';
import { LenderSurveyComponent } from 'components/lender-survey/lender-survey.comp';


@NgModule({
  declarations: [
    AppComponent, EnvSurveyComponent, MultiChoiceStepComponent, CountrySelectorComponent, LenderSurveyComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MaterialModule,
    MatNativeDateModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule
  ],
  entryComponents: [AppComponent],
  bootstrap: [AppComponent],
})
export class AppModule { }
