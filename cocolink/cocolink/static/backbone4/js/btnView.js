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
            // clickイベントの登録
            'click' : 'click'
        },
        click : function(e) {
            // ユーザー一覧を描画する
            this.userView.render();
        }
    });



    return BtnShowView;

});