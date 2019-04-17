function get_last_tweets() {
    var form = $('#report-form');
    $.ajax({
        url : form.attr('action'),
        type : form.attr('method'),
        data: form.serialize(),

        success : function (response) {
            $('#word_list').innerHTML = response
        }
    })
}
function delete_last_tweets() {
    $('#word_list').innerHTML = ''
}