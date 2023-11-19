import turtle
import random
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=500)

# Define constants
NUM_CREATURES = 2
INITIAL_SIZE = 10
MAX_SIZE = 18
FOOD_SIZE = 6
STEP_SIZE = 5
SIZE_MUTATION_RATE = 0.1
HUNGER_LIMIT = 25
HUNGER_MUTATION_RATE = 0.1
HUNGER_MUTATION_RANGE = 5
SPEED_MUTATION_RATE = 0.1
SPEED_MUTATION_RANGE = 2
FOOD_COUNT = 4

# Define a function to create a creature
def create_creature():
    size = INITIAL_SIZE
    creature = turtle.Turtle(shape='circle')
    creature.size = size
    creature.hunger = 0
    creature.hunger_limit = HUNGER_LIMIT
    creature.speed = 2  # Default speed
    creature.color(random.random(), 0, 0)  # Random red color
    creature.penup()
    creature.setpos(random.randint(-200, 200), random.randint(-200, 200))
    creature.dx = random.randint(-STEP_SIZE, STEP_SIZE)
    creature.dy = random.randint(-STEP_SIZE, STEP_SIZE)
    return creature

# Define a function to move a creature with seeking behavior
def move_creature(creature):
    # Calculate the direction vector towards the nearest food
    nearest_food = min(food, key=lambda f: creature.distance(f))
    dx, dy = nearest_food.xcor() - creature.xcor(), nearest_food.ycor() - creature.ycor()
    distance = math.sqrt(dx**2 + dy**2)

    # Normalize the direction vector
    if distance > 0:
        dx /= distance
        dy /= distance

    # Move the creature towards the food with adjusted speed
    creature.setx(creature.xcor() + dx * STEP_SIZE * creature.speed)
    creature.sety(creature.ycor() + dy * STEP_SIZE * creature.speed)

    # Bounce off the walls
    if creature.xcor() > 250:
        creature.setx(250)
    elif creature.xcor() < -250:
        creature.setx(-250)
    if creature.ycor() > 250:
        creature.sety(250)
    elif creature.ycor() < -250:
        creature.sety(-250)

    # Increase hunger
    creature.hunger += 1

    # Kill the creature if it's too hungry
    if creature.hunger > creature.hunger_limit:
        creature.hideturtle()
        creature.clear()
        creature.penup()
        creatures.remove(creature)

# Define a function for creature eating
def eat_creature(creature, food):
    if creature.distance(food) < creature.size:
        creature.size += FOOD_SIZE
        if creature.size > MAX_SIZE:
            creature.size = MAX_SIZE
        food.setpos(random.randint(-200, 200), random.randint(-200, 200))
        creature.hunger -= 3

# Define a function for creature mating
def mate_creature(creature, partner):
    # Size mutation
    if random.random() < SIZE_MUTATION_RATE:
        child_size = creature.size + random.randint(-5, 5)
    else:
        child_size = (creature.size + partner.size) / 2

    # Clamp child size to stay within the allowed range
    child_size = max(INITIAL_SIZE, min(MAX_SIZE, child_size))

    # Hunger mutation
    if random.random() < HUNGER_MUTATION_RATE:
        child_hunger_limit = creature.hunger_limit + random.randint(-HUNGER_MUTATION_RANGE, HUNGER_MUTATION_RANGE)
    else:
        child_hunger_limit = (creature.hunger_limit + partner.hunger_limit) / 2

    # Clamp child hunger limit to a minimum value of 1
    child_hunger_limit = max(1, child_hunger_limit)

    # Speed mutation
    if random.random() < SPEED_MUTATION_RATE:
        child_speed = creature.speed + random.uniform(-SPEED_MUTATION_RANGE, SPEED_MUTATION_RANGE)
    else:
        child_speed = (creature.speed + partner.speed) / 2

    # Clamp child speed to stay within the allowed range
    child_speed = max(0.5, min(3, child_speed))

    child = create_creature()
    child.size = child_size
    child.hunger_limit = child_hunger_limit
    child.speed = child_speed
    return child

# Data collection function
def collect_data(creatures):
    data = []
    for creature in creatures:
        creature_data = {
            "size": creature.size,
            "hunger": creature.hunger,
            "position": (creature.xcor(), creature.ycor()),
            "speed": creature.speed
        }
        data.append(creature_data)
    return data

# Create the creatures
creatures = [create_creature() for _ in range(NUM_CREATURES)]

# Create the food
food = [turtle.Turtle(shape='circle', visible=False) for _ in range(FOOD_COUNT)]
for f in food:
    f.color('green')
    f.penup()
    f.setpos(random.randint(-200, 200), random.randint(-200, 200))
    f.showturtle()

# Data collection setup
data_collection_interval = 10
collected_data = [collect_data(creatures)]

# Main loop
iteration = 0
while creatures:
    for creature in creatures[:]:
        move_creature(creature)
        for f in food:
            eat_creature(creature, f)
        for partner in creatures[:]:
            if creature != partner and creature.distance(partner) < creature.size / 2:
                child = mate_creature(creature, partner)
                creatures.append(child)

    # Hide and remove dead creatures
    for creature in creatures[:]:
        if creature.hunger > creature.hunger_limit:
            creature.hideturtle()
            creature.clear()
            creature.penup()
            creatures.remove(creature)

    # Collect data for the creatures at specific intervals
    if iteration % data_collection_interval == 0:
        collected_data.append(collect_data(creatures))

    screen.update()
    iteration += 1

# Delete all remaining creatures before finishing
for creature in creatures:
    creature.hideturtle()
    creature.clear()
    creature.penup()

print("Simulation completed.")
turtle.done()

# Process the collected data as needed
print("Collected Data:")
for idx, data in enumerate(collected_data):
    print(f"Iteration {idx * data_collection_interval}:")
    for creature_data in data:
        print(creature_data)
