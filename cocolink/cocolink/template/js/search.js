$(function() {

	var Search = function() {};
	Search.prototype = $.extend({}, GetListUtil.prototype, {

		init: function() {

			this._bind();
		},

		_bind: function() {

			self.map = new Map();
			self.map.init();
			self.map.get_map();
			//self.map.get_present_location();
			//self.map.change_area();//まだ動いてません！

			 var showMap = function(position) {
				         var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
				         var options = {
				             zoom: 16,
				             center: latlng,
				             mapTypeId: google.maps.MapTypeId.ROADMAP
				         };

				         var map = new google.maps.Map($("#map_canvas").get(0), options);
				         var marker = new google.maps.Marker({
				                         map: map,
				                         position: latlng
				                     });
				}

			 	//現在地に戻るボタン
				$("#abtn").click(function() {
					navigator.geolocation.getCurrentPosition(showMap);
					return false;
				 });

			 	//検索ボタン
				$(".js-submit").click(function() {

					//alert($('body').data('swLatlng'));
					//alert($('body').data('neLatlng'));
					var bounds = $('body').data('defaultBounds');
					alert(bounds);
					self.map.get_place_list(bounds);

				});
		}

	});

	var search = new Search();
	search.init();


});



