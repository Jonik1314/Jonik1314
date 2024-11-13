const openPdfButton = document.getElementById("openPdf");

    openPdfButton.addEventListener("click", function() {
      window.open("Centr/static/pdf_files/4234345.pdf", "_blank"); // Замените "4234345.pdf" на путь к вашему PDF-файлу
    });