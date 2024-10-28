import { Component, OnInit } from '@angular/core';
import { FooterComponent } from "../../components/footer/footer.component";
import { StorageDataService } from '../../services/storage-data.service';
declare var $: any;
declare var WOW: any;
declare var OwlCarousel: any;
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FooterComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  private userLoggedIn : boolean = false;
  private isUser : boolean = false;
  private isNgo : boolean = false;
  constructor(private storage : StorageDataService) { }

  ngOnInit(): void {
    this.initSpinner();
    this.initWOW();
    this.initStickyNavbar();
    this.initCarousels();
    this.initCounterUp();
    this.initBackToTop();
    this.initUser();
  }

  initUser() : void {
    
    if(this.storage.getStorageData("user",false) == 1){
      this.isUser = true;
      this.userLoggedIn = true;
    }else if(this.storage.getStorageData("user",false) == 0){
      this.userLoggedIn = true;
      this.isNgo = true;
    }
  }

  initSpinner(): void {
    setTimeout(() => {
      if ($('#spinner').length > 0) {
        $('#spinner').removeClass('show');
      }
    }, 1);
  }

  initWOW(): void {
    new WOW().init();
  }

  initStickyNavbar(): void {
    $(window).scroll(() => {
      if ($(window).scrollTop() > 45) {
        $('.navbar').addClass('sticky-top shadow-sm');
      } else {
        $('.navbar').removeClass('sticky-top shadow-sm');
      }
    });
  }

  initCarousels(): void {
    $(".header-carousel").owlCarousel({
      animateOut: 'fadeOut',
      items: 1,
      margin: 0,
      stagePadding: 0,
      autoplay: true,
      smartSpeed: 500,
      dots: true,
      loop: true,
      nav: true,
      navText: [
        '<i class="bi bi-arrow-left"></i>',
        '<i class="bi bi-arrow-right"></i>'
      ]
    });

    $(".blog-carousel").owlCarousel({
      autoplay: true,
      smartSpeed: 1500,
      center: false,
      dots: false,
      loop: true,
      margin: 25,
      nav: true,
      navText: [
        
        '<i class="fa fa-angle-left"></i>',
        '<i class="fa fa-angle-right"></i>'
      ],
      responsiveClass: true,
      responsive: {
        0: {
          items: 1
        },
        576: {
          items: 1
        },
        768: {
          items: 2
        },
        992: {
          items: 2
        },
        1200: {
          items: 3
        }
      }
    });

    $(".testimonial-carousel").owlCarousel({
      autoplay: true,
      smartSpeed: 1500,
      center: false,
      dots: true,
      loop: true,
      margin: 25,
      nav: true,
      navText: [
        
        '<i class="fa fa-angle-left"></i>',
        '<i class="fa fa-angle-right"></i>'
      ],
      responsiveClass: true,
      responsive: {
        0: {
          items: 1
        },
        576: {
          items: 1
        },
        768: {
          items: 2
        },
        992: {
          items: 2
        },
        1200: {
          items: 3
        }
      }
    });
  }

  initCounterUp(): void {
    $('[data-toggle="counter-up"]').counterUp({
      delay: 5,
      time: 2000
    });
  }

  initBackToTop(): void {
    $(window).scroll(() => {
      if ($(window).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
      } else {
        $('.back-to-top').fadeOut('slow');
      }
    });

    $('.back-to-top').click(() => {
      $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
      return false;
    });
  }

}
