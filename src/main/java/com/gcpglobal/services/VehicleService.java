package com.gcpglobal.services;

import com.gcpglobal.models.LicencePlate;
import com.gcpglobal.models.VehicleType;

public interface VehicleService {
	void registerVehicle(LicencePlate licencePlate, VehicleType vehicleType);
	
}
