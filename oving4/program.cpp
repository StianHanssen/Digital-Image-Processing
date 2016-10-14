// Local headers
#include "program.hpp"
#include "gloom/gloom.hpp"
#include "gloom/shader.hpp"


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
	unsigned int createVAO(float* vertices, GLuint verticesLen, unsigned int* indices, GLuint indicesLen);
	float vertices[] = {-0.6, -0.6, 0.0, 0.6, -0.6, 0.0, 0.0, 0.6, 0.0};
	float vertices2[] = { -1.0, -1.0, 0.0, 
						  0.0, -1.0, 0.0, 
						  1.0, -1.0, 0.0,
						  -0.5, 0.0, 0.0,
						  0.5, 0.0, 0.0, 
						  0.0, 1.0, 0.0,
						  0.9, 0.7, 0.0,
						  0.9, 0.9, 0.0, 
						  0.7, 0.9, 0.0,
						  -0.9, 0.7, 0.0,
						  -0.7, 0.9, 0.0,
						  -0.9, 0.9, 0.0, };
	float vertices3[] = { 0.6, -0.8, -1.2, 0.0, 0.4, 0.0, -0.8, -0.2, 1.2 };
	unsigned int indices[] = {0, 1, 2};
	unsigned int indices2[] = {0, 1, 3, 1, 2, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11};
	GLuint verticesLen = 36;
	GLuint indicesLen = 15;
	unsigned int vaoid = createVAO(vertices2, verticesLen,  indices2, indicesLen);
	printGLError();
	Gloom::Shader shader;
	shader.makeBasicShader("D:/Prosjekter/Visdat/Digital-Image-Processing/oving4/gloom/gloom/shaders/simple.vert",
						   "D:/Prosjekter/Visdat/Digital-Image-Processing/oving4/gloom/gloom/shaders/simple.frag");
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
}

unsigned int createVAO(float* vertices, GLuint verticesLen, unsigned int* indices, GLuint indicesLen)
{
	unsigned int vaoid = 0;
	glGenVertexArrays(1, &vaoid); // Create new VAO
	glBindVertexArray(vaoid); // Bind the VAO

	unsigned int vboid = 0;
	glGenBuffers(1, &vboid); // Create new VBO
	glBindBuffer(GL_ARRAY_BUFFER, vboid); // Bind the VBO
	glBufferData(GL_ARRAY_BUFFER, verticesLen * sizeof(float), vertices, GL_STATIC_DRAW);
	unsigned int vertexAttribID1 = 0;
	glVertexAttribPointer(vertexAttribID1, 3, GL_FLOAT, GL_FALSE, 0, 0);
	glEnableVertexAttribArray(vertexAttribID1);

	unsigned int ibid = 0;
	glGenBuffers(1, &ibid);
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibid);
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, indicesLen * sizeof(unsigned int), indices, GL_STATIC_DRAW);

	return vaoid;
}