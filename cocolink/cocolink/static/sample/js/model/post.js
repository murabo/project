// 投稿情報を格納するモデル
var PostModel = Backbone.Model.extend({
    urlRoot : api_url+'post.json',
    defaults : function() {
        return {
                'message' : null
        };
    }
});