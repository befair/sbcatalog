var app = angular.module("sbApp", ["ngMaterial", "ngNewRouter"])
.config(function($mdThemingProvider) {
  $mdThemingProvider.theme("light-green");
})
.filter("customCurrency", function() {
  return function(value, currencySymbol) {
    // format float value and add currency symbol
    return parseFloat(value.replace(",",".")).toFixed(2).toString() + " " + currencySymbol;
  };
})
.controller("AppController", function($router) {
  $router.config([
    { path: "/",        redirectTo: "/map" },
    { path: "/map", component: "map" },
    { path: "/catalog", component: "catalog" },
    { path: "/about",   component: "about" }
  ]);

  this.title = "Welcome to Social Business Catalog";
  this.subtitle = "This is the solidarity-based suppliers' repository. Enjoy!";
})
.controller("AboutController", function() {});
