// Local headers
#include "program.hpp"
#include "gloom/gloom.hpp"
#include "gloom/shader.hpp"
#include "glm/glm.hpp"
#include "glm/gtx/transform.hpp"
#include "glm/mat4x4.hpp"
#include "glm/vec3.hpp"
#include "glm/vec2.hpp"
#include "glm/gtc/matrix_transform.hpp"
#include "glm/gtc/type_ptr.hpp"

glm::vec3 positions(0.0f, 0.0f, 5.0f); //x, y, z
glm::vec2 angles(0.0f, 0.0f); //x - yaw - horizontal, y - pitch - vertical
GLfloat movementSpeed = 0.2;
GLfloat angleSpeed = 0.1;

void runProgram(GLFWwindow* window)
{
	// Set GLFW callback mechanism(s)
	glfwSetKeyCallback(window, keyboardCallback);

	// Enable depth (Z) buffer (accept "closest" fragment)
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LESS);

	// Configure miscellaneous OpenGL settings
	glEnable(GL_CULL_FACE);

	// Set default colour after clearing the colour buffer
	glClearColor(0.3f, 0.3f, 0.4f, 1.0f);

	// Set up your scene here (create Vertex Array Objects, etc.)
	printGLError();
	GLuint createVAO(GLfloat* vertices, GLuint verticesLen, GLuint* indices, GLuint indicesLen, GLfloat* colours, GLuint coloursLen);
	glm::mat4 camera();
	GLfloat vertices[] = { 
		-1.000f, -1.00f, 0.0f,
		 0.000f, -1.00f, 0.0f,
		 1.000f, -1.00f, 0.0f,
		-0.500f,  0.00f, 0.0f,
		 0.500f,  0.00f, 0.0f,
		 0.000f,  1.00f, 0.0f,
		-0.250f, -0.50f, 0.0f,
		 0.000f, -0.50f, 0.0f,
		 0.250f, -0.50f, 0.0f,
		-0.125f, -0.25f, 0.0f,
		 0.125f, -0.25f, 0.0f,
		 0.000f,  0.00f, 0.0f, 
	};
	GLuint indices[] = { 
		0, 1, 3,
		1, 2, 4,
		3, 4, 5,
		6, 7, 9,
		7, 8, 10,
		9, 10, 11 
	};
	GLfloat colours[] = { 
		0.583f, 0.771f, 0.014f,
		0.609f, 0.115f, 0.436f,
		0.327f, 0.483f, 0.844f,
		0.822f, 0.569f, 0.201f,
		0.435f, 0.602f, 0.223f,
		0.597f, 0.770f, 0.761f,
		0.559f, 0.436f, 0.730f,
		0.359f, 0.583f, 0.152f,
		0.327f, 0.483f, 0.844f,
		0.559f, 0.861f, 0.639f,
		1.000f, 1.000f, 1.000f,
		0.195f, 0.548f, 0.859f 
	};
	glm::mat4x4 transform2 = glm::mat4(1);
	printGLError();
	GLuint verticesLen = 36;
	GLuint indicesLen = 18;
	GLuint colourLen = 36;
	GLuint vaoid = createVAO(vertices, verticesLen, indices, indicesLen, colours, colourLen);
	printGLError();
	Gloom::Shader shader;
	shader.makeBasicShader(
		"D:/Prosjekter/Visdat/Digital-Image-Processing/oving4/gloom/gloom/shaders/simple.vert",
		"D:/Prosjekter/Visdat/Digital-Image-Processing/oving4/gloom/gloom/shaders/simple.frag"
	);
	printGLError();

	// Rendering Loop
	while (!glfwWindowShouldClose(window))
	{
		// Clear colour and depth buffers
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		// Draw your scene here
		// Activate shader program
		shader.activate();
		glBindVertexArray(vaoid);
		glUniformMatrix4fv(0, 1, GL_FALSE, &camera()[0][0]);
		glDrawElements(GL_TRIANGLES, indicesLen, GL_UNSIGNED_INT, 0);
		//glDrawArrays(GL_TRIANGLES, 0, 3);
		printGLError();
		// Deactivate shader program
		shader.deactivate();

		// Handle other events
		glfwPollEvents();

		// Flip buffers
		glfwSwapBuffers(window);
	}
}


void keyboardCallback(GLFWwindow* window, int key, int scancode,
	int action, int mods)
{
	// Use escape key for terminating the GLFW window
	if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
	{
		glfwSetWindowShouldClose(window, GL_TRUE);
	}
	// Move left
	if (key == GLFW_KEY_A && action == GLFW_PRESS)
	{
		positions.x -= movementSpeed;
	}
	// Move right
	else if (key == GLFW_KEY_D && action == GLFW_PRESS)
	{
		positions.x += movementSpeed;
	}
	// Move forward
	if (key == GLFW_KEY_W && action == GLFW_PRESS)
	{
		positions.z -= movementSpeed;
	}
	// Move back
	else if (key == GLFW_KEY_S && action == GLFW_PRESS)
	{
		positions.z += movementSpeed;
	}
	// Move up
	if (key == GLFW_KEY_E && action == GLFW_PRESS)
	{
		positions.y += movementSpeed;
	}
	// Move down
	else if (key == GLFW_KEY_Q && action == GLFW_PRESS)
	{
		positions.y -= movementSpeed;
	}
	// Rotate horizontally clockwise
	if (key == GLFW_KEY_RIGHT && action == GLFW_PRESS)
	{
		angles.x += angleSpeed;
	}
	// Rotate horizontally anti clockwise
	else if (key == GLFW_KEY_LEFT && action == GLFW_PRESS)
	{
		angles.x -= angleSpeed;
	}
	// Rotate vertically clockwise
	if (key == GLFW_KEY_DOWN && action == GLFW_PRESS)
	{
		angles.y -= angleSpeed;
	}
	// Rotate vertically anti clockwise
	else if (key == GLFW_KEY_UP && action == GLFW_PRESS)
	{
		angles.y += angleSpeed;
	}

}

GLuint createVAO(GLfloat* vertices, GLuint verticesLen, GLuint* indices, GLuint indicesLen, GLfloat* colours, GLuint coloursLen)
{
	GLuint vaoid = 0;
	glGenVertexArrays(1, &vaoid); // Create new VAO
	glBindVertexArray(vaoid); // Bind the VAO

	GLuint vboid1 = 0;
	glGenBuffers(1, &vboid1); // Create new VBO
	glBindBuffer(GL_ARRAY_BUFFER, vboid1); // Bind the VBO
	glBufferData(GL_ARRAY_BUFFER, verticesLen * sizeof(GLfloat), vertices, GL_STATIC_DRAW);
	GLuint vertexAttribID1 = 0;
	glVertexAttribPointer(vertexAttribID1, 3, GL_FLOAT, GL_FALSE, 0, 0);
	glEnableVertexAttribArray(vertexAttribID1);

	GLuint vboid2 = 0;
	glGenBuffers(1, &vboid2); // Create new VBO
	glBindBuffer(GL_ARRAY_BUFFER, vboid2); // Bind the VBO
	glBufferData(GL_ARRAY_BUFFER, coloursLen * sizeof(GLfloat), colours, GL_STATIC_DRAW);
	GLuint vertexAttribID2 = 1;
	glVertexAttribPointer(vertexAttribID2, 3, GL_FLOAT, GL_FALSE, 0, 0);
	glEnableVertexAttribArray(vertexAttribID2);

	GLuint ibid = 0;
	glGenBuffers(1, &ibid);
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibid);
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, indicesLen * sizeof(GLuint), indices, GL_STATIC_DRAW);

	return vaoid;
}

glm::mat4 camera()
{
	glm::mat4 projection = glm::perspective(glm::radians(45.0f), 1.0f, 0.1f, 100.0f);
	glm::mat4 view = glm::rotate(glm::mat4(1.0f), angles.y, glm::vec3(-1.0f, 0.0f, 0.0f));
	view = glm::rotate(view, angles.x, glm::vec3(0.0f, 1.0f, 0.0f));
	view = glm::translate(view, -positions);
	return projection * view;
}