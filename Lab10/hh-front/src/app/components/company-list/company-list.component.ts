import { Component, OnInit } from '@angular/core';
import { Company, CompanyService, Vacancy } from '../../company.service';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  imports: [CommonModule, HttpClientModule],
  standalone: true
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];
  vacancies: Vacancy[] = [];
  selectedCompanyId: number | null = null;

  loadingCompanies = false;
  loadingVacancies = false;
  companyError = '';
  vacancyError = '';

  constructor(private companyService: CompanyService) {
    console.log('CompanyListComponent constructor called');
  }

  ngOnInit(): void {
    console.log('CompanyListComponent ngOnInit called');
    this.loadCompanies();
  }

  loadCompanies(): void {
    console.log('loadCompanies called');
    this.loadingCompanies = true;
    this.companyService.getCompanies().subscribe({
      next: (data) => {
        console.log('Companies loaded:', data);
        this.companies = data;
        this.companyError = '';
      },
      error: (error) => {
        console.error('Error loading companies:', error);
        this.companyError = 'Failed to load companies.';
      },
      complete: () => {
        console.log('loadCompanies completed');
        this.loadingCompanies = false;
      }
    });
  }

  onSelectCompany(id: number): void {
    this.selectedCompanyId = id;
    this.vacancyError = '';
    this.loadingVacancies = true;

    this.companyService.getCompanyVacancies(id).subscribe({
      next: (data) => {
        this.vacancies = data;
      },
      error: () => {
        this.vacancyError = 'Failed to load vacancies.';
      },
      complete: () => {
        this.loadingVacancies = false;
      }
    });
  }
}