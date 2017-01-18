$(document).ready(function(){
  handleWordSubmission();
  $(".update-form").on("submit", function(event){
    event.preventDefault();
    var update1 = $(".update1:checked").val();
    var update2 = $(".update2:checked").val();
    var update3 = $(".update3:checked").val();
    $.ajax({
      url: '/train',
      type: 'PUT',
      dataType: 'json',
      data: {train1: update1, train2: update2, train3: update3},
    })
    .done(function() {
      console.log("success");
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
    })
}
