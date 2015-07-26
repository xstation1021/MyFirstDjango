'use strict';

angular.module('chicoryApp')
    .factory('Ingredient', function ($resource) {
        return $resource('api/ingredients/:id', {}, {
                'query': {method: 'GET', isArray: true},
                'get': {
                    method: 'GET',
                    transformResponse: function (data) {
                        data = angular.fromJson(data);
                        return data;
                    }
                },
                'create': {method: 'POST', url:'api/ingredients/add'},
                'update': {method: 'PUT', url:'api/ingredients/update'},
            });
        });

