export function submit(e, url, redirect_url) {
    const data = new FormData();
    e.preventDefault();
    const inputs = document.querySelectorAll('input');
    inputs.forEach((input) => {
       data.append(input.name,input.value);
    });
    const area = document.querySelector('textarea');
    data.append(area.name, area.value);
    try {
        console.log(data)
        fetch(window.location.pathname, { method: 'post', body: data }).then(() => {
            window.location = redirect_url;
        });
    } catch (error) {

    }
}