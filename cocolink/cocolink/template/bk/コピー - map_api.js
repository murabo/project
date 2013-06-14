$(function() {

	var MapApi = function() {};
	MapApi.prototype = $.extend({}, GetListUtil.prototype, {

		init: function() {
			this._bind();
		},

		_bind: function() {
			this._get_map();


		},

		//現在地取得
		_get_map: function(event){


			if(navigator.geolocation){

				// 位置情報取得に成功したとき
			  var position = function (position) {
					lat= position.coords.latitude;
					lng= position.coords.longitude;
					var latlng = new google.maps.LatLng(lat, lng);
					var myOptions = {
							zoom: 19,
							center: latlng,
							mapTypeId: google.maps.MapTypeId.ROADMAP
					};
					var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
					var marker = new google.maps.Marker({
							position: latlng,
							map: map,
					});
			  }

			  // 位置情報取得に失敗したとき
			  var error = function (error) {
			    alert(error.message);
			  }
			  // 位置情報取得時に設定するオプション
			  var option = {
			    enableHighAccuracy: true,
			    maximumAge: 60*2000,
			    timeout : 1000,
			  };
			  navigator.geolocation.watchPosition(position,error,option);


				//現在地表示
				$("#abtn").click(function() {
					navigator.geolocation.getCurrentPosition(position);
					return false;
				 });


			}else{
				alert("ほんとごめんなさい。無理です。");
			}

		},


		_getAddress: function(event){
			var geocoder = new google.maps.Geocoder();
			geocoder.geocode({
				latLng: latlng
			}, function(results, status) {
				if (status == google.maps.GeocoderStatus.OK) {
					if (results[0].geometry) {
						var address = results[0].formatted_address.replace(/^日本, /, '');
						new google.maps.InfoWindow({
							content: address + "<br>(Lat, Lng) = " + latlng
						}).open(map, new google.maps.Marker({
							position: latlng,
							map: map
						}));
					}
				} else if (status == google.maps.GeocoderStatus.ERROR) {
					alert("サーバとの通信時に何らかのエラーが発生！");
				} else if (status == google.maps.GeocoderStatus.INVALID_REQUEST) {
					alert("リクエストに問題アリ！geocode()に渡すGeocoderRequestを確認せよ！！");
				} else if (status == google.maps.GeocoderStatus.OVER_QUERY_LIMIT) {
					alert("短時間にクエリを送りすぎ！落ち着いて！！");
				} else if (status == google.maps.GeocoderStatus.REQUEST_DENIED) {
					alert("このページではジオコーダの利用が許可されていない！・・・なぜ！？");
				} else if (status == google.maps.GeocoderStatus.UNKNOWN_ERROR) {
					alert("サーバ側でなんらかのトラブルが発生した模様。再挑戦されたし。");
				} else if (status == google.maps.GeocoderStatus.ZERO_RESULTS) {
					alert("見つかりません");
				} else {
					alert("えぇ～っと・・、バージョンアップ？");
				}
			});
		}








	});

	var map_api = new MapApi();
	map_api.init();


});



