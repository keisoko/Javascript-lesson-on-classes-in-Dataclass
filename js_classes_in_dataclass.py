"""Codecademy JavaScript lesson on Classes in the Python Dataclass syntax"""

import random
import string
from dataclasses import dataclass, field
from enum import Enum


def generate_id(length: int):
    """Helper function to generate id."""
    return "".join(random.choices(string.hexdigits.upper(), k=length))


class Specialty(Enum):
    """Hospital Employee Specialty"""

    SURGEON = "Surgeon"
    NURSE = "Nurse"


class HospitalDepartments(Enum):
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

    @property
    def take_vacation_days(self, REMAINING_VACATION_DAYS: int = 20) -> int:
        """Calculates remaining vacation days"""
        return REMAINING_VACATION_DAYS - self.days_off

    @staticmethod
    def generate_password(PASSWORD_UPPER_LIMIT: int = 10_000) -> int:
        """Generates random password"""
        return random.randint(0, PASSWORD_UPPER_LIMIT)

    def __post_init__(self):
        """Generates hospital id"""
        self.hospital_id = generate_id(length=8)


@dataclass
class Surgeon(HospitalEmployee):
    """Child Class representing Surgeon."""

    hospital_department: HospitalDepartments


@dataclass
class Nurse(HospitalEmployee):
    """Child Class representing Nurse."""

    certifications: list[str] = field(default_factory=list)

    def add_certification(self, new_certification: str) -> None:
        """Appends a new certification to the certifications list."""
        if new_certification not in self.certifications:
            self.certifications.append(new_certification)


class InstancesHolder:
    """Creates class instances"""

    surgeon_romero = Surgeon(
        name="Francisco Romero",
        specialty=Specialty.SURGEON,
        hospital_department=HospitalDepartments.CARDIOVASCULAR,
        days_off=4,
    )
    surgeon_jackson = Surgeon(
        name="Ruth Jackson",
        specialty=Specialty.SURGEON,
        hospital_department=HospitalDepartments.NEUROSURGERY,
        days_off=5,
    )
    surgeon_octavian = Surgeon(
        name="Tavi Octavian",
        specialty=Specialty.SURGEON,
        hospital_department=HospitalDepartments.ORTHOPEDICS,
        days_off=6,
    )

    nurse_olynyk = Nurse(
        name="Olynyk",
        specialty=Specialty.NURSE,
        certifications=["Trauma", "Pediatrics"],
        days_off=7,
    )
    nurse_spensa = Nurse(
        name="Spensa",
        specialty=Specialty.NURSE,
        certifications=["Cardiovascular", "Orthopedics"],
        days_off=8,
    )


def main():
    """Main program."""

    print()

    surgeon_romero = InstancesHolder.surgeon_romero
    surgeon_jackson = InstancesHolder.surgeon_jackson
    surgeon_octavian = InstancesHolder.surgeon_octavian

    surgeons = [surgeon_romero, surgeon_jackson, surgeon_octavian]

    for surgeon in surgeons:
        if surgeon.hospital_department.value[0] in "aeiouAEIOU":
            print(
                f"My name is {surgeon.name}, I am an {surgeon.hospital_department.value} {surgeon.specialty.value}, my id is {surgeon.hospital_id}, I have {surgeon.take_vacation_days} vacation days remaining and my password is {HospitalEmployee.generate_password()}.",
                end="\n\n",
            )
        else:
            print(
                f"My name is {surgeon.name}, I am a {surgeon.hospital_department.value} {surgeon.specialty.value}, my id is {surgeon.hospital_id}, I have {surgeon.take_vacation_days} vacation days remaining and my password is {HospitalEmployee.generate_password()}.",
                end="\n\n",
            )

    nurse_olynyk = InstancesHolder.nurse_olynyk
    nurse_spensa = InstancesHolder.nurse_spensa

    nurse_olynyk.add_certification("Genetics")
    nurse_spensa.add_certification("Neurology")

    nurses = [nurse_olynyk, nurse_spensa]
    for nurse in nurses:
        print(
            f"My name is {nurse.name}, I am a {nurse.specialty.value}, my id is {nurse.hospital_id}, I am certified to work at {nurse.certifications},\nI have {nurse.take_vacation_days} vacation days remaining and my password is {HospitalEmployee.generate_password()}.",
            end="\n\n",
        )


if __name__ == "__main__":
    main()
