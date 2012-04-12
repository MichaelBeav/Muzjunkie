define([
    'lib/backbone'
  , 'model/band'
  ], function  (Backbone, Band) {
  describe('Band model', function  () {

    function createBand() {
      return new Band();
    }

    it('is a backbone model', function isAModel () {
      var band = createBand();
      expect(band).to.have.keys('cid', 'attributes', 'changed');
    });

  });
});
