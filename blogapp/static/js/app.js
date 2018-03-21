

 $(document).ready(
    function ()
              {
                    carouselImages();
                    populateTweets();
                    newsletterPopup();
                    if($("body").attr('data-title')=="index")
                        {
                            setTimeout(function(){
                            $("#subscribeModal.modal").modal("show");
                              },2000);        
                        }
                    
              }
);



function carouselImages()
{
    var items = $(".item");
    var image;

    $(".item .content").each(function(index){
                    putImage($(this));
                    });
}

function putImage(item)
{
    var imageUrl = item.attr("data-image");
    item.css({
        "background-image" : 'url('+imageUrl+')',
    });
}


// twitter sharing api


window.twttr = (function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0],
    t = window.twttr || {};
  if (d.getElementById(id)) return t;
  js = d.createElement(s);
  js.id = id;
  js.src = "https://platform.twitter.com/widgets.js";
  fjs.parentNode.insertBefore(js, fjs);

  t._e = [];
  t.ready = function(f) {
    t._e.push(f);
  };

  return t;
}(document, "script", "twitter-wjs"));


// populating tweets

function populateTweets()
{
    var currentUrl = $(".twitter-btn").attr("href");
    var heading = $(".blog-heading").text();
    var author = $(".blog-author").text();
    var updatedUrl = currentUrl+"?text="+heading+" - "+author;
    console.log(updatedUrl);
    $(".twitter-btn").attr("href",updatedUrl);
}



//////////////////////////
// Pop Up Element
/////////////////////////


function newsletterPopup()
{
     var subscribeModal = '<div id="subscribeModal" class="modal fade" role="dialog">'+
              '<div class="modal-dialog">'+

                '<div class="modal-content">'+
                  '<div class="modal-header">'+
                    '<button type="button" class="close" data-dismiss="modal">&times;</button>'+
                    '<h4 class="modal-title">Subscribe to our newsletter</h4>'+
                  '</div>'+
                  '<div class="modal-body">'+
                    '<form class="form-horizontal" id="subscriptionForm">'+
                        '<div class="form-group">'+
                            '<label for="email" class="col-sm-2">Email:</label>'+
                            '<div class="col-sm-10">'+
                                  '<input class="form-control" type="text" name="email"/>'+
                            '</div>'+
                        '</div>'+

                        '<div class="form-group">'+
                            '<button class="btn btn-default normal-cta">Subscribe</button>'+
                        '</div>'+

                        '<div class="form-group">'+
                            '<button class="btn btn-default alternate-cta">Not Interested?</button>'+
                        '</div>'+
                    '</form>'+
                  '</div>'+
                  '<div class="modal-footer">'+
                    '<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>'+
                  '</div>'+
                '</div>'+
              '</div>'+
            '</div>';

    $('body').append(subscribeModal);
    
  var popup = '<div class="popup"><div class="panel panel-default">'+
                  '<div class="panel-heading">Subscribe' +
      
  '</div>'+
                  '<div class="panel-body">'+
      '<p>Subscribe to our newsletter</p>'
  +
      '<button class="btn btn-default normal-cta" type="button" data-toggle="modal" data-target="#subscribeModal">Subscribe</button>'+'</div>'+
              '</div></div>';


  $('body').append(popup);

}

app.js
Displaying app.js.