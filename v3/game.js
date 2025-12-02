const rows = 8, cols = 8;
const bombsCount = Math.floor(rows * cols * 0.15);

const game = document.getElementById("game");
const statusText = document.getElementById("status");
const scoreEl = document.getElementById("score");
const solvedList = document.getElementById("solvedList");
const flagBtn = document.getElementById("flagModeBtn");
const resetBtn = document.getElementById("resetBtn");

let board, revealed, flagged, flagMode = false, score = 0;

const inequalities = [
  "2x + 4 ≥ 10", "x - 3 < 5", "3x > 9", "-x + 4 > 1",
  "2(3+x) ≥ 10", "x*2 ≤ 6", "5x > 15", "x + 2 ≥ 1"
];

const ecuacionesLineales = [
  "2x + 4 = 10", "x - 3 = 5", "3x = 9", "-x + 4 = 1",
];
// Random inequality generator
const getIneq = () => inequalities[Math.floor(Math.random() * inequalities.length)];
const getEq = () => ecuacionesLineales[Math.floor(Math.random() * ecuacionesLineales.length)];

flagBtn.onclick = () => {
  flagMode = !flagMode;
  flagBtn.classList.toggle("active", flagMode);
};

resetBtn.onclick = createBoard;

function createBoard() {
  game.style.gridTemplateColumns = `repeat(${cols}, 1fr)`;
  score = 0;
  updateScore();

  solvedList.innerHTML = "";
  statusText.textContent = "";

  board = Array(rows).fill().map(() => Array(cols).fill(0));
  revealed = Array(rows).fill().map(() => Array(cols).fill(false));
  flagged = Array(rows).fill().map(() => Array(cols).fill(false));

  // place bombs
  let bombs = 0;
  while (bombs < bombsCount) {
    const r = Math.floor(Math.random() * rows);
    const c = Math.floor(Math.random() * cols);
    if (board[r][c] !== "B") {
      board[r][c] = "B";
      bombs++;
    }
  }

  // numbers
  for (let r = 0; r < rows; r++)
    for (let c = 0; c < cols; c++)
      if (board[r][c] !== "B") {
        let count = 0;
        for (let i = -1; i <= 1; i++)
          for (let j = -1; j <= 1; j++)
            if (board[r+i]?.[c+j] === "B") count++;
        board[r][c] = count;
      }

  render();
}

function render() {
  game.innerHTML = "";
  for (let r = 0; r < rows; r++)
    for (let c = 0; c < cols; c++) {
      const cell = document.createElement("div");
      cell.className = "cell";
      cell.dataset.row = r;
      cell.dataset.col = c;
      cell.onclick = clickCell;
      game.append(cell);
    }
}

function clickCell() {
  const r = +this.dataset.row;
  const c = +this.dataset.col;

  if (revealed[r][c]) return;
  if (flagMode) return toggleFlag(r, c);

  if (board[r][c] === "B") return lose(this);

  reveal(r, c);
}

function toggleFlag(r, c) {
  const cell = game.children[r * cols + c];
  flagged[r][c] = !flagged[r][c];
  cell.textContent = flagged[r][c] ? "🚩" : "";
  cell.classList.toggle("flagged", flagged[r][c]);
}

function reveal(r, c) {
  if (r < 0 || c < 0 || r >= rows || c >= cols || revealed[r][c]) return;

  const cell = game.children[r * cols + c];
  revealed[r][c] = true;
  cell.classList.add("revealed");

  if (board[r][c] > 0) {
    const text = getIneq();
    const text2 = getEq();
    cell.textContent = text;
    cell.textContent2 = text2;
    logSolved(text);
    addPoints(10);
  } else {
    cell.textContent = "";
    cell.textContent = "";
    for (let i = -1; i <= 1; i++)
      for (let j = -1; j <= 1; j++)
        if (i || j) reveal(r+i, c+j);
  }

  checkWin();
}

function logSolved(text) {
  const li = document.createElement("li");
  li.textContent = text;
  solvedList.append(li);
}

function addPoints(amount) {
  score += amount;
  updateScore();
}

function updateScore() {
  scoreEl.textContent = score;
}

function lose(cell) {
  cell.textContent = "💣";
  cell.classList.add("bomb");
  statusText.textContent = "💥 Perdiste";
  disable();
}

function checkWin() {
  const revealedCount = revealed.flat().filter(x => x).length;
  if (revealedCount === rows * cols - bombsCount) {
    statusText.textContent = "🎉 ¡Ganaste!";
    addPoints(100);
    disable();
  }
}

function disable() {
  for (const c of game.children) c.onclick = null;
}

createBoard();
