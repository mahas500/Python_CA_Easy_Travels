import { TestBed } from '@angular/core/testing';

import { ServerendpointsService } from './serverendpoints.service';

describe('ServerendpointsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ServerendpointsService = TestBed.get(ServerendpointsService);
    expect(service).toBeTruthy();
  });
});
