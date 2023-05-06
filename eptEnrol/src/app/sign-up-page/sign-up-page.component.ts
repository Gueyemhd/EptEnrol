import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'sign-up',
  templateUrl: './sign-up-page.component.html',
  styleUrls: ['./sign-up-page.component.css']
})
export class SignUpPageComponent implements OnInit{

  imageUrl!:string;
  ngOnInit(): void {
    this.imageUrl = "assets/image.jpeg"
  }

}
