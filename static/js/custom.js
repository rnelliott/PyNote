// Back to projects -> 'back to blog' button
$('.iD').click(function () {
    var dataHref = $(this).attr('data-href')
    $("#ajax-content").load(dataHref)
    //$('#third').trigger('click');
});