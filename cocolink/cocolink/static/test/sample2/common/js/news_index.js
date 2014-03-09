var pos = 0;
var length = 0;

Event.observe(window, 'load', scrollIndex, false);

function scrollIndex(evt) {
	if ( pos > length -1) {
		pos = 0;
	}
	if ( pos < 0 ) {
		pos = length - 1;
	}
	var cals = $A(document.getElementsByClassName('demo3'));
	cals.each(function(item,idx){
		if ( idx == pos ) {
			item.show();
		} else {
			item.hide();
		}
		length = idx; 
	});
	length = length + 1;
}
