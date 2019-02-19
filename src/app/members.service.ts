import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
// import {MembersList} from './members-list/members-list.component';

@Injectable({
  providedIn: 'root'
})
export class MembersService {
 
  constructor(private httpClient:HttpClient) {}

  fetchMembers() {
    return this.httpClient.get('http://127.0.0.1:5000/members')
  };
  

};
