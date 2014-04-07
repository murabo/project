define([
  "jquery",
  "underscore",
  "backbone"
], function($, _, Backbone) {

    // ユーザー情報を格納するモデル
    var User = Backbone.Model.extend({
        // 属性指定が無いインスタンス生成の際のデフォルト属性（本サンプルでは無くてもいい）
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