// view-script.js
document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector(".status-form");
  const infoBox = document.getElementById("applicantInfo");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const input = document.getElementById("applicantId").value.trim().toLowerCase();
    const data = localStorage.getItem(`application_${input}`);

    if (!data) {
      alert("Application not found. Please check your name or ID.");
      infoBox.style.display = "none";
      return;
    }

    const app = JSON.parse(data);
    document.getElementById("infoName").textContent = app.name;
    document.getElementById("infoType").textContent = app.permitType;
    document.getElementById("infoDate").textContent = app.date;
    document.getElementById("infoStatus").textContent = app.status;
    document.getElementById("infoRemarks").textContent = app.remarks;

    infoBox.style.display = "block";
  });
});
