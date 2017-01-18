$(document).ready(function(){
  $(".rating").hide();
  handleWordSubmission();
  $(".update-form").on("submit", function(event){
    event.preventDefault();
    $.ajax({
      url: '/train',
      type: 'POST',
      dataType: 'json',
      data: {train1: update1, train2: update2, train3: update3, lineOne: line1, lineTwo: line2, lineThree: line3},
    })
    .done(function(response) {
      $(".rating").hide();
      $(".form").show();
    })
    .fail(function() {
      console.log("error");
    })
    .always(function() {
      console.log("complete");
    });

  })
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
          $form.hide();
          $(".rating").show();
        })
    })
}
