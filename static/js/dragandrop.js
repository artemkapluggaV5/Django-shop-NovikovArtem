document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('sortable-container');
    if (!container) return;

    const notyf = new Notyf({
        duration: 3000,
        position: { x: 'right', y: 'bottom' },
    });

    const updateUrl = container.getAttribute('data-url');
    const csrfToken = container.getAttribute('data-csrf');

    new Sortable(container, {
        animation: 150,
        handle: '.drag-handle',
        ghostClass: 'sortable-ghost',
        onEnd: function() {
            let order = [];
            container.querySelectorAll('.item-sortable').forEach(function(el) {
                order.push(el.getAttribute('data-id'));
            });

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
                    notyf.success('Порядок успешно сохранен!');
                } else {
                    notyf.error('Ошибка: ' + (data.message || 'не удалось сохранить'));
                }
            })
            .catch(error => {
                notyf.error('Ошибка сети или сервера');
            });
        }
    });
});