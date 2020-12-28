# SnakePong
Snakepong is a mix between the old games "pong" & "snake", where the game is played like pong but one of the paddles of pong can be controlled like snake. 
Since this is a task and not a replacement for the exam, I will only work on this for 1 day.

## Analysis of the problem
It is a pretty complex game, using bounce physics on the ball, is also has 2 big moveable parts: the snake and the paddle. 
The components are:
- screen
- paddle
- snake
- ball
- points
![snakepong](./img/snakepong.png)

## Scheme
This is a guess of the code that will be needed and a scheme of how they would interact.

Code:
- main.py: Just start the game
- game.py: handle everything in the game
- screen.py: visualize the game
- snake.py: move(Double linked list)
- paddle.py: move(Single linked list)
- ball.py: move(bounce-physics, collision detection)

Scheme:
![scheme](./img/scheme.png)

## Documentation

This is too difficult of a task for me, I would just watch a tutorial and copy that because I don't know how to make this. So I will make what I know, it will be more like snake: the berry will spawn at random coordinates and the snake will only be a head (i will try to make the tail with a Double/ Single linked list but that will be extra), i will try to make the snake move with keyboard input and even make a simple algorithm(it will just look where the berry is and go there), this course is called Algorithms after all. I will also try to make pytests for these.