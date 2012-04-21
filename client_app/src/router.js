define([
    'lib/backbone',
    'view/band'
  ], function (Backbone, BandView) {


  
  var Router = Backbone.Router.extend({
    routes: {
      'bands': 'bandList',
      'bands/:id': 'band'
    },

    bandList: function bandListRoute() {
      console.log('Show me band list');
    },

    band: function bandRoute(id) {
      new BandView({ el: $('div#content'), modelId: id });
    }
  });

  var router = new Router();

  return router;

});
