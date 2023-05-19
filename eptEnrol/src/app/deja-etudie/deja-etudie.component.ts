import { Component, OnInit } from '@angular/core';
import { flaskdataService, candidats_infos, etatDossier } from '../flaskdata.service';

@Component({
  selector: 'app-deja-etudie',
  templateUrl: './deja-etudie.component.html',
  styleUrls: ['./deja-etudie.component.css']
})
export class DejaEtudieComponent {
  etat = "Validé"
  candsEtudies !: candidats_infos[];
  constructor( private _api:flaskdataService){}

  ngOnInit(): void {
  this._api.getDossierEtudies().subscribe((response: candidats_infos[]) => {
    this.candsEtudies = response;
  });

  }
}
