import { Component, EventEmitter, Input, Output } from '@angular/core';
import { countryMap } from 'types/dictionaries';

@Component({
    selector: 'country-selector',
    templateUrl: 'country-selector.html',
    styleUrls: ['country-selector.scss']
})
export class CountrySelectorComponent {
    @Input() country: number;
    @Output() countryChange = new EventEmitter<number>();
    countriesRef = countryMap;

    onCountryChange() {
        console.log(this.country)
        this.countryChange.emit(this.country);
    }

    getCountryCode(code: string): number {
        return parseInt(code);
    }
}