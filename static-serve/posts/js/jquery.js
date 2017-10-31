$(document).ready(function(){

  // List of posts api data
  $.ajax({
    url: '/api/posts/',
    method: 'GET',
    success: function(data){
      // iterate through the array of objects
      $.each(data, function(key, value){
        var postUser= value.username;
        var postTitle = value.title;
        var postSlug = value.slug;
        var postCreated = value.date_created;
        var postContent = value.content;
        var postShort;
        var likeToggle = value.likeToggle;
        var numLikes = value.likes;
        var displayLikes;
        if (numLikes > 0) {
          displayLikes = '(' + numLikes + ')';
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

        $('#posts-container').append(
          "<div>" + "<h4>" + postUser + ": " + "<a href='/posts/"
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

  // Like button
  // $(document.body).on('click', '.post-like', function(e){
  //     e.preventDefault();
  //     var this_ = $(this);
  //     var postId = this_.attr('post-id');
  //     var likeUrl = '/api/posts/' + postId + '/like/';
  //
  //     $.ajax({
  //       method: 'GET',
  //       url: likeUrl,
  //       success: function(data){
  //         // need to work the logic in here
  //         if (data.liked){
  //           this_.text('UnLiked');
  //         } else {
  //           this_.text('Liked');
  //         };
  //       },
  //       error: function(data){
  //         console.log('error');
  //         console.log(data);
  //       }
  //     })
  //   });

}); // end of document ready
