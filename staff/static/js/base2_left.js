window.onload=function(){
	//filtration height control
	var FHeight=$('#filtration').height();	
	function Resize(){
		if($(window).width()>767){
			if(FHeight<$('#content_wrapper1').height()){
				$(window).css('height','auto');
				$('#filtration').height($('#content_wrapper1').height()+20);			    
			}else{
				$(window).css('height','100%');
				if($(window).height()> ($('#filtration').height()+70) ){
					$('#filtration').height($(window).height()-70);
				}else{
					$('#filtration').css('height','auto');
					$(window).css('height','auto');
				};				
			};
			$('#content_wrapper1').outerWidth($('#content_wrapper').width()-$('.Tspan2').width()-2);
		}else{
			$('#filtration').height(FHeight);
		};			
	};
	Resize();
	window.onresize=function(){
		Resize();
	};
	$('.Tcheckbox').on('click',function(){
		if($(this).hasClass('Tcheckbox1')){
			$(this).removeClass('Tcheckbox1');
		}else{
			$(this).addClass('Tcheckbox1');
		};		
	});
	$('.Tplus').on('click',function(){		
		
		if($(this).parent('.Tadd').css('right')=="-260px"){
			$(this).parent('.Tadd').animate({
				'right':"0px"
			},500,'linear',function(){});
		}else{
			$(this).parent('.Tadd').animate({
				'right':"-260px"
			},500,'linear',function(){});
		}
		
	})
}
