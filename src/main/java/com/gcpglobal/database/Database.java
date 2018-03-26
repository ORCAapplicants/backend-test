package com.gcpglobal.database;

import com.gcpglobal.models.Event;
import com.gcpglobal.models.Vehicle;

public interface Database {
	void createNewVehicle(Vehicle vehicle);
	
	void createNewEvent(Event event);
	
	void updateEvent(Event event);
	
	void getAlEventsForVehicle(Vehicle vehicle);
}
