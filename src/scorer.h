/*
 * scorer.h
 *
 *  Created on: Nov 30, 2014
 *      Author: guillaume
 */

#ifndef SCORER_H_
#define SCORER_H_

#include "SFML/Graphics.hpp"
#include "drawable.h"

using namespace sf;

class Scorer : public Text {

protected:
	unsigned short leftScore, rightScore;
	Font font;

public:
	Scorer();
	void score(bool left);
};

#endif /* SCORER_H_ */
