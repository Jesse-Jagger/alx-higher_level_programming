//using jQuery to make an AJAX request to fetch data from an API 
//and then updating the text content of a DIV element with the response.//

$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
