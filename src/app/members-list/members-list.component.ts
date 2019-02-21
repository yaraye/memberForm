import { Component, OnInit, Input, EventEmitter, OnDestroy, HostListener  } from '@angular/core';
import {MembersService} from '../members.service'
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-members-list',
  templateUrl: './members-list.component.html',
  styleUrls: ['./members-list.component.css']
})
export class MembersListComponent implements OnInit, OnDestroy {
  membersData: any;
  firstName: string;

  constructor(private memberService: MembersService) {}

  @Input('sortable-column')
  columnName: string;

  @Input('sort-direction')
  sortDirection: string = '';


  

  @HostListener('click')
  sort() {
      this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
      this.memberService.columnSorted({ sortColumn: this.columnName, sortDirection: this.sortDirection });
    }

    private columnSortedSubscription: Subscription

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
    this.columnSortedSubscription = this.memberService.columnSorted$.subscribe(event => {
      // reset this column's sort direction to hide the sort icons
      if (this.columnName != event.sortColumn) {
          this.sortDirection = '';
      }
  });
  }
//call the api from get
// create service auth service---member service ----import member-list. com ---
ngOnDestroy() {
  this.columnSortedSubscription.unsubscribe();
}
}
