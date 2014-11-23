#include <GL/glfw.h>
#include <iostream>
#include <cmath>
#include <cassert>

using namespace std;

//feel free to mess with these constants.
const GLfloat CIRCLE_RADIUS = 0.11f;
const GLuint COLOR[] = { 0xFFFFFFFF};


struct Vtx {
	GLfloat x, y;
	GLuint color;
};

struct Circle {
	GLfloat x, y, vx, vy, r;
};

struct Paddle {
	GLfloat side;
};

const GLsizei N_VERTICES_PER_CIRCLE = 8;
Vtx vertices[N_VERTICES_PER_CIRCLE + 8];


const GLfloat PIE = 3.14159265f;

float random() {
	float doop = (float)rand()/RAND_MAX;
	return doop;
}

void generatePolygon(GLfloat radius, GLfloat angularOffset, GLfloat x, GLfloat y, GLsizei nVertices, GLuint startPoint) {
	const GLfloat factor = 2.0f * PIE/nVertices;
	for (int i = 0; i < nVertices; i++)
	{
		GLfloat theta = i*factor;
		vertices[i + startPoint].x = radius * cos(angularOffset + theta) + x;
		vertices[i + startPoint].y = radius * sin(angularOffset + theta) + y;
	}
}
void generatePaddle(GLfloat side, GLfloat ycenter, GLuint startPoint)
{

	vertices[startPoint].x = side;
	vertices[startPoint+1].x = side + 0.1;
	vertices[startPoint+2].x = side +0.1;
	vertices[startPoint+3].x = side;

	vertices[startPoint].y = ycenter + 0.25;
	vertices[startPoint+1].y = ycenter + 0.25;
	vertices[startPoint+2].y = ycenter - 0.25;
	vertices[startPoint+3].y = ycenter - 0.25;
	
}

void drawCircle(const Circle &c) {
	generatePolygon(c.r, 0, c.x, c.y, N_VERTICES_PER_CIRCLE, 0);
	glDrawArrays(GL_TRIANGLE_FAN, 0, N_VERTICES_PER_CIRCLE);
}

void drawPaddles(const Paddle &left, const Paddle &right, GLfloat leftCenter, GLfloat rightCenter)
{
	generatePaddle(left.side, leftCenter, N_VERTICES_PER_CIRCLE);
	generatePaddle(right.side, rightCenter, N_VERTICES_PER_CIRCLE+4);
	glDrawArrays(GL_TRIANGLE_FAN, N_VERTICES_PER_CIRCLE, 4);
	glDrawArrays(GL_TRIANGLE_FAN, N_VERTICES_PER_CIRCLE+4, 4);
}

int main() {
	if ( !glfwInit() ) {
		std::cerr << "Unable to initialize OpenGL!\n";
		return -1;
	}

	if ( !glfwOpenWindow(720,720, //width and height of the screen
				8,8,8,8, //Red, Green, Blue and Alpha bits
				0,0, //Depth and Stencil bits
				GLFW_WINDOW)) {
		std::cerr << "Unable to create OpenGL window.\n";
		glfwTerminate();
		return -1;
	}

	glfwSetWindowTitle("GLFW Simple Example");

	// Ensure we can capture the escape key being pressed below
	glfwEnable( GLFW_STICKY_KEYS );

	// Enable vertical sync (on cards that support it)
	glfwSwapInterval( 1 );

	glClearColor(0,0,0,0);
	
	glEnableClientState(GL_VERTEX_ARRAY);
	glEnableClientState(GL_COLOR_ARRAY);


	//sets up the color of the vertices
	for ( size_t i = 0; i < N_VERTICES_PER_CIRCLE + 8; ++i ) {
		vertices[i].color = COLOR[0];
	}


	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	
	Circle c1 = {-0.5, 0, cos(2*PIE*random()), sin(2*PIE*random()), CIRCLE_RADIUS};
	Paddle left = {-1};
	Paddle right = {0.9};

	double t = 0;
	const double dt = 0.025;
	float leftCenter = 0;
	float rightCenter = 0;
	float paddleSpeed = dt;
	int leftScore = 0;
	int rightScore = 0;
	bool isPoop = false;
	bool scoreRecorded = false;
	do {
		int width, height;
		// Get window size (may be different than the requested size)
		//we do this every frame to accommodate window resizing.
		glfwGetWindowSize( &width, &height );
		glViewport( 0, 0, width, height );

		glClear(GL_COLOR_BUFFER_BIT);
		
		t += dt;
		
		c1.x += c1.vx * dt;
		c1.y += c1.vy * dt;

		if ( c1.x > 1 - (c1.r+0.1)) 
		{
			if (!(rightCenter + 0.3 >= c1.y && c1.y >= rightCenter - 0.3))
			{
				isPoop = true;
			}
			if (!isPoop)
			{
				c1.vx *= -1;
				c1.x = 1 - (c1.r+0.1); 
			}
			else if (isPoop && !scoreRecorded)
			{
				leftScore ++;
				cout << "Player 1: " << leftScore << " || Player 2: " << rightScore<<"\n";
				scoreRecorded = true;
			}
		}
		else if ( c1.x < -1 + (c1.r+0.1)) 
		{
			if (!(leftCenter + 0.3 >= c1.y && c1.y >= leftCenter - 0.3))
			{
				isPoop = true;
			}
			if (!isPoop)
			{
				c1.vx *= -1;
				c1.x = -1 + (c1.r+0.1);
			}
			else if (isPoop && !scoreRecorded)
			{
				rightScore ++;
				cout << "Player 1: " << leftScore << " || Player 2: " << rightScore<<"\n";
				scoreRecorded = true;
			}
		}

		if ( c1.y > 1 - c1.r ) {
			c1.vy *= -1;
			c1.y = 1 - c1.r;
		} else if ( c1.y < -1 + c1.r ) {
			c1.vy *= -1;
			c1.y = -1 + c1.r;
		}

		if (glfwGetKey(GLFW_KEY_UP) == GLFW_PRESS)
		{
			rightCenter += paddleSpeed;
		}
		if (glfwGetKey(GLFW_KEY_DOWN) == GLFW_PRESS)
		{
			rightCenter -= paddleSpeed;
		}

		if (glfwGetKey(GLFW_KEY_LSHIFT) == GLFW_PRESS)
		{
			leftCenter += paddleSpeed;
		}
		if (glfwGetKey(GLFW_KEY_LCTRL) == GLFW_PRESS)
		{
			leftCenter -= paddleSpeed;
		}


		//BALL RESETTER
		if (glfwGetKey(GLFW_KEY_SPACE) == GLFW_PRESS)
		{
			c1.x = 0; 
			c1.y = 0;
			c1.vx = cos(2*PIE*random());
			c1.vy = sin(2*PIE*random());
			leftCenter = 0;
			rightCenter = 0;
			isPoop = false;
			scoreRecorded = false;
		}

		glVertexPointer(2, GL_FLOAT, sizeof(Vtx), vertices);
		glColorPointer(4, GL_UNSIGNED_BYTE, sizeof(Vtx), &(vertices[0].color));
		

		drawCircle(c1);
		drawPaddles(left, right, leftCenter, rightCenter);
		//VERY IMPORTANT: displays the buffer to the screen
		glfwSwapBuffers();
	} while ( glfwGetKey(GLFW_KEY_ESC) != GLFW_PRESS &&
			glfwGetWindowParam(GLFW_OPENED) );

	glfwTerminate();
	return 0;
}
