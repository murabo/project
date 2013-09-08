// フィード情報を格納するモデル
var FeedModel = Backbone.Model.extend({
	//urlRoot : 'http://127.0.0.1:3000/',
    defaults : function() {
        return {

                'body_text' : null,
                'created_at' : null,
                'username' : null,
                'id' : null
            
        };
    }
});
