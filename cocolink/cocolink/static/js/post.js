$(function() {

	var Post = function() {};
	Post.prototype = $.extend({}, GetListUtil.prototype, {

		self: function() { },
		init: function() {
			this._bind();
			this._initialize();
		},
		_initialize :function() {
			self.ajax = $.extend({}, Super.prototype, AjaxUtil.prototype);
			self.ajaxvo = new AjaxVo;

			self.map = new Map();
			self.map.init();
			self.map.get_map();
			self.map.get_present_location();
			self.map.check_browser();

		},
		_bind: function() {

			var that= this;
			$(".dsp_map_page").click(function() {
				that._toggle_txt_page();
			});
			$(document).on('click', '#js-result-list li', function() {
				that._dsp_place_info($(this));
				that._toggle_txt_page();
				//self.map.geocoder($(this));//詳細住所はとりあえず取得なし！
			});

			$(document).on('click', '.js_star', function() {
				that._review($(this));
			});

			//送信
			$(document).on('click', '.js-submit', function() {
				that.submit();
			});
			//this._get_list();
		},
		//地図画面と投稿画面の表示切り替え
		_toggle_txt_page: function() {
			$('.txt_page,.map_page').toggleClass('disp_none disp_block');
		},
		//選択したリストを投稿画面に表示
		_dsp_place_info: function(that) {
			$('.txt_page').find('.place').html(that);

			//送信用変数にセット
			$(".js-subumit-lng").val(that.find('.js-lng').val());
			$(".js-subumit-reference").val(that.find('.js-reference').val());
			$(".js-subumit-lat").val(that.find('.js-lat').val());


		},
		//評価の★を選択
		_review: function(that) {
			var n = that.attr('id').split("_");
			$(".star_review").find('.starlevel5').removeClass().addClass('starlevel5 star'+n[1]);
		},
		submit: function(that) {


        var data = {};

        data.csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();
        data.message = $(".js_post_textarea").val();
		data.lat_x = $(".js-subumit-lat").val();
		data.lng_y = $(".js-subumit-lng").val();
		data.reference = $(".js-subumit-reference").val();
		data.message = $('#js-message').val();
		data.category = $('#category option:selected').val();
		data.public_flg = ($(".js-public-flg:checked").val())? '1': '0';
		data.review = ($(".js-review-flg:checked").val())? '1': '0';//0〜5
			  		

			$.ajax({
			  type: "POST",
			  url: "http://127.0.0.1:8080/ajax_post/",
			  dataType: "json",
			  data:data
			});

		}






	});

	var post = new Post();
	post.init();


});



