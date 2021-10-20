let coins;
let player;
let score = 0;

var img;
var net;
var bas;

function preload() {
  img = loadImage("sky.jpg");
  net = loadImage("basketball_net.png");
  bas = loadImage("basketball.png");
}

function setup() {
  createCanvas(600, 600);
  image(net, 0, 0);
  coins = new Group();
  for (let i = 0; i < 10; i++) {
    let c = createSprite(
      random(100, width-100),
      random(100, height-100),
      40, 40);
    c.shapeColor = color(255, 165, 0);
    coins.add(c);
  }
  //player = createSprite(50, 50, 40, 40);
  player = createSprite(50, 50, 0, 0);
  player.shapeColor = color(255);
}

function draw() {
  background(50);
  image(img, 0, 0, 800, 600);
  image(net, mouseX - net.width/2, mouseY - net.height/2);
  player.velocity.x = 
    (mouseX-player.position.x)*0.1;
  player.velocity.y = 
    (mouseY-player.position.y)*0.1;
  player.overlap(coins, getCoin);
  drawSprites();
  fill(255);
  noStroke();
  textSize(72);
  textAlign(CENTER, CENTER);
  if (coins.length > 0) {
    text(score, width/2, height/2);
  }
  else {
    text("you win!", width/2, height/2);
  }
}


function getCoin(player, coin) {
  coin.remove();
  score += 1;
}