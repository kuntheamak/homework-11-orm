from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# Define a SQLAlchemy model
Base = declarative_base()

# define model/class
class Employee(Base):
    __tablename__ = "employee"
    emp_num = Column(Integer, primary_key=True)
    emp_lname = Column(String(30))
    emp_fname = Column(String(30))
    emp_initial = Column(String(1))
    emp_hiredate = Column(Date)
    job_code = Column(Integer, ForeignKey("job.job_code"))
    emp_years = Column(Integer)
    emp_total_hours = Column(Integer)


class Job(Base):
    __tablename__ = "job"
    job_code = Column(Integer, primary_key=True)
    job_description = Column(String(30))
    job_chg_hour = Column(Float)
    job_last_update = Column(Date)


class Assignment(Base):
    __tablename__ = "assignment"
    assign_num = Column(Integer, primary_key=True)
    assign_date = Column(Date)
    proj_num = Column(Integer)
    emp_num = Column(Integer)
    assign_job = Column(Integer)
    assign_chg_hr = Column(Float)
    assign_hour = Column(Float)
    assign_charge = Column(Float)

    

class Project(Base):
    __tablename__ = "project"
    proj_num = Column(Integer, primary_keu=True)
    proj_name = Column(Integer)
    proj_value = Column(Float)
    proj_balance = Column(Float)
    emp_num = Column(Integer)
    