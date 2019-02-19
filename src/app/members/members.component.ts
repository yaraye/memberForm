import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import { IMultiSelectOption } from 'angular-2-dropdown-multiselect';
import {MembersService} from '../members.service';



@Component({
  selector: 'app-members',
  templateUrl: './members.component.html',
  styleUrls: ['./members.component.css']
})
export class MembersComponent implements OnInit {
memberData:any;
reason_array:any;
months_array:any;
membersData:any;


  constructor(private router:Router, private memberService: MembersService) { 
  //  to display the options we need the reason_array
    this.reason_array = ['Building', 'Collection baskets', 'Donation', 'Membership', 'Tithe','other'],
   this.months_array = ['January', 'February', 'March', 'April', 'May'],
   this.memberData= {
        first_name: '',
        last_name:'',
        reason:'', 
        payment_month:'',
        amount : ''
        // this.date = ''
        // received_by :''
    }
  
  }
  listMembers() {
    this.memberService.fetchMembers().subscribe((data) => {
      this.memberData = data;
      console.log(data);
    }, (err) => {
      console.log('error')
    });
  }

  ngOnInit() {
    
}
handleSubmit() {
  console.log(this.memberData);
    this.router.navigate(['memberData']);

  // this.http.post('http://127.0.0.1:5000/members')
}
// // onBlurMethod(){
// //     alert(this.memberData.first_name);
// //     alert(this.memberData.last_name);

//     // call the APi to fatch the data ans make sure first and name exist
//   }

}

// to bind the data
// [(ngModel)]= 'memberData.first_name' #first_name = 'ngModel' 
// export class MembersComponent implements OnInit {
//   memberData:any;
//   reason_array:any
  
//     constructor(private router:Router) { 
//       this.reason_array = ['Donation', 'Members Fee', 'Collection'],
//      this.memberData= {
//           first_name: '',
//           last_name:'',
//           reason:'', 
//           payment_month:'',
//           amount : 0
//           // this.date = ''
//           // received_by :''
//       }
    
//     }