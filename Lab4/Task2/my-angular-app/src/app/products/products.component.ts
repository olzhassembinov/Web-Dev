import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Product {
  image: string;
  name: string;
  description: string;
  rating: number;
  link: string;
}

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css'],
  imports: [CommonModule]
})
export class ProductsComponent {
  products: Product[] = [
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h1b/hd6/64377056231454.jpg?format=preview-large',
      name: 'Apple iPhone 13',
      description: 'Смартфон Apple iPhone 13 128GB',
      rating: 4.5,
      link: 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-10101010/'
    },
    {
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h1b/hd6/64377056231454.jpg?format=preview-large',
      name: 'Samsung Galaxy S23',
      description: 'Флагманский смартфон Samsung',
      rating: 4.8,
      link: 'https://kaspi.kz/shop/p/samsung-galaxy-s23-10101011/'
    }
  ];

  share(product: Product, platform: string) {
    let shareUrl = '';
    if (platform === 'whatsapp') {
      shareUrl = `https://wa.me/?text=${encodeURIComponent(product.link)}`;
    } else if (platform === 'telegram') {
      shareUrl = `https://t.me/share/url?url=${encodeURIComponent(product.link)}`;
    }
    window.open(shareUrl, '_blank');
  }
}
