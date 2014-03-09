function search_start() {
	  var keyword = $("keyword").value.replace(/(\n|\r)+/g, " ");
	  // empty keyword?
	  if (keyword.replace(/(^\s+)|(\s+$)/g, "").length == 0) {
	    location.href = 'http://sp-search.auone.jp/search';
	    return;
	  }

	  keyword = keyword.replace(/^\s+|\s+$/g, "");

	// commit keyword to falcon
	var url = 'http://sp-search.auone.jp/search?q=' + encodeURIComponent(keyword)  + '&client=' + client + '&channel='+ channel + '&sr=' + sr;
	location.href = url;
}

function delval() {
	$('keyword').value = '';
}