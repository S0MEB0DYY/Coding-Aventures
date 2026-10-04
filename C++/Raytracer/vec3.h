#ifndef VEC3_H
#define VEC3_H
#include <cmath>

class vec3 {
    public:
      float x;
      float y;
      float z;

      vec3(float x, float y, float z);

      vec3 operator+(const vec3& u);
      vec3 operator-(const vec3& u);
      vec3 operator*(const vec3& u);
      vec3 operator/(const vec3& u);
      vec3 operator+(const float u);
      vec3 operator-(const float u);
      vec3 operator*(const float u);
      vec3 operator/(const float u);


      static float dot(const vec3& v, const vec3& u);
      static float magnitude(const vec3& v);
      static vec3 normalize(const vec3& v);
}
#endif
