/**
 * Bounce. 
 * 
 * When the shape hits the edge of the window, it reverses its direction. 
 */
 
int rad = 10;        // Width of the shape
int paddlewidth = 5;
int paddleheight = 20;

float xpos, ypos;    // Starting position of shapes
float paddlex1, paddley1;
float paddlex2, paddley2;    

float xspeed = 2.8;  // Speed of the shape
float yspeed = 3;  // Speed of the shape

int xdirection = 1;  // Left or Right
int ydirection = 1;  // Top to Bottom


void setup() 
{
  size(640, 360);
  noStroke();
  frameRate(30);
  ellipseMode(RADIUS);
  rectMode(RADIUS);
  // Set the starting position of the shape
  xpos = width/2;
  ypos = paddley1 = paddley2 = height/2;
  paddlex1 = 10;
  paddlex2 = width-10;  
}

void draw() 
{
  background(0);
  if(xpos-rad>width||xpos+rad<0){
    xpos=width/2;
    ypos=height/2;
  }
  // Update the position of the shape
  xpos = xpos + ( xspeed * xdirection );
  ypos = ypos + ( yspeed * ydirection );
  
  // Test to see if the shape exceeds the boundaries of the screen
  // If it does, reverse its direction by multiplying by -1
  if ((xpos > paddlex2-paddlewidth-rad && ypos > paddley2-paddleheight && ypos < paddley2+paddleheight) || (xpos < paddlex1+paddlewidth+rad && ypos > paddley1-paddleheight && ypos < paddley1+paddleheight)) {
    xdirection *= -1;
  }
  if (ypos > height-rad || ypos < rad) {
    ydirection *= -1;
  }

  // Draw the shape
  ellipse(xpos, ypos, rad, rad);
  rect(paddlex1, paddley1, paddlewidth, paddleheight);
  rect(paddlex2, paddley2, paddlewidth, paddleheight);
}

void keyPressed(){
  if(keyCode=='S'){
    paddley1+=5;
  }
  if(keyCode=='W'){
    paddley1-=5;
  }
  if(keyCode==DOWN){
    paddley2+=5;
  }
  if(keyCode==UP){
    paddley2-=5;
  }
}
