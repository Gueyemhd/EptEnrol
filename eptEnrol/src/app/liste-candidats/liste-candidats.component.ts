import { Component, OnInit } from '@angular/core';
import { flaskdataService, candidats_infos, etatDossier } from '../flaskdata.service';


@Component({
  selector: 'app-liste-candidats',
  templateUrl: './liste-candidats.component.html',
  styleUrls: ['./liste-candidats.component.css']
})
export class ListeCandidatsComponent implements OnInit{
  etat = "Validé"
  candsAetudier !: etatDossier[];
  candsEtudies !: candidats_infos[];
  constructor( private _api:flaskdataService){}

  ngOnInit(): void {
  this._api.getDossierEtudies().subscribe((response: candidats_infos[]) => {
    this.candsEtudies = response;
    // console.log(this.candsEtudies);
  });

  this._api.getInfoCandidat().subscribe((response: etatDossier[]) => {
    this.candsAetudier = response
    // console.log(this.candsAetudier);
  });
}
}
