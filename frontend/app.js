// sbcatalog frontend
var app = angular.module("sbApp", ["ngMaterial", "ngNewRouter"])
    .factory("setupService", function($http) {
        // default settings
        var settings = {
            "apiBaseUrl" : "http://localhost:5000",
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
        return {
            getSettings: function() {
                // return a promises that will
                // be used in the appController
                return $http.get('/settings.json')
                    .then(function(result) {
                        // replace default with custom settings
                        _.forEach(result.data, function(v,k) {
                            settings[k] = v;
                        });
                        // settings that will be passed to the callback
                        return settings;
                    }, function() {
                        // settings that will be passed to the callback
                        return settings;
                    });
            }
        };
    })
    .config(function($mdThemingProvider) {
        $mdThemingProvider.theme("light-green");
    })
    .controller("AppController", function($router, $rootScope, setupService) {

        setupService.getSettings().then(function(settings) {
            $rootScope.settings = settings;
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
