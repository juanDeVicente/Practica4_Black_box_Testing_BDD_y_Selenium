function get_last_tweets() {
    var form = $('#report-form');
    event.preventDefault();
    $.ajax({
        url : form.attr('action'),
        type : form.attr('method'),
        data: form.serialize(),

        success : function (response) {
            console.log(response);
            document.getElementById('word_list').innerHTML = response;
        }
    })
}
function delete_last_tweets() {
    document.getElementById('word_list').innerHTML = '';
}