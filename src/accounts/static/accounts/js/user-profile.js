$(document).ready(function(){

  var userId = $('#user-id').html();

  // List of a user posts api
  $.ajax({
    url: '/api/profiles/' + userId + '/',
    method: 'GET',
    success: function(data){
      //$('#posts-user').append("<h1>" + data.username + "</h1>");
      $('#posts-user').append("<h2>Followers " + '(' + data.followed_by + ")</h2>");
      $('#posts-user').append("<h2>Following " + '(' + data.ifollow + ")</h2>");
      $('#posts-user').append("<h2>Posts " + '(' + data.myPosts.length + ")</h2><hr>");
      // iterate through the array of objects
      for (var i = 0; i < data.myPosts.length; i++) {
        $('#posts-user').append("<div>" + data.myPosts[i] + "<hr></div>");
      };
    },
    error: function(data){
      console.log('error');
      console.log(data);
    }
  });


}); // end of document ready
