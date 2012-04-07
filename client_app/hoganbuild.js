var fs = require('fs');
var Hogan = require('hogan.js');

var T_PATH = 'src/template/'; // path to templates
var B_PATH = 'public/build/template/'; // path to result

function failFast(err) {
  if (err) {
    throw err;
  }
}

function tFilter(name) {
  return (name.slice(-9) === '.mustache');
}

function readCompileWrite(path, name) {
  fs.readFile(path, 'utf8', function onRead(err, content) {
    var template = Hogan.compile(content, { asString: 1 });
    template = 
      'define([],function(){return ' +
      template + '}';
    var jsName = name.replace('.mustache', '.js');
    console.log('Compiling ' + name + '...');
    fs.writeFile(B_PATH + jsName, template, 'utf8', failFast);
  });
}

exports.run = function run() {
    fs.readdir(T_PATH, function readCallback(err, result) {
    failFast(err);
    var templates = result.filter(tFilter);
    for (var i = 0, l = templates.length; i < l; i++) {
      var path = T_PATH + templates[i];
      readCompileWrite(path, templates[i]);
    }
  });
}

