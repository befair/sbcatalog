// catalog controller for sbcatalog frontend
app.filter("categories", function() {
    return function(data, category) {
        if (category === "all")
            return data;

        else
            // return the category-filtered list
            return _.filter(data, function(x) {
                // short-circuitation is used to avoid accessing null attributes
                return x.products && _.find(x.products.product, function(y) {
                    // contains relation is used to manage category levels
                    return y && y.category && _.contains(y.category, category);
                });
            });
    };
})
    .filter("customCurrency", function() {
        return function(value, currencySymbol) {
            if (value)
                // format float value and add currency symbol
                return parseFloat(value.replace(",",".")).toFixed(2).toString()
                                  + " " + currencySymbol;
        };
    })
    .controller("CatalogController",
               function($mdDialog, $http, $filter, $rootScope) {

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
                controller: function($scope, $mdDialog, supplier) {
                    $scope.supplier = supplier;
                    $scope.showPrices = this.showPrices;

                    // close catalog
                    $scope.closeDialog = function() {
                        $mdDialog.hide();
                    };
                }
            });
        };

        // set pagination start from page number
        $rootScope.setPageNumber = function(page) {
            $rootScope.paginationStart = (page-1) * $rootScope.pagination;
        }

        // triggered when filter change
        $rootScope.onSelectChange = function() {
            // filter the list of suppliers
            $rootScope.totalSuppliers = $filter("categories")($rootScope.suppliers,
                                                              $rootScope.search.name).length;
            // get number of pages from supplier count
            $rootScope.pagesNumber = Math.ceil($rootScope.totalSuppliers / 
                                               $rootScope.pagination);

            // create a list of pages with number as label
            $rootScope.pages = [];
            for (var i=1; i <= $rootScope.pagesNumber; i++) 
                $rootScope.pages.push(i);

            // reset actual page
            $rootScope.setPageNumber(1);
        }

        $http.get($rootScope.settings.apiBaseUrl + "/supplier/").success(function(data) {
            // get data payload
            $rootScope.suppliers = data._items;

            $rootScope.suppliers.forEach(function(s) {
                  // generate a string from address object
                  s.addressString = (s.address.street? (s.address.street + " - ") : '') +
                                    (s.address.locality? s.address.locality: '');

                  //copy categories in a var to avoid two-way binding for categories selection
                  $rootScope.categories.push(s.name);
            });

            // init environment
            $rootScope.onSelectChange();
        });
    });
