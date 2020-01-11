document.getElementById('searchbar').addEventListener('keypress', function(event) {
        if (event.keyCode == 13) {
            document.getElementById('searchbarform').submit();
            return false;
        }
    });