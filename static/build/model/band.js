define([
    'lib/backbone'
  , 'datasource'
  ], function  (Backbone, datasource) {

  var exports = {};

  exports.Model = Backbone.Model.extend({

    urlRoot: datasource.bandRoot

  });

  exports.Collection = Backbone.Collection.extend({

    url: datasource.bandList

  });

  return exports;
  
});
