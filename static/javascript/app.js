$(document).ready(function() {
    handleWordSubmission();
})

function handleWordSubmission() {
    $('.container').on("submit", "#newHaikuForm", function(event) {
        event.preventDefault();
    })
}
