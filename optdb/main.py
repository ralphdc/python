#!/usr/bin/env python3

from app import App
import argparse



def main(args):

	city163 = App.get_unit('city163')
	#city163.handle_province()

	if args.operate == 'pro':
		city163.handle_province()
	elif args.operate == 'bj':
		city163.handle_beijing()
	elif args.operate == 'sh':
		city163.handle_shanghai()
	elif args.operate == 'parse_city':
		city163.handle_guangdong_city()
	elif args.operate == 'parse_zone':
		city163.handle_guangdong_zone()
	elif args.operate == 'parse':
		city163.parse_data()
	else:
		print("[Error] Parameter passed error!")



if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--operate', type=str)
	parser.add_argument('-p', '--pname', type=str)
	args = parser.parse_args()

	main(args)