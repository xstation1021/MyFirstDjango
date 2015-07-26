'use strict';

angular.module('chicoryApp')
    .config(function ($stateProvider) {
        $stateProvider
            .state('error', {
                url: '/error',
                views: {
                    'content@': {
                        templateUrl: 'sttic/scripts/app/error/error.html'
                    }
                },
            })
    });
