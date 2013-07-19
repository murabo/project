$(function() {

	var vali = new Validate(),
	$error = $(".js-error"),
	$email = $("#js-email"),
	$password = $("#js-password"),
	$form1 = $("#form1");


	//ログインボタン押下
	$(".js-submit").click(function(e){

		e.preventDefault();
		var chk_cnt = 2;
		$error.html("");
		
		if(!vali.email($email,err_txt['txt4'])) chk_cnt--;
		if(!vali.count($password,6,16,err_txt['txt1'])) chk_cnt--;

 		if(chk_cnt == 0) $form1.submit();

	});


});



