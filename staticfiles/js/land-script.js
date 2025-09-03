document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("treePermitForm");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("fullname").value.trim();
    const address = document.getElementById("address").value.trim();
    const trees = document.getElementById("trees").value.trim();
    const reason = document.getElementById("reason").value.trim();
    const date = new Date().toISOString().split("T")[0];
    const files = document.getElementById("documents").files;

    const documents = await convertFilesToBase64(files);

    const application = {
      name,
      address,
      trees,
      reason,
      permitType: "Tree Cutting",
      date,
      documents
    };

    const key = "application_" + Date.now();
    localStorage.setItem(key, JSON.stringify(application));
    alert("✅ Application submitted successfully!");
    form.reset();
  });

  // Helper function to convert FileList to base64 array
  async function convertFilesToBase64(fileList) {
    const base64Array = [];
    for (let file of fileList) {
      const base64 = await new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = () => reject("Failed to read file");
        reader.readAsDataURL(file);
      });
      base64Array.push(base64);
    }
    return base64Array;
  }
});
