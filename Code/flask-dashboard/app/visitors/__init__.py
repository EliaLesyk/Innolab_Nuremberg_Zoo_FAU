from flask import Blueprint

blueprint = Blueprint(
    'visitors_bluebrint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)