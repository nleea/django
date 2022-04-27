(function () {
    let table = new DataTable('#data', {
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search'
            }, // parametros
            dataSrc: ""
        },
        columns: [
            { "data": "id" },
            { "data": "nombre" },
            { "data": "desc" },
            { "data": "desc" },
        ],
        columnDefs: [
            {
                targets: [3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return (
                        `<td>
                        <a href=${'/erp/category/edit/' + row.id + '/'} class="btn btn-primary p-1">
                            <i class="bi bi-pencil-square"></i>
                        </a>
                        <a class="btn btn-danger p-1" href=${'/erp/category/delete/' + row.id}><i class="bi bi-trash"></i></a>
                    </td>`
                    );
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
})();