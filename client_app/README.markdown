### Requirements

*   [node.js](http://nodejs.org/)
*   [npm](http://npmjs.org/)

And others, listed in `package.json`. In order to install them, run in `client_app` folder:

    npm install .

### Tests

For testing, use [buster.js](http://busterjs.org/) framework. It should be installed globally, in order to work properly.

    npm install -g buster   # use sudo, if needed

To run tests in console, first start *buster* server:
    
    buster server

Then open your browser (or even several ones) and point them to url `localhost:1111`. After browser has been captured by buster server, run:

    buster test

### Code standart
[http://nodeguide.com/style.html](nodejs code standart)
