var SHOW_PRICES = false;

var app = angular.module('app', ['ngMaterial']);

app.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('light-green');
});

// filter to format currency
app.filter("customCurrency", function() {
      return function(value, currencySymbol) {
          // format float value and add currency symbol
          return parseFloat(value.replace(',','.')).toFixed(2).toString() + " " + currencySymbol;
      };
});

app.controller('AppCtrl', function($scope, $mdDialog, $http, $rootScope){

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
  $scope.showBio = function($event, s) {
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
      clickOutsideToClose: true,
      templateUrl: "components/catalog/supplier.html",
      locals: {
        supplier: s
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

  // INITIALIZE ENV
  $scope.search = {};
  $scope.suppliers = [];

  //$http.get('http://sbcatalog.labs.befair.it/api/supplier/')
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
});
