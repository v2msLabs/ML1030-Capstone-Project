import { HttpErrorResponse } from '@angular/common/http';
import { LenderSurveyComponent } from 'components/lender-survey/lender-survey.comp';
import { ModelInput, SimulatorSurvey } from 'types/definitions';

export const survey2ModelInput = (survey: SimulatorSurvey | LenderSurveyComponent): ModelInput => {
    if (!survey)
        return null;
    return {
        input: Object.keys(survey).reduce((acc, k) => { acc.push(survey[k]); return acc; }
            , [])
    };
}

export const showError = (error: Error | HttpErrorResponse) => {
    console.error(error);

    if (error instanceof Error) {
        // A client-side or network error occurred. Handle it accordingly.
        alert(error.stack);
    } else {
        // The backend returned an unsuccessful response code.
        // The response body may contain clues as to what went wrong,
        alert(error.message);
    }

}