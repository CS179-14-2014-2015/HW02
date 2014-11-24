#include <GL/glfw.h>
#include <iostream>
#include <cmath>
#include <cassert>

#define 	GLFW_KEY_W   87	
#define 	GLFW_KEY_S   83
#define 	GLFW_KEY_D   68
#define 	GLFW_KEY_A   65


using namespace std;
const GLfloat PIE = 3.14159265f;


const GLfloat CIRCLE_RADIUS = 0.040f;
const GLuint CIRCLE_COLORS[] = { 0x550000FF, 0x55FF0000, 0x5500FF00 };


const GLfloat CENTER_DISTANCE = 0.3f;
const GLfloat ROTATION_SPEED = 0.5f;
const GLsizei N_VERTICES_PER_CIRCLE = 32;
const GLsizei N_VERTICES_PER_RECTANGLE = 4;
GLfloat XY_OFFSET[] = {0, 0};
GLfloat XY_OFFSET2[] = {0, 0};
GLfloat moveSpeed = 0.03f;
GLfloat STARTERX_OFFSET[] = {-1, 0.9};
GLfloat STARTERY_OFFSET[] = {-0.1, -0.1};
GLfloat starter = 4;
int leftScore = 0;
int rightScore = 0;
const GLenum BLENDING_FACTOR[] = {GL_SRC_COLOR, GL_ONE};

struct Vtx {
	GLfloat x, y;
	GLuint color;
};

struct Circle {
	GLfloat x, y, vx, vy, r;
};



Vtx vertices[(N_VERTICES_PER_RECTANGLE*2) + N_VERTICES_PER_CIRCLE];

void arrowkeys(char key)
{
	if (key == glfwGetKey(GLFW_KEY_W))
	{
		if(STARTERY_OFFSET[0] >= 1-0.4)
		{
			STARTERY_OFFSET[0] = 1-0.4;
		}
		else
		{
			STARTERY_OFFSET[0] += moveSpeed;
		}
	}

	if (key == glfwGetKey(GLFW_KEY_S))
	{
		
		if(STARTERY_OFFSET[0] <= -1)
		{
			STARTERY_OFFSET[0] = -1;
		}
		else 
		{
			STARTERY_OFFSET[0] -= moveSpeed;
		}
		
	}

	if (key == glfwGetKey(GLFW_KEY_UP))
	{
		if(STARTERY_OFFSET[1] >= 0.6)
		{
			STARTERY_OFFSET[1] = 0.6;
		}
		else
		{
			STARTERY_OFFSET[1] += moveSpeed;
		}
	}

	if (key == glfwGetKey(GLFW_KEY_DOWN))
	{
		
		if(STARTERY_OFFSET[1] <= -1)
		{
			STARTERY_OFFSET[1] = -1;
		}
		else 
		{
			STARTERY_OFFSET[1] -= moveSpeed;
		}
		
	}
	
}
void generateRectangle(GLfloat startingX, GLfloat startingY, GLuint start)
{
	vertices[0+start].x = startingX;
	vertices[1+start].x = startingX; 
	vertices[2+start].x = startingX + 0.1f;
	vertices[3+start].x = startingX + 0.1f;

	vertices[0+start].y = startingY;
	vertices[1+start].y = startingY + 0.4f;
	vertices[2+start].y = startingY + 0.4f; 
	vertices[3+start].y = startingY;
}




void drawRectangles(GLfloat leftX, GLfloat leftY, GLfloat rightX, GLfloat rightY, GLfloat starterLeft, GLfloat starterRight)
{
	generateRectangle(leftX, leftY, starterLeft);
	generateRectangle(rightX, rightY, starterRight);
	glDrawArrays(GL_TRIANGLE_FAN, 0, N_VERTICES_PER_RECTANGLE);
	glDrawArrays(GL_TRIANGLE_FAN, N_VERTICES_PER_RECTANGLE, N_VERTICES_PER_RECTANGLE);
	
}





void generatePolygon(GLfloat radius, GLfloat angularOffset, GLfloat x, GLfloat y, GLvoid *pointer, GLsizei nVertices, GLuint stride) {
	assert(nVertices >= 3);
	GLfloat *vtx = (GLfloat*)pointer;
	vtx[0] = x;
	vtx[1] = y;

	const GLfloat n = nVertices - 2;
	const GLfloat factor = 2.0f * PIE/n;
	for ( GLsizei i = 1; i <= n + 1; ++i ) {
		GLfloat theta = i * factor;
		
		GLfloat *vtx = (GLfloat*)(((GLubyte*)pointer) + stride * i);
		vtx[0] = radius * std::cos(angularOffset + theta) + x;
		vtx[1] = radius * std::sin(angularOffset + theta) + y;
	}
}

void drawCircle(const Circle &c) {
	generatePolygon(c.r, 0, c.x, c.y, vertices +(2*N_VERTICES_PER_RECTANGLE), N_VERTICES_PER_CIRCLE, sizeof(Vtx));
	glDrawArrays(GL_TRIANGLE_FAN, 2*N_VERTICES_PER_RECTANGLE, N_VERTICES_PER_CIRCLE);
}


int main() {
	if ( !glfwInit() ) {
		std::cerr << "Unable to initialize OpenGL!\n";
		return -1;
	}

	if ( !glfwOpenWindow(640,640, //width and height of the screen
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

	Circle c1 = { 0, 0, 1, 1, CIRCLE_RADIUS};
	
	//sets up the color of the vertices
	for ( size_t i = 0; i < N_VERTICES_PER_RECTANGLE; ++i ) {
		vertices[i].color = CIRCLE_COLORS[0];
	}

	for ( size_t i = N_VERTICES_PER_RECTANGLE; i < 2 * N_VERTICES_PER_RECTANGLE; ++i ) {
		vertices[i].color = CIRCLE_COLORS[1];
	}
	
	for ( size_t i = 2*N_VERTICES_PER_RECTANGLE; i < ((2 * N_VERTICES_PER_RECTANGLE) + N_VERTICES_PER_CIRCLE); ++i ) {
		vertices[i].color = CIRCLE_COLORS[2];
	}
	
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	double t = 0;
	double dt = 0.03f;
	do {
		int width, height;
		// Get window size (may be different than the requested size)
		//we do this every frame to accommodate window resizing.
		glfwGetWindowSize( &width, &height );
		glViewport( 0, 0, width, height );

		glClear(GL_COLOR_BUFFER_BIT);

		glDisable(GL_BLEND);
		
		glEnable(GL_BLEND);
		
		glVertexPointer(2, GL_FLOAT, sizeof(Vtx), vertices);
		glColorPointer(4, GL_UNSIGNED_BYTE, sizeof(Vtx), &(vertices[0].color));
		if ((leftScore<10)&&(rightScore<10))
		{
			t += dt;
		}
		if (t>=1)
		{
			
			c1.x += c1.vx * dt;
			c1.y += c1.vy * dt;
		
		}
		if ( c1.x > 1 - c1.r ) {
			c1.x = 0;
			c1.y = 0;
			leftScore++;
			cout << "Player 1: " << leftScore << "  Player 2: " << rightScore<<"\n";
			STARTERY_OFFSET[0] = -0.1;
			STARTERY_OFFSET[1] = -0.1;
			t=0;
			if (leftScore == 10)
			{
				cout<< "Player 1 WINS! \n";
				cout<< "Press SPACEBAR to play again.\nPress ESC to exit.\n";
				
			}
		} else if ( c1.x < -1 + c1.r ) {
			c1.x = 0;
			c1.y = 0;
			rightScore++;
			cout << "Player 1: " << leftScore << "  Player 2: " << rightScore<<"\n";
			STARTERY_OFFSET[0] = -0.1;
			STARTERY_OFFSET[1] = -0.1;
			t = 0;
			if (rightScore == 10)
			{
				cout<< "Player 2 WINS! \n";
				cout<< "Press SPACEBAR to play again.\nPress ESC to exit.\n";
			}
		}

		if ( c1.y > 1 - c1.r ) {
			c1.vy *= -1;
			c1.y = 1 - c1.r;
		} else if ( c1.y < -1 + c1.r ) {
			c1.vy *= -1;
			c1.y = -1 + c1.r;
		}

		//ball movement when hit by paddle
		if (c1.x <= STARTERX_OFFSET[0]+0.1)
		{

			if ((c1.y >= STARTERY_OFFSET[0]) && (c1.y <= STARTERY_OFFSET[0]+0.4f))
			{
				c1.vx *= -1;
				c1.x = STARTERX_OFFSET[0]+0.1 + c1.r;
			}
		}

		if (c1.x >= STARTERX_OFFSET[1])
		{

			if ((c1.y >= STARTERY_OFFSET[1]) && (c1.y <= STARTERY_OFFSET[1]+0.4f))
			{
				c1.vx *= -1;
				c1.x = STARTERX_OFFSET[1] - c1.r;
			}
		}

		//<play>
		//glBlendEquation(GL_FUNC_ADD);
		
		if (GLFW_PRESS == glfwGetKey(GLFW_KEY_SPACE))
		{
			leftScore = 0;
			rightScore = 0;
			c1.x = 0;
			c1.y = 0;
			t = 0;
			STARTERY_OFFSET[0] = -0.1;
			STARTERY_OFFSET[1] = -0.1;
			cout << "RESTART!\n";
		}
		arrowkeys(GLFW_PRESS);
	
		drawCircle(c1);

		drawRectangles(STARTERX_OFFSET[0], STARTERY_OFFSET[0], STARTERX_OFFSET[1], STARTERY_OFFSET[1], 0, starter);
		//dt = 0.03;
		//glBlendEquation(GL_MAX);
		
		//</play>

		//VERY IMPORTANT: displays the buffer to the screen
		glfwSwapBuffers();
	} while ( glfwGetKey(GLFW_KEY_ESC) != GLFW_PRESS &&
			glfwGetWindowParam(GLFW_OPENED) );

	glfwTerminate();
	return 0;
}
