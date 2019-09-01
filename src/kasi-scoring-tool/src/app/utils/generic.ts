import { LenderSurveyComponent } from 'components/lender-survey/lender-survey.comp';
import { SimulatorSurvey, ModelInput } from 'types/definitions';

export const survey2ModelInput = (survey: SimulatorSurvey | LenderSurveyComponent): ModelInput => {
    if (!survey)
        return null;
    return {
        input: Object.keys(survey).reduce((acc, k) => { acc.push(survey[k]); return acc; }
            , [])
    };
}