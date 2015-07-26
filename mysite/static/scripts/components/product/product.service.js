'use strict';

angular.module('chicoryApp')
    .factory('Product', function ($resource) {
        return $resource('api/products/:id', {}, {
                'query': {method: 'GET', isArray: true},
                'get': {
                    method: 'GET',
                    transformResponse: function (data) {
                        data = angular.fromJson(data);
                        return data;
                    }
                },
                'create': {method: 'POST', url:'api/products/add'},
                'update': {method: 'PUT', url:'api/products/update'},
            });
        });

