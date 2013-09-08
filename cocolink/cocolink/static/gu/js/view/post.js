//投稿画面表示領域のビュー
var PostView = Backbone.View.extend({
    el : $("body"),
    model : null,
    collection : null,     
    initialize : function(options) {
        
        this.model = options.model;
    	_.bindAll(this, "open","close","save");

    },
    events: {
        'click　.js_open' : 'open',
        'click　.js_close' : 'close',
        'click　.js_submit' : 'save',
    },
    open : function() {

        $(".js-post_page").css('display','block');
		$(".js-main_page,.js-app_header,.js-tab").css('display','none');
		$(".js-wrapper").addClass('H100p');

    },
    close : function() {

        $(".js-post_page").css('display','none');
        $(".js-main_page,.js-app_header,.js-tab").css('display','block');

    },
    save : function(e) {

        var data = {};
        data.message = $(".js_post_textarea").val();
                    
        $.ajax({
            type: "POST",
            //url: "http://127.0.0.1:3000/",
            url: "http://157.7.129.122:3000/",     
            data: data,
            success: function(msg){
                alert( "Data Saved: " + msg );
            }
        });

        //this.close();
        window.location.reload();

        // this.model.set({'message': $(".js_post_textarea").val()});
        // this.model.save(null, {
        //     success : function(model, resp) {
        //        location.reload();
        //     },
        //     error : function(model, resp) {
        //         alert('エラー：送信に失敗しました。');
        //         return false;
        //     }
        // });
    }
    
});