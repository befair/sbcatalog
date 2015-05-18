// sbcatalog frontend 
var app = angular.module("sbApp", ["ngMaterial", "ngNewRouter"])
    .config(function($mdThemingProvider) {
        $mdThemingProvider.theme("light-green");
    })
    .filter("customCurrency", function() {
        return function(value, currencySymbol) {
            // format float value and add currency symbol
            return parseFloat(value.replace(",",".")).toFixed(2).toString() 
                              + " " + currencySymbol;
        };
    })
    .controller("AppController", function($http, $router, $rootScope) {

        var defaultSettings = {
            "apiBaseUrl" : "http://localhost:5000"
        };

        var checkDefaultSettings = function() {
            for (var x in defaultSettings)
                if (!$rootScope.settings.hasOwnProperty(x))
                    $rootScope.settings[x] = defaultSettings[x];
        };

        $http.get("/settings.json")
            .success(function(data) {
                $rootScope.settings = data;
                checkDefaultSettings();
            })
            .error(function() {
                $rootScope.settings = {} ;
                checkDefaultSettings();
            });


        $router.config([
            { path: "/",        redirectTo: "/map" },
            { path: "/map",     component: "map",     as: "map" },
            { path: "/catalog", component: "catalog", as: "catalog" },
            { path: "/about",   component: "about",   as: "about" }
        ]);

        this.title = "Welcome to Social Business Catalog";
        this.subtitle = "This is the solidarity-based suppliers' repository. Enjoy!";
    });
