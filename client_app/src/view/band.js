define([
  'lib/backbone',
  'template/band',
  'model/band'
  ], function (Backbone, tmpl, Band) {
    
    return Backbone.View.extend({

      initialize: function initBandView(options) {
        var _thisView = this;

        if (!options || (!options.model && !options.modelId)) {
          throw Error('Init options not supplied for BandView.\n' +
            '"model" or "modelId" are expected in options hash.');
        }

        // fetch model, if it is not passed in options
        if (!options.model) {
          var model = new Band.Model({ id: options.modelId });
          model.fetch({
            success: function modelFetched(m, resp) {
              _thisView.model = m;
              _thisView.render();
            }
          });
          return this;
        }
        this.render();
        return this;
      },

      render: function renderBandView() {
        console.log(this.$el);
        this.$el.html(tmpl.render(this.model.toJSON()));
        console.log('rendered');
        this.trigger('ready');
        return this;
      }

    });
});
