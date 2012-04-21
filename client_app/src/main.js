require([
    'order!lib/jquery'
  , 'order!lib/bootstrap.min.js'
  , 'view/index'
  , 'lib/backbone'
  , 'router'
  ], function (_, _, Index, Backbone) {

  var index = new Index({ el : 'body.app' });
  Backbone.history.start();
});
