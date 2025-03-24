import { Component, Input, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
  @Input() product: { name: string; description: string; image: string; likes: number} = {
    name: '',
    description: '',
    image: '',
    likes: 0
  };

  is_liked = true;

  increaseLikes(): void {
    if (this.product && this.is_liked) {
      this.product.likes = 1;
      this.is_liked = false;
    }
    else
    {
      this.product.likes = 0;
      this.is_liked = false;
    }
  }

}
