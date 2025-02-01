document.getElementById('searchInput').addEventListener('input', function (e) {
    const searchText = e.target.value.trim().toLowerCase(); // Trim to remove extra spaces
    const rows = document.querySelectorAll('tbody tr');
    
    rows.forEach(row => {
        const text = row.textContent.toLowerCase(); // Convert text to lowercase for comparison
        if (text.includes(searchText)) {
            row.style.display = ''; // Show the row if it matches
        } else {
            row.style.display = 'none'; // Hide the row if it doesn't match
        }
    });
});
