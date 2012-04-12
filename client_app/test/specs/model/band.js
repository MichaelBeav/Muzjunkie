define([
    'lib/backbone'
  , 'model/band'
  , 'datasource'
  ], function  (Backbone, Band, datasource) {
  describe('Band model', function  () {

    function createBand() {
      return new Band();
    }

    it('is a backbone model', function isAModel () {
      var band = createBand();
      expect(band).to.have.keys('cid', 'attributes', 'changed');
    });

    it('gets urlRoot from datasource file', function urlRootFrmDataSrc () {
      var band = createBand();
      expect(band.urlRoot).to.be(datasource.bandRoot);
    });

  });
});
