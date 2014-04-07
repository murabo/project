define([
  "jquery",
  "underscore",
  "backbone"
], function($, _, Backbone) {

    var User = Backbone.Model.extend({

        defaults : function() {
            return {
                'data' : {
                    'user_id' : null,
                    'name' : null,
                    'postno' : null,
                    'address' : null
                }
            };
        }
    });

    return User;

});