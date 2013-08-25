//投稿画面表示領域のビュー
var PostView = Backbone.View.extend({
    el : $("body"),
    model : null,
    collection : null,     
    initialize : function(options) {
        
        this.model = options.model;
    	_.bindAll(this, "open","save");

    },
    events: {
        'click　.js_open' : 'open',
        'click　.js_submit' : 'save'
    },
    open : function() {

        $(".js-post_page").css('display','block');
		$(".js-main_page,.js-app_header,.js-tab").css('display','none');
		$(".js-wrapper").addClass('H100p');

    },
    save : function(e) {

        this.model.set({'message': $(".js_post_textarea").val()});
        this.model.save(null, {
            success : function(model, resp) {
               location.reload();
            },
            error : function(model, resp) {
                alert('エラー：送信に失敗しました。');
                return false;
            }
        });
    }
    
});