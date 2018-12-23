#!/usr/bin/env python3

from . import Base
from db import db_session
from data import *
from log import Log 

from models import Province, City, Zone

import hashlib
import os

class City163(Base):

	zone_dict = {
		'guangdong': '19',

	}

	zone_provice_code = ["19","11", "7", "10", "18", "17", "15", "22", "4", "5", "6", "8", "9", "12", "13", "14", "16", "20", "21", "23", "24", "25", "26", "27", "28", "29", "30"]

	zone_data = [
		(guangdong_city, guangdong_zone),
		(zhejiang_city, zhejiang_zone),
		(liaoning_city, liaoning_zone),
		(jiangsu_city, jiangsu_zone),
		(hunan_city, hunan_zone),
		(hubei_city, hubei_zone),
		(shandong_city, shandong_zone),
		(sichuan_city, sichuan_zone),
		(hebei_city, hebei_zone),
		(sanxi_city, shanxi_zone),
		(neimenggu_city, neimenggu_zone),
		(jilin_city, jilin_zone),
		(heilongjiang_city, heilongjiang_zone),
		(anhui_city, anhui_zone),
		(fujian_city, fujian_zone),
		(jiangxi_city, jiangxi_zone),
		(henan_city, henan_zone),
		(guangxi_city, guangxi_zone),
		(hainan_city, hainan_zone),
		(guizhou_city, guizhou_zone),
		(yunnan_city, yunnan_zone),
		(xizang_city, xizang_zone),
		(shanxi_city, shanxi_zone),
		(gansu_city, gansu_zone),
		(qinghai_city, qinghai_zone),
		(ningxia_city, ningxia_zone),
		(xinjiang_city, xinjiang_zone)
	]

	def __init__(self):
		super(City163, self).__init__()

		self.db = db_session._db_session_()

	def handle_province(self):

		try:
			for k,v in province_dict.items():
				print("%s - %s" % (k,v))
				province = Province(str(k), v)
				self.db.add(province)
				
			self.db.commit()
		except Exception as e:
			Log.get_logger().exception(e)
			raise
		print("handle province ok!")


	def handle_beijing(self):
		try:
			for k, v in beijing.items():
				print("%s - %s" % (k,v))
				city = City('0', k, v)
				self.db.add(city)
			self.db.commit()
		except Exception as e:
			Log.get_logger().exception(e)
			raise

		print("handle beijing ok!")

	def handle_shanghai(self):
		try:
			for k, v in shanghai.items():
				print("%s - %s" % (k,v))
				city = City('1', k, v)
				self.db.add(city)
			self.db.commit()
		except Exception as e:
			Log.get_logger().exception(e)
			raise

		print("handle shanghai ok!")

	def handle_guangdong_city(self):
		from data import guangdong_city
		for k , v in guangdong_city.items():
			print("%s - %s" % (k, v))
			city = City('19', k, v)
			t= self.db.add(city)
			print(t.rowcount)
		self.db.commit()
		print('insert guangdog city is ok!')

	def handle_guangdong_zone(self):
		from data import guangdong_zone
		for k, v in guangdong_zone.items():
			if v:
				for v_k, v_v in v.items():
					zone = Zone(k, v_k, v_v)
					self.db.add(zone)
		self.db.commit()
		print('insert guangdong zone is ok!')

	def handle_zhejiang_city(self):
		from data import zhejiang_city
		for k , v in zhejiang_city.items():
			print("%s - %s" % (k, v))
			city = City('11', k, v)
			self.db.add(city)
		self.db.commit()
		print('insert zhejiang city is ok!')

	def handle_zhejiang_zone(self):
		from data import zhejiang_zone
		for k, v in zhejiang_zone.items():
			if v:
				for v_k, v_v in v.items():
					zone = Zone(k, v_k, v_v)
					self.db.add(zone)
		self.db.commit()
		print('insert zhejiang zone is ok!')


	def parse_data(self):
		try:
			for i in range(len(self.zone_provice_code)):
				print("provice code: %s" % self.zone_provice_code[i])
				for k , v in self.zone_data[i][0].items():
					city_code = hashlib.md5(os.urandom(16)).hexdigest()
					city = City(self.zone_provice_code[i], city_code, v)
					self.db.add(city)
					print("add city: %s" % v)
					city_zones = self.zone_data[i][1].get(k)
					if city_zones:
						for zk, zv in city_zones.items():
							if zv:
								zone = Zone(city_code, zk, zv)
								self.db.add(zone)
								print("city: %s - zone: %s" % (v, zv))
				self.db.commit()
		except Exception as e:
			self.db.rollback()
		finally:
			self.db.close()