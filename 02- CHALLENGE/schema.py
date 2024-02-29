from __future__ import annotations
from typing import Any, List, Optional
from pydantic import BaseModel,Extra

class Skill(BaseModel):
    name: str
    level: str
    experience: int

class Aptitude(BaseModel):
    name: str

class Tool(BaseModel):
    name: str
    level: str
    experience: int

class Language(BaseModel):
    name: str
    level: str

class Benefit(BaseModel):
    name: str

class JobPost(BaseModel):
    # id: Optional[int] = None
    # companyId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    createdAt: Optional[str] = None
    availableSlots: Optional[int] = None
    skills: Optional[List[Skill]] = None
    aptitudes: Optional[List[Aptitude]] = None
    tools: Optional[List[Tool]] = None
    languages: Optional[List[Language]] = None
    benefits: Optional[List[Benefit]] = None
    scholarity: Optional[str] = None
    workhours: Optional[str] = None
    locationConditions: Optional[str] = None
    nationalRemote: Optional[Any] = None
    minSalary: Optional[int] = None
    maxSalary: Optional[int] = None
    minAge: Optional[int] = None
    maxAge: Optional[Any] = None
    sex: Optional[str] = None
    yearsOfExperience: Optional[int] = None
    status: Optional[str] = None
    country: Optional[str] = None
    updatedAt: Optional[str] = None
    driversLicense: Optional[bool] = None
    degree: Optional[bool] = None
    validPassport: Optional[bool] = None
    validVisa: Optional[bool] = None
    nationalRelocation: Optional[bool] = None
    internationalRelocation: Optional[bool] = None
    availabilityToTravel: Optional[bool] = None
    seniority: Optional[str] = None
    showSalaryRange: Optional[bool] = None
    state: Optional[str] = None
    city: Optional[str] = None
    postalCode: Optional[str] = None
    slug: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    companyName: Optional[str] = None
    companyImg: Optional[str] = None
    class Config:
        extra = Extra.ignore
