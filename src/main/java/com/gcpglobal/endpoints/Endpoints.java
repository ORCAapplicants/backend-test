package com.gcpglobal.endpoints;

import java.util.List;

import com.gcpglobal.models.LicencePlate;
import com.gcpglobal.models.PaymentReport;
import com.gcpglobal.models.VehicleType;

public interface Endpoints {
	void vehicleEnters(LicencePlate licencePlate);
	
	void vehicleLeaves(LicencePlate licencePlate);
	
	void registerVehicle(LicencePlate licencePlate, VehicleType vehicleType);
	
	void rebootMonth();
	
	List<PaymentReport> paymentReport();
}
