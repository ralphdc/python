#!/usr/bin/env python3

from sqlalchemy import Column, String, CHAR, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Province(Base):

	__tablename__ = 'province'

	province_id = Column(Integer, nullable=False, primary_key=True, unique=True, autoincrement=True)
	province_code = Column(String(1000), nullable=False, unique=True)
	province_name = Column(String(255), nullable=False, unique=True)
	created_at = Column(DateTime, default=func.now())
	updated_at = Column(DateTime, default=func.now(), onupdate=func.utc_timestamp())

	def __init__(self, code, name):
		self.province_code = code 
		self.province_name = name


class City(Base):
	__tablename__ = 'city'

	city_id = Column(Integer, nullable=False, primary_key=True, unique=True, autoincrement=True)
	city_province_code =  Column(String(1000), nullable=False)
	city_name = Column(String(255), nullable=False, unique=True)
	city_code = Column(String(255), nullable=False, unique=True)

	def __init__(self, pcode, code, name):
		self.city_province_code = pcode
		self.city_name = name
		self.code = code 

class Zone(Base):
	__tablename__ = 'zone'

	zone_id = Column(Integer, nullable=False, primary_key=True, unique=True, autoincrement=True)
	zone_city_code = Column(String(255), nullable=False)
	zone_code = Column(String(255), nullable=False, unique=True)
	zone_name = Column(String(255), nullable=False, unique=True)

	def __init__(self, ccode, code, name):
		self.zone_city_code = ccode 
		self.zone_code = code 
		self.zone_name = name 

	def __repr__(self):
		return "table: %s" % self.__tablename__


#Base.metadata.drop_all()
#Base.metadata.create_all()