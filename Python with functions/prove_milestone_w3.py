import tkinter as tk
from tkinter.constants import X, Y


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    #function sky
    # SKY
    draw_sky(canvas,0, 0, 800, 350)
    # SUN
    draw_sun(canvas,0,0,110,110)
    #draw birds
    draw_birds(canvas,700,125,725,100)
    draw_birds(canvas,700,125,740,125)
    draw_birds(canvas,600,125,625,100)
    draw_birds(canvas,600,125,640,125)
    draw_birds(canvas,650,75,675,50)
    draw_birds(canvas,650,75,685,75)
    draw_birds(canvas,550,35,575,20)
    draw_birds(canvas,550,35,595,35)

    # PASTURE
    draw_pasture(canvas,0, 350, 800, 500)
    
    #CLOUDS
    draw_clouds(canvas,300,150,110,100)
    draw_clouds(canvas,500,150,110,100)
    draw_clouds(canvas,450,200,750,150)
    draw_clouds(canvas,200,250,600,300)
    
    #LAKE
    draw_lake(canvas,450,400,790,500)
    
    # FISH
    draw_fish(canvas,500,430,510,420,510,440)
    draw_fish(canvas,525,475,535,465,535,485)
    draw_fish(canvas,550,450,560,430,560,470)
    draw_fish(canvas,600,450,610,430,610,470)
    draw_fish(canvas,600,480,610,470,610,490)
    draw_fish(canvas,625,430,635,420,635,440)
    draw_fish(canvas,650,450,660,430,660,470)
    draw_fish(canvas,675,475,685,465,685,485)
    draw_fish(canvas,700,450,710,430,710,470)
    
    tree_center = scene_left + 500
    tree_top = scene_top + 250
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    tree_center = scene_left + 400
    tree_top = scene_top + 300
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    tree_center = scene_left + 300
    tree_top = scene_top + 250
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    tree_center = scene_left + 200
    tree_top = scene_top + 300
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    tree_center = scene_left + 100
    tree_top = scene_top + 250
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    tree_center = scene_left + 600
    tree_top = scene_top + 300
    tree_height = 150
    
    tree_center = scene_left + 700
    tree_top = scene_top + 250
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    
# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

#function sky
def draw_sky(canvas, left, top, right, bottom):
    for i in range(top,bottom):
       canvas.create_line(left,i, right,i, fill="#51d1f6", width=1)
#draw pasture
def draw_pasture(canvas, left, top, right, bottom):
    for i in range(top,bottom):
       canvas.create_line(left,i, right,i, fill="green", width=1)
#draw clouds
def draw_clouds(canvas,left,top,right,bottom):
    canvas.create_oval(left,top,right,bottom,fill="white",outline="white", width=2)


#draw sun
def draw_sun(canvas,left,top,right,bottom):
    canvas.create_oval(left,top,right,bottom, fill="yellow",outline="yellow", width=1)
#draw birds
def draw_birds(canvas,left, top, right, bottom):
    canvas.create_line(left, top, right, bottom,fill="brown", width=1)

#draw lake
def draw_lake(canvas,left,top,right,bottom):
    canvas.create_oval(left,top,right,bottom, fill="#256D7B",outline="#256D7B", width=1)
# body fish
def draw_fish(canvas,l1,ol1,l2,ol2,l3,ol3):
    canvas.create_polygon(l1,ol1,l2,ol2,l3,ol3, fill="#E9967A", width=3)


def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

main()