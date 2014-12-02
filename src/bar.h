/*
 * Bar.h
 *
 *  Created on: Nov 26, 2014
 *      Author: guillaume
 */

#ifndef BAR_H_
#define BAR_H_

#include "SFML/Graphics.hpp"
#include "drawable.h"

using namespace sf;

class Bar : public RectangleShape, public sfTools::Drawable {

protected:
	bool isMovingUp;
	bool isMovingDown;

public:
	Bar(bool left);		//Initialisation differ depending on left or right bar
	void moveUp();		//Move the bar up when isMovingUp is true and isTop is false
	void moveDown();  //Move the bar when isMovingDown is true and isBottom is false
	bool isTop();		//Say whether the bar is at the top of the window or not
	bool isBottom();	//Say whether the bar is at the bottom of the window or not
    bool getIsMovingDown();	//get the value of is moving up. Updated by user  input
    bool getIsMovingUp();		//get the value of is moving up. Updated by user  input
    void setIsMovingDown(bool isMovingDown);		//Set the value of isMovingDown
    void setIsMovingUp(bool isMovingUp);			//Set the value of isMovingUp
    void restart();	//Replace the bar
    void update(); 	//Update
};

#endif /* BAR_H_ */
