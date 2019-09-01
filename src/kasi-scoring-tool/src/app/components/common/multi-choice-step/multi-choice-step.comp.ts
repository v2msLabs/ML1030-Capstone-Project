import { Component, EventEmitter, Input, OnChanges, Output, SimpleChanges } from '@angular/core';
import { StepPosition } from 'types/definitions';

@Component({
    selector: 'multi-choice-step',
    templateUrl: 'multi-choice-step.html',
    styleUrls: ['multi-choice-step.scss']
})
export class MultiChoiceStepComponent implements OnChanges {

    @Input() choices: Object;
    @Input() choice: number;
    @Input() position: StepPosition = StepPosition.Middle;
    @Output() choiceChange = new EventEmitter<number>();
    StepPositionRef = StepPosition
    choiceMap: Map<string, string>;

    ngOnChanges(changes: SimpleChanges): void {
        if (!changes.choices)
            return;
        const { currentValue } = changes.choices;
        if (currentValue) {
            this.choiceMap = new Map(Object.entries(currentValue))
        } else {
            this.choiceMap = new Map();
        }

    }

    onChoiceChange() {
        this.choiceChange.emit(this.choice);
    }

    getOptonCode(key: string): number {
        return parseInt(key);
    }
}