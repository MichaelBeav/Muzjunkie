var fs = require('fs');
var requirejs = require('requirejs');
var connect = require('connect');
var hoganBuild = require('./hoganbuild');

function rebuildProject() {
  // r.js build
  var config = JSON.parse(fs.readFileSync('build.js', 'utf8'));
  requirejs.optimize(config, function buildResponse(buildResponse) {
    //buildResponse is just a text output of the modules
    //included. Load the built file for the contents.
    //Use config.out to get the optimized file contents.
    console.log(buildResponse);
  });

  hoganBuild.run();
}

var timeout;
var watcher = fs.watch('src', function watchDir(action, fileName) {
  if (fileName.slice(-3) !== '.js') {
    return;
  }
  clearTimeout(timeout);
  timeout = setTimeout(rebuildProject, 100);
});

// Rebuild project and start serving
rebuildProject();
connect()
    .use(connect.static('test'))
    .use(connect.static('public/build'))
    .listen(8001);

console.log('Tests listening on 8001');
