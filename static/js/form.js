export function submit(e, url, redirect_url) {
    const data = new FormData();
    e.preventDefault();
    const inputs = document.querySelectorAll('input');
    inputs.forEach((input) => {
        if (input.name === 'image') {
            var blobURL = window.createBlobURL(input.files[0]);
            data.append(input.name, URL.createObjectURL(blobURL));
            window.revokeBlobURL(blobURL);
        } else
            data.append(input.name, input.value);
    });
    const area = document.querySelector('textarea');
    const select = document.querySelector('.select');
    if (area) data.append(area.name, area.value);
    if (select) data.append(select.name, select.value);
    try {
        fetch(url, { method: 'post', body: data }).then(async (e) => {
            const resp = await e.json();
            if (resp.hasOwnProperty('error')) {
                const alert = document.querySelector('.alert');
                alert.style.setProperty('display', 'block', 'important')
                const container = alert.children[1].children[0];
                Object.keys(resp['error']).forEach((key) => {
                    container.innerHTML += `<li>${resp['error'][key]}</li>`
                });
                setTimeout(() => alert.style.setProperty('display', 'none', 'important'), 3000)
                return false;
            }
        }).catch(async (e) => {
            const resp = await e.json();
            if (resp.hasOwnProperty('error')) {
                const alert = document.querySelector('.alert');
                alert.style.setProperty('display', 'block', 'important');
                const container = alert.children[1].children[0];
                Object.keys(resp['error']).forEach((key) => {
                    container.innerHTML += `<li>${resp['error'][key]}</li>`
                });
                setTimeout(() => alert.style.setProperty('display', 'none', 'important'), 3000)
                return false;
            }
        });
    } catch (error) {
        const alert = document.querySelector('.alert');
        console.log(alert)
    }
}