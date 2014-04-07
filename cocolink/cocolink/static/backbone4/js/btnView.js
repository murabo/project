define([
  "jquery",
  "underscore",
  "backbone",
  "userModels",
], function($, _, Backbone,userView) {

    var BtnShowView = Backbone.View.extend({
        el : $('#btn_show'),
        userView : null,
        initialize : function(data) {
            this.userView = data.userView;
        },
        events: {
            'click' : 'click'
        },
        click : function(e) {
            this.userView.render();
        }
    });

    return BtnShowView;

});