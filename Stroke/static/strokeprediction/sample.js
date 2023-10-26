function stroke_prediction() {

    let val = Math.floor(Math.random() * 51) + 30;

    document.getElementById("pred").innerText =  val; 
    // csrf cookie
    const csrftoken = Cookies.get('csrftoken');

    try {
        fetch("/predict_stroke",{
            method: 'POST',
            headers: {
                'X-CSRFToken':csrftoken
            },
            body: JSON.stringify({
                input:val
            })
        })
        .then(response => response.json())
        .then(response => {
            
            // console.log(response);
    
        });
    } finally {
        return false;
    }

}