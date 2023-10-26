function strokeprediction() {

    let inputs = [
        document.forms['prediction_form']['gender'].value,
        document.forms['prediction_form']['work'].value,
        document.forms['prediction_form']['age'].value,
        document.forms['prediction_form']['residence'].value,
        document.forms['prediction_form']['hypetension'].value,
        document.forms['prediction_form']['agl'].value,
        document.forms['prediction_form']['heart'].value,
        document.forms['prediction_form']['bmi'].value,
        document.forms['prediction_form']['married'].value,
        document.forms['prediction_form']['smoking'].value,
    ];

    // csrf cookie
    const csrftoken = Cookies.get('csrftoken');

    fetch('/predictstroke',{
        method: 'POST',
        headers: {
            'X-CSRFToken':csrftoken
        },
        body: JSON.stringify({
            input   : inputs
        })
    })
    .then(response => response.json())
    .then(response => {
        
        document.getElementById("pred").innerText = response.results;

    });
}