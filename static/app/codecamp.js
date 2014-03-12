var codecampApp = angular.module('codecampApp', ['ngRoute']).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

codecampApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/presenters', {
        templateUrl: '/static/app/codecamp/speakers.html',
        controller: 'speakersCtrl'
      }).
      otherwise({
            templateUrl: '/static/app/codecamp/index.html'
        })
  }]);

var speakersCtrl = function($scope, $http) {

    if (!$scope.speakers){
        var request = $http.get('api/speaker/?format=json');
        request.success(function (data) {
            $scope.speakers = data.objects;
        });
    }
}

