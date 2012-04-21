define([
  'view/band',
  'template/band',
  'model/band'
  ], function (BandView, bandTmpl, Band) {

  describe('band view', function () {
    function getSomeModel() {
      return new Band.Model({ name: 'MegaBand', primary_genre: 'Hardcore' });
    };

    function getModelWithId(id) {
      return new Band.Model({ id: id, name: 'Band#' + id });
    };

    var requests = [];
    var xhr = null;

    beforeEach(function () {
      xhr = sinon.useFakeXMLHttpRequest();
      xhr.onCreate = function (req) {
        requests.push(req);
      };
    });

    afterEach(function () {
      requests = [];
      xhr.restore();
    });

    it('renders a template', function () {
      var model = getSomeModel();
      var view = new BandView({ model: model });
      expect(view.$el.html()).to.be(bandTmpl.render(model.toJSON()));
    });

    it('retrieves model by id, if model is not passed', function (done) {
      var view = new BandView({ modelId: 1 });

      expect(requests).to.have.length(1);

      view.on('ready', function onViewReady() {
        expect(view.model.toJSON()).to.eql(model.toJSON());
        done();
      });

      var req = requests[0];
      var model = getModelWithId(1);
      // response to XHR-requested model
      req.respond(200, {}, JSON.stringify(model.toJSON()));
    });

    it('throws an error if neither model nor modelId passed',
        function () {

      function createViewWithoutModel() {
        var view = new BandView({});
      }
      expect(createViewWithoutModel).to.throwError();
    });

  });

});
