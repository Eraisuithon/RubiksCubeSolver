from Group_Colors import get_color_groups
from State_Controller import state, show_state
from Algorithms import BFS, Best_First, A_star

colors = get_color_groups()
start = f'LBUUULBFUULRUFLBRRDDUFDUDURDBLBLRFRRBDLBRFFFDFRBDBDFLL'
print("Starting state is this: ")
show_state(start)

print()
print('#####')
print()
print("Applying Best First: ")
sol = Best_First(start)
print(f"Solved in {len(sol)} moves: ")
print(sol)
print('---')
print("Applying A*: ")
sol = A_star(start)
print(f"Solved in {len(sol)} moves: ")
print(sol)
# print("Applying BFS: ")
# print(BFS(start))
