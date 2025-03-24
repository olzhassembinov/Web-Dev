import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { AlbumsService } from '../../services/albums.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink]
})
export class AlbumDetailComponent implements OnInit {
  album: any;
  newTitle: string = '';

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private albumsService: AlbumsService
  ) {}

  ngOnInit() {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.albumsService.getAlbum(id).subscribe(data => {
      this.album = data;
      this.newTitle = data.title;
    });
  }

  saveTitle() {
    if (this.album) {
      this.albumsService.updateAlbum(this.album.id, this.newTitle).subscribe(data => {
        this.album.title = data.title;
      });
    }
  }

  goBack() {
    this.router.navigate(['/albums']);
  }
}
