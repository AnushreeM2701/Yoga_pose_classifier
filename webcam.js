const video = document.getElementById('webcam');
const resultText = document.getElementById('result');

// Start webcam
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => {
    console.error("Error accessing webcam:", err);
  });

function capture() {
  resultText.innerText = "⏳ Capturing in 5 seconds...";
  setTimeout(() => {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);

    const imageData = canvas.toDataURL('image/jpeg');

    fetch('/predict-webcam', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ image: imageData })
    })
    .then(response => response.json())
    .then(data => {
      resultText.innerText = `🧘 Predicted Pose: ${data.pose} (${data.confidence}%)`;
    })
    .catch(err => {
      console.error(err);
      resultText.innerText = "❌ Error predicting pose.";
    });
  }, 5000);
}
