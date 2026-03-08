// static/js/tracker.js
document.addEventListener('DOMContentLoaded', function() {
    // Track initial visit
    trackVisit();
    
    // Track various activities
    document.addEventListener('click', function(e) {
        trackActivity('click', {
            element: e.target.tagName,
            id: e.target.id,
            class: e.target.className
        });
    });
    
    document.addEventListener('scroll', function() {
        trackActivity('scroll', {
            position: window.scrollY
        });
    });
    
    // Track form submissions
    document.addEventListener('submit', function(e) {
        trackActivity('form_submit', {
            form_id: e.target.id
        });
    });
});

function trackVisit() {
    fetch('/track-visit/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        // Store visit ID for activity tracking
        localStorage.setItem('visit_id', data.visit_id);
    });
}

function trackActivity(activityType, details) {
    const visitId = localStorage.getItem('visit_id');
    if (!visitId) return;
    
    fetch('/track-activity/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            visit_id: visitId,
            activity_type: activityType,
            activity_details: JSON.stringify(details)
        })
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}