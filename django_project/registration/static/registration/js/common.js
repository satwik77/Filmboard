//common js
$(document).ready(function() {
    var count  = $('.navbar-right ul.dropdown-menu li').length;
	if(count-1 > 0)
	$('.badge').html(count-1);
});
