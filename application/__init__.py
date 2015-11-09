import logging

from flask import Flask

from common.config import load_configuration
from routes import AppRoutes


# load configuration
# ------------------
config = load_configuration()

# Logger configuration
# --------------------

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logging.getLogger('scoring').addHandler(ch)

# Initialize app
# --------------
app = Flask(__name__)

# Initialize metrics backend
# --------------------------
if config.debug or not config.graphite.enable:
    import greplin.scales.flaskhandler as statserver
    statserver.registerStatsHandler(app, __name__, prefix='/status/')
else:
    from greplin.scales.graphite import GraphitePeriodicPusher
    graphitePeriodicPusher = GraphitePeriodicPusher(config.graphite.host, config.graphite.port, None, period=10)
    graphitePeriodicPusher.allow("*")
    graphitePeriodicPusher.start()

if config.debug:
    app.config["DEBUG"] = config.debug

routes = AppRoutes(app)
