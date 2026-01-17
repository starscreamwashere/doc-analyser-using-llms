const fileInput = document.getElementById('fileInput');
const fileNameDisplay = document.getElementById('fileNameDisplay');
const analyzeBtn = document.getElementById('analyzeBtn');
const loader = document.getElementById('loader');
const resultDiv = document.getElementById('result');
const analysisContent = document.getElementById('analysisContent');

// Show filename when selected
fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        fileNameDisplay.innerText = `Selected: ${e.target.files[0].name}`;
    }
});

// Handle Analysis
analyzeBtn.addEventListener('click', async () => {
    const file = fileInput.files[0];
    if (!file) {
        alert("Please select a medical report PDF first.");
        return;
    }

    // UI State: Loading
    analyzeBtn.disabled = true;
    loader.style.display = "block";
    resultDiv.style.display = "none";

    try {
        const data = await MedicalAPI.analyze(file);
        
        // UI State: Success
        analysisContent.innerText = data.analysis;
        resultDiv.style.display = "block";
    } catch (error) {
        alert(`Error: ${error.message}`);
    } finally {
        // UI State: Reset
        analyzeBtn.disabled = false;
        loader.style.display = "none";
    }
});