import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from "./components/header/header.component";
import { HomeComponent } from "./pages/home/home.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent, HomeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'donation_platform';

  ngOnInit() {
    this.logImagePath();
  }

  logImagePath(imagePath: string = 'assets/img/carousel-2.png'): void {
    console.log('Image path:', imagePath);
  }

}
