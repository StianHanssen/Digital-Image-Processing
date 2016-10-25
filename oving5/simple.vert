#version 430 core

layout(location = 0) in vec3 position;
layout(location = 1) in vec3 vertexColor;
layout(location = 0) uniform mat4 transform;
out vec3 fragmentColor;

void main()
{
	gl_Position = transform * vec4(position, 1.0f);
	fragmentColor = vertexColor;
}
