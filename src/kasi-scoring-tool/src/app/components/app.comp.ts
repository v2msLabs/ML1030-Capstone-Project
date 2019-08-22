import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, NavigationEnd } from '@angular/router';
import { AppRouts, AppNames } from 'types/definitions';

@Component({
  selector: 'app-root',
  templateUrl: 'app.html',
  styleUrls: ['app.scss']
})
export class AppComponent {
  activeApp = AppNames.Simulator;
  AppRoutsRef = AppRouts;
  AppNameRef = AppNames;

  constructor(private router: Router, private route: ActivatedRoute) {
    router.events.subscribe(e => {
      if (e instanceof NavigationEnd) {
        this.setAppName(e.url);

      }
    });
  }

  navigate(path: AppRouts) {
    this.router.navigate([path]);
    this.setAppName(path);

  }

  private setAppName(path: string | AppRouts) {
    if (!path) {
      return;
    }
    let p = path.replace("/","")
    if (p === AppRouts.Simulator) {
      this.activeApp = AppNames.Simulator;
    } else {
      this.activeApp = AppNames.LenderEvaluator;
    }
  }

}