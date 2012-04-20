require([
    "order!lib/jquery"
  , "order!lib/bootstrap.min.js"
  , "view/index"
  , "router"
  ], function (_, _, Index) {

  var index = new Index({ el : 'body' });
});
