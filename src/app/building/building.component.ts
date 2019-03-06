import { Component, OnInit } from '@angular/core';
import {MembersService} from '../members.service';

@Component({
  selector: 'app-building',
  templateUrl: './building.component.html',
  styleUrls: ['./building.component.css']
})
export class BuildingComponent implements OnInit {
  membersData: any;
  firstName: string;



  constructor(private memberService: MembersService ) {
  
  }

  listMembers() {
    this.memberService.fetchBuilding().subscribe((data) => {
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

