// 获取画布和2D绘图上下文
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// 小恐龙相关变量
let dinoX = 50;
let dinoY = 150;
let dinoWidth = 40;
let dinoHeight = 40;

// 跳跃相关变量
let isJumping = false;
let jumpHeight = 0;
let gravity = 1;

// 障碍物相关变量
let obstacleX = 800;
let obstacleWidth = 30;
let obstacleHeight = 30;

// 绘制小恐龙
function drawDino() {
    ctx.fillStyle = 'green';
    ctx.fillRect(dinoX, dinoY, dinoWidth, dinoHeight);
}

// 绘制障碍物
function drawObstacle() {
    ctx.fillStyle = 'brown';
    ctx.fillRect(obstacleX, 150, obstacleWidth, obstacleHeight);
}

// 处理跳跃逻辑
function jump() {
    if (!isJumping) {
        isJumping = true;
        jumpHeight = -10;
    }
}

// 更新小恐龙状态
function updateDino() {
    if (isJumping) {
        dinoY += jumpHeight;
        jumpHeight += gravity;
        if (dinoY >= 150) {
            dinoY = 150;
            isJumping = false;
        }
    }
}

// 更新障碍物状态
function updateObstacle() {
    obstacleX -= 5;
    if (obstacleX < -obstacleWidth) {
        obstacleX = 800;
    }
}

// 游戏循环
function gameLoop() {
    // 清空画布
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawDino();
    drawObstacle();
    updateDino();
    updateObstacle();
    requestAnimationFrame(gameLoop);
}

// 监听键盘空格键事件
document.addEventListener('keydown', function (event) {
    if (event.key ==='') {
        jump();
    }
});

// 监听触摸屏幕事件
canvas.addEventListener('touchstart', function (event) {
    jump();
    event.preventDefault();
});

// 启动游戏循环
gameLoop();
