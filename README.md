# Tic-Tac-Toe Game

A real-time **Tic-Tac-Toe** game for two players, built with Flask, Flask-SocketIO, and a simple front-end using HTML, CSS, and JavaScript.

---

## Features

- **Real-Time Gameplay**: Players see moves in real-time using WebSocket.
- **Dynamic Turn Display**: The game shows whose turn it is (`X` or `O`).
---

## Game Structure

### Entities Used
1. **Backend**:
   - `app.py`: Handles the Flask server and WebSocket communication via Flask-SocketIO.
   - `game_logic.py`: Contains the core Tic-Tac-Toe game logic, including the board state, turn handling, and win/draw condition checks.

2. **Frontend**:
   - `index.html`: Provides the structure of the game interface.
   - `style.css`: Styles the game grid, buttons, and status messages.
   - `script.js`: Manages the WebSocket connection and updates the UI in real-time based on server responses.

---

### Game Flow

1. **Initialization**:
   - When the game starts, the server initializes a blank 3x3 board and sets the first player to `X`.
   - The front-end displays a welcome message and a grid for the game.

2. **Player Turns**:
   - A player clicks on a grid cell to make a move.
   - The front-end sends the move to the server (`make_move` event) with the player's symbol (`X` or `O`) and the cell's position.
     
3. **Game End**:
   - If a player wins or the game ends in a draw, the game prevents further moves and displays the result.
   - Players can click the **Restart** button to reset the game.

---

### Win Condition Check
The win condition is checked in the `check_win` method of `game_logic.py`. It verifies:
- **Rows**: If all cells in any row contain the same symbol (`X` or `O`).
- **Columns**: If all cells in any column contain the same symbol.
- **Diagonals**: If all cells in either diagonal contain the same symbol.

The draw condition is checked by ensuring all cells are filled and no win condition is met.

---

## Installation

### Prerequisites
- Python 3.x installed on your system.
- Git installed to clone the repository.

### Steps
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/tic-tac-toe.git](https://github.com/rubenhoba28/TicTacToe.git)
   cd tic-tac-toe
   
2. Clone the repository:
   Create a virtual environment and activate it
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## How to Run

### Backend
1. Start the Flask server:
   ```bash
   python backend/app.py
   
2. The backend server runs on: http://localhost:5001

### Frontend

1. Serve the `frontend` directory:

   - **Using Python**:
     ```bash
     python -m http.server 8000
     ```

   - **Using Node.js with `http-server` (if installed)**:
     ```bash
     npx http-server -p 8000
     ```

2. Open the frontend in your browser by visiting:  
   [http://localhost:8000](http://localhost:8000)


   



