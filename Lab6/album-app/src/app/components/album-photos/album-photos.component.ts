import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumsService } from '../../services/albums.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css'],
  standalone: true,
  imports: [CommonModule]
})
export class AlbumPhotosComponent implements OnInit {
  photos: any[] = [];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private albumsService: AlbumsService
  ) {}

  ngOnInit() {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.albumsService.getAlbumPhotos(id).subscribe(data => this.photos = data);
  }

  goBack() {
    this.router.navigate([`/albums/${this.route.snapshot.paramMap.get('id')}`]);
  }
}
