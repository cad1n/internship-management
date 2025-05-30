import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class SetorService {
  private setores: string[] = [
    'Setor A',
    'Setor B',
    'Setor C',
    'Setor D',
    'Setor E'
  ];

  constructor(private readonly http: HttpClient) {}

  getSetores(): string[] {
    return this.setores;
  }

  addSetor(setor: string): void {
    this.setores.push(setor);
  }

  removeSetor(setor: string): void {
    this.setores = this.setores.filter(s => s !== setor);
  }
}
