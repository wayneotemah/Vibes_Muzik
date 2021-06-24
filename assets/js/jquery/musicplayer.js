$(document).ready(function(){
	var song = document.getElementById("playing_track");
	$('#playmusic').on('click',function (){
			$(song)[0].play();
			$('#playmusic').hide();
			$('#pausemusic').fadein();


	});
	$('#pausemusic').on('click',function(){
		$(song)[0].pause();
		$('#playmusic').fadein();
		$('#pausemusic').hide();


	});
	
});