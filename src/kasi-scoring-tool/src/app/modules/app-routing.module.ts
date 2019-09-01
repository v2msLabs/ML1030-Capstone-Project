import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EnvSurveyComponent } from 'components/env-survey/env-survey.comp';
import { LenderSurveyComponent } from 'components/lender-survey/lender-survey.comp';
import { AppRout } from 'types/definitions';


const routes: Routes = [
  { path: AppRout.Simulator, component: EnvSurveyComponent },
  { path: AppRout.LenderEvaluator, component: LenderSurveyComponent },
  {
    path: '**', redirectTo: AppRout.Simulator, pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
