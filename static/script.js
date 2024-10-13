document.getElementById('recommendation-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const courseInput = document.getElementById('course').value; // Get the course name
    const recommendationsDiv = document.getElementById('recommendations');

    // Clear previous recommendations
    recommendationsDiv.innerHTML = '';

    // Send a POST request to the Flask server
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ course: courseInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.length > 0 && data[0] !== 'No recommendation available') {
            data.forEach(course => {
                const recommendationItem = document.createElement('div');
                recommendationItem.className = 'recommendation-item';
                recommendationItem.textContent = course;
                recommendationsDiv.appendChild(recommendationItem);
            });
        } else {
            const noRecommendationItem = document.createElement('div');
            noRecommendationItem.className = 'recommendation-item';
            noRecommendationItem.textContent = 'No recommendations available.';
            recommendationsDiv.appendChild(noRecommendationItem);
        }
    })
    .catch(error => {
        console.error('Error fetching recommendations:', error);
        const errorItem = document.createElement('div');
        errorItem.className = 'recommendation-item';
        errorItem.textContent = 'An error occurred while fetching recommendations.';
        recommendationsDiv.appendChild(errorItem);
    });
});
