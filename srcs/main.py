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
	return (os.system(f'tasklist /fi "imagename eq aces.exe" > nul 2>&1')  == 0)


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
		current_state = "future state function"
		current_details = "future details function"
		rpc.update(state=current_state, details=current_details, start=current_time)
		time.sleep(10)

if __name__ == "__main__" :
    rich_presence_loop()