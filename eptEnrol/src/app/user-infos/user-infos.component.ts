import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { flaskdataService,  candidats_infos  } from '../flaskdata.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-user-infos',
  templateUrl: './user-infos.component.html',
  styleUrls: ['./user-infos.component.css']
})
export class UserInfosComponent implements OnInit{
  validation !: candidats_infos[];
  userEmail !:string;
  candidat !:candidats_infos;
  statut !: string;
  path !: string;
 

  constructor( private _api:flaskdataService, private route: ActivatedRoute, private http: HttpClient){}

  ngOnInit(): void {
  this._api.getInfosValidation().subscribe((response: candidats_infos[]) => {
    this.validation = response;
  
  this.userEmail = this.route.snapshot.paramMap.get('email') ?? '';
  this.candidat = this.validation.find((item: candidats_infos) => item.email === this.userEmail)?? this.validation[0];
  this.path = `http://127.0.0.1:5000/fichier-pdf?chemin=../Documents/${this.candidat.prenom}-${this.candidat.nom}-${this.candidat.email}/${this.candidat.bulletins_path}`
  console.log(this.path);
  });
}
etat : string = 'validée!'
updateDatabase(email : string): void {
  this.http.post('http://127.0.0.1:5000/update-database', {'email':email}).subscribe(
    (response : any) => {
      console.log(response.message);
    }
  );
  this.statut = 'validée!';
}

updateDatabase1(email : string): void {
  this.http.post('http://127.0.0.1:5000/update-database1', {'email':email}).subscribe(
    (response : any) => {
      console.log(response.message);
    }
  );
  this.statut = 'rejetée!';
}

/* openPDF() {
  const options = {
    responseType: 'blob' as 'blob' 
  };

  this.http.get(this.path, options)
    .subscribe((response: any) => {
      const file = new Blob([response], { type: 'application/pdf' }); 
      const fileURL = URL.createObjectURL(file);
      window.open(fileURL); 
    });
} */
}