from canvas import Canvas
from shapes import Square, Rectangle

canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))

colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input('Enter canvas color (white or black): ')

canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])

while True:
    user_choice = input("Enter the name of the shape you want to draw, if you want exit write exit: ").lower()
    if 'rectangle' in user_choice:
        Rectangle(int(input('Enter x coordinate: ')),
                  int(input('Enter y coordinate: ')),
                  int(input('Enter width this shape: ')),
                  int(input('Enter height this shape: ')),
                  (int(input("How much red should the rectangle have? ")),
                   int(input('How much green? ')),
                   int(input('How much blue? ')))).draw(canvas)
    elif 'square' in user_choice:
        Square(int(input('Enter x coordinate: ')),
               int(input('Enter y coordinate: ')),
               int(input('Enter side size this shape: ')),
               (int(input("How much red should the rectangle have? ")),
                int(input('How much green? ')),
                int(input('How much blue? ')))
               ).draw(canvas)
    elif 'exit' in user_choice:
        break
    else:
        print('Not correct figure.')


canvas.make("canvas.png")
