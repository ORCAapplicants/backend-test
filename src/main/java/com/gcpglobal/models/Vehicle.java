package com.gcpglobal.models;

import java.util.List;

public class Vehicle {
	private VehicleType vehicleType;
	private LicencePlate licencePlate;
	private List<Event> events;
	
	public VehicleType getVehicleType() {
		return vehicleType;
	}
	public void setVehicleType(VehicleType vehicleType) {
		this.vehicleType = vehicleType;
	}
	public LicencePlate getLicencePlate() {
		return licencePlate;
	}
	public void setLicencePlate(LicencePlate licencePlate) {
		this.licencePlate = licencePlate;
	}
	public List<Event> getEvents() {
		return events;
	}
	public void setEvents(List<Event> events) {
		this.events = events;
	}
	
	
}
