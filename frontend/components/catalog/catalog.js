app.controller("CatalogController", function($mdDialog, $http, $filter, $rootScope) {

  this.showPrices = false;
  $rootScope.pagination = 24;
  $rootScope.search = {};
  $rootScope.suppliers = [];
  $rootScope.categories = [];

  // Catalog Modal
  $rootScope.showCatalog = function($event, supplier) {
    $mdDialog.show({
      parent: angular.element(document.body),
      targetEvent: $event,
      clickOutsideToClose: true,
      templateUrl: "components/catalog/supplier.html",
      locals: {
        supplier: supplier
      },
      // controller: function(scope, $mdDialog, supplier) {
      controller: function(scope, $mdDialog, supplier) {
        scope.supplier = supplier;
        scope.showPrices = this.showPrices;
        scope.closeDialog = function() {
          $mdDialog.hide();
        };
      }
    });
  };

  $rootScope.setPageNumber = function(page) {
    $rootScope.paginationStart = (page-1) * $rootScope.pagination;
  }

  $rootScope.onSelectChange = function() {
    $rootScope.totalSuppliers = $filter("filter")($rootScope.suppliers,
                                                  $rootScope.search.name).length;
    $rootScope.pagesNumber = Math.ceil($rootScope.totalSuppliers / $rootScope.pagination);
    $rootScope.pages = [];
    for (var i=1; i <= $rootScope.pagesNumber; i++) {
      $rootScope.pages.push(i);
    }
    $rootScope.setPageNumber(1);
  }

  //$http.get("http://sbcatalog.labs.befair.it/api/supplier/")
  $http.get("http://localhost:5000/supplier/")
    .success(function(data) {
      $rootScope.suppliers = data._items;
      //copy categories in a var to avoid two-way binding for categories selection
      for (var supplier in $rootScope.suppliers) {
          $rootScope.categories.push(supplier.name);
      }

      $rootScope.onSelectChange();
  });
});
