window.onload=function(){
	//filtration height control
	var FHeight=$('#filtration').height();
	function Resize(){
		if($(window).width()>767){
			$('#filtration').height($('#content_wrapper').height());
			$('#content_wrapper').outerWidth($('#content_wrapper1').width()-$('.Tspan2').width()-1);
		}else{
			$('#filtration').height(FHeight);
		};
		if($(window).width()<1230){
			$('.Ttable ul').width(919);
			$('.Ttable ul li.Ttd1').width(184);
			$('.Ttable ul li.Ttd2').width(73);
			$('.Ttable ul li.Ttd3').width(73);
			$('.Ttable ul li.Ttd4').width(267);
			$('.Ttable ul li.Ttd5').width(138);
			$('.Ttable ul li.Ttd6').width(92);
			$('.Ttable ul li.Ttd7').width(92);
		}else{
			$('.Ttable ul').css('width','100%');
			$('.Ttable ul li.Ttd1').css('width','20%');
			$('.Ttable ul li.Ttd2').css('width','8%');
			$('.Ttable ul li.Ttd3').css('width','8%');
			$('.Ttable ul li.Ttd4').css('width','28%');
			$('.Ttable ul li.Ttd5').css('width','15%');
			$('.Ttable ul li.Ttd6').css('width','10%');
			$('.Ttable ul li.Ttd7').css('width','10%');
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
