document.addEventListener("DOMContentLoaded", function() {
        var rows = document.querySelectorAll(".clickable-row");

        rows.forEach(function(row) {
            row.addEventListener("click", function() {
                var href = row.dataset.href;
                if (href) {
                    window.location.href = href;
                }
            });
        });
    });


function validateForm() {
    var quantityInput = document.getElementById('quantity');
    var quantityValue = quantityInput.value.trim();

    if (!/^\d+$/.test(quantityValue)) {
        alert('Please enter a valid number.');
        return false;
    }

    return true;
}
