// 投稿情報を格納するモデル
var PostModel = Backbone.Model.extend({
    //urlRoot : 'http://127.0.0.1:3000/',
    urlRoot: 'http://157.7.129.122:3000/',
    defaults : function() {
        return {
                'message' : null
        };
    }
});