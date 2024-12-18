from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()

DATABASE_URL = os.getenv("MYSQL_DATABASE")
engine = create_engine(DATABASE_URL)

# class Students(Base):
#     __tablename__ = "students"
    
#     student_id = Column(String(50), primary_key=True)
#     student_name = Column(String(256), nullable=False)
#     current_sem = Column(String(50), unique=False, nullable=True)
#     current_group = Column(Integer, ForeignKey('group.group_id'), nullable=True)
    
#     group = relationship('Group', back_populates='students')

#     def __repr__(self):
#         return f"<Students(student_id={self.student_id}, student_name='{self.student_name}', current_sem='{self.current_sem}', current_group='{self.current_group}')>"
# class Lecturers(Base):
#     __tablename__ = "lecturers"

#     lecturer_id = Column(String(50), primary_key=True)
#     lecturer_name = Column(String(256), nullable=False)
#     lecturer_email = Column(String(256), nullable=True)

#     def __repr__(self):
#         return f"<Lecturers(lecturer_key={self.lecturer_key}, lecturer_name='{self.lecturer_name}', lecturer_id='{self.lecturer_id}')>"
# class Group(Base):
#     __tablename__ = "group"

#     group_id = Column(Integer, primary_key=True)
#     group_name = Column(String(256), nullable=False, unique=False)
#     semester = Column(String(256), nullable=True)
#     cohort = Column(String(256), nullable=True)
#     students = relationship('Students', back_populates='group')

#     def __repr__(self):
#         return f"<Group(group_id={self.group_id}, group_name='{self.group_name}')>"

#     def to_dict(self):
#         return {
#             "group_id": self.group_id,
#             "group_name": self.group_name,
#             "semester": self.semester,
#             "cohort": self.cohort
#         }
