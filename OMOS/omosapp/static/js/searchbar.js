document.getElementById('searchbar').addEventListener('keypress', function(event) {
        if (event.keyCode == 13) {
            event.preventDefault();
        }
    });