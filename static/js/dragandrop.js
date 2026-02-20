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
            });
        }
    });
});