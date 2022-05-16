export function submit(e, url, redirect_url) {
    const data = new FormData();
    e.preventDefault();
    const inputs = document.querySelectorAll('input');
    inputs.forEach((input) => {
        data.append(input.name, input.value);
    });
    const select = document.querySelector('#id_gender');
    data.append(select.name, select.value);
    try {

        fetch(url, { method: 'post', body: data }).then(async (e) => {
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
            } else {
                window.location = window.location.pathname;
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