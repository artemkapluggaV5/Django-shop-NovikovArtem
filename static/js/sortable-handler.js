import { showSuccess, showError } from './notifications.js';

document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('sortable-container');
    if (!container) return;

    const updateUrl = container.getAttribute('data-url');
    const csrfToken = container.getAttribute('data-csrf');

    new Sortable(container, {
        animation: 150,
        handle: '.drag-handle',
        ghostClass: 'sortable-ghost',
        onEnd: function() {
            const order = Array.from(container.querySelectorAll('.item-sortable'))
                               .map(el => el.getAttribute('data-id'));

            fetch(updateUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ order: order })
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'ok') {
                    showSuccess('Порядок успешно сохранен!');
                } else {
                    showError(data.message);
                }
            })
            .catch(error => {
                console.error('Fetch error:', error);
                showError('Ошибка сети или сервера');
            });
        }
    });
});