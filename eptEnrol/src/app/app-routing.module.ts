import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { UserInfosComponent } from './user-infos/user-infos.component';
import { ListeCandidatsComponent } from './liste-candidats/liste-candidats.component';
import { InscriptionConcoursComponent } from './inscription-concours/inscription-concours.component';
import { AEtudierComponent } from './a-etudier/a-etudier.component';
import { DejaEtudieComponent } from './deja-etudie/deja-etudie.component';
import { SignUpPageComponent } from './sign-up-page/sign-up-page.component';

const routes: Routes = [
  { path: '', component: InscriptionConcoursComponent },
  { path: 'user', component: UserInfosComponent },
  { path: 'listeCandidats', component: ListeCandidatsComponent},
  { path: 'dejaEtudies', component: DejaEtudieComponent},
  { path: 'aEtudier', component: AEtudierComponent},
  { path: 'connexion', component: SignUpPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
