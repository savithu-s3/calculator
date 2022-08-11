import time
import os

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def process():
    clear_terminal()
    print("""
     _     _ _                     ______      _ 
    | |   | | |_                  / _____)    | |
    | |   | | | |_   ____ ____   | /      ____| |
    | |   | | |  _) / ___) _  |  | |     / _  | |
    | |___| | | |__| |  ( ( | |  | \____( ( | | |
    \_______|_|\___)_|   \_||_|   \______)_||_|_|
                                    BY SAVITHU_S3""")
    print("-------------------------------------------------")
    print("|                                               |")
    print(">>>       https://github.com/savithu-s3       <<<")
    print("|                                               |")
    print(">>>         savithusapumal@gmail.com          <<<")
    print("|                                               |")
    print("-------------------------------------------------")

    print("""
    =================================
      Area = 1
      Perimeter & Circumference = 2
      Volume = 3
    =================================

    Exit = Exit

    """)

    type = input("What type of calculator do you need (Enter a number from above) : ")

    yes = ["Yes","yes","Y","y"]

    def jump_process():
        time.sleep(2)
        input("Press any key to continue...")
        process()
    
    def exit_process():
        print("Exiting in 3 seconds")
        time.sleep(3)
        exit()

    # |----------------AREA SUBFUNCTIONS---------------|

    # <<<<<<<<<<<<<<< Shapes >>>>>>>>>>>>>>>

    # 1 Square
    def square_area():
        clear_terminal()
        side_len = input("Enter the side length : ")
        if side_len.isnumeric():
            side_len = int(side_len)
            sq_ar = side_len*side_len
            print("---------------------------------------------------------")
            print(">>> Area of square : ", sq_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(sq_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            square_area()


    # 2 Rectangle
    def rectangle_area():
        clear_terminal()
        rect_len = input("Enter length : ")
        rect_bread = input("Enter breadth : ")
        if (rect_len.isnumeric()) and (rect_bread.isnumeric()):
            rect_len = int(rect_len)
            rect_bread = int(rect_bread)
            rec_ar = rect_bread*rect_len
            print("---------------------------------------------------------")
            print(">>> Area of rectangle : ", rec_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(rec_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            rectangle_area()

    # 3 Circle
    def circle_area():
        clear_terminal()
        radius = input("Enter radius : ")
        if radius.isnumeric():
            radius = int(radius)
            mul_o_sev = radius%7
            pi = 3.14
            if (mul_o_sev == 0):
                pi = 22/7
            cir_ar = pi*radius*radius
            print("---------------------------------------------------------")
            print(">>> Area of circle : ", cir_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(cir_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            circle_area()

    # 4 Triangle
    def triangle_area():
        clear_terminal()
        base = input("Enter base length : ")
        height = input("Enter perpendicular height : ")
        if (base.isnumeric()) and (height.isnumeric()):
            base = int(base)
            height = int(height)
            tri_ar = (base*height)/2
            print("---------------------------------------------------------")
            print(">>> Area of triangle : ", tri_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(tri_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            triangle_area()

    # 5 Hexagon
    def hexagon_area():
        clear_terminal()
        hex_len = input("Enter length of a side : ")
        if hex_len.isnumeric():
            hex_len = int(hex_len)
            hex_ar = ((3*(3**0.5))/2)*(hex_len**2)
            hex_ar = round(hex_ar, 2)
            print("---------------------------------------------------------")
            print(">>> Area of hexagon : ", hex_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(hex_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            hexagon_area()

    # 6 Pentagon
    def pentagon_area():
        clear_terminal()
        pen_len = input("Enter length of a side : ")
        if pen_len.isnumeric():
            pen_len = int(pen_len)
            pen_ar = (1/4)*((5*(5+2*(5**0.5)))**0.5)*(pen_len**2)
            pen_ar = round(pen_ar, 2)
            print("---------------------------------------------------------")
            print(">>> Area of pentagon : ", pen_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(pen_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            pentagon_area()


    # 7 Oval
    def oval_area():
        clear_terminal()
        radius1 = input("Enter radius 1 : ")
        radius2 = input("Enter radius 2 : ")
        if (radius1.isnumeric()) and (radius2.isnumeric()):
            radius1 = int(radius1)
            radius2 = int(radius2)
            pi = 3.14
            oval_ar = pi*radius1*radius2
            oval_ar = round(oval_ar, 2)
            print("---------------------------------------------------------")
            print(">>> Area of oval : ", oval_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(oval_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            oval_area()

    # AREA OF SHAPES - SELECTOR

    def area_shapes():
        clear_terminal()
        print("""
        =================================
        ----Area Of Shapes----
        
        Square = 1
        Rectangle = 2
        Circle = 3
        Triangle = 4
        Oval = 5
        Regualar Hexagon = 6
        Regualar Pentagon = 7
        =================================
        
        Exit = Exit

        """)

        shape_area = input("Enter the number of a shape from above : ")

        if (shape_area == "1"):
            square_area()
        elif (shape_area == "2"):
            rectangle_area()
        elif (shape_area == "3"):
            circle_area()
        elif (shape_area == "4"):
            triangle_area()
        elif (shape_area == "5"):
            oval_area()
        elif (shape_area == "6"):
            hexagon_area()
        elif (shape_area == "7"):
            pentagon_area()
        elif (shape_area == "Exit" or shape_area == "exit" or shape_area == "EXIT" or shape_area == "eXIT"):
            exit_process()
        else:
            print("You entered an incorrect value")
            area_shapes()

    # <<<<<<<<<<<<<<< Solids >>>>>>>>>>>>>>>

    # 1 Cube
    def cube_area():
        clear_terminal()
        side_leng = input("Enter side Length : ")
        if side_leng.isnumeric():
            side_leng = int(side_leng)
            cube_ar = (side_leng*side_leng)*6
            print("---------------------------------------------------------")
            print(">>> Area of cube : ", cube_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(cube_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            cube_area()


    # 2 Cuboid
    def cuboid_area():
        clear_terminal()
        length = input("Enter side Length : ")
        breadth = input("Enter Breadth : ")
        height = input("Enter Height : ")
        if (length.isnumeric()) and (breadth.isnumeric()) and (height.isnumeric()):
            length = int(length)
            breadth = int(breadth)
            height = int(height)
            cuboid_ar = ((length*height)*2) + ((breadth*height)*2) + ((length*breadth)*2)
            print("---------------------------------------------------------")
            print(">>> Area of cuboid : ", cuboid_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(cuboid_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            cuboid_area()

    # 3 Ball
    def ball_area():
        clear_terminal()
        radius = input("Enter the radius : ")
        if radius.isnumeric():
            radius = int(radius)
            mul_o_sev = radius%7
            pi = 3.14
            if (mul_o_sev == 0):
                pi = 22/7
            ball_ar = (4*pi*radius*radius)
            print("---------------------------------------------------------")
            print(">>> Area of ball : ", ball_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(ball_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            ball_area()

    # 4 Cylinder
    def cylinder_area():
        clear_terminal()
        radius = input("Enter the radius of a circle : ")
        height = input("Enter the height of the cylinder : ")
        if (radius.isnumeric()) and (height.isnumeric()):
            radius = int(radius)
            height = int(height)
            mul_o_sev = radius%7
            pi = 3.14
            if (mul_o_sev == 0):
                pi = 22/7
            circ_ar = (pi*radius*radius)*2
            breadth = 2*pi*radius
            cylinder_ar = (height*breadth) + circ_ar
            print("---------------------------------------------------------")
            print(">>> Area of cylinder : ", cylinder_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(cylinder_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            cylinder_area()

    # 5 Tetrahedron
    def tetrahedron_area():
        clear_terminal()
        height = input("Enter the perpendicular height of a triangle : ")
        base = input("Enter the base length of a triangle : ")
        if (height.isnumeric()) and (base.isnumeric()):
            height = int(height)
            base = int(base)
            tri_ar = (height*base)/2
            tetra_ar = tri_ar*4
            print("---------------------------------------------------------")
            print(">>> Area of tetrahedron : ", tetra_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(tetra_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            tetrahedron_area()

    # 6 Pyramid
    def pyramid_area():
        clear_terminal()
        height = input("Enter the perpendicular height of a triangle : ")
        base = input("Enter the base length of a triangle : ")
        if (height.isnumeric()) and (base.isnumeric()):
            height = int(height)
            base = int(base)
            tri_ar = ((height*base)/2)*4
            pyr_ar = (base*base) + tri_ar
            print("---------------------------------------------------------")
            print(">>> Area of pyramid : ", pyr_ar, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(pyr_ar)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            pyramid_area()

    # AREA OF SOLIDS - SELECTOR

    def area_solids():
        clear_terminal()
        print("""
        =================================
        ----Area Of Solids----
        
        Cube = 1
        Cuboid = 2
        Ball = 3
        Cylinder = 4
        Tetrahedron = 5
        Pyramid = 6
        =================================
        
        Exit = Exit

        """)

        solid_area = input("Enter the number of a solid from above : ")

        if (solid_area == "1"):
            cube_area()
        elif (solid_area == "2"):
            cuboid_area()
        elif (solid_area == "3"):
            ball_area()
        elif (solid_area == "4"):
            cylinder_area()
        elif (solid_area == "5"):
            tetrahedron_area()
        elif (solid_area == "6"):
            pyramid_area()
        elif (solid_area == "Exit" or solid_area == "exit" or solid_area == "EXIT" or solid_area == "eXIT"):
            exit_process()
        else:
            print("You entered an incorrect value")
            area_solids()

    # |---------------PERIMETER SUBFUNCTIONS---------------|

    # 1 Square
    def square_perimeter():
        clear_terminal()
        side_length = input("Enter side length : ")
        if side_length.isnumeric():
            side_length = int(side_length)
            per_sq = side_length*4
            print("---------------------------------------------------------")
            print(">>> Perimeter of square : ", per_sq, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_sq)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            square_perimeter()

    # 2 Rectangle
    def rectangle_perimeter():
        clear_terminal()
        length = input("Enter the length : ")
        breadth = input("Enter the breadth : ")
        if (length.isnumeric()) and (breadth.isnumeric()):
            length = int(length)
            breadth = int(breadth)
            per_rec = (length*2) + (breadth*2)
            print("---------------------------------------------------------")
            print(">>> Perimeter of rectangle : ", per_rec, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_rec)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            rectangle_perimeter()

    # 3 Circle
    def circle_perimeter():
        clear_terminal()
        radius = input("Enter the radius : ")
        if radius.isnumeric():
            radius = int(radius)
            mul_o_sev = radius%7
            pi = 3.14
            if (mul_o_sev == 0):
                pi = 22/7
            per_circ = (2*pi*radius)
            print("---------------------------------------------------------")
            print(">>> Circumference of circle : ", per_circ, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_circ)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            circle_perimeter()

    # 4 Oval
    def oval_perimeter():
        clear_terminal()
        radius1 = input("Enter radius 1 : ")
        radius2 = input("Enter radius 2 : ")
        if (radius1.isnumeric()) and (radius2.isnumeric()):
            radius1 = int(radius1)
            radius2 = int(radius2)
            pi = 3.14
            per_oval = 2*pi*(((radius1**2 + radius2**2)/2)**0.5)
            per_oval = round(per_oval, 2)
            print("---------------------------------------------------------")
            print(">>> Circumference of oval : ", per_oval, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_oval)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            oval_perimeter()

    # 5 Equilateral Triangle
    def triangle_perimeter():
        clear_terminal()
        side_length = input("Enter the side length : ")
        if side_length.isnumeric():
            side_length = int(side_length)
            per_tri = side_length*3
            print("---------------------------------------------------------")
            print(">>> Perimeter of Triangle : ", per_tri, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_tri)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            triangle_perimeter()

    # 6 Regular Pentagon
    def pentagon_perimeter():
        clear_terminal()
        side_length = input("Enter the side length : ")
        if side_length.isnumeric():
            side_length = int(side_length)
            per_pent = side_length*5
            print("---------------------------------------------------------")
            print(">>> Perimeter of pentagon : ", per_pent, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_pent)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            pentagon_perimeter()

    # 7 Regular Hexagon
    def hexagon_perimeter():
        clear_terminal()
        side_length = input("Enter the side length : ")
        if side_length.isnumeric():
            side_length = int(side_length)
            per_hex = side_length*6
            print("---------------------------------------------------------")
            print(">>> Perimeter of Hexagon : ", per_hex, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_hex)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            hexagon_perimeter()


    # |---------------VOLUME SUBFUNCTIONS---------------|

    # 1 Cube
    def cube_volume():
        clear_terminal()
        side_length = input("Enter the side length : ")
        if side_length.isnumeric():
            side_length = int(side_length)
            vol_cube = side_length**3
            print("---------------------------------------------------------")
            print(">>> Volume of cube : ", vol_cube, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_cube)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            cube_volume()

    # 2 Cuboid
    def cuboid_volume():
        clear_terminal()
        length = input("Enter the length : ")
        breadth = input("Enter the breadth : ")
        height = input("Enter the height : ")
        if (length.isnumeric()) and (breadth.isnumeric()) and (height.isnumeric()):
            length = int(length)
            breadth = int(breadth)
            height = int(height)
            vol_cuboid = length*breadth*height
            print("---------------------------------------------------------")
            print(">>> Volume of cuboid : ", vol_cuboid, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_cuboid)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            cuboid_volume()

    # 3 Ball
    def ball_volume():
        clear_terminal()
        radius = input("Enter the radius : ")
        if radius.isnumeric():
            radius = int(radius)
            pi = 3.14
            vol_ball = (4/3)*pi*(radius**3)
            vol_ball = round(vol_ball, 2)
            print("---------------------------------------------------------")
            print(">>> Volume of ball : ", vol_ball, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_ball)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            ball_volume()

    # 4 Tetrahedron
    def tetrahedron_volume():
        clear_terminal()
        side_length = input("Enter the side length : ")
        if side_length.isnumeric():
            side_length = int(side_length)
            vol_tetra = side_length**3/((2**0.5)*6)
            vol_tetra = round(vol_tetra, 2)
            print("---------------------------------------------------------")
            print(">>> Volume of tetrahedron : ", vol_tetra, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_tetra)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            tetrahedron_volume()

    # 5 Pyramid
    def pyramid_volume():
        clear_terminal()
        length = input("Enter the length : ")
        width = input("Enter the width : ")
        height = input("Enter the perpendicular height : ")
        if (length.isnumeric()) and (width.isnumeric()) and (height.isnumeric()):
            length = int(length)
            width = int(width)
            height = int(height)
            vol_pyr = (1/3)*((length*width)*height)
            vol_pyr = round(vol_pyr, 2)
            print("---------------------------------------------------------")
            print(">>> Volume of pyramid : ", vol_pyr, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_pyr)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            pyramid_volume()

    # 6 Cylinder
    def cylinder_volume():
        clear_terminal()
        radius = input("Enter the radius of a circle : ")
        height = input("Enter the height : ")
        if (radius.isnumeric()) and (height.isnumeric()):
            radius = int(radius)
            height = int(height)
            pi = 3.14
            vol_cyl = pi*(radius**2)*height
            vol_cyl = round(vol_cyl, 2)
            print("---------------------------------------------------------")
            print(">>> Volume of cylinder : ", vol_cyl, "<<<")
            print("---------------------------------------------------------")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_cyl)
                print("Answer Copied...!!!")
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            cylinder_volume()

    # |---------------<MAIN FUNCTIONS>---------------|

    # AREA FUNCTION
    def area():
        clear_terminal()
        print("""
        =================================
        ----Area----
        
        Shapes = 1
        Solids = 2
        =================================

        Exit = Exit

        """)
        
        area_sel = input("Area of Shapes or Solids (Enter a number from above) : ")

        if (area_sel == "1"):
            area_shapes()
        elif (area_sel == "2"):
            area_solids()
        elif (area_sel == "Exit" or area_sel == "exit" or area_sel == "EXIT" or area_sel == "eXIT"):
            exit_process()
        else:
            print("You entered an incorrect value")
            area()

    # PERIMETER FUNCTION
    def perimeter():
        clear_terminal()
        print("""
        =================================
        ----Perimeter & Circumference----
        
        Square = 1
        Rectangle = 2
        Circle = 3
        Oval = 4
        Equilateral Triangle = 5
        Regular Pentagon = 6
        Regular Hexagon = 7
        =================================
        
        Exit = Exit

        """)

        perimeter_sel = input("Enter the number of a Shape from above : ")

        if (perimeter_sel == "1"):
            square_perimeter()
        elif (perimeter_sel == "2"):
            rectangle_perimeter()
        elif (perimeter_sel == "3"):
            circle_perimeter()
        elif (perimeter_sel == "4"):
            oval_perimeter()
        elif (perimeter_sel == "5"):
            triangle_perimeter()
        elif (perimeter_sel == "6"):
            pentagon_perimeter()
        elif (perimeter_sel == "7"):
            hexagon_perimeter()
        elif (perimeter_sel == "Exit" or perimeter_sel == "exit" or perimeter_sel == "EXIT" or perimeter_sel == "eXIT"):
            exit_process()
        else:
            print("You entered an incorrect value")
            perimeter()

    # VOLUME FUNCTION
    def volume():
        clear_terminal()
        print("""
        =================================
        ----Volume----
        
        Cube = 1
        Cuboid = 2
        Ball = 3
        Tetrahedron = 4
        Pyramid = 5
        Cylinder = 6
        =================================
        
        Exit = Exit
        
        """)

        volume_sel = input("Enter the number of a Solid from above : ")

        if (volume_sel == "1"):
            cube_volume()
        elif (volume_sel == "2"):
            cuboid_volume()
        elif (volume_sel == "3"):
            ball_volume()
        elif (volume_sel == "4"):
            tetrahedron_volume()
        elif (volume_sel == "5"):
            pyramid_volume()
        elif (volume_sel == "6"):
            cylinder_volume()
        elif (volume_sel == "Exit" or volume_sel == "exit" or volume_sel == "EXIT" or volume_sel == "eXIT"):
            exit_process()
        else:
            print("You entered an incorrect value")
            volume()

    if (type == "1"):
        area()
    elif (type == "2"):
        perimeter()
    elif (type == "3"):
        volume()
    elif (type == "Exit" or type == "exit" or type == "EXIT" or type == "eXIT"):
        exit_process()
    else:
        print("You entered an incorrect value")
        time.sleep(2)
        process()

process()