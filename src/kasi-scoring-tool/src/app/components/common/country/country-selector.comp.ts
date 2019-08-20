import { Component, Output, EventEmitter, Input } from '@angular/core';
import { countries, countryMap } from 'types/dictionaries';

@Component({
    selector: 'country-selector',
    templateUrl: 'country-selector.html',
    styleUrls: ['country-selector.scss']
})
export class CountrySelectorComponent {
    @Input() country:string;
    @Output() countryChange = new EventEmitter<string>();
    countryMapRef = countryMap;

    onCountryChange() {
        this.countryChange.emit(this.country);
    }
}