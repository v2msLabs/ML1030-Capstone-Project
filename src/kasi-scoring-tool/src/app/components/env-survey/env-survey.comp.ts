import { Component, ViewChild } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { questions, countryMap, optionMap22_23_24, optionMap26, optionMap36, optionMap18, optionMap20, optionMap25, amountsPerCounty } from 'types/dictionaries';
import { StepPosition, SimulatorSurvey } from 'types/definitions';
import { MatVerticalStepper } from '@angular/material/stepper';


@Component({
  selector: 'env-survey',
  templateUrl: 'env-survey.html',
  styleUrls: ['env-survey.scss']
})
export class EnvSurveyComponent {
  Questions = questions;
  Map22_23_24 = optionMap22_23_24;
  Map26 = optionMap26;
  Map18 = optionMap18;
  Map20 = optionMap20;
  Map25 = optionMap25;
  Map36 = optionMap36;
  CountryMap = countryMap;
  AmountsPerCountry = amountsPerCounty;
  survey: SimulatorSurvey;
  StepPositionRef = StepPosition;

  @ViewChild("stepper", { static: false })
  private stepper: MatVerticalStepper;

  constructor(private _formBuilder: FormBuilder) {
    this.setDefaultValues();
  }

  reset() {
    this.stepper.reset();
    this.setDefaultValues();
  }

  private setDefaultValues() {
    this.survey = { q1: "3", q2: "2", q3: "3", q4: "2", q5: "2", q6: "3", q7: "1", q8: "1", q9: "8", q10: "3" };
  }
}