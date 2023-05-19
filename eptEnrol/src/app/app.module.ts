import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserInfosComponent } from './user-infos/user-infos.component';
import { ListeCandidatsComponent } from './liste-candidats/liste-candidats.component';
import { InscriptionConcoursComponent } from './inscription-concours/inscription-concours.component';
import { AEtudierComponent } from './a-etudier/a-etudier.component';
import { DejaEtudieComponent } from './deja-etudie/deja-etudie.component';
import { SignUpPageComponent } from './sign-up-page/sign-up-page.component';
import { EtatDossierComponent } from './etat-dossier/etat-dossier.component';
// import { FormsModule } from '@angular/forms';




@NgModule({
  declarations: [
    AppComponent,
    UserInfosComponent,
    ListeCandidatsComponent,
    InscriptionConcoursComponent,
    AEtudierComponent,
    DejaEtudieComponent,
    SignUpPageComponent,
    EtatDossierComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    // FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
