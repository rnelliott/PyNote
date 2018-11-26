// Back to projects -> 'back to blog' button
$('.iD').click(function () {
    console.log('clicked hai now!', $(this).attr('data-href'));
    var dataHref = $(this).attr('data-href')
    $("#ajax-content").load(dataHref)
    //$('#third').trigger('click');
});