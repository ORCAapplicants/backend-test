package com.gcpglobal.services;

import com.gcpglobal.models.LicencePlate;

public interface EventsService {
	void createEntranceEvent(LicencePlate licenePlate);
	
	void updateEventAsCarLeaves(LicencePlate licencePlate);

}
