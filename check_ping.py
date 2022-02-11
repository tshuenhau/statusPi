import os

def check_ping(hostname):
	response = os.system("ping -c 1 " + hostname)
	if(response == 1):
		response = os.system("ping -c 1 " + hostname)
		if(response == 1):
			response = os.system("ping -c 1 " + hostname)
		
	
	return response
