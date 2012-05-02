## Requirements

To set up all requirements, use [pip](http://www.pip-installer.org/en/latest/index.html):

    pip install -r requirements.txt

## Usage

To try it out, simply start the module, by running:

    python bandmodule/web_server.py

And then use `curl`:

    curl -XPOST http://localhost:8080/band/MegaBand -d '{
    name : MegaBand
    }'

    curl -XGET http://localhost:8080/band/MegaBand

## Run Tests

    ./run_tests.sh
