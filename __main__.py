from application import app
from application.common.config import load_configuration

# fetch config
config = load_configuration()
listen_port = config.listen_port

# start app
if config.debug and config.environment == "development":
    app.config["SERVER_NAME"] = "127.0.0.1:%s" % listen_port
    app.run()
