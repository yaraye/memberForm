import { Component, OnInit } from '@angular/core';
import {MembersService} from '../members.service';


@Component({
  selector: 'app-membership',
  templateUrl: './membership.component.html',
  styleUrls: ['./membership.component.css']
})
export class MembershipComponent implements OnInit {
  membersData: any;
  firstName: string;



  constructor(private memberService: MembersService ) {
  
  }

  listMembers() {
    this.memberService.fetchMembership().subscribe((data) => {
      this.membersData = data;
      console.log(data);
    }, (err) => {
      console.log('error')
    });
  }
    
   

  ngOnInit() {
  
    this.listMembers();
  }

edit(){
  console.log('edited');
}


}

