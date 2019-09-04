import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EndPoint, ModelInput, ModelPrediction } from 'types/definitions';

const httpOptions = {
    headers: new HttpHeaders({
        'Content-Type': 'application/json'
    })
};

@Injectable()
export class ModelService {

    constructor(private http: HttpClient) { }

    predict(url: EndPoint, input: ModelInput): Observable<ModelPrediction> {
        return this.http.post<ModelPrediction>(url, input, httpOptions)
    }


}