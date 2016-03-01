    if(document.documentElement.scrollHeight - $(window).height() + 140 < $('#exp').offset().top)
	$('#exp-fix-float div').css('display','block');
	if(document.documentElement.scrollHeight - $(window).height() + 140 < $('#rec').offset().top)
	$('#rec-fix-float div').css('display','block');

$.material.init();
//card js
$(".sec-nav li a").click(function() {
	$('.active').removeClass('active');
	$(this).parent('li').addClass('active');
	var aId = '';
	aId = $(this).attr('id');
	//console.log($(this).attr('id'));
	var res = aId.split('-');
	var divId = res[1];
	//console.log(divId);
    $('html, body').animate({
        scrollTop: $("#"+divId).offset().top - 90
    }, 500);
});
var expDist = $('#exp').offset().top,
	inExp = false,
	inRec = false,
	inAbout = false,
    recDist = $('#rec').offset().top,
	$window = $(window);
$(window).resize(function(){
	expDist = $('#exp').offset().top;
	recDist = $('#rec').offset().top;
	if(document.documentElement.scrollHeight - $(window).height() + 140 < $('#exp').offset().top)
	$('#exp-fix-float div').css('display','block');
	else
		$('#exp-fix-float div').css('display','none');
	if(document.documentElement.scrollHeight - $(window).height() + 140 < $('#rec').offset().top)
	$('#rec-fix-float div').css('display','block');
	else
		$('#rec-fix-float div').css('display','none');

});
$window.scroll(function() {
	//console.log($window.scrollTop() + 90);
	//console.log(expDist);
	//console.log(recDist);
    if ( $window.scrollTop() + 140 > expDist ) {
		//console.log('in-exp');
        $('.float-container div.wrapper').css('top','-55px');
		if(inExp) {  }
		if(!inExp) {
		//	console.log('in-this');
		$('.sec-nav li.active').removeClass('active');
		$('#nav-exp').parent().addClass('active');
		inExp = true; inRec = false; inAbout = false;
		}
    }
	if ( $window.scrollTop() + 140 > recDist ) {
        $('.float-container div.wrapper').css('top','-110px');
		if(inRec) {  }
		else {
		$('.active').removeClass('active');
		$('#nav-rec').parent('li').addClass('active');
		inExp = false; inRec = true; inAbout = false;
		}
    }
	if ( $window.scrollTop() + 140 < expDist )  {
		$('.float-container div.wrapper').css('top','0px');
		if(inAbout) {  }
		else {
		//		console.log('inthis');
		$('.active').removeClass('active');
		$('#nav-about').parent('li').addClass('active');
		inExp = false; inDist = false; inAbout = true;
		}
	}
});
$(document).ready(function() {
    var count  = $('.navbar-right ul.dropdown-menu li').length;
	if(count-1 > 0)
	$('.badge').html(count-1);
});
$('#personal-info ul li').each(function(index) {
    if($(this).children('span').text() == "" || $(this).children('span').text() == "None" || $(this).children('span').text() == "0.0")
		$(this).not('#inventory-li').css('display','none');
	if($(this).children('span').text() == "Portfolio Makers") $('#inventory-li').css('display','none');
});
$(document).ready(function(e) {
    			$.ajax({
				url: "../see_applied/",
  				method : "GET"
			    }).done(function( html ) {
					$('.main.applied').css('opacity',1);
	   				$( ".main.applied" ).html(html);
 			}); 
			
});


