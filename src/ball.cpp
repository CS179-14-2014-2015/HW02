/*
 * ball.cpp
 *
 *  Created on: Nov 26, 2014
 *      Author: guillaume
 */

#include "ball.h"

Ball::Ball() : CircleShape(10){
	//Initialize the sound
	buffer.loadFromFile("ball.wav");
	sound.setBuffer(buffer);

	//initialize ball properties
	setFillColor(Color::Red);
	setOrigin(10, 10);		//Origin at the center of the circle, speed at 0
	restart();
}

void Ball::restart(){

	//reset speed, position and flag
	setPosition(40, 300);
	xSpeed = 0;
	ySpeed = 0;
	isRunning = false;
}

void Ball::update(Bar const& left, FloatRect const& right) {

	//top or bottom collision
	if(hitTop() || hitBottom()) {
		ySpeed = -ySpeed;
		sound.play();
	}

	//right and left bar collisions, increase the ball's speed
	if(getGlobalBounds().intersects(right) || getGlobalBounds().intersects(left.getGlobalBounds())){
		sound.play();
		if(xSpeed > 0){
			xSpeed = -xSpeed - 1;
		}
		else{
			xSpeed = - xSpeed + 1;
		}
		if(ySpeed > 0){
			ySpeed++;
		}
		else{
			ySpeed--;
		}
	}

	// left or right exit
	if(exit())
		return;

	//the ball must follow the bar when not yet launched
	if(!isRunning){
		setPosition(40, left.getPosition().y);
	}

	//move the ball according to its speed
	move(xSpeed, ySpeed);
}

bool Ball::hitTop() const {
	return getPosition().y <= 10;
}

bool Ball::hitBottom() const{
	return getPosition().y >= 590;
}

bool Ball::hitRightExit() const{
	return getPosition().x >= 990;
}

bool Ball::hitLeftExit() const{
	return getPosition().x <= 10;
}

void Ball::run(){
	xSpeed = 6;
	ySpeed = 6;
	isRunning = true;
}

bool Ball::exit() const {
	return (hitRightExit() || hitLeftExit()) ? true : false;
}












