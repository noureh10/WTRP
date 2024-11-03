import current_state as cs
from pypresence import Presence as prsc
import sys
import os
import time

# Important stuff
DISCORD_APP_ID = "1301947717672632432"
RPC_NO_CONNECT = "RPC has failed to connect, aborting"
PN_NOT_PRESENT = "War Thunder is not launched, aborting"
EXIT_FAILURE = 1
EXIT_SUCCESS = 0

def error_message(message):
	print(message, file=sys.stderr)

def is_wt_active():
	process_name = "aces.exe"
	output = os.popen(f'tasklist /FI "IMAGENAME eq {process_name}"').read()
	return (process_name in output)

def rich_presence_loop():
	if (not (is_wt_active())):
		error_message(PN_NOT_PRESENT)
		sys.exit(EXIT_FAILURE)
	rpc = prsc(DISCORD_APP_ID)
	try:
		rpc.connect()
	except:
		error_message(RPC_NO_CONNECT)
		exit(1)
	current_time = time.time()
	while (is_wt_active()):
		main_data = cs.get_vehicle()
		secondary_data = "..."
		rpc.update(state="...", details=main_data, start=current_time)
		time.sleep(15) 

if __name__ == "__main__" :
    rich_presence_loop()