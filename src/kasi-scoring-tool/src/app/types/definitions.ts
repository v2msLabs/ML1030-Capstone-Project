export enum StepPosition {
    First, Middle, Last
}

export enum AppRout {
    Simulator = "simulator",
    LenderEvaluator = "lender-evaluator"
}

export enum AppName {
    Simulator = "Lending Environment Simulator",
    LenderEvaluator = "Lender Evaluator"
}

export enum EndPoint {
    Simulator = "api/simulator-model",
    Evaluator = "api/evaluator-model"
}

export interface SimulatorSurvey{
    q1:number;
    q2:number;
    q3:number;
    q4:number;
    q5:number;
    q6:number;
    q7:number;
    q8:number;
    q9:number;
}

export interface LenderScoreSurvey extends SimulatorSurvey {
    q10:number;
}

export interface ModelPrediction {
    category:number;
}

export interface ModelInput {
    input:number[]
}