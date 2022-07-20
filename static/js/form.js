console.log("Hey");

function submitUsername () {
    var userInput = d3.select("#username").property("value");

    d3.json("/get-info", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({
            name: userInput
        })
    }).then(resp => {
        console.log(resp["nameReceived"]);
    })
}