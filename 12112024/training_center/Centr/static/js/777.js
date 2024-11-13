// Получаем элемент логотипа
const logo = document.querySelector('.logo');

// Добавляем анимацию при наведении курсора
logo.addEventListener('mouseover', () => {
  logo.style.transform = 'scale(1.1)'; // Увеличивает размер логотипа
});

logo.addEventListener('mouseout', () => {
  logo.style.transform = 'scale(1)'; // Возвращает логотип в исходный размер
});