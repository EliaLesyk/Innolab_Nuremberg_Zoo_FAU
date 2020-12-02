import random

from app.visitors import blueprint
from flask import render_template


@blueprint.route('/visitor-screen')
def visitor_screen():
    return render_template('visitor-screen.html', segment='index')

@blueprint.route('/get-temperature')
def get_temperature():
    # TODO make this read a value from a mocking file
    temp = random.randint(0,40)
    return str(str(temp) + ' °C')

@blueprint.route('/get-humidity')
def get_humidity():
    # TODO make this read a value from a mocking file
    hum = random.randint(60,100)
    return str(str(hum) + ' %')