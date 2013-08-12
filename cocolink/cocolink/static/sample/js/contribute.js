(function($){

	

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


	$.fn.post = function(topic_id,url) {
		if (undefined == $('body').data('Post')) {
			var post = new $.Post(this, topic_id,url);
			$('body').data('Post', post);
		}
	}

	$.Post = function(element,topic_id,url) {

		var myself = this;
		myself.settings = {};

		var selectors = {
			submit: '.js-submit',
			textarea: '#js-post_textarea',
			platform: '.js-icon_platform',
			hidden_img: '#js-hidden_post_img',
			close: '.js-close',
			post_btn: '.js-post_to_topic',
			select: '#js-contribute_select',
			theme_btn: '.js-theme_btn',
			theme_txt: '.js-theme_txt',
			theme_id: '#js-theme_id',
			target_time: '#js-target_time',
			this_theme_btn: '.js-this_theme_btn',
			disp_target_time: '.js-disp_target_time',
			user_theme: '.js_user_theme',
			$user_theme: $('.js_user_theme'),
			$user_theme_input_bx: $('.js_user_theme_input_bx'),
			user_theme_btn:'.js_user_theme_btn',
			$hidden_user_theme: $('#js_hidden_user_theme'),
		};

		myself.init = function() {
			myself._initialize();
			myself._bind();
		};

		myself._initialize = function(options) {

			myself.settings = $.extend({}, Super.prototype, selectors,AjaxUtil.prototype);
			myself._topic_id = topic_id;;//ワタシツイート トピックID
			myself._theme_id = '';//ネタID
			myself.ajaxvo = new AjaxVo;
			myself.ajaxvo.path = api_path['topic_contribute_comment_delete'];

			myself.validate = new Validate();
			myself.validate.counter($("#js-post_textarea"),$("#js-post_counter"),1000);
		};

		myself._bind = function() {
			var obj = myself.settings;
			var $body = $('body');

			//投稿ボタン
			$(document).on('click', obj.post_btn, function(event) {
				myself._open();
			});
			//送信

			$(document).on('click', '.js-submit', function(event) {
				myself._post($(this),topic_id);
			});
	
			//ポップアップ閉じる
			$(document).on('click', obj.close, function(event) {
				myself._close();
			});


		};


		myself._post = function(self,topic_id) {

			var obj = myself.settings;
			if((myself.validate.isset($(obj.textarea), ''))){
				return;
			}else{

				var ajaxvo = new AjaxVo;
				ajaxvo.path = api_path['topic_contribute_post'];

				var str_sns = '';//api送信用
				//onにしたsns取得
				$('.js-platform').find('li').each(function(i){
					var myid = myself.settings._getid($(this));
					if($(this).children().hasClass('bg_on')){
						if (str_sns != '') str_sns +=',';
						str_sns += myid[1];
					}
				});

				myself._theme_id = $(obj.theme_id).val();
				var user_theme = obj.$hidden_user_theme.val();

				ajaxvo.data = { 'topic_id': myself._topic_id ,
								'body': $(obj.textarea).val(),
								'image': $(obj.hidden_img).val(),
								'share_sns': str_sns,
								'theme_id':myself._theme_id ,
								'target_time': $(obj.target_time).val(),
								'user_theme': (user_theme) ? escape_q(user_theme) : ''
								};
			 	
			    var msg = $(obj.textarea).val();
			    s.emit("C_to_S_message", {value:msg}); //!!!!!!!!!!!!!!サーバへ送信
			    myself._close();

			}
		};


		myself._open = function(){

			setTimeout(function(){
				window.scrollTo(0,1);
			}, 1);

			$(".js-post_page").displayBlock();
			$(".js-main_page,.js-app_header,.js-tab,.js-footer,#deca_header,#deca_footer,#amb_header,.ad_frame").displayNone();
			$(".js-wrapper").addClass('H100p');
			//focusElement(obj.textarea);
			//Android 2.3 以下は、エリアの上に余白追加。
		};

		myself._close = function(self){
		
			var obj = myself.settings;
			$('.js-modal').displayNone();
			$(".js-main_page,.js-app_header,.js-tab,.js-footer,#deca_header,#deca_footer,#amb_header,.ad_frame").displayBlock();
			$(".js-wrapper").removeClass('H100p');
			//初期化
			$(obj.textarea).val('');

		};



		myself.init();

	};


})(jQuery);




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


	var User2 = Backbone.Model.extend({
        urlRoot : './backbone_save_test.php',
        defaults : function() {
            return {
                'topic_id' : null,
                'body' : null
            };
        }
    });

    var BtnSend = Backbone.View.extend({
        //el : $('.js-submit'),
        model : User2,
        initialize : function(options) {
            this.model = options.model;
        },
        events: {
            'click .js-submit' : 'click',
			'click  .post_to_topic' : 'opnen',
        },
        click : function(e) {
            var reqData = {
                'topic_id' : '2',
                'body' : $('#js-post_textarea').val()
            };
            // 送信するデータをModelにセット
            this.model.set(reqData);
            // save()を呼び出すと、model.urlRootにPOSTリクエストが送信される
            this.model.save(null, {
                success : function(model, resp) {
                    // レスポンスを受け取ってalert表示する
                    alert('名前：'+resp.user_name+' 住所：'+resp.address+' を受け付けました。');
                    // レスポンスを受け取ってテンプレートに表示する
                    $('#post_data_area').html(_.template($('#post_data_template').html(), resp));
                },
                error : function(model, resp) {

 			    var msg = $("#js-post_textarea").val();
			    s.emit("C_to_S_message", {value:msg}); //!!!!!!!!!!!!!!サーバへ送信


                    alert('エラー：送信に失敗しました。');
                    return false;
                }
            });
        },
        open : function(e) {
           alert();
        }
    });





    var user = new User2();
    var btnSend = new BtnSend({model: user});




