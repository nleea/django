const closeButton = document.querySelectorAll('.closeButton');
const closeButtonDelete = document.querySelectorAll('.closeButtonDelete');


function close(e) {
    const modal = document.getElementById('myModalClient');
    modal.classList.toggle('show');
    modal.style.display = 'none';
}

function closeDelete(){
    const modal = document.getElementById('myModalClientDelete');
    modal.classList.toggle('show');
    modal.style.display = 'none';
}

closeButton.forEach((e) => {
    e.addEventListener('click', close);
});

closeButtonDelete.forEach((e) => {
    e.addEventListener('click', closeDelete);
});

function message_error(obj) {
    var html = '';
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    }
    else {
        html = '<p>' + obj + '</p>';
    }
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}