define([
    'lib/backbone'
  , 'template/index'
  , 'view/navbar'
  ], function (Backbone, tmpl, Navbar) {
 
    var Index = Backbone.View.extend({

      initialize: function initIndex() {
        this.render();
      },

      render: function renderIndex() {
        this.$el.html(tmpl.render());
        var navbar = new Navbar({ el: this.$('header') });
      }

    });

    return Index;

});
