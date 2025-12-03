// --- Config ---
const rows = 8, cols = 8;
const bombsCount = Math.floor(rows * cols * 0.15);

const game = document.getElementById("game");
const statusText = document.getElementById("status");
const scoreEl = document.getElementById("score");
const solvedList = document.getElementById("solvedList");
const flagBtn = document.getElementById("flagModeBtn");
const resetBtn = document.getElementById("resetBtn");

let board, revealed, flagged, flagMode = false, score = 0;

// --- Generador de ecuaciones/desigualdades con resultado -3..3 ---
const generateIneq = () => {
  const x = Math.floor(Math.random()*7)-3; // -3..3
  const a = Math.floor(Math.random()*5)+1;
  const b = Math.floor(Math.random()*10)-5;
  const ops = ["+", "-"];
  const op = ops[Math.floor(Math.random()*ops.length)];
  return `${a}x ${op} ${b} ≥ ${a*x + (op === "+"?b:-b)}`;
}
const generateEq = () => {
  const x = Math.floor(Math.random()*7)-3;
  const a = Math.floor(Math.random()*5)+1;
  const b = Math.floor(Math.random()*10)-5;
  return `${a}x + ${b} = ${a*x+b}`;
}

// --- Botones ---
flagBtn.onclick = () => { flagMode = !flagMode; flagBtn.classList.toggle("active", flagMode); };
resetBtn.onclick = createBoard;

// --- Tablero ---
function createBoard() {
  game.style.gridTemplateColumns = `repeat(${cols}, 1fr)`;
  score = 0; updateScore();
  solvedList.innerHTML = ""; statusText.textContent = "";
  
  board = Array(rows).fill().map(() => Array(cols).fill(0));
  revealed = Array(rows).fill().map(() => Array(cols).fill(false));
  flagged = Array(rows).fill().map(() => Array(cols).fill(false));

  // colocar bombas
  let bombs = 0;
  while(bombs < bombsCount){
    const r=Math.floor(Math.random()*rows), c=Math.floor(Math.random()*cols);
    if(board[r][c] !== "B"){ board[r][c]="B"; bombs++; }
  }

  // números alrededor
  for(let r=0;r<rows;r++)
    for(let c=0;c<cols;c++)
      if(board[r][c] !== "B"){
        let count = 0;
        for(let i=-1;i<=1;i++)
          for(let j=-1;j<=1;j++)
            if(board[r+i]?.[c+j] === "B") count++;
        board[r][c] = count;
      }

  render();
}

// --- Render ---
function render(){
  game.innerHTML="";
  for(let r=0;r<rows;r++)
    for(let c=0;c<cols;c++){
      const cell=document.createElement("div");
      cell.className="cell";
      cell.dataset.row=r; cell.dataset.col=c;
      cell.onclick = clickCell;
      game.append(cell);
    }
}

// --- Click ---
function clickCell(){
  const r=+this.dataset.row, c=+this.dataset.col;
  if(revealed[r][c]) return;
  if(flagMode) return toggleFlag(r,c);
  if(board[r][c]==="B") return lose();
  reveal(r,c);
}

// --- Flag ---
function toggleFlag(r,c){
  const cell=game.children[r*cols+c];
  flagged[r][c]=!flagged[r][c];
  cell.textContent=flagged[r][c]?"🚩":"";
  cell.classList.toggle("flagged", flagged[r][c]);
}

// --- Reveal ---
function reveal(r,c){
  if(r<0||c<0||r>=rows||c>=cols||revealed[r][c]) return;
  const cell=game.children[r*cols+c];
  revealed[r][c]=true;
  cell.classList.add("revealed");

  if(board[r][c]>0){
    const text = generateIneq();
    const text2 = generateEq();
    cell.textContent = text;
    logSolved(text);
    addPoints(10);
  } else {
    cell.textContent="";
    for(let i=-1;i<=1;i++)
      for(let j=-1;j<=1;j++)
        if(i||j) reveal(r+i,c+j);
  }
  checkWin();
}

// --- Log ---
function logSolved(text){
  const li=document.createElement("li");
  li.textContent=text;
  solvedList.append(li);
}

// --- Puntaje ---
function addPoints(amount){ score+=amount; updateScore(); }
function updateScore(){ scoreEl.textContent=score; }

// --- Perder ---
function lose(){
  statusText.textContent="💥 Perdiste";
  showBombs();
  disable();
}

// --- Ganar ---
function checkWin(){
  const revealedCount = revealed.flat().filter(x=>x).length;
  if(revealedCount === rows*cols - bombsCount){
    statusText.textContent="🎉 ¡Ganaste!";
    addPoints(100);
    showBombs(true);
    disable();
  }
}

// --- Mostrar bombas ---
function showBombs(win=false){
  for(let r=0;r<rows;r++)
    for(let c=0;c<cols;c++){
      if(board[r][c]==="B"){
        const cell=game.children[r*cols+c];
        cell.textContent = win ? "💰" : "💣";
        cell.classList.add("bomb");
      }
    }
}

// --- Desactivar ---
function disable(){ for(const c of game.children) c.onclick=null; }

createBoard();
