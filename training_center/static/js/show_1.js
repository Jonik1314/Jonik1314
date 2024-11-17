// Функция для отображения содержимого
function showContent(targetId) {
    document.querySelectorAll('.content_a').forEach(el => {
        el.style.display = 'none';
        });

    document.getElementById(targetId).style.display = 'block';
    }