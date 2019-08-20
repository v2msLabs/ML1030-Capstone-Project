import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { EnvSurveyComponent } from 'components/env-survey/env-survey.comp';
import { LenderSurveyComponent } from 'components/lender-survey/lender-survey.comp';


const routes: Routes = [
  { path: 'simulator', component: EnvSurveyComponent },
  { path: 'lender-score', component: LenderSurveyComponent },
  {
    path: '**', redirectTo: '/simulator', pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { enableTracing: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
