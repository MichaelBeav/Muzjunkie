define([
    'lib/backbone'
  ], function (Backbone) {
    
    var Router = Backbone.Router.extend({
      routes: {
        'bands': 'bandList',
        'bands/:id': 'band'
      },

      bandList: function bandListRoute() {
        console.log('Show me band list');
      },

      band: function bandRoute(id) {
        console.log('Show me the band #' + id);
      }
    });

    var router = new Router();
    Backbone.history.start();

    return router;

});
