import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface candidats_infos {
  'numero_candidat': number,
  'prenom': string,
  'nom': string,
  'email': string,
  'numero_dossier':string,
  'etat_dossier': string,
  'paiement': boolean,
  'numero_fiche': number,
  'adresse': string,
  'tel_candidat': string,
  'tel_parent': string,
  'etablissement': string,
  'serie': string,
  'date_naissance': string,
  'lieu_naissance': string,
  'nationalite': string,
  'option': string,
  'centre_examen': string,
  'annee_obtention_bac': number,
  'mention_bac': string,
  'numero_document': number,
  'diplome_path': string,
  'bulletins_path': string,
  'releve_path': string

}

export interface etatDossier {
  'prenom': string,
  'nom': string,
  'email': string,
  'numero_dossier':number,
  'etat_dossier': string,
  'serie' : string,

}


@Injectable({
  providedIn: 'root'
})
export class flaskdataService {
  urlApiAetudier ="http://127.0.0.1:5000/infoCandidat"
  urlApiEtudies = "http://127.0.0.1:5000/etudies"
  urlApiValidation = "http://127.0.0.1:5000/validation"
  urlApiAll = "http://127.0.0.1:5000/all"

  constructor(private _http : HttpClient) { }
  
  getInfoCandidat():Observable <etatDossier[]> {
    return this._http.get<etatDossier[]>(`${this.urlApiAetudier}`);
  }

  getDossierEtudies():Observable <candidats_infos[]> {
    return this._http.get<candidats_infos[]>(`${this.urlApiEtudies}`);
  }

  getAllDossierEtudies():Observable <candidats_infos[]> {
    return this._http.get<candidats_infos[]>(`${this.urlApiAll}`);
  }

  getInfosValidation():Observable <candidats_infos[]>{
    return this._http.get<candidats_infos[]>(`${this.urlApiValidation}`)
  }

}

