$(document).ready(function() {
	
	$(".button-collapse").sideNav();
	$(".dropdown-button").dropdown();
	$('select').material_select();
	$('.modal').modal();
	$('.tooltipped').tooltip();
	setTimeout(function() {
        $('#message').fadeOut('slow');
    }, 5000);

});
