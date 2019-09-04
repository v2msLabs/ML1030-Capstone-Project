import { Component, EventEmitter, Output, ViewChild } from '@angular/core';
import { MatVerticalStepper } from '@angular/material/stepper';
import { ModelService } from 'src/app/services/model.service';
import { showError, survey2ModelInput } from 'src/app/utils/generic';
import { EndPoint, ModelPrediction, SimulatorSurvey, StepPosition } from 'types/definitions';
import { amountsPerCounty, countries, options18, options20, options21, options22_23_24, options26, questions } from 'types/dictionaries';


@Component({
  selector: 'env-survey',
  templateUrl: 'env-survey.html',
  styleUrls: ['env-survey.scss']
})
export class EnvSurveyComponent {
  @Output() score = new EventEmitter<number>();
  Questions = questions;
  ref22_23_24 = options22_23_24;
  ref26 = options26;
  ref18 = options18;
  ref20 = options20;
  ref21 = options21;
  countriesRef = countries;
  amountsPerCountryRef = amountsPerCounty;
  survey: SimulatorSurvey;
  StepPositionRef = StepPosition;
  displaySpinner = false;
  @ViewChild("stepper", { static: false })
  private stepper: MatVerticalStepper;

  constructor(private modelService: ModelService) {
    this.setDefaultValues();
  }

  reset() {
    this.stepper.reset();
    this.setDefaultValues();
    this.score.emit(undefined);
  }

  predict() {
    this.displaySpinner = true;
    this.modelService.predict(EndPoint.Simulator, survey2ModelInput(this.survey)).subscribe(
      (data: ModelPrediction) => {
        this.displaySpinner = false;
        this.score.emit(data.category);
      }
      , err => { this.displaySpinner = false; showError(err); }
    );
  }

  private setDefaultValues() {
    this.survey = { q1: 3, q2: 2, q3: 3, q4: 2, q5: 2, q6: 3, q7: 1, q8: 1, q9: 2 };
  }
}