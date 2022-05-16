let tblClient;

function getData() {
    tblClient = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "id" },
            { "data": "names" },
            { "data": "surnames" },
            { "data": "dni" },
            { "data": "date_birthday" },
            { "data": "gender" },
            { "data": "id" },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" class="btn btn-warning btn-xs btn-flat update-client" rel="edit"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat delete-client" rel="delete"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            const button_add = document.querySelectorAll('.update-client');
            const button_delete = document.querySelectorAll('.delete-client');
            button_add.forEach((b) => {
                b.addEventListener('click', (e) => {
                    const modal = document.getElementById('myModalClient');
                    modal.classList.toggle('show');
                    modal.style.display = 'block';
                });
            });
            button_delete.forEach((b) => {
                b.addEventListener('click', (e) => {
                    const modal = document.getElementById('myModalClientDelete');
                    modal.classList.toggle('show');
                    modal.style.display = 'block';
                });
            })
        }
    });
}

$(function () {
    getData()

    $('#data tbody').on('click', 'a[rel="edit"]', function () {
        var tr = tblClient.cell($(this).closest('td, li')).index();
        var data = tblClient.row(tr.row).data();
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="names"]').val(data.names);
        $('input[name="surnames"]').val(data.surnames);
        $('input[name="dni"]').val(data.dni);
        $('input[name="date_birthday"]').val(data.date_birthday);
        $('input[name="direccion"]').val(data.direccion);
        $('select[name="gender"]').val(data.gender);
    });

    $('#data tbody').on('click', 'a[rel="delete"]', function () {
        var tr = tblClient.cell($(this).closest('td, li')).index();
        var data = tblClient.row(tr.row).data();
        $('input[name="action"]').val('delete');
        $('input[name="id"]').val(data.id);
    });

});