define([
  "jquery",
  "underscore",
  "backbone",
  "userModels",
], function($, _, Backbone,User) {

    // ユーザー情報モデルを複数格納するためのコレクション
    var UserList = Backbone.Collection.extend({
        // リソースから取得した結果を格納するモデル
        model : User,
        // モデルの内容取得先リソース
        url : 'http://localhost:8000/app/backbone/list.json',
        // リソースから取得した結果をモデルに格納する前に参照できる。
        // returnされた値のみがモデルに格納される
        parse : function(resp) {
            if (resp.error) {
                // エラーがあればエラーメッセージ表示
                alert(resp.error.message);
            }
            // モデルに格納するデータ部分を返す
            return resp.data;
        }
    });

    return UserList;

});

