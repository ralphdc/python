#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config


class db_session():

	@classmethod
	def _db_session_(cls):
		db_host = Config.db_host or None
		db_port = Config.db_port or None 
		db_name = Config.db_name or None 
		db_user = Config.db_user or None 
		db_pwd 	= Config.db_pwd or None

		if not db_host or not db_port or not db_name or not db_user or not db_pwd:
			raise Exception("[ Error ] - db configure is wrong!")

		try:
			# 初始化数据库连接:
			engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" % (db_user, db_pwd, db_host, db_port, db_name))
			# 创建DBSession类型:
			DBSession = sessionmaker(bind=engine)
		except Exception as e:
			raise

		return DBSession()