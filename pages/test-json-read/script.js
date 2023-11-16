function loadJSON() {
    fetch('data.json')
      .then(response => response.json())
      .then(data => {
        const contentDiv = document.getElementById('content');
        contentDiv.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
      })
      .catch(error => {
        console.error('An error occurred:', error);
      });
  }
  