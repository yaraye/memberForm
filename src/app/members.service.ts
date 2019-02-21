import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { Subject } from 'rxjs';
// import {MembersList} from './members-list/members-list.component';

@Injectable({
  providedIn: 'root'
})
export class MembersService {
 
  constructor(private httpClient:HttpClient) {}
  private columnSortedSource = new Subject<ColumnSortedEvent>();

  columnSorted$ = this.columnSortedSource.asObservable();

  columnSorted(event: ColumnSortedEvent) {
      this.columnSortedSource.next(event);
  }

  fetchMembers() {
    return this.httpClient.get('http://127.0.0.1:5000/members')
  };
  

};
export interface ColumnSortedEvent {
    sortColumn: string;
    sortDirection: string;
}