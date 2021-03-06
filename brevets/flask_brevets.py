"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    # km, brevet_km, date_time are three things client has sent to server

    open_time = ""
    close_time = ""
    valid_input = True

    beginTime = request.args.get('date_time', type=str)
    km = request.args.get('km', 999, type=float)
    brevet = request.args.get('brevet_km', 200, type=int)
    limit = brevet * 1.1

    if (km > limit) or (km < 0):
        valid_input = False
        # alert("error input!")
    else:
        # logging.info("formatted beginTime={}".format(beginTime))
        # app.logger.info("km={}".format(km))
        # app.logger.info("request.args: {}".format(request.args))
        # FIXME: These probably aren't the right open and close times
        # and brevets may be longer than 200km
        open_time = acp_times.open_time(km, brevet, beginTime)
        # logging.info("calculated time: {}".format(open_time))
        close_time = acp_times.close_time(km, brevet, beginTime)
        
    result = {"open": open_time, "close": close_time, "isValid": valid_input}
    return flask.jsonify(result=result)
        




    # result = {"open": open_time, "close": close_time}
    # return flask.jsonify(result=result)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
