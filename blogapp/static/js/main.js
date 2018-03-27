  
 $(document).ready(function(){
   $(".upvote").click(function(){
   	   $.ajax({
    	url: "https://upvote/"+$(".upvote",
    	type:"GET",
        data:{"searchterm":"hello",
               "noofterms":3}, 
        success: function(result){
                console.log(result)}
     });
   });
});
