function saveData() {
    // Collect the data from the form inputs
    const age = document.getElementById('age').value;
    const interests = document.getElementById('interests').value;
    const formality = document.getElementById('formality').value;
    const humor = document.getElementById('humor').value;
    const positivity = document.getElementById('positivity').value;
    const visuals = document.querySelector('input[name="visuals"]:checked')?.value === 'true';
    const language = document.querySelector('input[name="language"]:checked')?.value === 'true';
    const speech = document.querySelector('input[name="speech"]:checked')?.value === 'true';

    // Create a JavaScript object to store the data
    const data = {
        age: age,
        interests: interests,
        formality: formality,
        humor: humor,
        positivity: positivity,
        visuals: visuals,
        language: language,
        speech: speech,
    };

    // Convert the data object to a JSON string
    const jsonData = JSON.stringify(data);

    // Create a Blob object from the JSON string
    const blob = new Blob([jsonData], { type: 'application/json' });

    // Create a download link and trigger the download
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'data.json';  // The name of the downloaded file

    // Append the link to the body (required for Firefox)
    document.body.appendChild(link);

    // Programmatically click the link
    link.click();

    // Remove the link after download (cleanup)
    document.body.removeChild(link);
}
