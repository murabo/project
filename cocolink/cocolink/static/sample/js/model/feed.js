 // フィード情報を格納するモデル
var FeedModel = Backbone.Model.extend({
    defaults : function() {
        return {
            'data' : {
                'create_datetime' : null,
                'name' : null,
                'message' : null
            }
        };
    }
});
