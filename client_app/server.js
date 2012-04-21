var fs = require('fs');
var requirejs = require('requirejs');
var connect = require('connect');
var hoganBuild = require('./hoganbuild');
var watch = require('nodewatch');

var WATCHED_EXT = ['js', 'mustache'];

function rebuildProject() {
  // r.js build
  var config = JSON.parse(fs.readFileSync('build.js', 'utf8'));
  hoganBuild.run();
  requirejs.optimize(config, function buildResponse(buildResponse) {
    //buildResponse is just a text output of the modules
    //included. Load the built file for the contents.
    //Use config.out to get the optimized file contents.
    console.log(buildResponse);
  });

}

var timeout;
watch.add('./src', true).onChange(function watcher (fileName) {
  var ext = fileName.split('.').splice(-1)[0];
  if (WATCHED_EXT.indexOf(ext) === -1) {
    return;
  }
  clearTimeout(timeout);
  timeout = setTimeout(rebuildProject, 100);
});

// Rebuild project and start serving
rebuildProject();
var server = connect()
  .use(connect.static('public'))
  .use('/test', connect.static('test'))
  .use('/node_modules', 
        connect.static('node_modules')) // use them for tests only!
  .listen(8000);

console.log('Listening on 8000...');
