

$(document).ready(function(){
   preventSubmitEvents(); 
});



function preventSubmitEvents(){
   
    var form = document.getElementsByTagName("form");
    
    if(form[0].id == "contactForm")
        {
            form[0].addEventListener("submit",event => {
            event.preventDefault();
            contactFormSubmission();
            console.log("form submission stopped");
            });
        }
    else if(form[0].id == "signupForm")
            {form[0].addEventListener("submit",event => {
            event.preventDefault();
            signupFormSubmission();
            console.log("form submission stopped");
            });
            }
    else if(form[0].id=="subscriptionForm")
        {  form[0].addEventListener("submit",event => {
            event.preventDefault();
            subscriptionFormSubmission();
            console.log("form submission stopped");
            });
            
        }
    else if(form[0].id=="commentForm")
        {  form[0].addEventListener("submit",event => {
            event.preventDefault();
            commentFormSubmission();
            console.log("form submission stopped");
            });
            
        }
}

function contactFormSubmission(){
  
    var values = {};
    var i = 0;
    $inputs = $("#contactForm :input");
    $inputs.each(function(){
        values[i] = $(this).val();
        i++;
    });
    
    if(values[0]!="")
        {
            $.ajax({
                    method: "POST",
                    url: "https://docs.google.com/forms/d/e/1FAIpQLSfnvfP8ZDVQ3u4gMj0LBgOl1IUqCsFydeoiM9qKC7-EPoJTCw/formResponse",
                    data: {
                        'entry.1988472699' : values[0],
                        'entry.1756766527' : values[1],
                        'entry.1114666575' : values[2],
                        'entry.644819668' : values[3],
                        'entry.2102364412' : values[4]
                    }
                }).done(function (){
                    console.log("contact form data sent to sheet");
                });        
        }
    
    window.location.reload();
    
    
}
    
function signupFormSubmission(){
  
    var values = {};
    var i = 0;
    $inputs = $("#signupForm :input");
    $inputs.each(function(){
        values[i] = $(this).val();
        i++;
    });
    
    if(values[0]!="")
        {
            $.ajax({
                    method: "POST",                   url:"https://docs.google.com/forms/d/e/1FAIpQLSelFqgjghJnO2aYa8ao6PiBMKTxV4nXDan38VQzhjYLJs2Kow/formResponse",
                    data: {
                        'entry.2055157495' : values[0],
                        'entry.891754708' : values[1],
                        'entry.644889342' : values[2],
                        
                    }
                }).done(function (){
                    console.log("contact form data sent to sheet");
                });        
        }
    
    window.location.reload();
    
}    

function subscriptionFormSubmission(){
  
    var values = {};
    var i = 0;
    $inputs = $("#subscriptionForm :input");
    $inputs.each(function(){
        values[i] = $(this).val();
        i++;
    });
    
    if(values[0]!="")
        {
            $.ajax({
                    method: "POST",
                    url:"https://docs.google.com/forms/d/e/1FAIpQLSfkqqy9Ue05J6D5sFj9PZzPtk9csGVCSJTe5IRwXRNi3z6rkA/formResponse",
                    data: {
                        'entry.1835715948' : values[0],
                        
                    }
                }).done(function (){
                    console.log("contact form data sent to sheet");
                });        
        }
    
        window.location.reload();
    
    
}

function commentFormSubmission(){
  
    var values = {};
    var i = 0;
    $inputs = $("#commentForm :input");
    $inputs.each(function(){
        values[i] = $(this).val();
        i++;
    });
    
    if(values[0]!="")
        {
            $.ajax({
                    method: "POST",                   url:"https://docs.google.com/forms/d/e/1FAIpQLSdEf8omkyz5n3SX2GPxoTRj_gqF4WallrHVoMfdT1MtPCDEmA/formResponse",
                    data: {
                        'entry.206934621' : values[0],
                        'entry.1217717410' : values[1],
                        'entry.251042345' : values[2],
                        'entry.930951112' : $(".blog-heading").text(),
                        
                    }
                }).done(function (){
                    console.log("contact form data sent to sheet");
                });        
        }
    
    window.location.reload();
}

