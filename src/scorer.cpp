/*
 * scorer.cpp
 *
 *  Created on: Nov 30, 2014
 *      Author: guillaume
 */

#include "scorer.h"
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

Scorer::Scorer() : Text(), font(),leftScore(0), rightScore(0) {

	if(!font.loadFromFile("Capture_it.ttf")) {
		std::cout << "Font not found." << std::endl;
	}

	setFont(font);
	setString("0 : 0");
	setCharacterSize(50);
	setColor(Color::Black);
	//setStyle(Text::Bold);
	setPosition(500 - getGlobalBounds().width / 2, 300 - getGlobalBounds().height / 2);		//center the text
}

void Scorer::score(bool left) {
	if(left)
		leftScore++;
	else
		rightScore++;

	cout << left << ", " << leftScore << " : " << rightScore<<endl;

	//Parse leftScore and rightScore into a String type
	string tmpLeft = static_cast<ostringstream*>( &(ostringstream() << leftScore) )->str();
	string tmpRight = static_cast<ostringstream*>( &(ostringstream() << rightScore) )->str();

	//Update the text
	string text = tmpLeft + " : " + tmpRight;
	setString(text);
}



