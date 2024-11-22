import turtle

# Fungsi untuk menggambar Fibonacci Tree
def fibonacci_tree(length, level):
    if level == 0 or length < 10:  # Hentikan jika level 0 atau panjang terlalu kecil
        return
    
    # Gambar batang utama
    turtle.forward(length)
    
    # Simpan posisi dan arah
    position = turtle.pos()
    heading = turtle.heading()
    
    # Cabang kiri
    turtle.left(30)  # Sudut cabang kiri
    fibonacci_tree(length * 0.7, level - 1)  # Panjang cabang kiri
    
    # Kembali ke posisi dan arah semula
    turtle.penup()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.pendown()
    
    # Cabang kanan
    turtle.right(60)  # Sudut cabang kanan
    fibonacci_tree(length * 0.7, level - 1)  # Panjang cabang kanan
    
    # Kembali ke posisi awal batang
    turtle.penup()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.pendown()

# Setup awal Turtle
turtle.speed(0)  # Kecepatan maksimal
turtle.left(90)  # Arahkan ke atas
turtle.penup()
turtle.goto(0, -200)  # Posisi awal di bawah
turtle.pendown()
turtle.color("brown")

# Menggambar Fibonacci Tree
fibonacci_tree(100, 7)  # Panjang batang 100, level rekursi 7

# Selesaikan gambar
turtle.hideturtle()
turtle.done()
