document.addEventListener("DOMContentLoaded", () => {
  const tableBody = document.querySelector(".data-table tbody");
  const deleteModal = document.getElementById("confirmModal");
  const viewModal = document.getElementById("viewModal");
  const confirmBtn = document.getElementById("confirmDelete");
  const cancelBtn = document.getElementById("cancelDelete");
  const closeViewBtn = document.getElementById("closeView");

  const viewName = document.getElementById("viewName");
  const viewPermitType = document.getElementById("viewPermitType");
  const viewDate = document.getElementById("viewDate");
  const viewAddress = document.getElementById("viewAddress");
  const viewTrees = document.getElementById("viewTrees");
  const viewReason = document.getElementById("viewReason");
  const viewDocuments = document.getElementById("viewDocuments");

  let rowToDelete = null;

  function loadApplications() {
    tableBody.innerHTML = "";

    Object.keys(localStorage).forEach((key) => {
      if (key.startsWith("application_")) {
        try {
          const app = JSON.parse(localStorage.getItem(key));
          const row = document.createElement("tr");

          row.innerHTML = `
            <td>${app.name || ""}</td>
            <td>${app.permitType || ""}</td>
            <td>${app.date || ""}</td>
            <td>
              <button class="btn-action view">View</button>
              <button class="btn-action delete">Delete</button>
            </td>
          `;
          row.dataset.key = key;
          tableBody.appendChild(row);
        } catch (err) {
          console.warn("Invalid JSON in localStorage key:", key);
        }
      }
    });
  }

  // Handle view and delete buttons
  tableBody.addEventListener("click", (e) => {
    const row = e.target.closest("tr");
    if (!row) return;
    const key = row.dataset.key;
    if (!key) return;

    if (e.target.classList.contains("delete")) {
      rowToDelete = row;
      deleteModal.style.display = "flex";
    }

    if (e.target.classList.contains("view")) {
      try {
        const app = JSON.parse(localStorage.getItem(key));
        viewName.textContent = app.name || "";
        viewPermitType.textContent = app.permitType || "";
        viewDate.textContent = app.date || "";
        viewAddress.textContent = app.address || "N/A";
        viewTrees.textContent = app.trees || "N/A";
        viewReason.textContent = app.reason || "N/A";

        // Display uploaded images
        viewDocuments.innerHTML = "";
        if (app.documents && app.documents.length) {
          app.documents.forEach((dataURL, index) => {
            const img = document.createElement("img");
            img.src = dataURL;
            img.alt = `Document ${index + 1}`;
            img.style.maxWidth = "100px";
            img.style.margin = "5px";
            img.style.border = "1px solid #ccc";
            img.style.borderRadius = "8px";
            viewDocuments.appendChild(img);
          });
        } else {
          viewDocuments.innerHTML = "<em>No documents uploaded.</em>";
        }

        viewModal.style.display = "flex";
      } catch (error) {
        alert("⚠️ Failed to load application data.");
        console.error("View error:", error);
      }
    }
  });

  // Confirm deletion
  confirmBtn.addEventListener("click", () => {
    if (rowToDelete) {
      const key = rowToDelete.dataset.key;
      localStorage.removeItem(key);
      rowToDelete.remove();
      rowToDelete = null;
    }
    deleteModal.style.display = "none";
  });

  // Cancel deletion
  cancelBtn.addEventListener("click", () => {
    rowToDelete = null;
    deleteModal.style.display = "none";
  });

  // Close the view modal
  closeViewBtn.addEventListener("click", () => {
    viewModal.style.display = "none";
  });

  // Load all saved applications on startup
  loadApplications();
});
