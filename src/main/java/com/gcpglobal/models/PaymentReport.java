package com.gcpglobal.models;

public class PaymentReport {
	private LicencePlate licencePlate;
	private Long minutes;
	private Long amountToPay;
	
	public Long getAmountToPay() {
		return amountToPay;
	}
	public void setAmountToPay(Long amountToPay) {
		this.amountToPay = amountToPay;
	}
	public Long getMinutes() {
		return minutes;
	}
	public void setMinutes(Long minutes) {
		this.minutes = minutes;
	}
	public LicencePlate getLicencePlate() {
		return licencePlate;
	}
	public void setLicencePlate(LicencePlate licencePlate) {
		this.licencePlate = licencePlate;
	}
}
