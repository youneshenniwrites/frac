$(document).ready(function(){

  $('#username-id').hide();
  var userId = $('#username-id').html();
  var verb;
  var followersCountUp;
  var followersCountDown;

  // Ajax Follow button
  $(document.body).on('click', '.follow-user', function(e){
      e.preventDefault();
      var this_ = $(this);
      var userId = this_.attr('user-id');
      var followUrl = '/api/profiles/' + userId + '/follow/';

      $.ajax({
        method: 'GET',
        url: followUrl,
        success: function(data){
           if (data.followed){
             verb = 'Unfollow';
             followersCountUp = parseInt($('#followers').text()) + 1;
             $('#followers').text(followersCountUp);
           } else {
             verb = 'Follow';
             followersCountDown = parseInt($('#followers').text()) - 1;
             $('#followers').text(followersCountDown);
           };
           // acts on the test value of the list api ajax call
           this_.text(verb);
        },
        error: function(data){
          console.log('error');
          console.log(data);
        }
      }) // end of ajax call
    }); // end of click event

    // List of a user posts api
    $.ajax({
      url: '/api/profiles/' + userId + '/',
      method: 'GET',
      success: function(data){
         var test;
         if (data.followed_boolean){
           test = 'Unfollow';
         } else {
           test = 'Follow';
         }

        // toggle follow this user
        $('#posts-user').append("<div><a href='#' class='follow-user' user-id="
        + data.username + ">" + test + "</a></div>");

        // Key infos about the user
        $('#posts-user').append("<h1>" + data.username + "</h1>");
        $('#posts-user').append("<h2>Followers " + '(<span id="followers">'
        + data.all_myFollowers + "</span>)</h2>");
        $('#posts-user').append("<h2>Following "
        + '(' + data.iFollow + ")</h2>");
        $('#posts-user').append("<h2>Total posts "
        + '(' + data.all_myPosts + ")</h2>");
        $('#posts-user').append("<h2>Total likes "
        + '(' + data.all_myLikes + ")</h2><hr>");

        // displays the list of all my posts
        $('#posts-user').append("<h2>List of posts</h2><hr>");
        for (var i = 0; i < data.all_myPosts_content.length; i++) {
          $('#posts-user').append("<div>"
          + data.all_myPosts_content[i] + "<hr></div>");
        };

        // displays the list of all py followers
        $('#posts-user').append("<h2>List of my followers</h2><hr>");
        if (data.all_myFollowers_list.length == 0) {
          $('#posts-user').append("<div>No followers yet.<hr></div>");
        } else {
          for (var i = 0; i < data.all_myFollowers_list.length; i++) {
            // displays the list of my followers
            $('#posts-user').append("<div><a href='/profiles/"
            + data.all_myFollowers_list[i]
            + "'>" + data.all_myFollowers_list[i] + "</a><hr></div>");
          };
        };

        // displays the list of all my followers
        $('#posts-user').append("<h2>List of whom I follow</h2><hr>");
        if (data.iFollow_list.length == 0) {
          $('#posts-user').append("<div>Not following any users.<hr></div>");
        } else {
          for (var i = 0; i < data.iFollow_list.length; i++) {
            // displays the list of my followers
            $('#posts-user').append("<div><a href='/profiles/"
            + data.iFollow_list[i]
            + "'>" + data.iFollow_list[i] + "</a><hr></div>");
          };
        };

      },
      error: function(data){
        console.log('error');
        console.log(data);
      }
    }); // end of ajax

}); // end of document ready
