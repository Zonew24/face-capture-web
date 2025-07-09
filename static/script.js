const video = document.getElementById('video');
const canvas = document.createElement('canvas');
const capturedImages = {};

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => video.srcObject = stream);

function capture(angle) {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext('2d').drawImage(video, 0, 0);
  capturedImages[angle] = canvas.toDataURL('image/jpeg');
  alert(`Đã chụp góc: ${angle}`);
}

document.getElementById('faceForm').onsubmit = function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  for (let angle in capturedImages) {
    formData.append(angle, capturedImages[angle]);
  }

  fetch('/upload', {
    method: 'POST',
    body: formData
  }).then(res => res.text())
    .then(msg => alert(msg));
};
