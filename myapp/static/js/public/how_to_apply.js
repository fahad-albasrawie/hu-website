

// show or hide btn
function showBtn(hidden_btn, show_btn){

    var hidden_btn1 = document.getElementById(hidden_btn);
    var show_btn1 = document.getElementById(show_btn);
    
    hidden_btn1.style.display = 'none';
    show_btn1.style.display = 'block';
}

function apply(hidden_btn, show_btn){
    var fullName = document.getElementById('fullname');
    var email_address = document.getElementById('email-address');
    var phone = document.getElementById('phone');
    var application = document.getElementById('Application');

    

    // check if the input fields are empty
    if(fullName.value === '' || email_address.value === '' || phone.value === '' || application.value === ''){
        alert('Please enter your full name');
        fullName.focus();
        return ;
    }else{
        showBtn(hidden_btn, show_btn)
        let data = {
            fullName: fullName.value,
            email_address: email_address.value,
            phone: phone.value,
            application: application.value
        }
    
        // Display the data
        console.log(data);
    
        // countDown()
    }

    
    


}

// Create a function that couts down to 5 seconds
function countDown(){
    var count = 5;
    var interval = setInterval(function(){
        console.log(count);
        count--;
        if(count === 0){
            console.log('Submitted');
            clearInterval(interval);
        }
    }, 1000);

    var hidden_btn = document.getElementById('apply_me');
    var show_btn = document.getElementById('applying');

    hidden_btn.style.display = 'block';
    show_btn.style.display = 'none';

    console.log('Application submitted');
}