/*function showNotification() {
    const notification = document.getElementById('notification-message');
    notification.classList.remove('hidden');
    setTimeout(() => {
        notification.classList.add('hidden');
    }, 5000);  // Hide message after 5 seconds
}

// Submit form and show notification
document.getElementById('adopt-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission
    const form = event.target;
    fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: {
            'X-CSRFToken': form.querySelector('input[name="csrfmiddlewaretoken"]').value
        }
    })
    .then(response => {
        if (response.ok) {
            showNotification(); // Show notification if form submission is successful
            form.reset(); // Reset the form after submission
        } else {
            console.error('Form submission failed:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});*/
document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('adoptForm');
    var notification = document.getElementById('notification-message');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Simulate form submission (you can remove this in production)
        setTimeout(function() {
            notification.classList.remove('hidden');
            // Optional: Hide the notification after a few seconds
            setTimeout(function() {
                notification.classList.add('hidden');
            }, 5000); // 5 seconds
        }, 1000); // 1 second, simulate form submission delay
    });
});