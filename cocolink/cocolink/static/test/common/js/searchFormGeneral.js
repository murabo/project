var GuideSentence = '他の記事を探す';
function ShowFormGuide(obj) {
  // 入力案内を表示
  if( obj.value == '' ) {
	 obj.value = GuideSentence;
	 obj.style.color = '#808080';
  }
}
function HideFormGuide(obj) {
  // 入力案内を消す
  if( obj.value == GuideSentence ) {
	 obj.value='';
	 obj.style.color = '#000000';
  }
}