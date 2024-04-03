$(function () {
  let endpoint = "https://www.fourtonfish.com/hellosalut/hello/";
  $('INPUT#btn_translate').on('click', function () {
    // get the language code entered by the user
    const lang_code = $('INPUT#language_code').val()

    // send get request
    endpoint = endpoint + '?lang=' + lang_code
    $.get(endpoint, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
