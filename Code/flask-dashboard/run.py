# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from os import listdir
from os.path import join, abspath
from flask_migrate import Migrate
from os import environ
from sys import exit
from decouple import config
from subprocess import Popen

from config import config_dict
from app import create_app, db
from app.home.models import Video

# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    
    # Load the configuration using the default values 
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app( app_config ) 
Migrate(app, db)

@app.before_first_request
def _fill_database_with_videos():
    db.session.query(Video).delete()
    db.session.commit()
    videos_path = 'app/base/static/assets/videos'
    videos = [(file_name, abspath(join(videos_path, file_name)))  for file_name in listdir(videos_path) if file_name.endswith('.mp4')]
    for video_name, video_path in videos:
        db.session.add(Video(video_name, video_path))
        db.session.commit()

if __name__ == "__main__":
    p = Popen(['python -m http.server'], shell=True)
    app.run()
