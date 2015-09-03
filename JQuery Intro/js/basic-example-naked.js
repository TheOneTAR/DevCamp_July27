function unfade(element) {
    var op = 0.1;  // initial opacity
    element.style.display = 'block';
    var timer = setInterval(function () {
        if (op >= 1){
            clearInterval(timer);
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op += op * 0.1;
    }, 10);
}

function removeThing(e) {
    e.target.parentNode.removeChild(e.target);
}

headers1 = document.getElementsByTagName('h1');
headers2 = document.getElementsByTagName('h2');

for (var i=0; i < headers1.length; i++) {
    headers1[i].className += " headline";
}

for (var i=0; i < headers2.length; i++) {
    headers2[i].className += " headline";
}

lis = document.querySelectorAll('li:nth-last-child(n+1)');
for (var i=0; i < lis.length; i++) {
    unfade(lis[i]);
}

ul = document.getElementsByTagName('ul');
ul[0].addEventListener('click', removeThing, true);