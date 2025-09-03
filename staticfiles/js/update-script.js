document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('statusForm');
  const message = document.getElementById('status-message');
  const notification = document.getElementById('user-notification');

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const userId = form.userId.value.trim();
    const status = form.status.value;
    const comment = form.comment.value.trim();

    if (!userId || !status) {
      showMessage('Please fill in all required fields.', 'error');
      return;
    }

    // Simulate updating status
    const feedback = `
      ✅ <strong>${userId}</strong> status updated to <strong>${status.toUpperCase()}</strong>.<br/>
      ${comment ? 'Comment: ' + comment : ''}
    `;
    showMessage(feedback, 'success');

    // Simulate user notification
    showNotification(`${userId} has been notified of the status update.`);

    form.reset();
  });

  function showMessage(text, type) {
    message.innerHTML = text;
    message.className = `status-msg ${type}`;
    message.style.display = 'block';
  }

  function showNotification(text) {
    notification.textContent = text;
    notification.style.display = 'block';
    notification.classList.add('visible');

    setTimeout(() => {
      notification.classList.remove('visible');
    }, 4000); // Auto-hide after 4 seconds
  }
});
