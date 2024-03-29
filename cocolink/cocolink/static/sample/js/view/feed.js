// フィード一覧表示領域のビュー
var FeedView = Backbone.View.extend({
    el : $("body"),
    model : null,
    collection : null,     
    initialize : function(options) {
        
        this.model = options.model;
        _.bindAll(this, "render");
        
        this.collection = new Get({
                                url: api_url+'timeline.json',
                                model:this.model
                            });

    },
    events: {
        'click　.js_btn_more' : 'render'
    },
    render : function() {

        this.collection.fetch({
            data : {
                user_id : "123"
            },
            dataType : 'json',
            success : $.proxy(this.add, this)
        });

    },
    add : function(collection, resp) {

        var that = this;
        if (collection.length == 0) {
            alert("0件");
            return;
        }
        collection.each(function(model) {
            $("#list").append(_.template($('#user_row_template').html(), model.attributes));
        });
    }
});
