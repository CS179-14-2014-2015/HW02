/*
 * game.cpp
 *
 *  Created on: Nov 26, 2014
 *      Author: guillaume
 */

#include "game.h"

Game::Game() : window (VideoMode(1000, 600), "Pong"), leftBar(true), rightBar(false), ball(), scorer(){
	window.setFramerateLimit(50);		//set the framerate at 50 fps, determinate the global speed of the game
}

void Game::test() {
	testBars();
	testBall();
}

void Game::testBars(){

	//Bars go up, ball do not move
	leftBar.setIsMovingUp(true);
	rightBar.setIsMovingUp(true);


	while (!leftBar.isTop()) {

        //wait for an event
        while (window.pollEvent(event)) {

                //Close the window
                if (event.type == sf::Event::Closed)
                        window.close();

        }

        //update the window
        update();

	}	//Bars are up

	leftBar.setIsMovingUp(false);
	rightBar.setIsMovingUp(false);

	//Bars go down
	leftBar.setIsMovingDown(true);
	rightBar.setIsMovingDown(true);
	ball.restart();

	while (!leftBar.isBottom()) {

		//wait for an event
		while (window.pollEvent(event)) {

			//Close the window
			if (event.type == sf::Event::Closed)
				window.close();
		}

		//update the window
		update();

	}	//Bars are down
	leftBar.restart();
	rightBar.restart();
}

void Game::testBall() {

	ball.restart();
	ball.run();

	rightBar.setPosition(rightBar.getPosition().x, 100);


	while (!ball.exit()) {

        //wait for an event
        while (window.pollEvent(event)) {

        	//Close the window
        	if (event.type == Event::Closed)
        		window.close();

		}
        update();
	}
}


void Game::run(){

	//Main loop
	while(window.isOpen()) {

		while(window.pollEvent(event)) {

			//Close the window
			if (event.type == Event::Closed)
				window.close();

			//Released Key management
			if(event.type == Event::KeyReleased){
				switch(event.key.code) {

					case(Keyboard::Space) :
						ball.run();
						break;

					case(Keyboard::W):
						leftBar.setIsMovingUp(false);
						break;

					case(Keyboard::S):
						leftBar.setIsMovingDown(false);
						break;

					case(Keyboard::Up):
                        rightBar.setIsMovingUp(false);
						break;

					case(Keyboard::Down):
							rightBar.setIsMovingDown(false);
							break;
				}
			}

			//Pressed keys management
			if(event.type == Event::KeyPressed) {
				switch(event.key.code) {

					case(Keyboard::W):
                    	leftBar.setIsMovingUp(true);
						break;

					case(Keyboard::S):
                    	leftBar.setIsMovingDown(true);
                        break;

                    case(Keyboard::Up):
                    	rightBar.setIsMovingUp(true);
                        break;

                    case(Keyboard::Down):
                    	rightBar.setIsMovingDown(true);
                    	break;
				}
			}

		}

		update();

        // check if game is over
        if(ball.exit()) {

        	//Update the score
        	if(ball.hitLeftExit())
                scorer.score(false);	//right scored
            if(ball.hitRightExit())
                scorer.score(true);		//left scored

            leftBar.restart();
            rightBar.restart();
            ball.restart();
        }

	}//End of main loop
}

void Game::update(){
	//clear the window
	window.clear(Color::White);

	//update the drawables
	leftBar.update();
	rightBar.update();
	ball.update(leftBar, rightBar.getGlobalBounds());

	//draw and display
	window.draw(scorer);
	window.draw(leftBar);
	window.draw(rightBar);
	window.draw(ball);

	window.display();
}







