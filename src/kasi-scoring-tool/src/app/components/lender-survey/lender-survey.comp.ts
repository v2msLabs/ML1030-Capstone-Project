import { Component, EventEmitter, Output, ViewChild } from '@angular/core';
import { MatVerticalStepper } from '@angular/material/stepper';
import { ModelService } from 'src/app/services/model.service';
import { survey2ModelInput } from 'src/app/utils/generic';
import { EndPoint, LenderScoreSurvey, ModelPrediction, StepPosition } from 'types/definitions';
import { amountsPerCounty, countries, options11, options12, options18, options20, options21, options22_23_24, options25, options26, questions } from 'types/dictionaries';


@Component({
  selector: 'lender-survey',
  templateUrl: 'lender-survey.html',
  styleUrls: ['lender-survey.scss']
})
export class LenderSurveyComponent {
  @Output() score = new EventEmitter<number>();
  Questions = questions;
  ref22_23_24 = options22_23_24;
  ref11 = options11;
  ref12 = options12;
  ref26 = options26;
  ref18 = options18;
  ref20 = options20;
  ref21 = options21; //optionMap21;
  ref25 = options25;
  countriesRef = countries;
  amountsPerCountryRef = amountsPerCounty;
  survey: LenderScoreSurvey;
  StepPositionRef = StepPosition;
  @ViewChild("stepper", { static: false })
  private stepper: MatVerticalStepper;

  constructor(private modelService: ModelService) {
    this.setDefaultValues();
  }

  reset() {
    this.stepper.reset();
    this.setDefaultValues();
  }

  predict() {
    this.modelService.predict(EndPoint.Evaluator, survey2ModelInput(this.survey)).subscribe(
      (data: ModelPrediction) => { this.score.emit(data.category); }
    );
  }

  private setDefaultValues() {
    this.survey = {
      q1: 2, q2: 2, q3: 3, q4: 3, q5: 2, q6: 2, q7: 1, q8: 3,
      q9: 1, q10: 4, q11: 4, q12: 2
    };
  }
}