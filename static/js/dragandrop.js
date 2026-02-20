document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('sortable-container');
    if (!container) return; // Если контейнера нет на странице, ничего не делаем

    // Берем данные из HTML-атрибутов
    const updateUrl = container.getAttribute('data-url');
    const csrfToken = container.getAttribute('data-csrf');

    new Sortable(container, {
        animation: 150,
        handle: '.drag-handle',
        ghostClass: 'sortable-ghost', // Класс для элемента, который тянем

        onEnd: function() {
            let order = [];

            // Собираем все ID элементов в новом порядке
            container.querySelectorAll('[data-id]').forEach(function(el) {
                order.push(el.getAttribute('data-id'));
            });

            // Отправляем запрос на сервер
            fetch(updateUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken // Используем токен из атрибута
                },
                body: JSON.stringify({ order: order })
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'ok') {
                    console.log('Порядок успешно сохранен в БД!');
                } else {
                    console.error('Ошибка сохранения:', data.message);
                }
            })
            .catch(error => console.error('Ошибка сети:', error));
        }
    });
});