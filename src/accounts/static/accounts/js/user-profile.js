$(document).ready(function(){

  var userId = $('#user-id').html();

  // List of a user posts api
  $.ajax({
    url: '/api/profiles/' + userId + '/',
    method: 'GET',
    success: function(data){
      $('#posts-user').append("<h2>Followers " + '(' + data.all_myFollowers + ")</h2>");
      $('#posts-user').append("<h2>Following " + '(' + data.iFollow + ")</h2>");
      $('#posts-user').append("<h2>Total posts " + '(' + data.all_myPosts + ")</h2>");
      $('#posts-user').append("<h2>Total likes " + '(' + data.all_myLikes + ")</h2><hr>");
      $('#posts-user').append("<h2>List of posts</h2><hr>")

      for (var i = 0; i < data.all_myPosts_content.length; i++) {
        // displays the list of all py posts
        $('#posts-user').append("<div>" + data.all_myPosts_content[i] + "<hr></div>");
      };

      // for (var i = 0; i < data.all_myPosts_content.length; i++) {
      //   // displays the list of my followers
      //   $('#posts-user').append("<div>" + data.all_myPosts_content[i] + "<hr></div>");
      // };

    },
    error: function(data){
      console.log('error');
      console.log(data);
    }
  });


}); // end of document ready
