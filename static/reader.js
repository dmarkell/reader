function pickBook(e) {
    var book_name = document.getElementById('book').value;
    var box = document.getElementById("text");
    var starter = document.getElementById("starter");

    if (book_name === "other") {
        box.removeAttribute('hidden');
        starter['disabled'] = 'disabled';
    } else {
        box['hidden'] = 'hidden'
        starter.removeAttribute('disabled');
    }
}

function changeColor() {
    var color = document.getElementById('color').value;
    document.getElementById('center').style.color = color;
    document.getElementsByTagName('td')[0].style.color = color;
}

function updateReader(left, center, right) {

    document.getElementById('left').innerHTML = left;
    document.getElementById('center').innerHTML = center;
    document.getElementById('right').innerHTML = right;
}

function streamWords(i) {
    if (streamWords.running) {

        var book_name = document.getElementById('book').value;
        var book = books[book_name];
        
        var words = book.split(/\s+/);
        
        var i = i || 0;
        
        var WPM = document.getElementById('WPM').value;
        var millis = 60/WPM*1000;

        if (i >= words.length) {
            toggleControls();
            return;
        };
        
        var word = words[i];

        setTimeout(
            function() {
                var left, center, right;
                var len = word.length;
                if (len == 1) {
                    left = right = '';
                    center = word[0];
                } else if (len > 1 && len < 6) {
                    left = word[0];
                    center = word[1];
                    right = word.slice(2);
                } else if (len >= 6 && len < 10) {
                    left = word.slice(0,2);
                    center = word[2];
                    right = word.slice(3);
                } else {
                    left = word.slice(0,3);
                    center = word[3];
                    right = word.slice(4);
                }
                updateReader(left, center, right);
                streamWords(i + 1);
            }, millis);
    } else {
        updateReader('Pic', 'k', '&nbsp;a text.');
    }
}

function toggleStarter() {
    var starter = document.getElementById('starter');
    if (starter.hasAttribute('disabled')) {
        starter.removeAttribute('disabled');
    } else {
        starter['disabled'] = 'disabled';
    };
}

function toggleStopper() {
    var starter = document.getElementById('stopper');
    if (starter.hasAttribute('disabled')) {
        starter.removeAttribute('disabled');
    } else {
        starter['disabled'] = 'disabled';
    };
}

function toggleControls() {
    var starter = document.getElementById('starter');
    var stopper = document.getElementById('stopper');
    var book_choice = document.getElementById('book');

    if (starter.hasAttribute('disabled')) {
        starter.removeAttribute('disabled');
        book_choice.removeAttribute('disabled');
        stopper['disabled'] = 'disabled';
    } else {
        stopper.removeAttribute('disabled');
        starter['disabled'] = 'disabled';
        book_choice['disabled'] = 'disabled';
    };
}

function start() {
    streamWords.running = true;
    streamWords();
    toggleControls();
}

function stop() {
    streamWords.running = false;
    toggleControls();
}
