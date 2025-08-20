function 右輪 (速度: number) {
    if (速度 < 0) {
        if (速度 <= -240) {
            DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, 240)
        } else {
            DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, 速度)
        }
    } else if (速度 > 0) {
        if (速度 >= 240) {
            DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 240)
        } else {
            DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 速度)
        }
    } else if (速度 == 0) {
        DFRobotMaqueenPlus.mototStop(Motors.M2)
    }
}
function L2碰到線 () {
    白線兩邊感測器()
    PID計算(L_IR)
    左輪(是要奪快 - PID輸出)
    右輪(是要奪快 + PID輸出)
}
function 左輪 (速度: number) {
    if (速度 < 0) {
        if (速度 <= -240) {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, 240)
        } else {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, 速度)
        }
    } else if (速度 > 0) {
        if (速度 >= 240) {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 240)
        } else {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 速度)
        }
    } else if (速度 == 0) {
        DFRobotMaqueenPlus.mototStop(Motors.M1)
    }
}
function R2碰到線 () {
    白線兩邊感測器()
    PID計算(R_IR)
    左輪(是要奪快 + PID輸出)
    右輪(是要奪快 - PID輸出)
}
input.onButtonPressed(Button.A, function () {
    停停停 = 0
    循線()
})
function 循線 () {
    while (停停停 == 0) {
        白線兩邊感測器()
        if (L_IR > 0) {
            L2碰到線()
        } else if (R_IR > 0) {
            R2碰到線()
        } else {
            P = 0
            I = 0
            D = 0
            PID輸出 = 0
            直走()
        }
        全部停的條件()
    }
}
function 全部停的條件 () {
    if (DFRobotMaqueenPlus.readPatrol(Patrol.L1) == 0 && DFRobotMaqueenPlus.readPatrol(Patrol.L2) == 0 && DFRobotMaqueenPlus.readPatrol(Patrol.L3) == 0 && (DFRobotMaqueenPlus.readPatrol(Patrol.R1) == 0 && DFRobotMaqueenPlus.readPatrol(Patrol.R2) == 0 && DFRobotMaqueenPlus.readPatrol(Patrol.R3) == 0)) {
        停停停 = 1
        左輪(0)
        右輪(0)
    }
}
function 白線兩邊感測器 () {
    L_IR = DFRobotMaqueenPlus.readPatrolVoltage(Patrol.L2)
    if (L_IR <= 1300) {
        L_IR = 0
    } else {
        L_IR = (DFRobotMaqueenPlus.readPatrolVoltage(Patrol.L2) - 1300) / 100
    }
    R_IR = DFRobotMaqueenPlus.readPatrolVoltage(Patrol.R2)
    if (R_IR <= 1300) {
        R_IR = 0
    } else {
        R_IR = (DFRobotMaqueenPlus.readPatrolVoltage(Patrol.R2) - 1300) / 100
    }
    serial.writeValue("R", R_IR)
    serial.writeValue("L", L_IR)
}
function 直走 () {
    左輪(是要奪快)
    右輪(是要奪快)
}
function PID計算 (誤差: number) {
    白線兩邊感測器()
    P = 誤差
    I = I + 誤差
    D = 誤差 - 前誤差
    PID輸出 = Kp * P + Ki * I + Kd * D
    前誤差 = 0
}
let 前誤差 = 0
let 停停停 = 0
let R_IR = 0
let L_IR = 0
let PID輸出 = 0
let D = 0
let I = 0
let P = 0
let Kd = 0
let Ki = 0
let Kp = 0
let 是要奪快 = 0
是要奪快 = 120
Kp = 5
Ki = 0
Kd = 22
Kd = 0
P = 0
I = 0
D = 0
PID輸出 = 0
basic.forever(function () {
	
})
