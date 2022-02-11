import os

def check_ping(hostname):
	response = os.system("ping -c 1 " + hostname)
	return response
