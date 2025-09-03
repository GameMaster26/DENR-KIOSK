document.addEventListener('DOMContentLoaded', () => {
  const list = document.querySelector('.feedback-list');
  const modal = document.getElementById('modalBox');
  const modalMessage = document.getElementById('modalMessage');
  const responseBox = document.getElementById('responseBox');
  const modalConfirm = document.getElementById('modalConfirm');
  const modalCancel = document.getElementById('modalCancel');
  const confirmationBox = document.getElementById('confirmationBox');

  let storedFeedback = JSON.parse(localStorage.getItem('penro_feedback') || '[]');
  let currentAction = '';
  let currentIndex = null;

  const ratingLabels = ['Very Poor', 'Poor', 'Average', 'Good', 'Excellent'];

  function renderFeedback() {
    list.innerHTML = '';

    if (storedFeedback.length === 0) {
      list.innerHTML = '<li>No feedback yet.</li>';
    } else {
      // Reverse without mutating the original array
      const reversedFeedback = [...storedFeedback].reverse();

      reversedFeedback.forEach((entry, reversedIndex) => {
        const originalIndex = storedFeedback.length - 1 - reversedIndex;
        const li = document.createElement('li');
        li.classList.add('feedback-item');

        const numRating = parseInt(entry.rating);
        const stars = '★'.repeat(numRating) + '☆'.repeat(5 - numRating);
        const label = ratingLabels[numRating - 1] || '';

        li.innerHTML = `
          <strong>${entry.name}</strong><br>
          <small>"${entry.message}"</small><br>
          <div class="star-display">
            <span class="star">${stars}</span> 
            <small class="star-label">(${label})</small>
          </div>
          <button class="btn-action respond-btn" data-index="${originalIndex}">Respond</button>
          <button class="btn-action delete-btn" data-index="${originalIndex}">Delete</button>
        `;

        list.appendChild(li);
      });

      // Attach event listeners
      document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          currentIndex = parseInt(btn.dataset.index);
          currentAction = 'delete';
          modalMessage.textContent = 'Are you sure you want to delete this feedback?';
          responseBox.style.display = 'none';
          modal.style.display = 'flex';
        });
      });

      document.querySelectorAll('.respond-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          currentIndex = parseInt(btn.dataset.index);
          currentAction = 'respond';
          modalMessage.textContent = `Write your response to ${storedFeedback[currentIndex].name}:`;
          responseBox.style.display = 'block';
          responseBox.value = '';
          modal.style.display = 'flex';
        });
      });
    }
  }

  modalConfirm.addEventListener('click', () => {
    modal.style.display = 'none';

    if (currentAction === 'delete') {
      storedFeedback.splice(currentIndex, 1);
      localStorage.setItem('penro_feedback', JSON.stringify(storedFeedback));
      showConfirmation('Feedback deleted successfully.');
      renderFeedback();
    } else if (currentAction === 'respond') {
      const reply = responseBox.value.trim();
      if (reply) {
        showConfirmation(`Response sent: "${reply}"`);
        // You can save responses in future implementation
      } else {
        showConfirmation('Response was empty. Nothing sent.');
      }
    }

    currentIndex = null;
    currentAction = '';
  });

  modalCancel.addEventListener('click', () => {
    modal.style.display = 'none';
  });

  function showConfirmation(msg) {
    confirmationBox.textContent = msg;
    confirmationBox.style.display = 'block';
    setTimeout(() => {
      confirmationBox.style.display = 'none';
    }, 3000);
  }

  renderFeedback();
});
