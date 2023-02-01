"""Codecademy JavaScript lesson on Classes in the Python Dataclass syntax"""

import random
from dataclasses import dataclass, field
from enum import StrEnum, auto
from uuid import uuid4


@dataclass(frozen=True)
class ConstantsNamespace:
    REMAINING_VACATION_DAYS: int = 20
    PASSWORD_UPPER_LIMIT: int = 10_000


constants = ConstantsNamespace()


def generate_id() -> str:
    """Helper function to generate id."""
    return uuid4().hex


class Specialty(StrEnum):
    """Enum class representing the Hospital Employee Specialty"""

    SURGEON = auto()
    NURSE = auto()


class Department(StrEnum):
    """Enum class representing the Hospital Departments"""

    CARDIOVASCULAR = auto()
    NEUROSURGERY = auto()
    ORTHOPEDICS = auto()


@dataclass(slots=True, kw_only=True)
class HospitalEmployee:
    """Dataclass representing the Hospital Employee"""

    name: str
    specialty: Specialty
    days_off: int
    hospital_id: str = field(init=False, default_factory=generate_id)
    hospital_email: str = field(init=False)

    def __post_init__(self):
        """Initializes the hospital employee email"""
        first_name, last_name = self.name.split()
        self.hospital_email = f"{first_name.lower()}.{last_name.lower()}@hospital.com"

    @property
    def display_email(self) -> str:
        """Returns the hospital employee email address"""
        return f"My email address is {self.hospital_email}."

    @staticmethod
    def generate_password() -> int:
        """Generates random password"""
        return random.randrange(constants.PASSWORD_UPPER_LIMIT)

    @property
    def display_id_and_password(self) -> str:
        """Returns surgeon's id and password"""
        return f"My id is {self.hospital_id} and my password is {HospitalEmployee.generate_password()}."

    @property
    def take_vacation_days(self) -> int:
        """Calculates remaining vacation days"""
        return constants.REMAINING_VACATION_DAYS - self.days_off

    @property
    def display_remaining_vacation_days(self) -> str:
        """Returns the surgeon's remaining vacation days"""
        return f"I have {self.take_vacation_days} vacation days remaining."


@dataclass(slots=True, kw_only=True)
class Surgeon(HospitalEmployee):
    """Child Class representing Surgeon."""

    hospital_department: Department

    @property
    def surgeon_description(self) -> str:
        """Describes the Surgeon."""
        if self.hospital_department.value[0] in "aeiou":
            return f"My name is {self.name} and I am an {self.hospital_department} {self.specialty}."
        else:
            return f"My name is {self.name} and I am a {self.hospital_department} {self.specialty}."


@dataclass(slots=True, kw_only=True)
class Nurse(HospitalEmployee):
    """Child Class representing Nurse."""

    certifications: list[str] = field(default_factory=list)

    @property
    def nurse_description(self) -> str:
        """Describes the Nurse"""
        return f"My name is {self.name} and I am a {self.specialty}."

    def add_certification(self, new_certification: str) -> None:
        """Appends a new certification to the certifications list."""
        if new_certification not in self.certifications:
            self.certifications.append(new_certification)

    @property
    def nurse_certifications(self) -> str:
        return f"I am certified to work at {self.certifications}."


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


def about_staff(staff_member) -> None:
    print(staff_member.display_email)
    print(staff_member.display_id_and_password)
    print(staff_member.display_remaining_vacation_days, "\n")


def execute_main() -> None:

    print()

    surgeons = [surgeon_romero, surgeon_jackson, surgeon_octavian]

    for surgeon in surgeons:
        print(surgeon.surgeon_description)
        about_staff(surgeon)

    nurse_olynyk.add_certification("Genetics")
    nurse_spensa.add_certification("Neurology")

    print()

    nurses = [nurse_olynyk, nurse_spensa]

    for nurse in nurses:
        print(nurse.nurse_description)
        print(nurse.nurse_certifications)
        about_staff(nurse)


if __name__ == "__main__":
    execute_main()
