import { Component } from '@angular/core';

@Component({
  selector: 'app-home-list',
  standalone: true,
  templateUrl: './home-list.component.html',
  styleUrls: ['./home-list.component.css']
})
export class HomeListComponent {
  homes = [
    {
      title: 'Acme Fresh Start Housing',
      location: 'Chicago, IL',
      image: 'assets/homes/home1.jpg'
    },
    {
      title: 'A113 Transitional Housing',
      location: 'Santa Monica, CA',
      image: 'assets/homes/home2.jpg'
    },
    {
      title: 'Warm Beds Housing Support',
      location: 'Juneau, AK',
      image: 'assets/homes/home3.jpg'
    },
    {
      title: 'Homestead Housing',
      location: 'Chicago, IL',
      image: 'assets/homes/home4.jpg'
    }
  ];
}