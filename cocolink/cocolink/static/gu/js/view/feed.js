// フィード一覧表示領域のビュー
var FeedView = Backbone.View.extend({
    el : $("body"),
    model : null,
    collection : null,     
    initialize : function(options) {
        
        this.model = options.model;
        _.bindAll(this, "render");
        
        this.collection = new Get({
                                //url: 'http://127.0.0.1:3000/',
                                url: 'http://157.7.129.122:3000/',
                                model:this.model
                            });
        this.render();

    },
    events: {
        'click　.js_btn_more' : 'render'
    },
    render : function() {

        this.collection.fetch({
            data : {
                offset : $("#list li:last").attr("data-post-id")
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
