$(function() {

	var Post1 = function() {};
	Post1.prototype = $.extend({}, GetListUtil.prototype, {

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
				self.map.geocoder($(this));
			});

			$(document).on('click', '.js_star', function() {
				that._review($(this));
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
		},
		//評価の★を選択
		_review: function(that) {
			var n = that.attr('id').split("_");
			$(".star_review").find('.starlevel5').removeClass().addClass('starlevel5 star'+n[1]);
		}



	});

	var post1 = new Post1();
	post1.init();


});



