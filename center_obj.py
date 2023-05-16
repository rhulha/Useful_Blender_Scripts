import bpy
from mathutils import Vector

obj = bpy.context.active_object

# error
# bbox_center = 0.5 * (obj.bound_box[0] + obj.bound_box[6])
# obj.location = bbox_center

bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
center, radius = Vector(), 0
for corner in bbox_corners:
    center += corner
center /= 8
for corner in bbox_corners:
    radius = max(radius, (corner - center).length)

obj.location = -center

