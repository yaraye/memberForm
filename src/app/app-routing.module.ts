import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from './login/login.component';
import {MembersComponent} from './members/members.component';
import {MembersListComponent} from './members-list/members-list.component';
import {AuthGuard} from './auth.guard';
import {RegistrationComponent} from './registration/registration.component';


const routes: Routes = [
  // this will give a dash bored the empty route
  {path: '', component: MembersComponent, pathMatch: 'full', canActivate: [AuthGuard]},
  {path: 'login', component: LoginComponent},
  {path: 'registration', component: RegistrationComponent},
  {path: 'members', component: MembersComponent, canActivate: [AuthGuard]},
  {path: 'membersList', component: MembersListComponent, canActivate: [AuthGuard]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
