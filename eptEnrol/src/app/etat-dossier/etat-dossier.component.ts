import { Component, OnInit } from '@angular/core';
import { flaskdataService, etatDossier } from '../flaskdata.service';

@Component({
  selector: 'app-etat-dossier',
  templateUrl: './etat-dossier.component.html',
  styleUrls: ['./etat-dossier.component.css']
})
export class EtatDossierComponent implements OnInit {
  infoCandidat !: etatDossier[];
  constructor( private _api:flaskdataService){}

  ngOnInit(): void {

  this._api.getInfoCandidat().subscribe((response: etatDossier[]) => {
    this.infoCandidat = response;
    //this.infoCandidat = response.reverse().slice(0, 5);
  
  });
}


}
