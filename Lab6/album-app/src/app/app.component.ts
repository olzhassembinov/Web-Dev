import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AlbumsComponent } from './components/albums/albums.component';
import { AlbumDetailComponent } from './components/album-detail/album-detail.component';
import { AlbumPhotosComponent } from './components/album-photos/album-photos.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, AlbumsComponent, AlbumDetailComponent, AlbumPhotosComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'album-app';
}
