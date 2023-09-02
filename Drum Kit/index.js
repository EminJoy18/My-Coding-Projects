document.querySelector(".w").addEventListener("click", sound);

document.querySelector(".a").addEventListener("click", function() {
    (new Audio('./sounds/tom-2.mp3')).play()
});

document.querySelector(".s").addEventListener("click", function() {
    (new Audio('./sounds/tom-3.mp3')).play()
});

document.querySelector(".d").addEventListener("click", function() {
    (new Audio('./sounds/tom-4.mp3')).play()
});

document.querySelector(".j").addEventListener("click", function() {
    (new Audio('./sounds/snare.mp3')).play()
});

document.querySelector(".k").addEventListener("click", function() {
    (new Audio('./sounds/crash.mp3')).play()
});

document.querySelector(".l").addEventListener("click", function() {
    (new Audio('./sounds/kick-bass.mp3')).play()
});

function sound(){
    var snd = new Audio('./sounds/tom-1.mp3')
    snd.play()//plays the sound
}


document.addEventListener("keypress", function(Event) {
    switch(Event.key)
    {
        case "w":
            var snd = new Audio('./sounds/tom-1.mp3');
            snd.play();
            break;

        case "a":
            (new Audio('./sounds/tom-2.mp3')).play();
            break;

        case "s":
            (new Audio('./sounds/tom-3.mp3')).play();
            break;

        case "d":
            (new Audio('./sounds/tom-4.mp3')).play();
            break;

        case "j":
            (new Audio('./sounds/snare.mp3')).play()
            break;

        case "k":
            var crash = new Audio('./sounds/crash.mp3');
            crash.play();
            break;

        case "l":
            (new Audio('./sounds/kick-bass.mp3')).play();
            break;
    }
});
