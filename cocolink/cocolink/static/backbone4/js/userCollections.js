define([
  "jquery",
  "underscore",
  "backbone",
  "userModels",
], function($, _, Backbone,User) {

    var UserList = Backbone.Collection.extend({

        model : User,
        url : 'http://157.7.129.122/static/backbone4/json/list.json',

        parse : function(resp) {
            if (resp.error) {
                alert(resp.error.message);
            }
            return resp.data;
        }
    });

    return UserList;

});

