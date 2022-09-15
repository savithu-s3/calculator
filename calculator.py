import time
import os
import pyperclip

history_file = "history.txt"
current_time = time.asctime()
clearHis = ["clshis","CLSHIS","Clshis","cLshis","CLShis","ClsHis","CLsHIs","clsHIS","clsHis"]

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def clear_history():
    with open(history_file, 'w') as clearFile:
        clearFile.write("")
        print("History file cleared...!")
        print("Wait 2 seconds..")
        time.sleep(2)
        process()

def process():
    clear_terminal()
    print("""
    \u001b[31;1m _     _ _                  \u001b[32;1m   ______      _ 
    \u001b[31;1m| |   | | |_                \u001b[32;1m  / _____)    | |
    \u001b[31;1m| |   | | | |_   ____ ____  \u001b[32;1m | /      ____| |
    \u001b[31;1m| |   | | |  _) / ___) _  | \u001b[32;1m | |     / _  | |
    \u001b[31;1m| |___| | | |__| |  ( ( | | \u001b[32;1m | \____( ( | | |
    \u001b[31;1m\_______|_|\___)_|   \_||_| \u001b[32;1m  \______)_||_|_|
    \u001b[31;1m                                \u001b[33;1mBY SAVITHU_S3\u001b[0m""")
    print("")
    print("\u001b[31;1mUltra \u001b[32;1mCal\u001b[0m🧮 - \u001b[34;1mVersion 2.2\u001b[0m")
    print("-------------------------------------------------")
    print("|                                               |")
    print(">>>       https://github.com/savithu-s3       <<<")
    print("|                                               |")
    print(">>>         savithusapumal@gmail.com          <<<")
    print("|                                               |")
    print("-------------------------------------------------")

    print("""
    \u001b[34m=================================\u001b[0m
      Area = 1
      Perimeter & Circumference = 2
      Volume = 3
    \u001b[34m=================================\u001b[0m
    
    Clear History = \u001b[33mclshis\u001b[0m
    Exit = \u001b[31mExit\u001b[0m

    """)

    type = input("What type of calculator do you need (Enter a number from above) or enter the command : ")

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
            sq_ar = str(sq_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of square :  " + sq_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of square :  \u001b[33;1m" + sq_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(sq_ar)
                print("Answer Copied...!!!")
                jump_process()
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
            rec_ar = str(rec_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of rectangle :  " + rec_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of rectangle :  \u001b[33;1m" + rec_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(rec_ar)
                print("Answer Copied...!!!")
                jump_process()
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            rectangle_area()

    # 3 Circle
    def circle_area():
        clear_terminal()
        print("""
        \u001b[34m=================================\u001b[0m
          Full Circle = 1
          Semicircle = 2
          Quarter circle = 3
        \u001b[34m=================================\u001b[0m
    
        Clear History = \u001b[33mclshis\u001b[0m
        Exit = \u001b[31mExit\u001b[0m

        """)
        circle_type = input("Enter the type of circle : ")
        if circle_type == "1":
            clear_terminal()
            radius = input("Enter radius : ")
            if radius.isnumeric():
                radius = int(radius)
                mul_o_sev = radius%7
                pi = 3.14
                if (mul_o_sev == 0):
                    pi = 22/7
                cir_ar = pi*radius*radius
                cir_ar = str(cir_ar)
                with open(history_file, 'r') as historyFileR:
                    readF = historyFileR.read()
                with open(history_file, 'w') as historyFileW:
                    historyFileW.write(readF + "\n" + current_time + " [Area of circle :  " + cir_ar + "]")
                print("\u001b[34m---------------------------------------------------------\u001b[0m")
                print(">>> Area of circle :  \u001b[33;1m" + cir_ar + "\u001b[0m <<<")
                print("\u001b[34m---------------------------------------------------------\u001b[0m")
                copy = input("Do you need to copy the answer : ")
                if copy in yes:
                    pyperclip.copy(cir_ar)
                    print("Answer Copied...!!!")
                    jump_process()
                else:
                    jump_process()
            else:
                print("Please enter only numbers!")
                circle_area()
        elif circle_type == "2":
            clear_terminal()
            radius = input("Enter radius : ")
            if radius.isnumeric():
                radius = int(radius)
                mul_o_sev = radius%7
                pi = 3.14
                if (mul_o_sev == 0):
                    pi = 22/7
                semicir_ar = (pi*radius*radius)/2
                semicir_ar = str(semicir_ar)
                with open(history_file, 'r') as historyFileR:
                    readF = historyFileR.read()
                with open(history_file, 'w') as historyFileW:
                    historyFileW.write(readF + "\n" + current_time + " [Area of semicircle :  " + semicir_ar + "]")
                print("\u001b[34m---------------------------------------------------------\u001b[0m")
                print(">>> Area of semicircle :  \u001b[33;1m" + semicir_ar + "\u001b[0m <<<")
                print("\u001b[34m---------------------------------------------------------\u001b[0m")
                copy = input("Do you need to copy the answer : ")
                if copy in yes:
                    pyperclip.copy(semicir_ar)
                    print("Answer Copied...!!!")
                    jump_process()
                else:
                    jump_process()
            else:
                print("Please enter only numbers!")
                circle_area()
        elif circle_type == "3":
            clear_terminal()
            radius = input("Enter radius : ")
            if radius.isnumeric():
                radius = int(radius)
                mul_o_sev = radius%7
                pi = 3.14
                if (mul_o_sev == 0):
                    pi = 22/7
                quartcir_ar = (pi*radius*radius)/4
                quartcir_ar = str(quartcir_ar)
                with open(history_file, 'r') as historyFileR:
                    readF = historyFileR.read()
                with open(history_file, 'w') as historyFileW:
                    historyFileW.write(readF + "\n" + current_time + " [Area of quarter circle :  " + quartcir_ar + "]")
                print("\u001b[34m---------------------------------------------------------\u001b[0m")
                print(">>> Area of semicircle :  \u001b[33;1m" + quartcir_ar + "\u001b[0m <<<")
                print("\u001b[34m---------------------------------------------------------\u001b[0m")
                copy = input("Do you need to copy the answer : ")
                if copy in yes:
                    pyperclip.copy(quartcir_ar)
                    print("Answer Copied...!!!")
                    jump_process()
                else:
                    jump_process()
            else:
                print("Please enter only numbers!")
                circle_area()
        else:
            print("Enter a correct value...!")
            time.sleep(3)
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
            tri_ar = str(tri_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of triangle :  " + tri_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of triangle :  \u001b[33;1m" + tri_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(tri_ar)
                print("Answer Copied...!!!")
                jump_process()
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
            hex_ar = str(hex_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of hexagon :  " + hex_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of hexagon :  \u001b[33;1m" + hex_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(hex_ar)
                print("Answer Copied...!!!")
                jump_process()
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
            pen_ar = str(pen_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of pentagon :  " + pen_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of pentagon :  \u001b[33;1m" + pen_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(pen_ar)
                print("Answer Copied...!!!")
                jump_process()
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
            oval_ar = str(oval_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of oval :  " + oval_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of oval :  \u001b[33;1m" + oval_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(oval_ar)
                print("Answer Copied...!!!")
                jump_process()
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            oval_area()

    # AREA OF SHAPES - SELECTOR

    def area_shapes():
        clear_terminal()
        print("""
        \u001b[34m=================================\u001b[0m
        ----Area Of Shapes----
        
        Square = 1
        Rectangle = 2
        Circle = 3
        Triangle = 4
        Oval = 5
        Regualar Hexagon = 6
        Regualar Pentagon = 7
        \u001b[34m=================================\u001b[0m
        
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
            cube_ar = str(cube_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of cube :  " + cube_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of cube :  \u001b[33;1m" + cube_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(cube_ar)
                print("Answer Copied...!!!")
                jump_process()
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
            cuboid_ar = str(cuboid_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of cuboid :  " + cuboid_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of cuboid :  \u001b[33;1m" + cuboid_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(cuboid_ar)
                print("Answer Copied...!!!")
                jump_process()
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
            ball_ar = str(ball_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of ball :  " + ball_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of ball :  \u001b[33;1m" + ball_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(ball_ar)
                print("Answer Copied...!!!")
                jump_process()
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
            cylinder_ar = str(cylinder_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of cylinder :  " + cylinder_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of cylinder :  \u001b[33;1m" + cylinder_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(cylinder_ar)
                print("Answer Copied...!!!")
                jump_process()
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
            tetra_ar = str(tetra_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of tetrahedron :  " + tetra_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of tetrahedron :  \u001b[33;1m" + tetra_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(tetra_ar)
                print("Answer Copied...!!!")
                jump_process()
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
            pyr_ar = str(pyr_ar)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Area of pyramid :  " + pyr_ar + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Area of pyramid :  \u001b[33;1m" + pyr_ar + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(pyr_ar)
                print("Answer Copied...!!!")
                jump_process()
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            pyramid_area()

    # AREA OF SOLIDS - SELECTOR

    def area_solids():
        clear_terminal()
        print("""
        \u001b[34m=================================\u001b[0m
        ----Area Of Solids----
        
        Cube = 1
        Cuboid = 2
        Ball = 3
        Cylinder = 4
        Tetrahedron = 5
        Pyramid = 6
        \u001b[34m=================================\u001b[0m
        
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
            per_sq = str(per_sq)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Perimeter of square :  " + per_sq + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Perimeter of square :  \u001b[33;1m" + per_sq + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_sq)
                print("Answer Copied...!!!")
                jump_process()
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
            per_rec = str(per_rec)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Perimeter of rectangle :  " + per_rec + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Perimeter of rectangle :  \u001b[33;1m" + per_rec + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_rec)
                print("Answer Copied...!!!")
                jump_process()
            else:
                jump_process()
        else:
            print("Please enter only numbers!")
            rectangle_perimeter()

    # 3 Circle
    def circle_perimeter():
        clear_terminal()
        print("""
        \u001b[34m=================================\u001b[0m
          Full Circle = 1
          Semicircle = 2
        \u001b[34m=================================\u001b[0m
    
        Clear History = \u001b[33mclshis\u001b[0m
        Exit = \u001b[31mExit\u001b[0m

        """)
        circle_type = input("Enter the type of circle : ")
        if circle_type == "1":
            radius = input("Enter the radius : ")
            if radius.isnumeric():
                radius = int(radius)
                mul_o_sev = radius%7
                pi = 3.14
                if (mul_o_sev == 0):
                    pi = 22/7
                per_circ = (2*pi*radius)
                per_circ = str(per_circ)
                with open(history_file, 'r') as historyFileR:
                    readF = historyFileR.read()
                with open(history_file, 'w') as historyFileW:
                    historyFileW.write(readF + "\n" + current_time + " [Circumference of circle :  " + per_circ + "]")
                print("\u001b[34m---------------------------------------------------------\u001b[0m")
                print(">>> Circumference of circle :  \u001b[33;1m" + per_circ + "\u001b[0m <<<")
                print("\u001b[34m---------------------------------------------------------\u001b[0m")
                copy = input("Do you need to copy the answer : ")
                if copy in yes:
                    pyperclip.copy(per_circ)
                    print("Answer Copied...!!!")
                    jump_process()
                else:
                    jump_process()
            else:
                print("Please enter only numbers!")
                circle_perimeter()
        elif circle_type == "2":
            radius = input("Enter the radius : ")
            if radius.isnumeric():
                radius = int(radius)
                mul_o_sev = radius%7
                pi = 3.14
                if (mul_o_sev == 0):
                    pi = 22/7
                arc_circ = (pi*radius)
                full_circ = arc_circ + (2*radius)
                full_circ = str(full_circ)
                arc_circ = str(arc_circ)
                with open(history_file, 'r') as historyFileR:
                    readF = historyFileR.read()
                with open(history_file, 'w') as historyFileW:
                    historyFileW.write(readF + "\n" + current_time + " [Perimeter of semicircle :  " + full_circ + "]")
                print("\u001b[34m---------------------------------------------------------\u001b[0m")
                print(">>> Arc length of semicircle :  \u001b[33;1m" + arc_circ + "\u001b[0m <<<")
                print(">>> Perimeter of semicircle : \u001b[33;1m" + full_circ + "\u001b[0m <<<")
                print("\u001b[34m---------------------------------------------------------\u001b[0m")
                copy = input("Do you need to copy the answer : ")
                if copy in yes:
                    pyperclip.copy("Arc Length : " + arc_circ + " , Perimeter : " + full_circ)
                    print("Answer Copied...!!!")
                    jump_process()
                else:
                    jump_process()
            else:
                print("Please enter only numbers!")
                circle_perimeter()
        else:
            print("Enter a correct value...!")
            time.sleep(3)
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
            per_oval = str(per_oval)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Circumference of oval :  " + per_oval + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Circumference of oval :  \u001b[33;1m" + per_oval + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_oval)
                print("Answer Copied...!!!")
                jump_process()
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
            per_tri = str(per_tri)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Perimeter of triangle :  " + per_tri + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Perimeter of triangle :  \u001b[33;1m" + per_tri + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_tri)
                print("Answer Copied...!!!")
                jump_process()
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
            per_pent = str(per_pent)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Perimeter of pentagon :  " + per_pent + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Perimeter of pentagon :  \u001b[33;1m" + per_pent + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_pent)
                print("Answer Copied...!!!")
                jump_process()
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
            per_hex = str(per_hex)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Perimeter of hexagon :  " + per_hex + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Perimeter of hexagon :  \u001b[33;1m" + per_hex + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(per_hex)
                print("Answer Copied...!!!")
                jump_process()
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
            vol_cube = str(vol_cube)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Volume of cube :  " + vol_cube + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Volume of cube :  \u001b[33;1m" + vol_cube + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_cube)
                print("Answer Copied...!!!")
                jump_process()
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
            vol_cuboid = str(vol_cuboid)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Volume of cuboid :  " + vol_cuboid + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Volume of cuboid :  \u001b[33;1m" + vol_cuboid + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_cuboid)
                print("Answer Copied...!!!")
                jump_process()
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
            vol_ball = str(vol_ball)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Volume of ball :  " + vol_ball + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Volume of ball :  \u001b[33;1m" + vol_ball + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_ball)
                print("Answer Copied...!!!")
                jump_process()
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
            vol_tetra = str(vol_tetra)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Volume of tetrahedron :  " + vol_tetra + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Volume of tetrahedron :  \u001b[33;1m" + vol_tetra + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_tetra)
                print("Answer Copied...!!!")
                jump_process()
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
            vol_pyr = str(vol_pyr)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Volume of pyramid :  " + vol_pyr + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Volume of pyramid :  \u001b[33;1m" + vol_pyr + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_pyr)
                print("Answer Copied...!!!")
                jump_process()
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
            vol_cyl = str(vol_cyl)
            with open(history_file, 'r') as historyFileR:
                readF = historyFileR.read()
            with open(history_file, 'w') as historyFileW:
                historyFileW.write(readF + "\n" + current_time + " [Volume of cylinder :  " + vol_cyl + "]")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            print(">>> Volume of cylinder :  \u001b[33;1m" + vol_cyl + "\u001b[0m <<<")
            print("\u001b[34m---------------------------------------------------------\u001b[0m")
            copy = input("Do you need to copy the answer : ")
            if copy in yes:
                pyperclip.copy(vol_cyl)
                print("Answer Copied...!!!")
                jump_process()
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
        \u001b[34m=================================\u001b[0m
        ----Area----
        
        Shapes = 1
        Solids = 2
        \u001b[34m=================================\u001b[0m

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
            print("You entered an incorrect value!!!")
            time.sleep(1)
            area()

    # PERIMETER FUNCTION
    def perimeter():
        clear_terminal()
        print("""
        \u001b[34m=================================\u001b[0m
        ----Perimeter & Circumference----
        
        Square = 1
        Rectangle = 2
        Circle = 3
        Oval = 4
        Equilateral Triangle = 5
        Regular Pentagon = 6
        Regular Hexagon = 7
        \u001b[34m=================================\u001b[0m
        
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
            print("You entered an incorrect value!!!")
            time.sleep(2)
            perimeter()

    # VOLUME FUNCTION
    def volume():
        clear_terminal()
        print("""
        \u001b[34m=================================\u001b[0m
        ----Volume----
        
        Cube = 1
        Cuboid = 2
        Ball = 3
        Tetrahedron = 4
        Pyramid = 5
        Cylinder = 6
        \u001b[34m=================================\u001b[0m
        
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
            print("You entered an incorrect value!!!")
            time.sleep(2)
            volume()

    if (type == "1"):
        area()
    elif (type == "2"):
        perimeter()
    elif (type == "3"):
        volume()
    elif (type == "Exit" or type == "exit" or type == "EXIT" or type == "eXIT"):
        exit_process()
    elif (type in clearHis):
        clear_history()
    else:
        print("You entered an incorrect value!!!")
        time.sleep(2)
        process()

process()