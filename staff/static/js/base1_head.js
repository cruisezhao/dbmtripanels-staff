$(document).ready(function(){	
	$('.Tpull-down').on('click',function(e){
		$(this).siblings('.Thover').slideToggle(300);
	    e.stopPropagation();
	});
	$('.Tpull-down1').on('click',function(e){
		$(this).siblings('.Thover1').slideToggle(300);
	    e.stopPropagation();
	});
	$('body').on('click',function(){
		$('.Thover').slideUp(300);
		$('.Thover1').slideUp(300);
	});
	$('.Thover,.Thover1').on('click',function(e){
		e.stopPropagation();
	});
	$('#staff').on('click',function(){
		window.location.href="http://staff.tripanels.com";
	});
	$('#logout').on('click',function(){
		window.location.href="/users/logout/";
	});
	
	$('.Tnav a').each(function(index,itself){
		if(window.location.pathname.indexOf($(this).text())>0){
			$(this).css({
				'background-color':"#0cc285",
				'color':"#ffffff"
			});
		};
	});
	//select button
    $('#toggle_all').click(function() {
        $('td input:checkbox[name=pk]').prop('checked', $(this).prop('checked'));
        if ($(this).is(':checked')) {
            $('#select_all_box').removeClass('hidden');
        } else {
            $('#select_all').prop('checked', false);
        }
    });
	
});	

