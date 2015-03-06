import datetime

def get_current_time_delta(delta=0):
	return datetime.datetime.now() + datetime.timedelta(hours=delta)