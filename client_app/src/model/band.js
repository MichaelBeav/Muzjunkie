define([
    'lib/backbone'
  , 'datasource'
  ], function  (Backbone, datasource) {

  return Backbone.Model.extend({

    urlRoot: datasource.bandRoot

  });
  
});
