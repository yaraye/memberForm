import { Component, OnInit } from '@angular/core';
import {MembersService} from '../members.service'

@Component({
  selector: 'app-members-list',
  templateUrl: './members-list.component.html',
  styleUrls: ['./members-list.component.css']
})
export class MembersListComponent implements OnInit {
  membersData: any;
  firstName: string;

  constructor(private memberService: MembersService) {
   }

  listMembers() {
    this.memberService.fetchMembers().subscribe((data) => {
      this.membersData = data;
      console.log(data);
    }, (err) => {
      console.log('error')
    });
  }

  ngOnInit() {
    this.listMembers();
  }
//call the api from get
// create service auth service---member service ----import member-list. com ---
}
