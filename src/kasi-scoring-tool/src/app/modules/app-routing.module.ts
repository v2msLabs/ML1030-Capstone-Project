import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { EnvSurveyComponent } from 'components/env-survey/env-survey.comp';
import { LenderSurveyComponent } from 'components/lender-survey/lender-survey.comp';
import { AppRouts } from 'types/definitions';


const routes: Routes = [
  { path: AppRouts.Simulator, component: EnvSurveyComponent },
  { path: AppRouts.LenderEvaluator, component: LenderSurveyComponent },
  {
    path: '**', redirectTo: AppRouts.Simulator, pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
