$(function () {
  const endpoint = "https://swapi-api.alx-tools.com/api/films/?format=json";
  $.get(endpoint, function (data) {
    data.results.forEach(x => {
      $("UL#list_movies").append(`<li>${x.title}</li>`)
    });
  });
});
