/*
 * game.h
 *
 *  Created on: Nov 26, 2014
 *      Author: guillaume
 */

#ifndef GAME_H_
#define GAME_H_

#include <SFML/Graphics.hpp>	//Used to create the window
#include "bar.h"
#include "ball.h"
#include "scorer.h"

using namespace sf;
using namespace std;

//Main class of the application
class Game {

protected:
	RenderWindow window; //the window
	Event event;	//Store user input
	Bar leftBar, rightBar;
	Ball ball;
	Scorer scorer;

public:
	Game();				//Set up the window and the parameters of the application
	void run(); 		//launch the game
	void test();	 	//launch a serial of tests
	void testBars();	//launch a test on the bars : test the move up and down functions
	void testBall();	//launch a test on the ball : test the reaction of the ball with obstacles
	void update();		//Update the window by clearing it, updating the drawables and drawing them
};

#endif /* GAME_H_ */
