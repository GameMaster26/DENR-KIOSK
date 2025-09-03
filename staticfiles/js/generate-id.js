function generateUserID() {
  const now = new Date();
  const yyyymmdd = now.toISOString().slice(0, 10).replace(/-/g, '');
  const random = Math.floor(Math.random() * 900 + 100);
  const userId = `USER-${yyyymmdd}${random}`;
  document.getElementById('username').value = userId;
}

function generateAdminID() {
  const now = new Date();
  const yyyymmdd = now.toISOString().slice(0, 10).replace(/-/g, '');
  const random = Math.floor(Math.random() * 900 + 100);
  const adminId = `ADMIN-${yyyymmdd}${random}`;
  document.getElementById('username').value = adminId;
}
