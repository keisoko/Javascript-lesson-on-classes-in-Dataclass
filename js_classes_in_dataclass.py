"""Codecademy JavaScript lesson on Classes in the Python Dataclass syntax"""

import random
from dataclasses import dataclass, field
from enum import Enum

import my_python_modules


class Specialty(Enum):
    """Hospital Employee Specialty"""

    SURGEON = "Surgeon"
    NURSE = "Nurse"


class HospitalDepartments(Enum):
    """Hospital Departments"""

    CARDIOVASCULAR = "Cardiovascular"
    NEUROSURGERY = "Neurosurgery"


@dataclass(slots=True)
class HospitalEmployee:
    """Dataclass representing the parent class of HospitalEmployee"""

    remaining_vacation_days = 20
    password_upper_limit = 10_000

    name: str
    specialty: Specialty
    days_off: int
    hospital_id: str = field(init=False)

    @property
    def take_vacation_days(self) -> int:
        """Calculates remaining vacation days"""
        return self.remaining_vacation_days - self.days_off

    @staticmethod
    def generate_password(password_upper_limit) -> int:
        """Generates random password"""
        return random.randint(0, password_upper_limit)

    def __post_init__(self):
        """Generates hospital id"""
        self.hospital_id = my_python_modules.generate_id(length=8)


@dataclass
class Surgeon(HospitalEmployee):
    """Child Class representing Surgeon."""

    department: HospitalDepartments


@dataclass
class Nurse(HospitalEmployee):
    """Child Class representing Nurse."""

    certifications: list[str] = field(default_factory=list)

    def add_certification(self, new_certification: str) -> None:
        """Appends a new certification to the certifications list."""
        if new_certification not in self.certifications:
            self.certifications.append(new_certification)


def main():
    """Main program."""

    surgeon_romero = Surgeon(
        name="Francisco Romero",
        specialty=Specialty.SURGEON,
        department=HospitalDepartments.CARDIOVASCULAR,
        days_off=4,
    )
    surgeon_jackson = Surgeon(
        name="Ruth Jackson",
        specialty=Specialty.SURGEON,
        department=HospitalDepartments.NEUROSURGERY,
        days_off=5,
    )
    nurse_olynyk = Nurse(
        name="Olynyk",
        specialty=Specialty.NURSE,
        certifications=["Trauma", "Pediatrics"],
        days_off=6,
    )
    nurse_spensa = Nurse(
        name="Spensa",
        specialty=Specialty.NURSE,
        certifications=["Cardiovascular", "Orthopedics"],
        days_off=3,
    )

    print()

    surgeons = [surgeon_romero, surgeon_jackson]

    for surgeon in surgeons:
        print(
            f"My name is {surgeon.name}, I am a {surgeon.department.value} {surgeon.specialty.value}, my id is {surgeon.hospital_id}, I have {surgeon.take_vacation_days} vacation days remaining and my password is {HospitalEmployee.generate_password(surgeon.password_upper_limit)}.",
            end="\n\n",
        )

    print()

    nurse_olynyk.add_certification("Genetics")
    nurse_spensa.add_certification("Neurology")

    nurses = [nurse_olynyk, nurse_spensa]
    for nurse in nurses:
        print(
            f"My name is {nurse.name}, I am a {nurse.specialty.value}, my id is {nurse.hospital_id}, I am certified to work at {nurse.certifications},\nI have {nurse.take_vacation_days} vacation days remaining and my password is {HospitalEmployee.generate_password(nurse.password_upper_limit)}.",
            end="\n\n",
        )


if __name__ == "__main__":
    main()