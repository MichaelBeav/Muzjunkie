## Run Requirements

*   [web.py](http://webpy.org/) WSGI implementation

        pip install web.py

## Test Requirements

*   [nosetest](http://readthedocs.org/docs/nose/en/latest/) for testing (with [yanc](http://pypi.python.org/pypi/yanc/) for coloring)

        pip install nose yanc

## Usage

To try it out, simply start the module, by running:

    python bandmodule/web_server.py

And then use `curl`:

    curl -XPOST http://localhost:8080/band/MegaBand -d '{
    id : MegaBand
    }'

    curl -XGET http://localhost:8080/band/MegaBand

## Run Tests

    ./run_tests.sh
