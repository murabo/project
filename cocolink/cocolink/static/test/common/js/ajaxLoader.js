  var count = 0;
  function rotate() {
    var elem = document.getElementById('div1');
	if ( elem != null ) {
		if ( $('div1').style.display != 'none' ) {
		    elem.style.MozTransform = 'scale(0.5) rotate('+count+'deg)';
		    elem.style.WebkitTransform = 'scale(0.5) rotate('+count+'deg)';
		    if (count>=360) { count = 0 }
		    count+=45;
		    window.setTimeout(rotate, 100);
		}
		else {
			//ロード中画像が消えたのでタイマー終了
		}
	}
  }
  //window.setTimeout(rotate, 100);	//画像表示中のみタイマーを動かす
