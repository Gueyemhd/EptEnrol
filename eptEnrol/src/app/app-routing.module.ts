import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { SignUpPageComponent } from "./sign-up-page/sign-up-page.component";
import { RegisterComponent } from "./register/register.component";

const routes: Routes = [
    {path: '', component:SignUpPageComponent},
    {path: 'register', component: RegisterComponent}

];

@NgModule({
    imports: [
        RouterModule.forRoot(routes)
    ],
    exports: [
        RouterModule
    ]
    
})

export class AppRoutingModule{


}