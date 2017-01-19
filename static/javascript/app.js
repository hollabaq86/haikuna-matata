$(document).ready(function(){
  $(".rating").hide();
  handleWordSubmission();
  $(".update-form").on("submit", function(event){
    event.preventDefault();
    var update1 = $(".update1:checked").val();
    var update2 = $(".update2:checked").val();
    var update3 = $(".update3:checked").val();
    var line1 = $("line1").val();
    var line2 = $("line2").val();
    var line3 = $("line3").val();
    $.ajax({
      url: '/train',
      type: 'POST',
      dataType: 'json',
      data: {train1: update1, train2: update2, train3: update3, lineOne: line1, lineTwo: line2, lineThree: line3},
    })
    .done(function(response) {
      $('input[name="update1"]').prop('checked', false);
      $('input[name="update2"]').prop('checked', false);
      $('input[name="update3"]').prop('checked', false);
      $(".rating").hide();
      $("#newHaikuForm").trigger('reset');
      $("#newHaikuForm").show();

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
  $('#newHaikuForm').on("submit", function(event) {
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
        function isWordInHaiku(word, response){
          if (findWord(word, response.lineOne) && findWord(word, response.lineTwo) && findWord(word, response.lineThree)) {
            return true
          }
          return false
        }
        function findWord(word, str) {
          return RegExp('\\b'+ word +'\\b').test(str)
        }
        debugger
        if (isWordInHaiku(word, response)) {
        } else {
        insertString = "<h4 class='no-word'>Sorry, I don't know that word, so I chose a new one</h4>"
        }
        $(".line1").text(response.lineOne);
        $(".line2").text(response.lineTwo);
        $(".line3").text(response.lineThree);
        $(".line1").prepend(insertString)
        $form.hide();
        $(".rating").show();
      })
  })
}
