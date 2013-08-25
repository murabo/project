var MyApp = {
    Models: {},
    Collections: {},
    Views: {},
    App: {},
    Templates: {}
};

MyApp.App = Backbone.View.extend({

	initialize: function(data) { 	
	
	},
});

new MyApp.App();

api_url = 'http://127.0.0.1:8080/static/sample/json/';


var s = io.connect('http://localhost:3000'); //ローカル

//サーバから受け取るイベント
s.on("connect", function () {});  // 接続時
s.on("disconnect", function (client) {});  // 切断時
s.on("S_to_C_message", function (data) {
addMessage(data.value);
});

//jqueryでメッセージを追加
function addMessage (value,color,size) {
var msg = value.replace( /[!@$%<>'"&|]/g, '' ); //タグ記号とかいくつか削除
 $("#list").prepend("<div class='msg'>" + msg + "</div>");
}    


