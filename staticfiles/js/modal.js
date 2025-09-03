function openConfirmationModal() {
  document.getElementById("confirmModal").classList.add("active");
}

function closeConfirmationModal() {
  document.getElementById("confirmModal").classList.remove("active");
}

function submitForm() {
  // Hide modal first
  closeConfirmationModal();

  // Submit the form
  document.getElementById("userForm").submit();
}

