//common js
$(document).ready(function() {
    var count  = $('.navbar-right ul.dropdown-menu li').length;
	if(count-1 > 0)
	$('.badge').html(count-1);
});
// card js
$('.card-block').click(function() {
//	console.log('1');
	if ($(this).css('top') == '0px')
    	$(this).css('top','-285px');
	else $(this).css('top','0px');
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
    if(window.location.href.toString().split("/").length - 1 == 5)
		$('.navbar-brand').attr('href','../../dashboard/');
    if(window.location.href.toString().split("/").length - 1 == 6)
		$('.navbar-brand').attr('href','../../../dashboard/');

});