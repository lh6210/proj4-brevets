"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import logging

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

# dictionary
ACP_RULES = [(1000, 26, 13.333), (600, 28, 11.428), (400, 30, 15), (200, 32, 15), (0, 34, 15)]




"""control_dist_km is from "km" input, brevet_dist_km is from the dropdown box, brevet_start_time is from "begin_date", "begin_time" input box"""
def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    # time is an arrow object
    time = arrow.get(brevet_start_time)  
    logging.info("In acp_times.py file.  Time is {}".format(time))

    brevet_dist = brevet_dist_km
    limit = brevet_dist * 1.10

    curr_control = control_dist_km

    interval = 0

    for stop, maxSpd, minSpd in ACP_RULES:
        if curr_control > stop:
            interval = interval + (curr_control - stop) / maxSpd
            logging.info("interval is {}".format(interval))
            curr_control = stop

    logging.info("the calculated interval is {}".format(interval))
    time = time.shift(hours=+interval) 
    logging.info("Now the shifted open_time is {}".format(time))
    result = time.format('YYYY-MM-DD HH:mm:ss ZZ')
    #logger.info("the date&time server returned is " + result) 


    return result 


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    return arrow.now().isoformat()
