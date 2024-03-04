import networkx as nx
import matplotlib.pyplot as plt
from IPython.display import display, Image

def visualize_game_tree():
    G = nx.Graph()

    def add_children(parent, board, depth, player):
        if depth >= 2 or analyzeboard(board) != 0:
            return

        for i in range(9):
            if board[i] == 0:
                new_board = board.copy()
                new_board[i] = player
                child = str(new_board)
                G.add_edge(parent, child)
                add_children(child, new_board, depth + 1, -player)

    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    root = str(board)
    G.add_node(root)
    add_children(root, board, 0, 1)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=5000, node_color='lightblue', font_size=10)
    plt.title("Game Tree (Depth 2)")
    plt.axis('off')
    plt.show()
    plt.savefig("game_tree.png")  # Save the plot as an image
    display(Image(filename='game_tree.png'))  # Display the image

def main():
    choice = '1'  # Single player game by default
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    moves = []

    if choice == '1':
        print("Computer : O Vs. You : X")
        player = 1
        for i in range(0, 9):
            if analyzeboard(board) != 0:
                break
            if i % 2 == 0:
                CompTurn(board)
            else:
                ConstBoard(board)
                User1Turn(board)
            moves.append(board.copy())

    x = analyzeboard(board)
    if x == 0:
        ConstBoard(board)
        print("Draw!!!")
    elif x == -1:
        ConstBoard(board)
        print("X Wins!!! Y Loose !!!")
    elif x == 1:
        ConstBoard(board)
        print("X Loose!!! O Wins !!!!")

    print("\nStates Played in the Path:")
    for move in moves:
        ConstBoard(move)

    visualize_game_tree()

if __name__ == "__main__":
    main()