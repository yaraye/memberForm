import { Component, OnInit } from '@angular/core';
import {MembersService} from '../members.service';

@Component({
  selector: 'app-donation',
  templateUrl: './donation.component.html',
  styleUrls: ['./donation.component.css']
})
export class DonationComponent implements OnInit {

  membersData: any;
  firstName: string;



  constructor(private memberService: MembersService ) {
  
  }

  listMembers() {
    this.memberService.fetchDonation().subscribe((data) => {
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

