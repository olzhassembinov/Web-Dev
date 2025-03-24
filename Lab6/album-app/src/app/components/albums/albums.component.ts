import { Component, OnInit } from '@angular/core';
import { AlbumsService } from '../.././services/albums.service';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css'],
  standalone: true,
  imports: [CommonModule, RouterLink]
})
export class AlbumsComponent implements OnInit {
  albums: any[] = [];

  constructor(private albumsService: AlbumsService) {}

  ngOnInit() {
    this.albumsService.getAlbums().subscribe(data => this.albums = data);
  }

  deleteAlbum(id: number) {
    this.albumsService.deleteAlbum(id).subscribe(() => {
      this.albums = this.albums.filter(album => album.id !== id);
    });
  }
}