let video;
let poseNet;
let mouthX = 0;
let mouthY = 0;
let eye1X, eye1Y, eye2X, eye2Y;
let img;
let dog;
let mouth;

function setup() {
  createCanvas(640, 480);
  video = createCapture(VIDEO);
  video.hide();
  poseNet = ml5.poseNet(video, modelReady);
  poseNet.on('pose', gotPoses);
  img = loadImage('eyebrow.png');
  dog = loadImage('dog.png');
  mouth = loadImage('mouth.png');
}

function gotPoses(poses) {
  // console.log(poses);
  if (poses.length > 0) {
    mouthX = poses[0].pose.keypoints[0].position.x;
    mouthY = poses[0].pose.keypoints[0].position.y;
    
    eye1X = poses[0].pose.keypoints[1].position.x;
    eye1Y = poses[0].pose.keypoints[1].position.y;
    
    eye2X = poses[0].pose.keypoints[2].position.x;
    eye2Y = poses[0].pose.keypoints[2].position.y;
  }
}

function modelReady() {
  console.log('model ready');
}

function draw() {
  image(video, 0, 0);

  //fill(100, 0, 0);
  //ellipse(mouthX, mouthY+50, 50, 40);
  
  eye(eye1X, eye1Y, 80, 1);
  eye(eye2X, eye2Y, 80, -1);
}

function eye(x, y, size, n) {
	let angle = frameCount * 0.1;
	
	fill(0);
	noStroke();
	ellipse(x, y, size/1.3, size/1.3);
    
    fill(255,111,148)
    ellipse(x,y+50,20,10)
	
	fill(255);
	noStroke();
	ellipse(x+cos(angle*n)*size/5, y+sin(angle*n)*size/5, size/3, size/3);
    image(img, x-50, y-80);
    image(dog, mouthX-200, mouthY+50, 130,130);
    image(mouth, mouthX-20, mouthY+30, 60, 50);
}
