export enum StepPosition {
    First, Middle, Last
}

export interface SimulatorSurvey{
    q1:string;
    q2:string;
    q3:string;
    q4:string;
    q5:string;
    q6:string;
    q7:string;
    q8:string;
    q9:string;
    q10:string;
}

export interface LenderScoreSurvey extends SimulatorSurvey {
    q11:string;
    q12:string;
}