package com.gcpglobal.endpoints.impl;

import java.util.List;

import com.gcpglobal.endpoints.Endpoints;
import com.gcpglobal.models.LicencePlate;
import com.gcpglobal.models.PaymentReport;
import com.gcpglobal.models.VehicleType;
import com.gcpglobal.services.EventsService;
import com.gcpglobal.services.VehicleService;

public class EndpointsImpl implements Endpoints{
	//EventsService instance should be injected via a framework.
	private EventsService eventsService;
	
	//VehicleService instance should be injected via a framework.
	private VehicleService vehicleService;
	
	
	public void vehicleEnters(LicencePlate licencePlate) {
		eventsService.createEntranceEvent(licencePlate);
	}

	public void vehicleLeaves(LicencePlate licencePlate) {
		eventsService.updateEventAsCarLeaves(licencePlate);
		
	}

	public void registerVehicle(LicencePlate licencePlate, VehicleType vehicleType) {
		vehicleService.registerVehicle(licencePlate, vehicleType);	
	}

	public void rebootMonth() {
		//Not needed to be implemented. PaymentReport method will only retrieve reports for givenMonth
		//BackEnd application should not need to know state of "current month"
		//API provided to client should be stateless. Month should be provided by client
		
	}

	public List<PaymentReport> paymentReport() {
		return null;
	}

}
