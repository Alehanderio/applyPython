import math

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        distance = math.sqrt((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2 + (z - self.center[2]) ** 2)
        return distance <= self.radius

def print_menu():
    print("\n1. Display sphere information")
    print("2. Set sphere radius")
    print("3. Set sphere center")
    print("4. Check if point is inside the sphere")
    print("5. Exit")

def main():
    argumets = int(input("Enter number of given args(0, 1 or 4):"))
    if argumets == 0:
        sphere = Sphere()
    elif argumets == 1:
        radius = float(input("Enter sphere radius: "))
        sphere = Sphere(radius)
    else:
        radius = float(input("Enter sphere radius: "))
        x = float(input("Enter x coordinate of sphere center: "))
        y = float(input("Enter y coordinate of sphere center: "))
        z = float(input("Enter z coordinate of sphere center: "))
        sphere = Sphere(radius, x, y, z)

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nSphere Information:")
            print("Radius:", sphere.get_radius())
            print("Center:", sphere.get_center())
            print("Volume:", sphere.get_volume())
            print("Surface Area:", sphere.get_square())
        elif choice == '2':
            new_radius = float(input("Enter new radius: "))
            sphere.set_radius(new_radius)
            print("Radius updated successfully.")
        elif choice == '3':
            new_x = float(input("Enter new x coordinate: "))
            new_y = float(input("Enter new y coordinate: "))
            new_z = float(input("Enter new z coordinate: "))
            sphere.set_center(new_x, new_y, new_z)
            print("Center coordinates updated successfully.")
        elif choice == '4':
            point_x = float(input("Enter x coordinate of point: "))
            point_y = float(input("Enter y coordinate of point: "))
            point_z = float(input("Enter z coordinate of point: "))
            if sphere.is_point_inside(point_x, point_y, point_z):
                print("The point is inside the sphere.")
            else:
                print("The point is outside the sphere.")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
