#include <cmath>
#include "vec3.h"

class vec3 {
    public:
      float x;
      float y;
      float z;

      vec3(float x, float y, float z) : x(x), y(y), z(z) {}

      vec3 operator+(const vec3& u) {
        return vec3(x + u.x, y + u.y, z + u.z);
      }
      vec3 operator-(const vec3& u) {
        return vec3(x - u.x, y - u.y, z - u.z);
      }
      vec3 operator*(const vec3& u) {
        return vec3(x * u.x, y * u.y, z * u.z);
      }
      vec3 operator/(const vec3& u) {
        return vec3(x / u.x, y / u.y, z / u.z);
      }
      vec3 operator+(const float u) {
        return vec3(x + u, y + u, z + u);
      }
      vec3 operator-(const float u) {
        return vec3(x - u, y - u, z - u);
      }
      vec3 operator*(const float u) {
        return vec3(x * u, y * u, z * u);
      }
      vec3 operator/(const float u) {
        return vec3(x / u, y / u, z / u);
      }

      static float dot(const vec3& v, const vec3& u) {
        return v.x * u.x + v.y * u.y + v.z * u.z;
      }
      static float magnitude(const vec3& v) {
        return(std::sqrt(dot(v ,v)));
      }
      static vec3 normalize(const vec3& v) {
        float vm = magnitude(v);
        return v / vm;
      }
};
