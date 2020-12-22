# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from app.home.models import Video
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound


@blueprint.route('/')
def visitor_screen():
    return render_template('visitor-screen.html')


@blueprint.route('/index')
@login_required
def index():
    return render_template('index.html', segment='index')


@blueprint.route('get-videos')
@login_required
def get_videos():
    videos = Video.query.all()
    for video in videos:
        print(video.path)
    return {'videos': [{'name': v.name, 'path': v.path} for v in videos]}


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:        
        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ):
    
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index' if current_user.is_authenticated else 'visitor-screen'

        return segment    

    except:
        return None  
