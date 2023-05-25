import { Component, OnInit } from '@angular/core';
import { flaskdataService,  candidats_infos  } from '../flaskdata.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-user-info-valide',
  templateUrl: './user-info-valide.component.html',
  styleUrls: ['./user-info-valide.component.css']
})
export class UserInfoValideComponent implements OnInit{
  userEmail !:string;
  candidat !:candidats_infos;
  candsEtudies !: candidats_infos[];

  constructor(private _api:flaskdataService, private route: ActivatedRoute){

  }

  ngOnInit(): void {
    this._api.getAllDossierEtudies().subscribe((response: candidats_infos[]) => {
      this.candsEtudies = response;

      this.userEmail = this.route.snapshot.paramMap.get('email') ?? '';
      this.candidat = this.candsEtudies.find((item: candidats_infos) => item.email === this.userEmail)?? this.candsEtudies[0];
  }
    );


  }

}
