import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Chart } from './chart/chart'
import { NgxEchartsModule } from 'ngx-echarts';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    Chart
  ],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App {

}
