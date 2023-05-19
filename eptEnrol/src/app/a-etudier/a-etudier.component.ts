import { Component, OnInit } from '@angular/core';
import { flaskdataService, candidats_infos, etatDossier } from '../flaskdata.service';

@Component({
  selector: 'app-a-etudier',
  templateUrl: './a-etudier.component.html',
  styleUrls: ['./a-etudier.component.css']
})
export class AEtudierComponent implements OnInit {
  candsAetudier !: etatDossier[];
  constructor( private _api:flaskdataService){}

  ngOnInit(): void {
  this._api.getInfoCandidat().subscribe((response: etatDossier[]) => {
    this.candsAetudier = response
  }); 
  }
}
