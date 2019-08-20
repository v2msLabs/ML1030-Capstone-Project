import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { StepPosition } from 'types/definitions';

@Component({
    selector: 'multi-choice-step',
    templateUrl: 'multi-choice-step.html',
    styleUrls: ['multi-choice-step.scss']
})
export class MultiChoiceStepComponent {
    @Input() choices: Map<string, string>;
    @Input() choice: string;
    @Input() position: StepPosition = StepPosition.Middle;
    @Output() choiceChange = new EventEmitter<string>();
    StepPositionRef = StepPosition


    onChoiceChange() {
        this.choiceChange.emit(this.choice);
    }
}