from datetime import date
from typing import List, Union


class Patient:
    def __init__(self,
                 patient_id: int,
                 name: str,
                 date_of_birth: date,
                 address: str,
                 contact_number: str,
                 email: str):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.contact_number = contact_number
        self.email = email

    def get_details(self) -> dict:
        return vars(self)

    def update_details(self, name: str, address: str, contact_number: str, email: str) -> None:
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.email = email


class Appointment:
    def __init__(self,
                 appointment_id: int,
                 patient: Patient,
                 date: date,
                 time: str,
                 dentist: str):
        self.appointment_id = appointment_id
        self.patient = patient
        self.date = date
        self.time = time
        self.dentist = dentist

    def schedule_appointment(self, date: date, time: str) -> None:
        self.date = date
        self.time = time

    def reschedule_appointment(self, new_date: date, new_time: str) -> None:
        self.date = new_date
        self.time = new_time

    def cancel_appointment(self) -> None:
        # Logic to cancel the appointment
        pass


class Treatment:
    def __init__(self,
                 treatment_id: int,
                 patient: Patient,
                 description: str,
                 date_performed: date,
                 results: str):
        self.treatment_id = treatment_id
        self.patient = patient
        self.description = description
        self.date_performed = date_performed
        self.results = results

    def record_treatment(self, description: str, date_performed: date, results: str) -> None:
        self.description = description
        self.date_performed = date_performed
        self.results = results

    def update_treatment_results(self, results: str) -> None:
        self.results = results


class Billing:
    def __init__(self,
                 bill_id: int,
                 patient: Patient,
                 treatment: Treatment,
                 amount: float,
                 date_issued: date,
                 due_date: date,
                 status: str):
        self.bill_id = bill_id
        self.patient = patient
        self.treatment = treatment
        self.amount = amount
        self.date_issued = date_issued
        self.due_date = due_date
        self.status = status

    def generate_bill(self, amount: float, date_issued: date, due_date: date) -> None:
        self.amount = amount
        self.date_issued = date_issued
        self.due_date = due_date

    def mark_as_paid(self) -> None:
        self.status = "Paid"


class Staff:
    def __init__(self,
                 staff_id: int,
                 name: str,
                 role: str):
        self.staff_id = staff_id
        self.name = name
        self.role = role

    def get_details(self) -> dict:
        return vars(self)

    def update_details(self, name: str, role: str) -> None:
        self.name = name
        self.role = role


class Equipment:
    def __init__(self,
                 equipment_id: int,
                 equipment_type: str,
                 manufacturer: str,
                 purchase_date: date,
                 last_maintenance_date: date):
        self.equipment_id = equipment_id
        self.equipment_type = equipment_type
        self.manufacturer = manufacturer
        self.purchase_date = purchase_date
        self.last_maintenance_date = last_maintenance_date

    def schedule_maintenance(self, maintenance_date: date) -> None:
        self.last_maintenance_date = maintenance_date

    def update_maintenance_date(self, new_date: date) -> None:
        self.last_maintenance_date = new_date


class Inventory:
    def __init__(self,
                 inventory_id: int,
                 item_name: str,
                 quantity: int,
                 last_ordered_date: date,
                 supplier: str):
        self.inventory_id = inventory_id
        self.item_name = item_name
        self.quantity = quantity
        self.last_ordered_date = last_ordered_date
        self.supplier = supplier

    def order_item(self, quantity: int) -> None:
        self.quantity += quantity
        # Logic to order the item, possibly updating the last_ordered_date

    def update_quantity(self, quantity: int) -> None:
        self.quantity = quantity


class Feedback:
    def __init__(self,
                 feedback_id: int,
                 patient: Patient,
                 comments: str,
                 date_submitted: date):
        self.feedback_id = feedback_id
        self.patient = patient
        self.comments = comments
        self.date_submitted = date_submitted

    def submit_feedback(self, comments: str) -> None:
        self.comments = comments

    def update_feedback(self, new_comments: str) -> None:
        self.comments = new_comments
