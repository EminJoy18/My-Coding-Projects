var images=['dice1.png','dice2.png','dice3.png','dice4.png','dice5.png','dice6.png']

var v1 = Math.floor(Math.random() * images.length)
var v2 = Math.floor(Math.random() * images.length)

document.querySelector('.img1').src = './images/'+images[v1];
document.querySelector('.img2').src = './images/'+images[v2];

if(v1 > v2)
{
    document.querySelector('h1').textContent = "Player1 wins!";
}
else if(v1 < v2)
{
    document.querySelector('h1').textContent = "Player2 wins!";
}
else{
    document.querySelector('h1').textContent = "It'a Tie";
}