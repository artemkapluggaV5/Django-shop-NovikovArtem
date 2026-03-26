document.addEventListener('DOMContentLoaded', function() {
    const cartRows = document.querySelectorAll('[data-product-id]');

    function updateCartTotal() {
        let total = 0;
        cartRows.forEach(row => {
            const totalPriceElem = row.querySelector('.total-price');
            total += parseFloat(totalPriceElem.textContent);
        });
        const totalElem = document.getElementById('cart-total');
        if (totalElem) totalElem.textContent = total.toFixed(2) + ' ₽';
        const mobileElem = document.getElementById('cart-total-mobile');
        if (mobileElem) mobileElem.textContent = total.toFixed(2);
    }

    cartRows.forEach(row => {
        const decreaseBtn = row.querySelector('.btn-decrease');
        const increaseBtn = row.querySelector('.btn-increase');
        const input = row.querySelector('.quantity-input');
        const unitPriceElem = row.querySelector('.text-end small') || row.querySelector('.unit-price');
        const totalPriceElem = row.querySelector('.total-price');
        const unitPrice = parseFloat(unitPriceElem.textContent);

        decreaseBtn.addEventListener('click', function() {
            let value = parseInt(input.value);
            if (value > 1) value--;
            input.value = value;
            totalPriceElem.textContent = (unitPrice * value).toFixed(2);
            updateCartTotal();
        });

        increaseBtn.addEventListener('click', function() {
            let value = parseInt(input.value);
            if (value < 20) value++;
            input.value = value;
            totalPriceElem.textContent = (unitPrice * value).toFixed(2);
            updateCartTotal();
        });

        input.addEventListener('input', function() {
            let value = parseInt(this.value);
            if (isNaN(value) || value < 1) value = 1;
            if (value > 20) value = 20;
            this.value = value;
            totalPriceElem.textContent = (unitPrice * value).toFixed(2);
            updateCartTotal();
        });
    });
});