import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserInfosComponent } from './user-infos/user-infos.component';
import { ListeCandidatsComponent } from './liste-candidats/liste-candidats.component';
import { InscriptionConcoursComponent } from './inscription-concours/inscription-concours.component';

@NgModule({
  declarations: [
    AppComponent,
    UserInfosComponent,
    ListeCandidatsComponent,
    InscriptionConcoursComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
