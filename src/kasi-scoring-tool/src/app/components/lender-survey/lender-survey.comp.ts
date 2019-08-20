import { Component, ViewChild } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { questions, countryMap, optionMap22_23_24, optionMap26, optionMap36, optionMap18, optionMap19, optionMap20, optionMap25, optionMap11, optionMap12, optionMap21 } from 'types/dictionaries';
import { StepPosition, LenderScoreSurvey } from 'types/definitions';
import { MatVerticalStepper } from '@angular/material/stepper';


@Component({
  selector: 'lender-survey',
  templateUrl: 'lender-survey.html',
  styleUrls: ['lender-survey.scss']
})
export class LenderSurveyComponent {
  Questions = questions;
  Map22_23_24 = optionMap22_23_24;
  Map11 = optionMap11;
  Map12 = optionMap12;
  Map26 = optionMap26;
  Map18 = optionMap18;
  Map19 = optionMap19;
  Map20 = optionMap20;
  Map21 = optionMap21;
  Map25 = optionMap25;
  Map36 = optionMap36;
  CountryMap = countryMap;
  survey: LenderScoreSurvey;
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
    this.survey = {
      q1: "1", q2: "2", q3: "1", q4: "1", q5: "1", q6: "1", q7: "1", q8: "1",
      q9: "1", q10: "1", q11: "1", q12: "1"
    };
  }
}