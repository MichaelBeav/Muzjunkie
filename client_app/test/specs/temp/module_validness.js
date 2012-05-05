define([  'require'
        , 'lib/underscore'
        , 'lib/backbone'], function (require) {
  describe('underscore', function underscoreTests () {

    it('is a require module', function () {
      var _ = require('lib/underscore');
      expect(_).to.be.a('function');
    });

  });

  describe('backbone', function backboneTest () {
    
    it('is a require module too', function () {
      var Backbone = require('lib/backbone');
      expect(Backbone).to.be.an('object');
    });

  });
  
});
