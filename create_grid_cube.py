import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cube_add(size=8.5, enter_editmode=False, location=(0, 0, 0))
cube_large = bpy.context.active_object

for x in range(-3, 4, 2):
    for y in range(-3, 4, 2):
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(x, 1, y))
        cube_small = bpy.context.active_object

        cube_small.scale = (1.5, 50, 1.5)
        bpy.ops.object.transform_apply(scale=True)

        mod = cube_large.modifiers.new(name='Boolean', type='BOOLEAN')
        mod.operation = 'DIFFERENCE'
        mod.object = cube_small

        bpy.context.view_layer.objects.active = cube_large
        cube_large.select_set(True)
        bpy.ops.object.modifier_apply(modifier='Boolean')
        bpy.data.objects.remove(cube_small)



for x in range(-3, 4, 2):
    for y in range(-3, 4, 2):
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(1, x, y))
        cube_small = bpy.context.active_object

        cube_small.scale = (50, 1.5, 1.5)
        bpy.ops.object.transform_apply(scale=True)

        mod = cube_large.modifiers.new(name='Boolean', type='BOOLEAN')
        mod.operation = 'DIFFERENCE'
        mod.object = cube_small

        bpy.context.view_layer.objects.active = cube_large
        cube_large.select_set(True)
        bpy.ops.object.modifier_apply(modifier='Boolean')
        bpy.data.objects.remove(cube_small)
        
for x in range(-3, 4, 2):
    for y in range(-3, 4, 2):
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(x, y, 1))
        cube_small = bpy.context.active_object

        cube_small.scale = (1.5, 1.5, 50)
        bpy.ops.object.transform_apply(scale=True)

        mod = cube_large.modifiers.new(name='Boolean', type='BOOLEAN')
        mod.operation = 'DIFFERENCE'
        mod.object = cube_small

        bpy.context.view_layer.objects.active = cube_large
        cube_large.select_set(True)
        bpy.ops.object.modifier_apply(modifier='Boolean')
        bpy.data.objects.remove(cube_small)
        
