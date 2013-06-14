$(function() {

	var MapApi = function() {};
	MapApi.prototype = $.extend({}, GetListUtil.prototype, {

		init: function() {
			this._bind();
			this._initialize();
		},
		_initialize :function() {
			self.ajax = $.extend({}, Super.prototype, AjaxUtil.prototype);
			self.ajaxvo = new AjaxVo;
		},
		_bind: function() {
			this._get_map();
		},
		//現在地取得
		_get_map: function(event){
			/**
			 * 現在開いている情報ウィンドウ
			 * @type google.maps.InfoWindow
			 */
			var openInfoWindow;

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

				google.maps.event.addListener(map, 'click', function(mouseEvent) {
					getAddress(mouseEvent.latLng);
				});

				var ll = "";
				function getAddress(latlng) {


					var str_la = latlng.toString();
					str_la = str_la.replace("(", "").replace(")", "").replace(/\s|　/g,"");

					$.ajax({
						url: 'http://dev-girlsup.me/api/1/user/place',
						type : 'GET',
						dataType: 'jsonp',
						 data:  {
								location:str_la,
								radius: 1000,
								//types: 'food',//複数おk
								language: 'ja',
								rankby: 'prominence',//重要度(デフォルトだから指定いらないかも)
								sensor: 'false',//gps
								key: 'AIzaSyBmZZTB4DAdN9OZq3K2NqYpgqZzDuc2am8'
						     },
						timeout: 15000,
						cache: false,
						beforeSend: function() {

						},
						jsonp : 'callback',
						error: function(data){
							alert('a');
						},
						success: function(data) {
							printProperties(data.results[2]);
						},
						complete: function (data){

						}
					});


					function printProperties(obj) {
					    var properties = '';
					    for (var prop in obj){
					        properties += prop + "=" + obj[prop] + "\n";
					    }
					    alert(properties);
					}









					var geocoder = new google.maps.Geocoder();
						geocoder.geocode({
							latLng: latlng
						}, function(results, status) {
							if (status == google.maps.GeocoderStatus.OK) {
								//alert(printProperties(results[0].address_components[0]));
				                if (results[0].geometry) {
				                    var ad = results[0].formatted_address.replace(/^日本, /, '');
				                    var ad2;
				                    //TODO 日本を消す？
				                    var zip = results[2].formatted_address.replace(/^日本 /, '');
				                    openInfoWindow = new google.maps.InfoWindow({
				                        content: zip + "<br>" + ad + "<br>(Lat, Lng) = " + latlng
				                    }).open(map, new google.maps.Marker({
				                        position: latlng,
				                        map: map
				                    }));
				                }

				               // printProperties(results[0]);
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


				function formatCode(c) {
					  return (c.match(/(\d{3})(\d{4})/))? "〒" + RegExp.$1 + "-" + RegExp.$2: "";
				}

				function printProperties(obj) {
				    var properties = '';
				    for (var prop in obj){
				        properties += prop + "=" + obj[prop] + "\n";
				    }
				    alert(properties);
				}
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

			//初期表示で現在地を表示
			navigator.geolocation.getCurrentPosition( position , error , option)

			//現在地へ戻るボタン
			$("#abtn").click(function() {
				navigator.geolocation.getCurrentPosition(position, error , option);
				return false;
			});

		}




	});

	var map_api = new MapApi();
	map_api.init();


});



