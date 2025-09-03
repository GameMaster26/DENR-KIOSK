document.addEventListener('DOMContentLoaded', () => {
  const submissionList = document.querySelector('.submission-list');

  if (!submissionList) return;

  submissionList.addEventListener('click', function (e) {
    const button = e.target.closest('button');
    if (!button) return;

    const listItem = button.closest('li');
    if (!listItem) return;

    if (button.classList.contains('approve')) {
      handleApprove(listItem);
    } else if (button.classList.contains('reject')) {
      showRejectConfirmation(listItem);
    } else if (button.classList.contains('confirm-reject')) {
      handleReject(listItem);
    } else if (button.classList.contains('cancel-reject')) {
      removeRejectBox(listItem);
    } else if (button.classList.contains('request')) {
      showRequestForm(listItem);
    } else if (button.classList.contains('submit-request')) {
      submitRequestInfo(listItem);
    }
  });

  function handleApprove(item) {
    item.style.backgroundColor = '#e8f5e9';
    setStatusMessage(item, '✅ Approved');
  }

  function showRejectConfirmation(item) {
    if (item.querySelector('.reject-box')) return; // Avoid duplicate

    const box = document.createElement('div');
    box.className = 'reject-box';
    box.innerHTML = `
      <p>Are you sure you want to reject this submission?</p>
      <button class="btn-action confirm-reject">Yes, Reject</button>
      <button class="btn-action cancel-reject">Cancel</button>
    `;
    item.appendChild(box);
  }

  function handleReject(item) {
    item.style.backgroundColor = '#ffebee'; // soft red
    setStatusMessage(item, '❌ Rejected');
    removeRejectBox(item);
  }

  function removeRejectBox(item) {
    const box = item.querySelector('.reject-box');
    if (box) box.remove();
  }

  function showRequestForm(item) {
    if (item.querySelector('.request-form')) return;

    const form = document.createElement('div');
    form.className = 'request-form';
    form.innerHTML = `
      <input type="text" class="info-input" placeholder="Enter required info..." />
      <button class="btn-action submit-request">Submit Info</button>
    `;
    form.style.marginTop = '10px';

    item.appendChild(form);
  }

  function submitRequestInfo(item) {
    const input = item.querySelector('.info-input');
    if (!input || !input.value.trim()) {
      alert('Please enter the information needed.');
      return;
    }

    const info = input.value.trim();
    item.style.backgroundColor = '#fffde7'; // light yellow
    setStatusMessage(item, `📩 Info Requested: ${info}`);

    const form = item.querySelector('.request-form');
    if (form) form.remove();
  }

  function setStatusMessage(item, message) {
    let status = item.querySelector('.status-msg');
    if (!status) {
      status = document.createElement('div');
      status.className = 'status-msg';
      status.style.marginTop = '8px';
      status.style.fontSize = '14px';
      status.style.color = '#333';
      item.appendChild(status);
    }
    status.textContent = message;
  }
});
