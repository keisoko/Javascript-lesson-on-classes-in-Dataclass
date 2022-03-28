"""Codecademy JavaScript lesson on Classes in the Python Dataclass syntax"""

import random
from dataclasses import dataclass, field
from enum import Enum, auto


class Specialty(Enum):
    """Hospital Employee Specialty"""
    SURGEON = auto()
    NURSE = auto()


class Department(Enum):
    """Hospital Departments"""
    CARDIOVASCULAR = auto()
    ORTHOPEDICS = auto()


@dataclass(kw_only=True, slots=True)
class HospitalEmployee:
    """Dataclass representing the parent class of HospitalEmployee"""
    remaining_vacation_days = 20
    name: str
    specialty: Specialty
    days_off: int

    @property
    def take_vacation_days(self):
        """Calculates remaining vacation days"""
        return self.remaining_vacation_days - self.days_off

    @staticmethod
    def generate_password():
        """Generates random password"""
        return random.randint(0, 10_000)


@dataclass(kw_only=True, slots=True)
class Surgeon(HospitalEmployee):
    """Child Class representing Surgeon."""
    department: Department


@dataclass(kw_only=True, slots=True)
class Nurse(HospitalEmployee):
    """Child Class representing Nurse."""
    certifications: list[str] = field(default_factory=list)

    def add_certification(self, new_certification):
        """Appends a new certification to the certifications list."""
        self.certifications.append(new_certification)


# Dictionaries to store class objects and their attributes

Surgeons = {
    "surgeon_romero": {
        "name": "Francisco Romero",
        "specialty": Specialty.SURGEON.name,
        "department": Department.CARDIOVASCULAR,
        "days_off": 4,
    },
    "surgeon_jackson": {
        "name": "Ruth Jackson",
        "specialty": Specialty.SURGEON.name,
        "department": Department.ORTHOPEDICS,
        "days_off": 5,
    }
}

Nurses = {
    "nurse_olynyk": {
        "name": "Olynyk",
        "specialty": Specialty.NURSE.name,
        "certifications": ["Trauma", "Pediatrics"],
        "days_off": 6,
    },
    "nurse_spensa": {
        "name": "Spensa",
        "specialty": Specialty.NURSE.name,
        "certifications": ["Cardiovascular", "Orthopedics"],
        "days_off": 3,
    }
}

# Unpacks dictionary stored class objects

surgeon_romero = Surgeon(**Surgeons["surgeon_romero"])
surgeon_jackson = Surgeon(**Surgeons["surgeon_jackson"])
nurse_olynyk = Nurse(**Nurses["nurse_olynyk"])
nurse_spensa = Nurse(**Nurses["nurse_spensa"])

surgeons = [surgeon_romero, surgeon_jackson]

for surgeon in surgeons:
    print(f"My name is {surgeon.name}, I am a {surgeon.department} {surgeon.specialty}, I have {surgeon.take_vacation_days} vacation days remaining and my password is {HospitalEmployee.generate_password()}.")

print()

nurse_olynyk.add_certification("Genetics")
nurse_spensa.add_certification("Neurology")

nurses = [nurse_olynyk, nurse_spensa]
for nurse in nurses:
    print(
        f"My name is {nurse.name}, I am a {nurse.specialty}, I am certified to work at {nurse.certifications},\nI have {nurse.take_vacation_days} vacation days remaining and my password is {HospitalEmployee.generate_password()}.")

print()
