import { Component, OnInit } from '@angular/core';
import { flaskdataService, etatDossier } from '../flaskdata.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-etat-dossier',
  templateUrl: './etat-dossier.component.html',
  styleUrls: ['./etat-dossier.component.css']
})
export class EtatDossierComponent implements OnInit {
  infoCandidat !: etatDossier[];
  nom !: string;
  prenom !: string;
  email !: string;
  serie !: string;
  etat !: string;
  


  constructor( private _api:flaskdataService, private route: ActivatedRoute){}

  ngOnInit(): void {


  this.route.queryParams.subscribe(params => {
    this.nom = params['nom'];
    this.prenom = params['prenom'];
    this.email = params['email'];
    this.serie = params['serie']; 
    this.etat = params['etat'];
    
    
  });
}


}
