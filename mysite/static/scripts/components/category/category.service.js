'use strict';

angular.module('chicoryApp')
    .factory('Category', function ($resource) {
        return $resource('api/categories/:id', {}, {
                'query': {method: 'GET', isArray: true},
                'get': {
                    method: 'GET',
                    transformResponse: function (data) {
                        data = angular.fromJson(data);
                        return data;
                    }
                },
                'create': {method: 'POST', url:'api/categories/add'},
                'update': {method: 'PUT', url:'api/categories/update'},
            });
        });

