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


			//mapをクリックして住所を取得、その住所で投稿
			$(document).on('click', '.js_star', function() {
				that._review($(this));
			});

			//送信
			$(document).on('click', '.js-submit', function() {
				that.submit();
			});
			//this._get_list();
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



