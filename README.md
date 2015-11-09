Demo Python application using Flask and Scales
==============================================

# Purpose

This repo contains an application skeleton for Flask development with Scales, which can be used to develop any 
API or backend server.

# Preparing the environment

**Warning: you should use a virtualenv or pyenv before doing the next commands.**

Run the following:

```shell
pip install -r requirements.txt && pip install -r requirements-devel.txt
```

Explanations :

  * requirements.txt: contains python modules required for normal run ;
  * requirements-devel.txt: contains python modules / utils for development.

# Metrics

In development mode, metrics are exposed on http://127.0.0.1:8090/status/, directly available.

In production mode, they are sent directly to the specified graphite server, being 127.0.0.1 by default 
(see application/common/config.py for defaults).

# Running

## Tests

Run the following in the repo:

```shell
py.test
```

## Development

Run the following in the repo:

```shell
python .
```

The app will listen on 127.0.0.1:8090 by default. The port can be changed via the ```listen_port``` directive 
in config/development.yml.

## Production

Run the following :

```shell
ENV=production gunicorn wsgi:app
```

The app will listen on 0.0.0.0:8000 by default, without any gunicorn configuration.