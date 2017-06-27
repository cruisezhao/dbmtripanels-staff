$(document).ready(function(){
    //go to index interface
    $('#head0 #logo').on('click',function(){
    	window.location.href="http://portal.tripanels.com/";
    });
	//GO TO all_products interface
	$('#all_Products').on('click',function(){
		window.location.href="http://portal.tripanels.com/all_products.html";
	});
	//hover email
  var $nameLength = $('#head0 #head1 #myName').width();
  if($nameLength < 110){
    $(this).find('.Hover').width(130);
  };
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
