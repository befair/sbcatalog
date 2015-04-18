/*
* Apllication Module
*
*/

var angularIO = angular.module('sbcatalogApp', ['ngMaterial'])
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


/*
* Apllication Controller
*
*/

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

  // FILTER BY CATEGORY CSS ATTR
  // THE JQUERY MODE
  $scope.filterByCategory = function(event) {
    if (category) {
        angular.element('.bio-card').css('display', 'none');
        var selector = '.bio-card[category=' + category + ']';
        angular.element(selector).css('display', 'block');
    }
  };

  // FILTER BY CATEGORY CSS ATTR
  // THE ANGULAR MODE
  $scope.filterByCategory = function(event) {
      if ($scope.category) {
          var sups_by_category = [];
          var sup;
          for ( sup in $scope.all_suppliers._items) {
              if (sup.name == $scope.category) {
                  sups_by_category.push(sup);
              }
          }
          $scope.suppliers._items = sups_by_category;
      }
  };
  // BIO MODAL
  $scope.showBio = function($event) {
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
      template:
        '<md-dialog class="modal" aria-label="List dialog">' +
        '  <md-content>' +
        '     <img class="left" src="' + pic + '" />' +
        '     <h3 class="text-headline">' + name + '</h3>' +
        '     <div class="modal-social">' + $twitter + $website + '</div>' +
        '     <p class="text-body">' + bio + '</p>' +
        '  </md-content>' +
        '  <div class="md-actions">' +
        '    <md-button ng-click="closeDialog()">' +
        '      Close Bio' +
        '    </md-button>' +
        '  </div>' +
        '</md-dialog>',
      locals: {
        items: $scope.items
      },
    controller: DialogController
    });

    function DialogController(scope, $mdDialog, items) {
      scope.items = items;
      scope.closeDialog = function() {
        $mdDialog.hide();
      };
    } };

  // INITIALIZE PRETTY PRINT
  prettyPrint();

  // INITIALIZE ENV
  $scope.category = null;
  $scope.search = {};
  $scope.suppliers = [];

  $http.get('http://localhost:5000/supplier/')
  .success(function(data) {
      $scope.all_suppliers = data;
      $scope.suppliers = data._items;
      //copy categories in a var to avoid two-way binding
      //for categories selection
      $scope.categories = [];
      var sup;
      for ( sup in $scope.all_suppliers._items) {
          $scope.categories.push(sup.name);
      }
  });
}]);
