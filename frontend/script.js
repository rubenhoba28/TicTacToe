const socket = io.connect('http://localhost:5001');

const board = document.getElementById('game-board');
const status = document.getElementById('status');
const restartButton = document.getElementById('restart');

let currentPlayer = 'X';
let gameOver = false;

function createBoard() {
    board.innerHTML = '';
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.dataset.row = i;
            cell.dataset.col = j;
            cell.addEventListener('click', handleClick);
            board.appendChild(cell);
        }
    }
    gameOver = false;
    currentPlayer = 'X';
    status.textContent = "It's X's turn.";
}

function handleClick(e) {
    if (gameOver) return;

    const row = e.target.dataset.row;
    const col = e.target.dataset.col;

    if (!e.target.classList.contains('taken')) {
        socket.emit('make_move', { player: currentPlayer, row: +row, col: +col });
    }
}

socket.on('update_board', (data) => {
    const { board, result } = data;

    board.forEach((row, i) => {
        row.forEach((cell, j) => {
            const cellDiv = document.querySelector(`[data-row="${i}"][data-col="${j}"]`);
            cellDiv.textContent = cell;
            if (cell !== '') cellDiv.classList.add('taken');
        });
    });

    if (result.includes('wins') || result === "It's a draw!") {
        gameOver = true;
        status.textContent = result;
    } else {
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        status.textContent = `It's ${currentPlayer}'s turn.`;
    }
});

restartButton.addEventListener('click', () => {
    socket.emit('restart_game');
    createBoard();
});

socket.emit('test_event', { test: 'Hello, server!' });
socket.on('test_response', (data) => {
    console.log(data.message);
});

createBoard();
