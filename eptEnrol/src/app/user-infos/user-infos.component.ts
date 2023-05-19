import { Component, OnInit } from '@angular/core';
import { flaskdataService,  candidats_infos  } from '../flaskdata.service';

@Component({
  selector: 'app-user-infos',
  templateUrl: './user-infos.component.html',
  styleUrls: ['./user-infos.component.css']
})
export class UserInfosComponent implements OnInit{
  validation !: candidats_infos[];
  constructor( private _api:flaskdataService){}

  ngOnInit(): void {
  this._api.getInfosValidation().subscribe((response: candidats_infos[]) => {
    this.validation = response;
    // console.log(this.candsEtudies);
  });

}

}
