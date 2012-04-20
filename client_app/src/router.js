define([
    'lib/backbone'
  ], function (Backbone) {
    
    var Router = Backbone.Router.extend({
      routes: {
        'bands/:id': 'band'
      },

      band: function (id) {
        console.log('Show me the band #' + id);
      }
    });

    new Router();
    Backbone.history.start();

    return Router;

});
