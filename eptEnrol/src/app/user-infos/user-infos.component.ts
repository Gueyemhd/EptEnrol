import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { flaskdataService,  candidats_infos  } from '../flaskdata.service';

@Component({
  selector: 'app-user-infos',
  templateUrl: './user-infos.component.html',
  styleUrls: ['./user-infos.component.css']
})
export class UserInfosComponent implements OnInit{
  validation !: candidats_infos[];
  userEmail !:string;
  candidat !:candidats_infos;

  constructor( private _api:flaskdataService, private route: ActivatedRoute){}

  ngOnInit(): void {
  this._api.getInfosValidation().subscribe((response: candidats_infos[]) => {
    this.validation = response;
  
  this.userEmail = this.route.snapshot.paramMap.get('email') ?? '';
  this.candidat = this.validation.find((item: candidats_infos) => item.email === this.userEmail)?? this.validation[0];
  });
}

}
