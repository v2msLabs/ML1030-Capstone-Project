import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { creditScore } from 'types/dictionaries';

@Component({
    selector: 'score',
    templateUrl: 'score.html',
    styleUrls: ['score.scss']
})
export class ScoreComponent implements OnChanges {

    @Input() scoreCategory: number;
    categoryRef = creditScore;
    category: string;

    ngOnChanges(changes: SimpleChanges): void {
        if (!changes.scoreCategory) {
            this.category = "";
            return;
        }
        const { currentValue } = changes.scoreCategory;
        this.category = this.categoryRef[currentValue];

    }

    getScoreClass(): string {
        switch (this.scoreCategory) {
            case 1:
                return "kasi-very-poor";
            case 2:
                return "kasi-poor";
            case 3:
                return "kasi-fair";
            case 4:
                return "kasi-good";
            case 5:
                return "kasi-very-good";
            default:
                return "";

        }
    }

}