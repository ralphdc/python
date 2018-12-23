#!/usr/bin/env python3

from .Base import Base
from .City163 import City163


class App():

	app_dict = {
		'base': Base,
		'city163': City163
	}

	@classmethod
	def get_unit(cls, ins):
		return cls.app_dict.get(ins)()