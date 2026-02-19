
document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('sortable-container');

    new Sortable(container, {
        animation: 150,
        handle: '.drag-handle',
        ghostClass: 'bg-light',

        onEnd: function() {
            let order = [];

            container.querySelectorAll('[data-id]').forEach(function(el) {
                order.push(el.getAttribute('data-id'));
            });

            fetch("{% url 'update_category_order' %}", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                body: JSON.stringify({ order: order })
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'ok') {
                    console.log('Порядок успешно сохранен в БД!');
                }
            });
        }
    });
});