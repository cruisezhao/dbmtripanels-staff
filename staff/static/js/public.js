$(document).ready(function(){   
    //go to index interface
    $('#head0 #logo').on('click',function(){
    	window.location.href="http://portal.databasemart.net/";
    });	
	//GO TO all_products interface
	$('#all_Products').on('click',function(){
		window.location.href="http://portal.databasemart.net/all_products.html";
	});	
	//hover email
	$('#head0 #head1 #myName').hover(function(){
		$(this).find('.Hover').stop().slideDown(300);
	},function(){
		$(this).find('.Hover').stop().slideUp(300);
	});
	$('#topNav #topNav1 ul a').each(function(){
	    if($(this).attr('href') == window.location.pathname){
	        $(this).addClass('onSelected');
	    };
	});
})