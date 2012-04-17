define([
    'lib/backbone'
  , 'template/index'
  ], function (Backbone, tmpl) {
 
    var Index = Backbone.View.extend({

      render: function renderIndex() {
        this.$el.html(tmpl.render());
      }

    });

    return Index;

});
