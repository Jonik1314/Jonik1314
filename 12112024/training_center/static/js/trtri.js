const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        const overlay = card.querySelector('.overlay');
        const button = card.querySelector('.overlay-content button');
        const link = card.dataset.link;

        card.addEventListener('mouseover', () => {
            overlay.classList.add('active');
        });

        card.addEventListener('mouseout', () => {
            overlay.classList.remove('active');
        });

        button.addEventListener('click', () => {
            window.location.href = link;
        });
    });