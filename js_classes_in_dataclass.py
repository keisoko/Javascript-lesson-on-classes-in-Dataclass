"""Codecademy JavaScript lesson on Classes in the Python Dataclass syntax"""

import random
import string
from dataclasses import dataclass, field
from enum import Enum

REMAINING_VACATION_DAYS: int = 20
PASSWORD_UPPER_LIMIT: int = 10_000


def generate_id(length: int):
    """Helper function to generate id."""
    return "".join(random.choices(string.hexdigits.upper(), k=length))


class Specialty(Enum):
    """Hospital Employee Specialty"""

    SURGEON = "Surgeon"
    NURSE = "Nurse"


class Department(Enum):
    """Hospital Departments"""

    CARDIOVASCULAR = "Cardiovascular"
    NEUROSURGERY = "Neurosurgery"
    ORTHOPEDICS = "Orthopedics"


@dataclass(slots=True)
class HospitalEmployee:
    """Dataclass representing the parent class of HospitalEmployee"""

    name: str
    specialty: Specialty
    days_off: int
    hospital_id: str = field(init=False)
    email_address: str = field(init=False)

    def __post_init__(self):
        """Initializes the hospital employee id and email address"""
        self.hospital_id = generate_id(length=8)
        first_name, last_name = self.name.split()
        self.email_address = f"{first_name}.{last_name}@hospital.com"

    @property
    def take_vacation_days(self) -> int:
        """Calculates remaining vacation days"""
        return REMAINING_VACATION_DAYS - self.days_off

    @staticmethod
    def generate_password() -> int:
        """Generates random password"""
        return random.randint(0, PASSWORD_UPPER_LIMIT)

    @property
    def say_email(self) -> str:
        """Display email address"""
        return f"my email address is {self.email_address}"


@dataclass(slots=True)
class Surgeon(HospitalEmployee):
    """Child Class representing Surgeon."""

    hospital_department: Department

    @property
    def surgeon_description(self) -> str:
        """Describes the Surgeon."""
        return f"My name is {self.name}, I am a {self.hospital_department} {self.specialty.value}, {self.say_email}, my id is {self.hospital_id}, I have {self.take_vacation_days} vacation days remaining and my password is {HospitalEmployee.generate_password()}."


@dataclass(slots=True)
class Nurse(HospitalEmployee):
    """Child Class representing Nurse."""

    certifications: list[str] = field(default_factory=list)

    def add_certification(self, new_certification: str) -> None:
        """Appends a new certification to the certifications list."""
        if new_certification not in self.certifications:
            self.certifications.append(new_certification)

    @property
    def nurse_description(self) -> str:
        """Describes the Nurse"""
        return f"My name is {self.name}, I am a {self.specialty.value}, my id is {self.hospital_id}, I am certified to work at {self.certifications},\n{self.say_email}, I have {self.take_vacation_days} vacation days remaining and my password is {HospitalEmployee.generate_password()}."


surgeon_romero = Surgeon(
    name="Francisco Romero",
    specialty=Specialty.SURGEON,
    hospital_department=Department.CARDIOVASCULAR,
    days_off=4,
)
surgeon_jackson = Surgeon(
    name="Ruth Jackson",
    specialty=Specialty.SURGEON,
    hospital_department=Department.NEUROSURGERY,
    days_off=5,
)
surgeon_octavian = Surgeon(
    name="Tavi Octavian",
    specialty=Specialty.SURGEON,
    hospital_department=Department.ORTHOPEDICS,
    days_off=6,
)

nurse_olynyk = Nurse(
    name="Olynyk Ivans",
    specialty=Specialty.NURSE,
    certifications=["Trauma", "Pediatrics"],
    days_off=7,
)
nurse_spensa = Nurse(
    name="Spensa Nightshade",
    specialty=Specialty.NURSE,
    certifications=["Cardiovascular", "Orthopedics"],
    days_off=8,
)


def main():
    """Main program."""

    print()

    surgeons = [surgeon_romero, surgeon_jackson, surgeon_octavian]

    for surgeon in surgeons:
        print(surgeon.surgeon_description, end="\n\n")

    nurse_olynyk.add_certification("Genetics")
    nurse_spensa.add_certification("Neurology")

    nurses = [nurse_olynyk, nurse_spensa]

    for nurse in nurses:
        print(nurse.nurse_description, end="\n\n")


if __name__ == "__main__":
    main()
