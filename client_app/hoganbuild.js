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
  return (name.split('.').slice(-1)[0] === 'mustache');
}

function readCompileWrite(path, name) {
  var content = fs.readFileSync(path, 'utf8');
  var template = Hogan.compile(content, { asString: 1 });
    template = 
      'define(["lib/hogan"],function(Hogan){return ' +
      'new Hogan.Template(' + template + ')});';
  var jsName = name.replace('.mustache', '.js');
  console.log('Compiling ' + name + '...');
  fs.writeFileSync(B_PATH + jsName, template, 'utf8');
}

exports.run = function run() {
  var result = fs.readdirSync(T_PATH);
  var templates = result.filter(tFilter);
  for (var i = 0, l = templates.length; i < l; i++) {
    var path = T_PATH + templates[i];
    readCompileWrite(path, templates[i]);
  }
}

