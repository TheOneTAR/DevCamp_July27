// Get the posts
$.ajax({
   url: "https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script",
   data: {
      format: 'json'
   },
    error: function() {
      $('#info').html('<p>An error has occurred</p>');
    },
    dataType: 'jsonp',
    success: function (data) {
        var posts = data.feed.entry;
        for (var i=0; i < posts.length; i++) {
            buildPost(posts[i].gsx$postbody['$t'],
                      posts[i].gsx$posttitle['$t'],
                      posts[i].gsx$timestamp['$t']);
        }

    },
    type: 'GET'
});

function buildPost(body, title, timestamp) {
    var newPost = "<section><h3>" + title + "</h3>";
    newPost += body + "</section>";
    $('#forum').append(newPost);
}
    function postForumPost() {
        var title = $('#title').val();
        var body = $('#body').val();

        $.ajax({
            url: "https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse",
            data: { "entry_434124687": title,
                    "entry_1823097801": body},
            type: "POST",
            dataType: "xml",
            statusCode: {
                0: function () {
                    window.location.replace("fakeForum.html");
                },
                200: function () {
                    window.location.replace("fakeForum.html");
                }
            }
        });
    }