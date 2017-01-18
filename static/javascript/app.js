$(document).ready(function() {
    handleWordSubmission();
})

function handleWordSubmission() {
    $('.container').on("submit", "#newHaikuForm", function(event) {
        event.preventDefault();
        var $form = $(this);
        var introHaiku = $(".haiku");
        var newHaiku = $(".resultHaiku");
        var url = $form.attr("action");
        var word = $(this).serialize();
        var request = $.ajax({
          url: url,
          type: "POST",
          data: word,
        });
        request.done(function(response){
        console.log(response);
          $(".line1").text(response.lineOne);
          $(".line2").text(response.lineTwo);
          $(".line3").text(response.lineThree);
          $form.remove();


        })
    })
}
