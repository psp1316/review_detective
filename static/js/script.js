document.getElementById("productForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    var productLink = document.getElementById("productLink").value;
    var resultContainer = document.getElementById("resultContainer");

    // Show loading animation
    resultContainer.innerHTML = '<div class="loader"></div>';

    // Make an HTTP POST request to the server
    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ productLink: productLink })
    })
    .then(response => response.json())
    .then(data => {
        // Extract the sentiment result from the response
        var sentiment = data.sentiment;

        // Create a popup element
        var popup = document.createElement("div");
        popup.classList.add("popup");
        popup.innerHTML = "<p>" + sentiment + "</p>";

        // Append the popup element to the result container
        resultContainer.innerHTML = "";
        resultContainer.appendChild(popup);

        // Clear the product link input
        document.getElementById("productLink").value = "";

        // Hide the popup when user pastes a new URL
        document.getElementById("productLink").addEventListener("input", function() {
            resultContainer.innerHTML = "";
        });
    })
    .catch(error => {
        console.log("Error:", error);
        // Show error message
        resultContainer.innerHTML = "<p>An error occurred. Please try again later.</p>";
    });
});
