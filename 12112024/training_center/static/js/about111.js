const rows = document.querySelectorAll('.row');

    rows.forEach(row => {
        row.addEventListener('click', () => {
            const target = row.dataset.target;
            const content = document.getElementById(target);

            if (content.classList.contains('show')) {
              content.classList.remove('show');
            } else {
              // Скрыть другие открытые блоки
              const openContents = document.querySelectorAll('.content.show');
              openContents.forEach(openContent => openContent.classList.remove('show'));

              content.classList.add('show');
        }
      });
    });