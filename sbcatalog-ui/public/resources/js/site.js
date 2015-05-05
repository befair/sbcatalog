/*
* Application Module
*
*/

// settings
// show prices
var SHOW_PRICES = false;

var angularIO = angular.module('sbcatalogApp', ['ngMaterial'])
// filter to format currency
.filter("customCurrency", function() {
      return function(value, currencySymbol) {
          // format float value and add currency symbol
          return parseFloat(value.replace(',','.')).toFixed(2).toString() + " " + currencySymbol;
      };
})
.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('green-light');
    /*.primaryPalette('blue', {
      'default': '700', // by default use shade 400 from the pink palette for primary intentions
      'hue-1': '100', // use shade 100 for the <code>md-hue-1</code> class
      'hue-2': '600', // use shade 600 for the <code>md-hue-2</code> class
      'hue-3': 'A100' // use shade A100 for the <code>md-hue-3</code> class
    })
    // If you specify less than all of the keys, it will inherit from the
    // default shades
    .accentPalette('purple', {
      'default': '200' // use shade 200 for default, and keep all other shades the same
    });*/


});


angularIO.controller('AppCtrl', ['$scope', '$mdDialog', '$http', '$rootScope', function($scope, $mdDialog, $http, $rootScope){

  // TOGGLE MAIN NAV (TOP) ON MOBILE
  $scope.toggleDocsMenu = function(event) {
    $scope.showDocsNav = !$scope.showDocsNav;
  };

  // TOGGLE DOCS NAV
  $scope.toggleMainMenu = function(event) {
    $scope.showMainNav = !$scope.showMainNav;
  };

  // TOGGLE DOCS VERSION & LANGUAGE
  $scope.toggleVersionMenu = function(event) {
    $scope.showMenu = !$scope.showMenu;
  };

  // BIO MODAL
  $scope.showBio = function($event, $index) {
    var index = $index;
    var parentEl = angular.element(document.body);
    var person = angular.element($event.currentTarget);
    var name = person.attr('data-name');
    var bio = person.attr('data-bio');
    var pic = person.attr('data-pic');
    var twitter = person.attr('data-twitter');
    var website =  person.attr('data-website');
    var $twitter = twitter !== 'undefined' ? '<a class="button button-subtle button-small" href="https://twitter.com/' +  person.attr('data-twitter') + '" md-button>Twitter</a>' : '';
    var $website = website !== 'undefined' ? '<a class="button button-subtle button-small" href="' + person.attr('data-website') + '" md-button>Website</a>' : '';

    $mdDialog.show({
      parent: parentEl,
      targetEvent: $event,
      templateUrl: "resources/supplier.html",
      locals: {
        supplier: $scope.suppliers[$index]
      },
      controller: DialogController
    });

    function DialogController(scope, $mdDialog, supplier) {
      scope.s = supplier;
      scope.showPrices = SHOW_PRICES;
      scope.closeDialog = function() {
        $mdDialog.hide();
      };
    }
  };

  // INITIALIZE PRETTY PRINT
  prettyPrint();

  // INITIALIZE ENV
  $scope.search = {};
  $scope.suppliers = [];

  //$http.get('http://api.sbcatalog.labs.befair.it/supplier/')
  $http.get('http://localhost:5000/supplier/')
  .success(function(data) {
      $scope.suppliers = data._items;
      //copy categories in a var to avoid two-way binding
      //for categories selection
      $scope.categories = [];
      var sup;
      for ( sup in $scope.suppliers) {
          $scope.categories.push(sup.name);
      }
      $scope.pagination = 30;
      $scope.total_suppliers = $scope.suppliers.length;
      $scope.pages_number = Math.ceil($scope.total_suppliers / $scope.pagination);
      $scope.pages = [];
      for (var i=1; i <= $scope.pages_number; i++) {
          $scope.pages.push(i);
      }

      $scope.setPageNumber = function(page) {
        $scope.actual_page = page;
        $scope.suppliers_filtered = $scope.suppliers.slice((page-1)*$scope.pagination, page*$scope.pagination);
      }

      $scope.setPageNumber(1);
  });
}]);
