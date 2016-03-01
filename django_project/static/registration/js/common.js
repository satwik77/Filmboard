//common js
$(document).ready(function() {
    var count  = $('.navbar-right ul.dropdown-menu li').length;
	if(count-1 > 0)
	$('.badge').html(count-1);
});
// card js
$('.card-block').click(function() {
//	console.log('1');
	if ($(this).css('top') == '0px') {
    	$(this).css('top','-285px');
		$(this).parent('.card').children('.card-arrow').addClass('up');
	}
	else { $(this).css('top','0px');
		$(this).parent('.card').children('.card-arrow').removeClass('up');
	}
});
$('.card-arrow').click(function() {
	$(this).parent('.card').children('.card-block').trigger('click');
});
$('.card').find('*').not('.card-img-top').not('.card-edit').filter( function() {
		return ($(this).html() == '') }).html('None');
$('.card').not('.card.profile').each(function() {
    if( $(this).find('span.tag.right').html().indexOf('Feature') >= 0)
		$(this).find('.card-img-top').addClass('back-fix').addClass('feature');
    if( $(this).find('span.tag.right').html().indexOf('Short') >= 0)
		$(this).find('.card-img-top').addClass('short').addClass('back-fix');
    if( $(this).find('span.tag.right').html().indexOf('TV') >= 0)
		$(this).find('.card-img-top').addClass('tv').addClass('back-fix');
    if( $(this).find('span.tag.right').html().indexOf('Music') >= 0)
		$(this).find('.card-img-top').addClass('music').addClass('back-fix');
    if( $(this).find('span.tag.right').html().indexOf('Ad') >= 0)
		$(this).find('.card-img-top').addClass('ad').addClass('back-fix');
    if( $(this).find('span.tag.right').html().indexOf('Reality') >= 0)
		$(this).find('.card-img-top').addClass('reality').addClass('back-fix');
    if( $(this).find('span.tag.right').html().indexOf('Any') >= 0)
		$(this).find('.card-img-top').addClass('any').addClass('back-fix');
    if( $(this).find('.card-title').html().indexOf('Artist') >= 0)
		$(this).find('.card-img-top').addClass('people').addClass('back-fix');
    if( $(this).find('.card-title').html().indexOf('Allied') >= 0)
		$(this).find('.card-img-top').addClass('allied').addClass('back-fix');
});

$(document).ready(function(e) {
    if(window.location.href.toString().split("/").length - 1 == 5) {
		$('.navbar-brand').attr('href','../../dashboard/');
		$('#logout-link').attr('href','../../logout');
		$('#project-link a').attr('href','../../projects'); }
    if(window.location.href.toString().split("/").length - 1 == 6) {
		$('.navbar-brand').attr('href','../../../dashboard/');
		$('#logout-link').attr('href','../../logout');
		$('#project-link a').attr('href','../../projects'); }
});
		function changeDateFormat(value) {
		if(value.search(" ") == -1) 
		return(value);
		else {
			if(value.search(".") > 0) {
				var month = value.split(".");
			}
			else var month = value.split(/ (.+)?/);
			console.log(month);
		    var	d = Date.parse(month[0] + "1, 2012"),
				monthNumber = new Date(d).getMonth() + 1,
				dateformat = month[1].split(","),
				monthInteger = "",
				dateNumber = "",
				dateInteger = parseInt(dateformat[0]);
				
				if(monthNumber < 10) monthInteger = "0" + monthNumber;
				else monthInteger = monthNumber;
				if(dateInteger < 10) dateNumber = "0" + dateInteger.toString();
				else dateNumber = dateInteger;
				console.log(dateNumber);
				return(parseInt(dateformat[1]) + "-" + monthInteger + "-"+ dateNumber); 
			}
		
	}
var availableTags = [
        "CANON 5DS R",
        "CANON 5DS",
        "CANON EOS 5D MARK II",
        "CANON EOS 5D MARK III",
        "CANON EOS 6D",
        "CANON EOS 7D",
        "CANON EOS 50D",
        "CANON EOS 60D",
        "CANON EOS M DIGITAL CAMERA",
        "CANON EOS REBEL SL1 DSLR",
        "CANON EOS REBEL T2I",
        "NIKON COOLPIX P7000",
        "NIKON COOLPIX S80",
        "NIKON COOLPIX S1100PJ",
        "NIKON COOLPIX S5100",
        "SONY ALPHA 900",
        "SONY ALPHA NEX-3"
    ];
