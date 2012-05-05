
define([
    'lib/backbone'
  , 'template/navbar'
  ], function (Backbone, tmpl) {
    
    return Backbone.View.extend({

      initialize: function initNavBar() {
        this.render();
      },

      render: function renderNavBar() {
        this.$el.html(tmpl.render());
      }
    
    });

});
