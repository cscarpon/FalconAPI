async function sendPrompt() {
    let prompt = document.getElementById("prompt").value;
    
    let response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: prompt })
    });

    let data = await response.json();
    document.getElementById("response").innerText = data.response;
}
