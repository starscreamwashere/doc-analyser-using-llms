const API_BASE_URL = "http://localhost:8000/api/v1/medical";

const MedicalAPI = {
    async analyze(file) {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch(`${API_BASE_URL}/analyze`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || "Failed to analyze document");
        }

        return await response.json();
    }
};