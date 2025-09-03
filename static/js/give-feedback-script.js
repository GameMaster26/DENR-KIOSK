document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('feedbackForm');
  const msgBox = document.getElementById('feedback-msg');
  const ratingInput = document.getElementById('rating');
  const ratingLabel = document.getElementById('ratingLabel');
  const stars = document.querySelectorAll('#starRating .fa-star');
  const labels = ['Very Poor', 'Poor', 'Average', 'Good', 'Excellent'];

  // STAR RATING LOGIC
  stars.forEach(star => {
    star.addEventListener('mouseover', () => {
      const value = parseInt(star.dataset.value);
      updateStars(value, 'hover');
    });

    star.addEventListener('mouseout', () => {
      const current = parseInt(ratingInput.value) || 0;
      updateStars(current, 'selected');
    });

    star.addEventListener('click', () => {
      const value = parseInt(star.dataset.value);
      ratingInput.value = value;
      ratingLabel.textContent = labels[value - 1];
      updateStars(value, 'selected');
    });
  });

  function updateStars(value, className) {
    stars.forEach(star => {
      const starValue = parseInt(star.dataset.value);
      star.classList.remove('hover', 'selected');
      if (starValue <= value) {
        star.classList.add(className);
      }
    });
  }

  // FEEDBACK SUBMISSION LOGIC
  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const name = form.name.value.trim();
    const message = form.message.value.trim();
    const rating = form.rating.value;

    if (!name || !message || !rating) {
      showMessage('Please fill in all fields.', 'error');
      return;
    }

    const feedbackData = {
      name,
      message,
      rating: `${rating} Star${rating > 1 ? 's' : ''}`,
      timestamp: new Date().toISOString()
    };

    const existing = JSON.parse(localStorage.getItem('penro_feedback') || '[]');
    existing.push(feedbackData);
    localStorage.setItem('penro_feedback', JSON.stringify(existing));

    showMessage('Thank you! Your feedback has been submitted.', 'success');
    form.reset();
    updateStars(0, 'selected');
    ratingLabel.textContent = 'Select a rating';
  });

  function showMessage(text, type) {
    msgBox.textContent = text;
    msgBox.className = `status-msg ${type}`;
    msgBox.style.display = 'block';
  }
});
