// alert('Hello contact us page')



function contactUs(){

    var fname = document.getElementById('fname').value
    var lname = document.getElementById('lname').value
    var email = document.getElementById('email').value
    var confirmEmail = document.getElementById('confirm-email').value

    var subject = document.getElementById('subject').value
    var message = document.getElementById('my_message').value


    // validate all input fields
    if(fname == '' || lname == '' || email == '' || confirmEmail == '' || subject == '' || message == ''){
        
        alert('All fields are required')
        return
    }


    var data = {
        fname: fname,
        lname: lname,
        email: email,
        confirmEmail: confirmEmail,
        subject: subject,
        message: message
    }

    // display data
    console.log(data)

}