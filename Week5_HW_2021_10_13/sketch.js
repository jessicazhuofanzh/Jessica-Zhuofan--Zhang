// HTML Select option object:
let portSelector;

let serial; // variable to hold an instance of the serialport library
 
function setup() {
  serial = new p5.SerialPort(); // make a new instance of the serialport library
  serial.on('list', printList); // set a callback function for the serialport list event
 
  serial.list(); // list the serial ports
}
 
// make a serial port selector object:
function printList(portList) {
  // create a select object:
  portSelector = createSelect();
  portSelector.position(10, 10);
  // portList is an array of serial port names
  for (var i = 0; i < portList.length; i++) {
    // add this port name to the select object:
    portSelector.option(portList[i]);
  }
  // set an event listener for when the port is changed:
  portSelector.changed(mySelectEvent);
}

function mySelectEvent() {
  let item = portSelector.value();
   // if there's a port open, close it:
  if (serial.serialport != null) {
    serial.close();
  }
  // open the new port:
  serial.open(item);
}

let xPos = 0;                     // x position of the graph

// let rad = 60; // Width of the shape
// let xpos, ypos; // Starting position of shape

// let xspeed = 2.8; // Speed of the shape
// let yspeed = 2.2; // Speed of the shape

// let xdirection = 1; // Left or Right
// let ydirection = 1; // Top to Bottom

let inData;                             // for incoming serial data
 
function setup() {
  createCanvas(800, 600);
  //noStroke();
  fill('#ff00aa22');
  //background(0x08, 0x16, 0x40);
  background('#ff00aa22');
  serial = new p5.SerialPort();       // make a new instance of the serialport library
  serial.on('list', printList);  // set a callback function for the serialport list event
  serial.on('connected', serverConnected); // callback for connecting to the server
  serial.on('open', portOpen);        // callback for the port opening
  serial.on('data', serialEvent);     // callback for when new data arrives
  serial.on('error', serialError);    // callback for errors
  serial.on('close', portClose);      // callback for the port closing
 
  serial.list();                      // list the serial ports
}

function draw() {
   //graphData(inData);
  ellipse(400, 300, inData, inData);
  ellipse(200, 100, inData, inData);
  ellipse(600, 400, inData, inData);
  ellipse(60, 40, inData, inData);
  ellipse(700, 40, inData, inData);
  ellipse(700, 500, inData, inData);
  ellipse(0, 500, inData, inData);
  ellipse(200, 400, inData, inData);
}

//function graphData(newData) {
  // map the range of the input to the window height:
  //var yPos = map(newData, 0, 255, 0, height);
  // draw the line in a pretty color:
  //stroke(0xA8, 0xD9, 0xA7);
  //line(xPos, height, xPos, height - yPos);
  // at the edge of the screen, go back to the beginning:
  //if (xPos >= width) {
    //xPos = 0;
    // clear the screen by resetting the background:
    //background(0x08, 0x16, 0x40);
  //} else {
    // increment the horizontal position for the next reading:
    //xPos++;
  //}
//}

function serverConnected() {
  console.log('connected to server.');
}
 
function portOpen() {
  console.log('the serial port opened.')
}
 
function serialEvent() {
  // read a string from the serial port:
  var inString = serial.readLine();
  // check to see that there's actually a string there:
  if (inString.length > 0 ) {
  // convert it to a number:
  inData = Number(inString);
  }
}
 
function serialError(err) {
  console.log('Something went wrong with the serial port. ' + err);
}
 
function portClose() {
  console.log('The serial port closed.');
}
