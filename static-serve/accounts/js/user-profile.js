$(document).ready(function(){

  // List of posts api data
  $.ajax({
    url: '/profiles/Batman7/',
    method: 'GET',
    success: function(data){
      // iterate through the array of objects
      $.each(data, function(key, value){
        var postUser= value.user;
        var postTitle = value.title;
        var postSlug = value.slug;
        var postCreated = value.date_created;
        var postContent = value.content;
        var postShort;
        var likeToggle = value.likeToggle;
        var numLikes = value.likes;
        var displayLikes;
        var trophee;
        if (numLikes > 0) {
          console.log(numLikes);
          displayLikes = '(' + numLikes + ')';
          if (numLikes === 3) {
            trophee = 'You won a new badge!';
            displayLikes += trophee;
          }
        } else {
          displayLikes = ' ';
        }

        if (postContent.length >= 50){
          // truncate long posts with a link to the detail post page
          postShort = jQuery.trim(postContent).substring(0, 50).split(" ").slice(0, -1).join(" ")
          + "<a href='/posts/" + postSlug + "'>" + "..." + "</a>";
        } else {
          postShort = postContent;
        }

        $('#posts-user').append(
          "<div>" + "<h4><a href='" + postUser.url + "'>" + postUser.username + "</a>: " + "<a href='/posts/"
          + postSlug + "'>" + postTitle + "</a>" + "<h5>"
          + postCreated + "</h5>" + postShort +
          "<div><a href='#' class='post-like' post-id=" + postSlug + ">Like " + displayLikes + " </a></div>"
          + "</div>" + "<hr>"
        );
      });
    },
    error: function(data){
      console.log('error');
      console.log(data);
    }
  });

}); // end of document ready
