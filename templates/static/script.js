function startTrace() {
    fetch("/status")
        .then(response => response.json())
        .then(data => {
            document.getElementById("output").innerHTML =
                data.message + "<br>Status: " + data.status;
        });
}