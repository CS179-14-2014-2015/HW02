/*
 * ball.h
 *
 *  Created on: Nov 26, 2014
 *      Author: guillaume
 */

#ifndef BALL_H_
#define BALL_H_

#include "SFML/Graphics.hpp"
#include "SFML/Audio.hpp"
#include "drawable.h"
#include "bar.h"

using namespace sf;

class Ball : public CircleShape, public sfTools::Drawable {

protected :
	float xSpeed;	//The current xSpeed of the ball
	float ySpeed;	//The current ySpeed of the ball
	bool isRunning;  //To know if the ball has been launched
	SoundBuffer buffer; // Contain the stream of ball.wav
	Sound sound;		//used to play the ball sound

public :
	Ball();					//Constructor, set up the ball
	void restart();		//Replace the ball at the midle of the left bar
	void run();				//give speed to the ball
	void update(const Bar & left, const FloatRect & right); //Move the ball according to it speed. This function need the actual position of the bars. increase the speed if touch a bar
    bool hitTop() const; //Detect if the ball hit the top of the window
    bool hitBottom() const; //Detect if the ball hit the top of the window
    bool hitRightExit() const; //Detect if the ball hit right side of the window
    bool hitLeftExit() const; //Detect if the ball hit left side of the window
    bool exit() const; //Detect if the ball exit the window
    void setXspeed(float speed);
    void setYspeed(float speed);
    void setIsMovingDown(bool isMovingDown);
    void setIsMovingUp(bool isMovingUp);
};

#endif /* BALL_H_ */
