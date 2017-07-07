$(document).ready(function(){
	$('.Tnav li').on('click',function(){
		$(this).addClass('active').siblings().removeClass('active');
	});
	$('.Tpull-down').on('click',function(e){
		$('.Thover').slideToggle(300);
	    e.stopPropagation();
	});
	$('body').on('click',function(){
		$('.Thover').slideUp(300);
	});
	$('.Thover').on('click',function(e){
		e.stopPropagation();
	});
	$('#staff').on('click',function(){
		window.location.href="http://staff.tripanels.com";
	});
	$('#logout').on('click',function(){
		window.location.href="/users/logout/";
	});
	
});	

