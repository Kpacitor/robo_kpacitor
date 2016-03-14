
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/robo_kpacitor/")

activate_this = '/var/www/robo_kpacitor/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from kpacitorpi import app as application
application.secret_key = 'Add your secret key'