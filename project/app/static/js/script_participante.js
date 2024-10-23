const searchBox = document.getElementById('search');
const activities = document.querySelectorAll('.activity');

// Função de pesquisa
searchBox.addEventListener('input', function() {
    const searchTerm = searchBox.value.toLowerCase();
    
    activities.forEach(activity => {
        const title = activity.querySelector('h2').textContent.toLowerCase();
        if (title.includes(searchTerm)) {
            activity.style.display = 'block';
        } else {
            activity.style.display = 'none';
        }
    });
});