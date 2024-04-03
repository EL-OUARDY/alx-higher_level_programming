$(function () {
  const endpoint = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  $.get(endpoint, function (data) {
    $("DIV#hello").text(data.hello)
  });
});
