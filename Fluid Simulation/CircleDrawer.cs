using UnityEngine;

[RequireComponent(typeof(LineRenderer))]
public class CircleUtility : MonoBehaviour
{
    private LineRenderer lineRenderer;

    [Header("Resolution Settings")]
    [Range(10, 100)]
    public int segments = 50;
    public float lineWidth = 0.1f;

    void Awake()
    {
        lineRenderer = GetComponent<LineRenderer>();
        lineRenderer.useWorldSpace = true;
        lineRenderer.loop = true;
        
        if (lineRenderer.material == null)
        {
            lineRenderer.material = new Material(Shader.Find("Sprites/Default"));
        }
    }

    public void DrawCircle(Vector2 position, float radius, Color color)
    {
        lineRenderer.widthMultiplier = lineWidth;
        lineRenderer.startColor = color;
        lineRenderer.endColor = color;
        lineRenderer.positionCount = segments;
        
        for (int i = 0; i < segments; i++)
        {
            float progress = (float)i / segments;
            float angle = progress * 2 * Mathf.PI;
            float xOffset = Mathf.Cos(angle) * radius;
            float yOffset = Mathf.Sin(angle) * radius;
            Vector3 pointWorldPosition = new Vector3(position.x + xOffset, position.y + yOffset, 0);

            lineRenderer.SetPosition(i, pointWorldPosition);
        }
    }
}
