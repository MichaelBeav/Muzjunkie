define([
    'lib/backbone'
  , 'model/band'
  , 'datasource'
  ], function  (Backbone, Band, datasource) {
  describe('Band model', function  () {
    
    var band;

    function createBand() {
      return new Band.Model();
    }

    beforeEach(function beforeTest() {
      band = createBand();
    });

    it('is a backbone model', function isAModel() {
      expect(band).to.have.keys('cid', 'attributes', 'changed');
    });

    it('gets urlRoot from datasource file', function urlRootFrmDataSrc() {
      expect(band.urlRoot).to.be(datasource.bandRoot);
    });

  });
});
