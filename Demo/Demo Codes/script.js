// Access element by ID for updating prediction boxes
var textModelBoxes = document.getElementById("text-model-boxes");

function updatePredictionBoxes(data) {
  if (!data) {
    textModelBoxes.innerHTML = '<p>No prediction data received.</p>';
    return; // Exit if no data
  }

  
  var prediction = data.prediction; // Assuming data is the response object

  // Update innerHTML with prediction values (adjust indices if needed)
  textModelBoxes.innerHTML = `
  <div class="prediction-section" id="text-model">
    <div id="text-model-boxes">
      <div class="prediction-box">
        <p><span class="math-inline">${(prediction[0] * 100).toFixed(2)}%</p\>
        <p>Real</p>
      </div>
      <div class="prediction-box">
        <p>${(prediction[1] * 100).toFixed(2)}%</p>
        <p>Fake</p>
      </div>
    </div>
    <div class="prediction-box">
        <p>${(prediction[2] * 100).toFixed(2)}%</p>
        <p>Undecided</p>
      </div>
    </div>
  </div>
  `;

  
  console.log("Prediction Real:", prediction[0]); // Assuming index 0 might be real
  console.log("Prediction Fake:", prediction[1]); // Assuming index 1 might be fake
  console.log("Prediction Fake:", prediction[2]); // Assuming index 1 might be fake


}


function predict() {
  var textInput = document.querySelector("#textInput").value;

  var data = {
    text: textInput
  };

  fetch("http://127.0.0.1:5000/predict", {  // Update URL with correct Flask endpoint
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    console.log(data); // Log the response data for debugging
    updatePredictionBoxes(data);
  })
  .catch(error => {
    console.error("Error:", error);
    updatePredictionBoxes(null); // Display error message
  });
}


// Call predict function (optional, can be called on a button click)
// predict(); // Uncomment to automatically run on page load
