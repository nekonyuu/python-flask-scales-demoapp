import logging

logger = logging.getLogger(__name__)

from flask import jsonify
from greplin import scales
from common.config import load_configuration


class AppRoutes(object):
    """
    Routes object, for high level metrics
    """
    client_errors = scales.IntStat('client_errors')
    hits = scales.IntStat('hits')
    latency = scales.PmfStat('latency')

    def __init__(self, app):
        """
        :param app:
        :type app: flask.Flask.app
        :return:
        """
        scales.init(self, '/')
        self.app = app
        self._config = load_configuration()

        # plugging routes
        self.app.add_url_rule(
            '/v1.0/hello/<name>',
            'hello_name',
            self.hello_name, methods=['GET']
        )

    def hello_name(self, name):
        """
        Say hello to name
        :param name:
        :type name: unicode
        :return:
        """
        self.hits += 1

        with self.latency.time():
            response = dict()
            rcode = 200

            if not isinstance(name, unicode):
                self.client_errors += 1
                response.update({
                    "message": "",
                    "error": "Bad Request"
                })
                rcode = 400
            else:
                response.update({
                    "message": "Hello %s" % name
                })

            return jsonify(response), rcode

