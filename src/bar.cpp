/*
 * bar.cpp
 *
 *  Created on: Nov 26, 2014
 *      Author: guillaume
 */
#include "bar.h"

//Create a bar of 20 px width and 200 px height
Bar::Bar(bool left) :	RectangleShape(Vector2f(20, 200)), isMovingUp(false), isMovingDown(false) {
	setFillColor(Color::Black); //Define the color of the bars

	setOrigin(10, 100);

	//Place the bar on left or right, and in the middle : 100 + x =  300
	if (left)
		setPosition(Vector2f(20, 300));
	else
		setPosition(Vector2f(980, 300));

}

bool Bar::getIsMovingDown() {
	return isMovingDown;
}

bool Bar::getIsMovingUp() {
	return isMovingUp;
}

void Bar::setIsMovingDown(bool isMovingDown) {
	this->isMovingDown = isMovingDown;
}

void Bar::setIsMovingUp(bool isMovingUp) {
	this->isMovingUp = isMovingUp;
}

bool Bar::isTop() {
	return getPosition().y <= 100;
}

bool Bar::isBottom() {
	return getPosition().y >= 500;
}

void Bar::moveUp() {

	//Check if the bar can go up
	if (isTop())
		return;

	//Move the bar up 4px
	move(0, -4);
}

void Bar::moveDown() {

	//Check if the bar can go down
	if (isBottom())
		return;

	//Move the bar down 4px
	move(0, 4);
}

void Bar::restart(){
	setPosition(getPosition().x, 300);	//we change only the y value
	isMovingDown = false;
	isMovingUp = false;
}

void Bar::update(){
	if(isMovingDown)
		moveDown();
	if(isMovingUp)
		moveUp();
}






