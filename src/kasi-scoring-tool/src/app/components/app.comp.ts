import { Component, Input } from '@angular/core';
import { ActivatedRoute, NavigationEnd, Router } from '@angular/router';
import { AppName, AppRout } from 'types/definitions';

@Component({
  selector: 'app-root',
  templateUrl: 'app.html',
  styleUrls: ['app.scss']
})
export class AppComponent {
  @Input() score: number;
  activeApp = AppName.Simulator;
  AppRoutsRef = AppRout;
  AppNameRef = AppName;

  constructor(private router: Router, private route: ActivatedRoute) {
    router.events.subscribe(e => {
      if (e instanceof NavigationEnd) {
        this.setAppName(e.url);

      }
    });
  }

  navigate(path: AppRout) {
    this.router.navigate([path]);
    this.setAppName(path);

  }

  onActivate(componentReference: any) {
    if ( componentReference && componentReference.score){
      this.score = 0;
      componentReference.score.subscribe((score:number) => {
        this.score = score; 
     })
    }

  }


  private setAppName(path: string | AppRout) {
    if (!path) {
      return;
    }
    let p = path.replace("/", "")
    if (p === AppRout.Simulator) {
      this.activeApp = AppName.Simulator;
    } else {
      this.activeApp = AppName.LenderEvaluator;
    }
  }

}