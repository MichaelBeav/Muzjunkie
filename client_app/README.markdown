### Requirements

*   [node.js](http://nodejs.org/)
*   [npm](http://npmjs.org/)

And others, listed in `package.json`. In order to install them, run in `client_app` folder:

    npm install .

### Tests with buster.js (currently not supported)

For testing, use [buster.js](http://busterjs.org/) framework. It should be installed globally, in order to work properly.

    npm install -g buster   # use sudo, if needed

To run tests in console, first start *buster* server:
    
    buster server

Then open your browser (or even several ones) and point them to url `localhost:1111`. After browser has been captured by buster server, run:

    buster test

### Tests with mocha
Start server:

    ./server

You will need to create 2 directories for the first time:

    mkdir public/build public/build/template

Navigate to `localhost:8000/test`.

### Code standart
[http://nodeguide.com/style.html](nodejs code standart)

### Dev server
Dev server watches `src` dir and recompiles scripts on every change. It also serves all content from `public` dir on `localhost:8000`. To run it, do:

    ./server
