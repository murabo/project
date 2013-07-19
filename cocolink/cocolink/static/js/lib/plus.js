(function($){

////////////////////////////////////////////////////////////////////////////////
/// invite
////////////////////////////////////////////////////////////////////////////////
	$.fn.plus = function(options){

		if (undefined == $('body').data('Puls')) {
			var plus = new $.Puls($(this), options);
			$('body').data('Puls', plus);
		}

	};

	$.Puls = function(element, options) {

		var myself = this;
		myself.settings = {};

		var selectors = {
			btn_plus: '.js_btn_plus',
			btn_minus:'.js_btn_minus'
		};

		var icon = {
			icon_plus: '<button type="button" class="btn btn_plus js_btn_plus">plus</button>',
			icon_minus: '<button type="button" class="btn btn_plus js_btn_minus">minus</button>',
		};

		myself.init = function() {
			myself._initialize();
			myself._bind();
		};

		myself._initialize = function() {

			myself.settings = $.extend({}, selectors, icon, Super.prototype, AjaxUtil.prototype);
			myself.ajaxvo = new AjaxVo;
			//myself.ajaxvo.path = api_path['plus'];
		};

		myself._bind = function() {
			var obj = myself.settings;

			$('body').on('click', obj.btn_plus,function () {
				myself._plus($(this));
			});

			$(document).on('click', obj.btn_minus ,function () {
				myself._minus($(this));
			});
		};

		myself._plus = function(that) {
			that.after(myself.settings.icon_minus).remove();
		};

		myself._minus = function(that) {
			that.after(myself.settings.icon_plus).remove();
		};

		myself.init();

	 }


})(jQuery);


