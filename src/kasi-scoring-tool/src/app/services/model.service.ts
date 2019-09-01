import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
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
            .pipe(
                catchError(e => this.handleError)
            );

    }

    private handleError(error: any) {
        console.error(error);
        if (error.error instanceof ErrorEvent) {
            // A client-side or network error occurred. Handle it accordingly.
            alert(error.error.message);
        } else {
            // The backend returned an unsuccessful response code.
            // The response body may contain clues as to what went wrong,
            alert(
                `Backend returned code ${error.status}, ` +
                `the message was: ${error.statusText}`);
        }
    }
}