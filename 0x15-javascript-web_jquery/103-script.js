$(function () {
  let endpoint = "https://www.fourtonfish.com/hellosalut/hello/";

  $('INPUT#btn_translate').on('click', getTranslation);
  // click event

  // keypress event
  $("INPUT#language_code").keypress(function (event) {
    // Check if the Enter key is pressed (key code 13)
    if (event.which === 13)
      getTranslation();
  });


  function getTranslation() {
    // get the language code entered by the user
    const lang_code = $('INPUT#language_code').val()

    // send get request
    endpoint = endpoint + '?lang=' + lang_code
    $.get(endpoint, function (data) {
      $('DIV#hello').html(data.hello);
    });
  }
});
