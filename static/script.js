// Basic event handlers for the buttons on the webpage.
// Set all of this once the page has loaded.
$(document).ready(function(){
    $( "#successAlert" ).hide()
    // A function to clear all fields and hide the alert zones.
        var clearData = function() {
        $(  "#errorAlert"  ).hide()
        $( "#successAlert" ).hide()
        $(   "#firstName"  ).val("")
        $(   "#lastName"   ).val("")
        $( "#registerCode" ).val("")
    }
    // Start the page with all the data clean and the message alerts hidden.
    clearData()
    // Make a POST request when clicking on "Register" button.
    $( "#register" ).bind('click', function() {
        var firstName =    $( "#firstName"    ).val()
        var lastName =     $( "#lastName"     ).val()
        var registerCode = $( "#registerCode" ).val()
        // The three values sent to the server in a JSON string at the data
        // field of the request body will be the first name, last name, and
        // the one-time use code.
        $.post("/register", {
            data: JSON.stringify({
                firstName: firstName,
                lastName: lastName,
                code: registerCode
            })
        }).done(function(data) {
        // If some data was returned, then something must've happened, so
        // display the errorAlert div and display the returned data on it. 
            if(data != null && data != "") {
                $( "#successAlert" ).hide()
                $(  "#errorAlert"  ).show()
                $(  "#errorAlert"  ).html(data)
            } else {
                clearData()
                $( "#successAlert" ).show()
                setTimeout(function() {
                    location.reload()
                }, 3000)
            }
        })
    })
    // Bind the clearData function to the Clear button. 
    $( "#clear" ).bind('click', clearData)	
})
