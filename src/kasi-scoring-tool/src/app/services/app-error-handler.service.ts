import { HttpErrorResponse } from '@angular/common/http';
import { ErrorHandler, Injectable } from '@angular/core';
import { showError } from '../utils/generic';


@Injectable()
export class AppErrorHandler implements ErrorHandler {


  constructor() { }

  handleError(error: Error | HttpErrorResponse) {
    showError(error);

  }
}