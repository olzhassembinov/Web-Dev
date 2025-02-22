import { Component } from '@angular/core';
import { HomeListComponent } from './home-list/home-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [HomeListComponent], // Добавляем импорт компонента
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'my-first-angular-app';
}