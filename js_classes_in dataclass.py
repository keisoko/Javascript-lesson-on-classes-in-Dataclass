"""Codecademy JavaScript lesson on Classes in the Python Dataclass syntax"""

from dataclasses import dataclass, field
import random


@dataclass
class HospitalEmployee:
    """Dataclass representing the parent class of HospitalEmployee"""
    remaining_vacation_days = 20

    __slots__ = ["name", "specialty", "days_off"]
    name: str
    specialty: str
    days_off: int

    def take_vacation_days(self, days_off):
        """Calculates remaining vacation days"""
        return self.remaining_vacation_days - days_off

    @staticmethod
    def generate_password():
        """Generates random password"""
        return random.randint(0, 10_000)


@dataclass
class Surgeon(HospitalEmployee):
    """Child Class representing Surgeon."""
    __slots__ = ["department"]
    department: str


@dataclass
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
        "specialty": "surgeon",
        "department": "Cardiovascular",
        "days_off": 4,
    },
    "surgeon_jackson": {
        "name": "Ruth Jackson",
        "specialty": "surgeon",
        "department": "Orthopedics",
        "days_off": 5,
    }
}

Nurses = {
    "nurse_olynyk": {
        "name": "Olynyk",
        "specialty": "nurse",
        "certifications": ["Trauma", "Pediatrics"],
        "days_off": 6,
    },
    "nurse_spensa": {
        "name": "Spensa",
        "specialty": "nurse",
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
    print(f"My name is {surgeon.name}, I am a {surgeon.department} \
{surgeon.specialty}, I have \
{surgeon.take_vacation_days(surgeon.days_off)} vacation days remaining \
and my random password is {HospitalEmployee.generate_password()}.")

print()

nurse_olynyk.add_certification("Genetics")
nurse_spensa.add_certification("Speciesology")

nurses = [nurse_olynyk, nurse_spensa]
for nurse in nurses:
    print(
        f"My name is {nurse.name}, I am a {nurse.specialty},\
I am certified to work at {nurse.certifications},\
 I have {nurse.take_vacation_days(nurse.days_off)} vacation days \
and my random password is {HospitalEmployee.generate_password()}.")
