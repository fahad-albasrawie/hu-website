// document.addEventListener('DOMContentLoaded', function () {
//   const dropdown = document.querySelector('.nav-item.dropdown');
//   const dropdownMenu = dropdown.querySelector('.dropdown-menu');

//   dropdown.addEventListener('mouseenter', function () {
//       dropdown.classList.add('show');
//       dropdownMenu.classList.add('show');
//       dropdown.setAttribute('aria-expanded', 'true');
//   });

//   dropdown.addEventListener('mouseleave', function () {
//       dropdown.classList.remove('show');
//       dropdownMenu.classList.remove('show');
//       dropdown.setAttribute('aria-expanded', 'false');
//   });
// });


// ====================================== Tiny Script ==============================
tinymce.init({
    selector: 'textarea#article',
    spellchecker_dialog: false,
    browser_spellcheck: false,
    height: 560,
    plugins: [
        'advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak',
        'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime',
        'media', 'table', 'emoticons', 'template', 'help'
    ],
    toolbar: 'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | ' +
        'bullist numlist outdent indent | link image | print preview media fullscreen | ' +
        'forecolor backcolor emoticons | help',
    menu: {
        favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
    },
    menubar: 'favs file edit view insert format tools table help',
    content_css: 'css/content.css',
    
     // Load your custom CSS here (relative path or full URL)
     content_css: "{{url_for('static', filename='css/public/news_layout.css')}}",

    // Add responsive class when inserting images
    image_class_list: [
        { title: 'Responsive', value: 'responsive-image' },
        { title: 'VResponsive', value: 'ytp-cued-thumbnail-overlay-image' },

    ],
    setup: function (editor) {
        editor.on('NodeChange', function (e) {
            if (e && e.element.nodeName.toLowerCase() === 'img') {
                e.element.classList.add('responsive-image');
            }
        });
    }
});

// ====================================== Tiny Script ==============================

// show or hide btn
function showHideBtn(hidden_btn, show_btn) {
    document.getElementById(hidden_btn).style.display = 'none';
    document.getElementById(show_btn).style.display = 'block';

} // End of showHideBtn

function subscribe_me(hidden_btn, show_btn) {

    var email = document.getElementById('email-field').value;
    var full_name = document.getElementById('full_name-field').value;
    var number = document.getElementById('number-field').value;

    var info_message = document.getElementById('info_message');
    var success_message = document.getElementById('success_message');
    var error_message = document.getElementById('error_message');


    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentHour = currentDate.getHours();
    const currentMinutes = currentDate.getMinutes();


    // Make the date and time in the standard format and save in variable like this format "2021-09-01 12:00:00"
    const standardDateTime = `${currentYear}-${currentDate.getMonth() + 1}-${currentDate.getDate()} ${currentHour}:${currentMinutes}`;

    // Convert data into obj
    data = {
        email: email,
        full_name: full_name,
        number: number,
        my_date: standardDateTime
    }


    console.log('Here is the subcribltion data...:', data)

    showHideBtn(hidden_btn, show_btn)
    
    info_message.style.display = 'none'
    success_message.style.display = 'none'
    error_message.style.display = 'none'


    fetch('/register_subscriber',
        {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(data),
            cache: 'no-cache',
            headers: new Headers({
                'content-type': 'application/json'
            })

        })
        // Then do something other withe respond...
        .then(function (response) {
            if (response.status != 200) {
                console.log('There was aproblem while sending data')
                console.log(`Response status were not 200: ${response.status}`);
                error_message.style.display = 'block'
                error_message.innerHTML = 'Qalad baa dhacay, fadlan hubi qadkaaga ama mar kale isku day!'
                showHideBtn(show_btn, hidden_btn)
                return;
            }
            response.json().then(function (data) {
                // This is the message from Python
                console.log('Fiiri xogta la soo celiyey:')
                console.log(data)

                if (data['status'] == 'success') {

                    console.log('You are logged in...')
                    // Redirect to admin dashboard
                    showHideBtn(show_btn, hidden_btn)
                    success_message.innerHTML = data['message'];
                    success_message.style.display = 'block'
                    return;

                } else if (data['status'] == 'error') {
                    showHideBtn(show_btn, hidden_btn)
                    error_message.innerHTML = data['message'];
                    error_message.style.display = 'block'

                }else {
                    showHideBtn(show_btn, hidden_btn)
                    info_message.innerHTML = data['message'];
                    info_message.style.display = 'block'

                }

            })
        })// End of then

}