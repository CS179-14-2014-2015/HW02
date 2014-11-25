/**
 * Bounce. 
 * 
 * When the shape hits the top and bottom edges of the window and the paddles, it reverses its direction. 
 */
 
int rad = 10;        // Width of the shape
int paddlewidth = 2;  // dimensions of the paddles
int paddleheight = 20;

float xpos, ypos;    // Starting position of shapes
float paddlex1, paddley1;
float paddlex2, paddley2;    

float xspeed = 2.8;  // Speed of the shape
float yspeed = 3;  // Speed of the shape
float paddlespeed = 5;

int xdirection = 1;  // Left or Right
int ydirection = 1;  // Top to Bottom

PFont f;

int score1 = 0;
int score2 = 0;

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
  // Create the font
  printArray(PFont.list());
  f = createFont("Rockwell", 30);
  textFont(f);
  textAlign(CENTER, CENTER);  
}

void draw() 
{
  background(0);
  text(score1,width/4,10);
  text(score2,3*width/4,10);
  if(xpos-rad>width||xpos+rad<0||(keyPressed && key==' ')){
    if(xpos-rad>width){
      score1++;
    }else if(xpos+rad<0){
      score2++;
    }
    xspeed=2.8;
    yspeed=3;
    xpos=width/2;
    ypos=height/2;
  }
  // Update the position of the shape
  xpos = xpos + ( xspeed * xdirection );
  ypos = ypos + ( yspeed * ydirection );
  
  // Test to see if the shape exceeds the boundaries of the screen
  // If it does, reverse its direction by multiplying by -1
  if ((xpos+rad>paddlex2-paddlewidth && ypos-rad<paddley2+paddleheight && ypos+rad>paddley2-paddleheight) || (xpos-rad<paddlex1+paddlewidth && ypos-rad<paddley1+paddleheight && ypos+rad>paddley1-paddleheight)) {
    xdirection *= -1;
    xspeed+=0.1;
    yspeed+=0.1;
  }
  if (ypos > height-rad || ypos < rad || (((ypos+rad>paddley1-paddleheight && ypos-rad<paddley1-paddleheight) || (ypos-rad<paddley1+paddleheight && ypos+rad>paddley1+paddleheight)) && xpos-rad<paddlex1+paddlewidth) || (((ypos+rad>paddley2-paddleheight && ypos-rad<paddley2-paddleheight) || (ypos-rad<paddley2+paddleheight && ypos+rad>paddley2+paddleheight)) && xpos+rad>paddlex2-paddlewidth)) {
    ydirection *= -1;
  }

  // Draw the shape
  ellipse(xpos, ypos, rad, rad);
  rect(paddlex1, paddley1, paddlewidth, paddleheight);
  rect(paddlex2, paddley2, paddlewidth, paddleheight);
  paddley1=mouseY;
  AI();
}

void AI(){
  if((paddley2+paddleheight<height || paddley2-paddleheight>0) && xdirection>0){
    if(paddley2-paddleheight/2>ypos){
      paddley2-=paddlespeed;
    }else if(paddley2+paddleheight/2<ypos){
      paddley2+=paddlespeed;
    }
  }else if(paddley2-paddleheight/2>height/2 || paddley2+paddleheight/2<height/2 && xdirection<0){
    if(paddley2-paddleheight/2>height/2){
      paddley2-=paddlespeed;
    }else{
      paddley2+=paddlespeed;
    }
  }
}
