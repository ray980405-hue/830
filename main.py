def 右輪(速度: number):
    if 速度 < 0:
        if 速度 <= -240:
            DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, 240)
        else:
            DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, 速度)
    elif 速度 > 0:
        if 速度 >= 240:
            DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 240)
        else:
            DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 速度)
    elif 速度 == 0:
        DFRobotMaqueenPlus.motot_stop(Motors.M2)
def L2碰到線():
    白線兩邊感測器()
    PID計算(L_IR)
    左輪(是要奪快 - PID輸出)
    右輪(是要奪快 + PID輸出)
def 左輪(速度2: number):
    if 速度2 < 0:
        if 速度2 <= -240:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, 240)
        else:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, 速度2)
    elif 速度2 > 0:
        if 速度2 >= 240:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 240)
        else:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 速度2)
    elif 速度2 == 0:
        DFRobotMaqueenPlus.motot_stop(Motors.M1)
def R2碰到線():
    白線兩邊感測器()
    PID計算(R_IR)
    左輪(是要奪快 + PID輸出)
    右輪(是要奪快 - PID輸出)

def on_button_pressed_a():
    global 停停停
    停停停 = 0
    循線()
input.on_button_pressed(Button.A, on_button_pressed_a)

def 循線():
    global P, I, D, PID輸出
    while 停停停 == 0:
        白線兩邊感測器()
        if DFRobotMaqueenPlus.read_patrol(Patrol.L2) == 0:
            L2碰到線()
        elif DFRobotMaqueenPlus.read_patrol(Patrol.R2) == 0:
            R2碰到線()
        else:
            P = 0
            I = 0
            D = 0
            PID輸出 = 0
            直走()
        全部停的條件()
def 全部停的條件():
    global 停停停
    if DFRobotMaqueenPlus.read_patrol(Patrol.L1) == 0 and DFRobotMaqueenPlus.read_patrol(Patrol.L2) == 0 and DFRobotMaqueenPlus.read_patrol(Patrol.L3) == 0 and (DFRobotMaqueenPlus.read_patrol(Patrol.R1) == 0 and DFRobotMaqueenPlus.read_patrol(Patrol.R2) == 0 and DFRobotMaqueenPlus.read_patrol(Patrol.R3) == 0):
        停停停 = 1
        左輪(0)
        右輪(0)
def 白線兩邊感測器():
    global L_IR, R_IR
    L_IR = DFRobotMaqueenPlus.read_patrol_voltage(Patrol.L2)
    if L_IR <= 1300:
        L_IR = 0
    else:
        L_IR = (DFRobotMaqueenPlus.read_patrol_voltage(Patrol.L2) - 1300) / 100
    R_IR = DFRobotMaqueenPlus.read_patrol_voltage(Patrol.R2)
    if R_IR <= 1300:
        R_IR = 0
    else:
        R_IR = (DFRobotMaqueenPlus.read_patrol_voltage(Patrol.R2) - 1300) / 100
    serial.write_value("R", R_IR)
    serial.write_value("L", L_IR)
def 直走():
    左輪(是要奪快)
    右輪(是要奪快)
def PID計算(誤差: number):
    global P, I, D, PID輸出, 前誤差
    白線兩邊感測器()
    P = 誤差
    I = I + 誤差
    D = 誤差 - 前誤差
    PID輸出 = Kp * P + Ki * I + Kd * D
    前誤差 = 誤差
前誤差 = 0
停停停 = 0
R_IR = 0
L_IR = 0
PID輸出 = 0
D = 0
I = 0
P = 0
Kd = 0
Ki = 0
Kp = 0
是要奪快 = 0
是要奪快 = 120
Kp = 7
Ki = 0
Kd = 11
Kd = 0
P = 0
I = 0
D = 0
PID輸出 = 0

def on_forever():
    pass
basic.forever(on_forever)
