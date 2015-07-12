// sbcatalog frontend
var app = angular.module("sbApp", ["ngMaterial", "ngNewRouter"])
    .config(function($mdThemingProvider) {
        $mdThemingProvider.theme("light-green");
    })
    .filter("customCurrency", function() {
        return function(value, currencySymbol) {
            if (value)
                // format float value and add currency symbol
                return parseFloat(value.replace(",",".")).toFixed(2).toString()
                                  + " " + currencySymbol;
        };
    })
    .filter("categories", function() {
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
    .controller("AppController", function($http, $router, $rootScope) {

        $rootScope.settings = {
            "apiBaseUrl" : "/api/v1",
            "productCategories": [
                "Abbigliamento",
                "Abbigliamento::Calzature",
                "Abbigliamento::Calzature::Calzature accessori",
                "Abbigliamento::Calzature::Calzature bambino",
                "Abbigliamento::Calzature::Calzature donna",
                "Abbigliamento::Calzature::Calzature uomo",
                "Abbigliamento::Vestiario",
                "Abbigliamento::Vestiario::Vestiario bambino",
                "Abbigliamento::Vestiario::Vestiario donna",
                "Abbigliamento::Vestiario::Vestiario uomo",
                "Alimenti",
                "Alimenti::Bevande",
                "Alimenti::Bevande::Analcoliche",
                "Alimenti::Bevande::Birra",
                "Alimenti::Bevande::Caffè",
                "Alimenti::Bevande::Liquori",
                "Alimenti::Bevande::Tisane e Infusi",
                "Alimenti::Bevande::Tè",
                "Alimenti::Bevande::Tè::Tè nero",
                "Alimenti::Bevande::Tè::Tè verde",
                "Alimenti::Bevande::Vino Bianco",
                "Alimenti::Bevande::Vino Rosso",
                "Alimenti::Carne::Bianca",
                "Alimenti::Carne::Bianca::Coniglio",
                "Alimenti::Carne::Bianca::Pollame",
                "Alimenti::Carne::Rossa",
                "Alimenti::Carne::Rossa::Maiale",
                "Alimenti::Carne::Rossa::Pecora",
                "Alimenti::Carne::Rossa::Vitello",
                "Alimenti::Cereali",
                "Alimenti::Conserve",
                "Alimenti::Conserve::Marmellate",
                "Alimenti::Conserve::Sughi pronti",
                "Alimenti::Dolci",
                "Alimenti::Dolci::Zucchero",
                "Alimenti::Farine",
                "Alimenti::Formaggi e latticini",
                "Alimenti::Formaggi e latticini::Capra",
                "Alimenti::Formaggi e latticini::Formaggi freschi",
                "Alimenti::Formaggi e latticini::Formaggi stagionati",
                "Alimenti::Formaggi e latticini::Mucca",
                "Alimenti::Formaggi e latticini::Pecora",
                "Alimenti::Frutta",
                "Alimenti::Frutta::Agrumi",
                "Alimenti::Frutta::Frutta fresca",
                "Alimenti::Frutta::Frutta secca",
                "Alimenti::Gelato",
                "Alimenti::Latte",
                "Alimenti::Legumi secchi",
                "Alimenti::Miele",
                "Alimenti::Olio",
                "Alimenti::Olio::Olio d’oliva",
                "Alimenti::Olio::Olio di semi",
                "Alimenti::Pasta",
                "Alimenti::Pasta::Pasta di semola di grano duro",
                "Alimenti::Pasta::Pasta integrale di grano duro",
                "Alimenti::Pasta::Pasta semi-integrale",
                "Alimenti::Pesce",
                "Alimenti::Pesce::Fiume",
                "Alimenti::Pesce::Mare",
                "Alimenti::Prodotti da forno",
                "Alimenti::Prodotti da forno::Biscotti",
                "Alimenti::Prodotti da forno::Dolci",
                "Alimenti::Prodotti da forno::Pane",
                "Alimenti::Riso",
                "Alimenti::Salumi",
                "Alimenti::Spezie",
                "Alimenti::Uova",
                "Alimenti::Verdura",
                "Cosmesi",
                "Cosmesi::Barba",
                "Cosmesi::Olii, crème e uguenti",
                "Cosmesi::Saponi e Detergenti intimi",
                "Cosmesi::Shampoo e Dentifricio",
                "Detergenti",
                "Edilizia",
                "Igiene casa",
                "Industria::Carta",
                "Piante",
                "Piante::Piante aromatiche"
            ]
        };

        $http.get("/ui/settings.json")
            .success(function(data) {
                for (k in data)
                    $rootScope.settings[k] = data[k];
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
