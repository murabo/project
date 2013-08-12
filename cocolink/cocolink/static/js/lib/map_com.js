
	var Map = function() {};
	Map.prototype = $.extend({}, GetListUtil.prototype, {

		init: function() {
			this._bind();
			this._initialize();
		},
		_initialize :function() {
			self.ajax = $.extend({}, Super.prototype, AjaxUtil.prototype);
			self.ajaxvo = new AjaxVo;
		},
		_bind: function() {

			$(".js-submit").on("click", this.get_place_list);

		},
		_map: '',
		//現在地の座標取得
		get_present_location: function() {



		},
		//現在地取得
		get_map: function(callback){

			var that = this;

			var openInfoWindow;
			var lat="";
			var lng="";

			// 位置情報取得に成功したとき
			var position = function (position) {
				lat = position.coords.latitude;
				lng = position.coords.longitude;

				var latlng = new google.maps.LatLng(lat, lng);
				var myOptions = {
					zoom: 19,
					center: latlng,
					mapTypeId: google.maps.MapTypeId.ROADMAP
				};
				that.map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
				var marker = new google.maps.Marker({
					position: latlng,
					map: that.map,
				});

				$("body").data("lat",lat);
				$("body").data("lng",lng);

				that.get_place_list();
				//that.change_area();
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
			navigator.geolocation.getCurrentPosition( position , error , option);
		},
		get_place_list: function(bounds){

			var beaches = [
			  ['Bondi Beach', 35.7156029, 139.8979243, 8],
			  ['Coogee Beach', -33.923036, 151.259052, 5],
			  ['Cronulla Beach', -34.028249, 151.157507, 3],
			  ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
			  ['Maroubra Beach', -33.950198, 151.259302, 1]
			];

			var template = $.trim($('#template').html());
			var pyrmont = new google.maps.LatLng($("body").data("lat"),$("body").data("lng"));

			 var request = {
			    location: pyrmont,
			    radius: '500',
			    types: ""
			  };

			var service = new google.maps.places.PlacesService(this.map);
			service.search(request, createList);
 			setMarkers(this.map, beaches);


			function createList(results, status){

 			 	if (status == google.maps.places.PlacesServiceStatus.OK) {

					var frag ="";
					var len= results.length;
					for (var i = 0; i < len; i++){

					    var properties = '';
					    var g = results[i].geometry['location'];
					    for (var prop in g){
					        properties += g[prop];
					    }

						frag+= template.replace( /{name}/ig, results[i].name)
										.replace( /{icon}/ig, results[i].icon)
										.replace( /{location}/ig, results[i]['geometry']['location'])
										.replace( /{{formatted_address}}/ig, results[i].formatted_address)
										.replace( /{vicinity}/ig, (undefined == results[i].vicinity)?"":results[i].vicinity );
					}

					

					$("#js-result-list").html(frag);


				}
			}






function setMarkers(map, locations) {
  // Add markers to the map

  // Marker sizes are expressed as a Size of X,Y
  // where the origin of the image (0,0) is located
  // in the top left of the image.

  // Origins, anchor positions and coordinates of the marker
  // increase in the X direction to the right and in
  // the Y direction down.
  var image = new google.maps.MarkerImage('images/beachflag.png',
      // This marker is 20 pixels wide by 32 pixels tall.
      new google.maps.Size(20, 32),
      // The origin for this image is 0,0.
      new google.maps.Point(0,0),
      // The anchor for this image is the base of the flagpole at 0,32.
      new google.maps.Point(0, 32));
  var shadow = new google.maps.MarkerImage('images/beachflag_shadow.png',
      // The shadow image is larger in the horizontal dimension
      // while the position and offset are the same as for the main image.
      new google.maps.Size(37, 32),
      new google.maps.Point(0,0),
      new google.maps.Point(0, 32));
      // Shapes define the clickable region of the icon.
      // The type defines an HTML <area> element 'poly' which
      // traces out a polygon as a series of X,Y points. The final
      // coordinate closes the poly by connecting to the first
      // coordinate.
  var shape = {
      coord: [1, 1, 1, 20, 18, 20, 18 , 1],
      type: 'poly'
  };
  for (var i = 0; i < locations.length; i++) {

    var beach = locations[i];
    var myLatLng = new google.maps.LatLng(beach[1], beach[2]);
    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        //shadow: shadow, //好きな画像をセット
        //icon: image,
        shape: shape,
        title: beach[0],
        zIndex: beach[3]
    });
  }
}









		},
		//詳細住所取得
		geocoder: function(that){

			var lat =that.find('.js-lat').val();
			var lng =that.find('.js-lng').val();

			//ジオコードオブジェクト
			var geocoder = new google.maps.Geocoder();
			geocoder.geocode(
			  {
			    'latLng': lat+','+lng
			  },
			  function(results, status){
			    if(status==google.maps.GeocoderStatus.OK){
			    	//処理
			    	alert(results);
			    }
			  }
			);

		},
		//地図の範囲変更
		//TODO
		change_area: function(){


			var that = this;
			google.maps.event.addListener(that.map, 'drag', dispLatLng);
			google.maps.event.addListener(that.map, "zoom_changed", dispLatLng);

			function dispLatLng(){

				  var latlng = that.map.getCenter();

				  var str = "[CENTER]=[" + latlng.lat() + "," + latlng.lng() + "]<br />";

				  var latlngBounds = that.map.getBounds();
				  var swLatlng = latlngBounds.getSouthWest();
				  str = str + "[SouthWest]=[" + swLatlng.lat() + "," + swLatlng.lng() + "]<br />";

				  var neLatlng = latlngBounds.getNorthEast();
				  str = str + "[NorthEast]=[" + neLatlng.lat() + "," + neLatlng.lng() + "]";


				$("body").data("lat",latlng.lat());
				$("body").data("lng",latlng.lng());

				//送信用
				var defaultBounds = new google.maps.LatLngBounds(
					new google.maps.LatLng(swLatlng.lat(),swLatlng.lng()),
					new google.maps.LatLng(neLatlng.lat(),neLatlng.lng()));


				$("body").data("defaultBounds",defaultBounds);

				document.getElementById("latlng").innerHTML = str;
			}
		},
		//File APIs 対応チェック
		check_browser: function(){
			if (window.File && window.FileReader && window.FileList && window.Blob) {
				$('#files').displayBlock();
				document.getElementById('files').addEventListener('change', this._handleFileSelect, false);
			}

		},
		//File 選択時の処理
		_handleFileSelect: function(event){

			var files = event.target.files;

			if( 1 < files.length){
				//TODO エラー処理
				alert('1ファイル選択してください');
			}else{
				var f = files[0];
				// 画像ファイルかテキスト・ファイルかを判定
				if (!f.type.match('image.*')) {
					alert("画像ファイルとテキスト・ファイル以外は表示できません。");
				}else{
					// FileReaderオブジェクトの生成
					var reader = new FileReader();
					// エラー発生時の処理
					reader.onerror = function (evt) {
						alert("読みとりに失敗しました");
					}

					var disp = $(".js-disp-img");

					// 画像ファイルの場合の処理
					if (f.type.match('image.*')) {
						// ファイル読取が完了した際に呼ばれる処理
						reader.onload = function (evt) {
						var src = evt.target.result;
							$('.js-disp-img').attr("src",src);
							$('.js-post-data-url').val(src);
						}

						// readAsDataURLメソッドでファイルの内容を取得
						reader.readAsDataURL(f);

					}
				}
			}

		}



	});




