from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 121
	S = Scenario("PADD_1", horizon=horizon)

	# resource
	MUL = S.Resources('MUL', num=1, size=7)
	MUL_in = S.Resources('MUL_in', num=1)
	INV = S.Resource('INV')
	ADD = S.Resources('ADD', num=4, periods=range(1, horizon))
	MUL_mem = S.Resources('MUL_mem', num=1, size=2)
	ADD_mem = S.Resources('ADD_mem', num=4, size=2)
	INPUT_mem_w = S.Resource('INPUT_mem_w', size=2)
	INPUT_mem_r = S.Resource('INPUT_mem_r', size=2)

	# result of previous scheduling
	t2_t1_t1_in = S.Task('t2_t1_t1_in', length=1, delay_cost=1)
	S += t2_t1_t1_in >= 0
	t2_t1_t1_in += MUL_in[0]

	t2_t1_t1_mem0 = S.Task('t2_t1_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_t1_mem0 >= 0
	t2_t1_t1_mem0 += INPUT_mem_r

	t2_t1_t1_mem1 = S.Task('t2_t1_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_t1_mem1 >= 0
	t2_t1_t1_mem1 += INPUT_mem_r

	t0_t1_t1_in = S.Task('t0_t1_t1_in', length=1, delay_cost=1)
	S += t0_t1_t1_in >= 1
	t0_t1_t1_in += MUL_in[0]

	t0_t1_t1_mem0 = S.Task('t0_t1_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_t1_mem0 >= 1
	t0_t1_t1_mem0 += INPUT_mem_r

	t0_t1_t1_mem1 = S.Task('t0_t1_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_t1_mem1 >= 1
	t0_t1_t1_mem1 += INPUT_mem_r

	t2_t1_t1 = S.Task('t2_t1_t1', length=7, delay_cost=1)
	S += t2_t1_t1 >= 1
	t2_t1_t1 += MUL[0]

	t0_t1_t1 = S.Task('t0_t1_t1', length=7, delay_cost=1)
	S += t0_t1_t1 >= 2
	t0_t1_t1 += MUL[0]

	t2_t0_t1_in = S.Task('t2_t0_t1_in', length=1, delay_cost=1)
	S += t2_t0_t1_in >= 2
	t2_t0_t1_in += MUL_in[0]

	t2_t0_t1_mem0 = S.Task('t2_t0_t1_mem0', length=1, delay_cost=1)
	S += t2_t0_t1_mem0 >= 2
	t2_t0_t1_mem0 += INPUT_mem_r

	t2_t0_t1_mem1 = S.Task('t2_t0_t1_mem1', length=1, delay_cost=1)
	S += t2_t0_t1_mem1 >= 2
	t2_t0_t1_mem1 += INPUT_mem_r

	t2_t0_t0_in = S.Task('t2_t0_t0_in', length=1, delay_cost=1)
	S += t2_t0_t0_in >= 3
	t2_t0_t0_in += MUL_in[0]

	t2_t0_t0_mem0 = S.Task('t2_t0_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_t0_mem0 >= 3
	t2_t0_t0_mem0 += INPUT_mem_r

	t2_t0_t0_mem1 = S.Task('t2_t0_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_t0_mem1 >= 3
	t2_t0_t0_mem1 += INPUT_mem_r

	t2_t0_t1 = S.Task('t2_t0_t1', length=7, delay_cost=1)
	S += t2_t0_t1 >= 3
	t2_t0_t1 += MUL[0]

	t2_t0_t0 = S.Task('t2_t0_t0', length=7, delay_cost=1)
	S += t2_t0_t0 >= 4
	t2_t0_t0 += MUL[0]

	t2_t1_t0_in = S.Task('t2_t1_t0_in', length=1, delay_cost=1)
	S += t2_t1_t0_in >= 4
	t2_t1_t0_in += MUL_in[0]

	t2_t1_t0_mem0 = S.Task('t2_t1_t0_mem0', length=1, delay_cost=1)
	S += t2_t1_t0_mem0 >= 4
	t2_t1_t0_mem0 += INPUT_mem_r

	t2_t1_t0_mem1 = S.Task('t2_t1_t0_mem1', length=1, delay_cost=1)
	S += t2_t1_t0_mem1 >= 4
	t2_t1_t0_mem1 += INPUT_mem_r

	t0_t1_t0_in = S.Task('t0_t1_t0_in', length=1, delay_cost=1)
	S += t0_t1_t0_in >= 5
	t0_t1_t0_in += MUL_in[0]

	t0_t1_t0_mem0 = S.Task('t0_t1_t0_mem0', length=1, delay_cost=1)
	S += t0_t1_t0_mem0 >= 5
	t0_t1_t0_mem0 += INPUT_mem_r

	t0_t1_t0_mem1 = S.Task('t0_t1_t0_mem1', length=1, delay_cost=1)
	S += t0_t1_t0_mem1 >= 5
	t0_t1_t0_mem1 += INPUT_mem_r

	t2_t1_t0 = S.Task('t2_t1_t0', length=7, delay_cost=1)
	S += t2_t1_t0 >= 5
	t2_t1_t0 += MUL[0]

	t0_t0_t1_in = S.Task('t0_t0_t1_in', length=1, delay_cost=1)
	S += t0_t0_t1_in >= 6
	t0_t0_t1_in += MUL_in[0]

	t0_t0_t1_mem0 = S.Task('t0_t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t0_t1_mem0 >= 6
	t0_t0_t1_mem0 += INPUT_mem_r

	t0_t0_t1_mem1 = S.Task('t0_t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t0_t1_mem1 >= 6
	t0_t0_t1_mem1 += INPUT_mem_r

	t0_t1_t0 = S.Task('t0_t1_t0', length=7, delay_cost=1)
	S += t0_t1_t0 >= 6
	t0_t1_t0 += MUL[0]

	t0_t0_t0_in = S.Task('t0_t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_t0_in >= 7
	t0_t0_t0_in += MUL_in[0]

	t0_t0_t0_mem0 = S.Task('t0_t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_t0_mem0 >= 7
	t0_t0_t0_mem0 += INPUT_mem_r

	t0_t0_t0_mem1 = S.Task('t0_t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_t0_mem1 >= 7
	t0_t0_t0_mem1 += INPUT_mem_r

	t0_t0_t1 = S.Task('t0_t0_t1', length=7, delay_cost=1)
	S += t0_t0_t1 >= 7
	t0_t0_t1 += MUL[0]

	t0_t0_t0 = S.Task('t0_t0_t0', length=7, delay_cost=1)
	S += t0_t0_t0 >= 8
	t0_t0_t0 += MUL[0]

	t9_t0_t2_mem0 = S.Task('t9_t0_t2_mem0', length=1, delay_cost=1)
	S += t9_t0_t2_mem0 >= 8
	t9_t0_t2_mem0 += INPUT_mem_r

	t9_t0_t2_mem1 = S.Task('t9_t0_t2_mem1', length=1, delay_cost=1)
	S += t9_t0_t2_mem1 >= 8
	t9_t0_t2_mem1 += INPUT_mem_r

	t0_t20_mem0 = S.Task('t0_t20_mem0', length=1, delay_cost=1)
	S += t0_t20_mem0 >= 9
	t0_t20_mem0 += INPUT_mem_r

	t0_t20_mem1 = S.Task('t0_t20_mem1', length=1, delay_cost=1)
	S += t0_t20_mem1 >= 9
	t0_t20_mem1 += INPUT_mem_r

	t9_t0_t2 = S.Task('t9_t0_t2', length=1, delay_cost=1)
	S += t9_t0_t2 >= 9
	t9_t0_t2 += ADD[0]

	t0_t0_t2_mem0 = S.Task('t0_t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t0_t2_mem0 >= 10
	t0_t0_t2_mem0 += INPUT_mem_r

	t0_t0_t2_mem1 = S.Task('t0_t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t0_t2_mem1 >= 10
	t0_t0_t2_mem1 += INPUT_mem_r

	t0_t20 = S.Task('t0_t20', length=1, delay_cost=1)
	S += t0_t20 >= 10
	t0_t20 += ADD[0]

	t0_t0_t2 = S.Task('t0_t0_t2', length=1, delay_cost=1)
	S += t0_t0_t2 >= 11
	t0_t0_t2 += ADD[0]

	t0_t21_mem0 = S.Task('t0_t21_mem0', length=1, delay_cost=1)
	S += t0_t21_mem0 >= 11
	t0_t21_mem0 += INPUT_mem_r

	t0_t21_mem1 = S.Task('t0_t21_mem1', length=1, delay_cost=1)
	S += t0_t21_mem1 >= 11
	t0_t21_mem1 += INPUT_mem_r

	t0_t21 = S.Task('t0_t21', length=1, delay_cost=1)
	S += t0_t21 >= 12
	t0_t21 += ADD[0]

	t7_t20_mem0 = S.Task('t7_t20_mem0', length=1, delay_cost=1)
	S += t7_t20_mem0 >= 12
	t7_t20_mem0 += INPUT_mem_r

	t7_t20_mem1 = S.Task('t7_t20_mem1', length=1, delay_cost=1)
	S += t7_t20_mem1 >= 12
	t7_t20_mem1 += INPUT_mem_r

	t2_t31_mem0 = S.Task('t2_t31_mem0', length=1, delay_cost=1)
	S += t2_t31_mem0 >= 13
	t2_t31_mem0 += INPUT_mem_r

	t2_t31_mem1 = S.Task('t2_t31_mem1', length=1, delay_cost=1)
	S += t2_t31_mem1 >= 13
	t2_t31_mem1 += INPUT_mem_r

	t7_t20 = S.Task('t7_t20', length=1, delay_cost=1)
	S += t7_t20 >= 13
	t7_t20 += ADD[0]

	t0_t31_mem0 = S.Task('t0_t31_mem0', length=1, delay_cost=1)
	S += t0_t31_mem0 >= 14
	t0_t31_mem0 += INPUT_mem_r

	t0_t31_mem1 = S.Task('t0_t31_mem1', length=1, delay_cost=1)
	S += t0_t31_mem1 >= 14
	t0_t31_mem1 += INPUT_mem_r

	t2_t31 = S.Task('t2_t31', length=1, delay_cost=1)
	S += t2_t31 >= 14
	t2_t31 += ADD[0]

	t0_t31 = S.Task('t0_t31', length=1, delay_cost=1)
	S += t0_t31 >= 15
	t0_t31 += ADD[2]

	t2_t30_mem0 = S.Task('t2_t30_mem0', length=1, delay_cost=1)
	S += t2_t30_mem0 >= 15
	t2_t30_mem0 += INPUT_mem_r

	t2_t30_mem1 = S.Task('t2_t30_mem1', length=1, delay_cost=1)
	S += t2_t30_mem1 >= 15
	t2_t30_mem1 += INPUT_mem_r

	t2_t30 = S.Task('t2_t30', length=1, delay_cost=1)
	S += t2_t30 >= 16
	t2_t30 += ADD[0]

	t7_t1_t2_mem0 = S.Task('t7_t1_t2_mem0', length=1, delay_cost=1)
	S += t7_t1_t2_mem0 >= 16
	t7_t1_t2_mem0 += INPUT_mem_r

	t7_t1_t2_mem1 = S.Task('t7_t1_t2_mem1', length=1, delay_cost=1)
	S += t7_t1_t2_mem1 >= 16
	t7_t1_t2_mem1 += INPUT_mem_r

	t2_t21_mem0 = S.Task('t2_t21_mem0', length=1, delay_cost=1)
	S += t2_t21_mem0 >= 17
	t2_t21_mem0 += INPUT_mem_r

	t2_t21_mem1 = S.Task('t2_t21_mem1', length=1, delay_cost=1)
	S += t2_t21_mem1 >= 17
	t2_t21_mem1 += INPUT_mem_r

	t7_t1_t2 = S.Task('t7_t1_t2', length=1, delay_cost=1)
	S += t7_t1_t2 >= 17
	t7_t1_t2 += ADD[1]

	t2_t21 = S.Task('t2_t21', length=1, delay_cost=1)
	S += t2_t21 >= 18
	t2_t21 += ADD[0]

	t9_t1_t2_mem0 = S.Task('t9_t1_t2_mem0', length=1, delay_cost=1)
	S += t9_t1_t2_mem0 >= 18
	t9_t1_t2_mem0 += INPUT_mem_r

	t9_t1_t2_mem1 = S.Task('t9_t1_t2_mem1', length=1, delay_cost=1)
	S += t9_t1_t2_mem1 >= 18
	t9_t1_t2_mem1 += INPUT_mem_r

	t7_t21_mem0 = S.Task('t7_t21_mem0', length=1, delay_cost=1)
	S += t7_t21_mem0 >= 19
	t7_t21_mem0 += INPUT_mem_r

	t7_t21_mem1 = S.Task('t7_t21_mem1', length=1, delay_cost=1)
	S += t7_t21_mem1 >= 19
	t7_t21_mem1 += INPUT_mem_r

	t9_t1_t2 = S.Task('t9_t1_t2', length=1, delay_cost=1)
	S += t9_t1_t2 >= 19
	t9_t1_t2 += ADD[0]

	t0_t1_t3_mem0 = S.Task('t0_t1_t3_mem0', length=1, delay_cost=1)
	S += t0_t1_t3_mem0 >= 20
	t0_t1_t3_mem0 += INPUT_mem_r

	t0_t1_t3_mem1 = S.Task('t0_t1_t3_mem1', length=1, delay_cost=1)
	S += t0_t1_t3_mem1 >= 20
	t0_t1_t3_mem1 += INPUT_mem_r

	t7_t21 = S.Task('t7_t21', length=1, delay_cost=1)
	S += t7_t21 >= 20
	t7_t21 += ADD[0]

	t0_t1_t3 = S.Task('t0_t1_t3', length=1, delay_cost=1)
	S += t0_t1_t3 >= 21
	t0_t1_t3 += ADD[0]

	t0_t30_mem0 = S.Task('t0_t30_mem0', length=1, delay_cost=1)
	S += t0_t30_mem0 >= 21
	t0_t30_mem0 += INPUT_mem_r

	t0_t30_mem1 = S.Task('t0_t30_mem1', length=1, delay_cost=1)
	S += t0_t30_mem1 >= 21
	t0_t30_mem1 += INPUT_mem_r

	t0_t1_t2_mem0 = S.Task('t0_t1_t2_mem0', length=1, delay_cost=1)
	S += t0_t1_t2_mem0 >= 22
	t0_t1_t2_mem0 += INPUT_mem_r

	t0_t1_t2_mem1 = S.Task('t0_t1_t2_mem1', length=1, delay_cost=1)
	S += t0_t1_t2_mem1 >= 22
	t0_t1_t2_mem1 += INPUT_mem_r

	t0_t30 = S.Task('t0_t30', length=1, delay_cost=1)
	S += t0_t30 >= 22
	t0_t30 += ADD[0]

	t0_t1_t2 = S.Task('t0_t1_t2', length=1, delay_cost=1)
	S += t0_t1_t2 >= 23
	t0_t1_t2 += ADD[0]

	t7_t0_t2_mem0 = S.Task('t7_t0_t2_mem0', length=1, delay_cost=1)
	S += t7_t0_t2_mem0 >= 23
	t7_t0_t2_mem0 += INPUT_mem_r

	t7_t0_t2_mem1 = S.Task('t7_t0_t2_mem1', length=1, delay_cost=1)
	S += t7_t0_t2_mem1 >= 23
	t7_t0_t2_mem1 += INPUT_mem_r

	t0_t0_t3_mem0 = S.Task('t0_t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t0_t3_mem0 >= 24
	t0_t0_t3_mem0 += INPUT_mem_r

	t0_t0_t3_mem1 = S.Task('t0_t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t0_t3_mem1 >= 24
	t0_t0_t3_mem1 += INPUT_mem_r

	t7_t0_t2 = S.Task('t7_t0_t2', length=1, delay_cost=1)
	S += t7_t0_t2 >= 24
	t7_t0_t2 += ADD[1]

	t0_t0_t3 = S.Task('t0_t0_t3', length=1, delay_cost=1)
	S += t0_t0_t3 >= 25
	t0_t0_t3 += ADD[3]

	t2_t20_mem0 = S.Task('t2_t20_mem0', length=1, delay_cost=1)
	S += t2_t20_mem0 >= 25
	t2_t20_mem0 += INPUT_mem_r

	t2_t20_mem1 = S.Task('t2_t20_mem1', length=1, delay_cost=1)
	S += t2_t20_mem1 >= 25
	t2_t20_mem1 += INPUT_mem_r

	t2_t1_t3_mem0 = S.Task('t2_t1_t3_mem0', length=1, delay_cost=1)
	S += t2_t1_t3_mem0 >= 26
	t2_t1_t3_mem0 += INPUT_mem_r

	t2_t1_t3_mem1 = S.Task('t2_t1_t3_mem1', length=1, delay_cost=1)
	S += t2_t1_t3_mem1 >= 26
	t2_t1_t3_mem1 += INPUT_mem_r

	t2_t20 = S.Task('t2_t20', length=1, delay_cost=1)
	S += t2_t20 >= 26
	t2_t20 += ADD[2]

	t2_t1_t2_mem0 = S.Task('t2_t1_t2_mem0', length=1, delay_cost=1)
	S += t2_t1_t2_mem0 >= 27
	t2_t1_t2_mem0 += INPUT_mem_r

	t2_t1_t2_mem1 = S.Task('t2_t1_t2_mem1', length=1, delay_cost=1)
	S += t2_t1_t2_mem1 >= 27
	t2_t1_t2_mem1 += INPUT_mem_r

	t2_t1_t3 = S.Task('t2_t1_t3', length=1, delay_cost=1)
	S += t2_t1_t3 >= 27
	t2_t1_t3 += ADD[0]

	t2_t0_t3_mem0 = S.Task('t2_t0_t3_mem0', length=1, delay_cost=1)
	S += t2_t0_t3_mem0 >= 28
	t2_t0_t3_mem0 += INPUT_mem_r

	t2_t0_t3_mem1 = S.Task('t2_t0_t3_mem1', length=1, delay_cost=1)
	S += t2_t0_t3_mem1 >= 28
	t2_t0_t3_mem1 += INPUT_mem_r

	t2_t1_t2 = S.Task('t2_t1_t2', length=1, delay_cost=1)
	S += t2_t1_t2 >= 28
	t2_t1_t2 += ADD[0]

	t2_t0_t2_mem0 = S.Task('t2_t0_t2_mem0', length=1, delay_cost=1)
	S += t2_t0_t2_mem0 >= 29
	t2_t0_t2_mem0 += INPUT_mem_r

	t2_t0_t2_mem1 = S.Task('t2_t0_t2_mem1', length=1, delay_cost=1)
	S += t2_t0_t2_mem1 >= 29
	t2_t0_t2_mem1 += INPUT_mem_r

	t2_t0_t3 = S.Task('t2_t0_t3', length=1, delay_cost=1)
	S += t2_t0_t3 >= 29
	t2_t0_t3 += ADD[3]

	t2_t0_t2 = S.Task('t2_t0_t2', length=1, delay_cost=1)
	S += t2_t0_t2 >= 30
	t2_t0_t2 += ADD[2]


	# new tasks
	t9_t20 = S.Task('t9_t20', length=1, delay_cost=1)
	t9_t20 += alt(ADD)

	t9_t20_mem0 = S.Task('t9_t20_mem0', length=1, delay_cost=1)
	t9_t20_mem0 += INPUT_mem_r
	S += t9_t20_mem0 <= t9_t20

	t9_t20_mem1 = S.Task('t9_t20_mem1', length=1, delay_cost=1)
	t9_t20_mem1 += INPUT_mem_r
	S += t9_t20_mem1 <= t9_t20

	t9_t21 = S.Task('t9_t21', length=1, delay_cost=1)
	t9_t21 += alt(ADD)

	t9_t21_mem0 = S.Task('t9_t21_mem0', length=1, delay_cost=1)
	t9_t21_mem0 += INPUT_mem_r
	S += t9_t21_mem0 <= t9_t21

	t9_t21_mem1 = S.Task('t9_t21_mem1', length=1, delay_cost=1)
	t9_t21_mem1 += INPUT_mem_r
	S += t9_t21_mem1 <= t9_t21

	t14_t0_t2 = S.Task('t14_t0_t2', length=1, delay_cost=1)
	t14_t0_t2 += alt(ADD)

	t14_t0_t2_mem0 = S.Task('t14_t0_t2_mem0', length=1, delay_cost=1)
	t14_t0_t2_mem0 += INPUT_mem_r
	S += t14_t0_t2_mem0 <= t14_t0_t2

	t14_t0_t2_mem1 = S.Task('t14_t0_t2_mem1', length=1, delay_cost=1)
	t14_t0_t2_mem1 += INPUT_mem_r
	S += t14_t0_t2_mem1 <= t14_t0_t2

	t14_t1_t2 = S.Task('t14_t1_t2', length=1, delay_cost=1)
	t14_t1_t2 += alt(ADD)

	t14_t1_t2_mem0 = S.Task('t14_t1_t2_mem0', length=1, delay_cost=1)
	t14_t1_t2_mem0 += INPUT_mem_r
	S += t14_t1_t2_mem0 <= t14_t1_t2

	t14_t1_t2_mem1 = S.Task('t14_t1_t2_mem1', length=1, delay_cost=1)
	t14_t1_t2_mem1 += INPUT_mem_r
	S += t14_t1_t2_mem1 <= t14_t1_t2

	t14_t20 = S.Task('t14_t20', length=1, delay_cost=1)
	t14_t20 += alt(ADD)

	t14_t20_mem0 = S.Task('t14_t20_mem0', length=1, delay_cost=1)
	t14_t20_mem0 += INPUT_mem_r
	S += t14_t20_mem0 <= t14_t20

	t14_t20_mem1 = S.Task('t14_t20_mem1', length=1, delay_cost=1)
	t14_t20_mem1 += INPUT_mem_r
	S += t14_t20_mem1 <= t14_t20

	t14_t21 = S.Task('t14_t21', length=1, delay_cost=1)
	t14_t21 += alt(ADD)

	t14_t21_mem0 = S.Task('t14_t21_mem0', length=1, delay_cost=1)
	t14_t21_mem0 += INPUT_mem_r
	S += t14_t21_mem0 <= t14_t21

	t14_t21_mem1 = S.Task('t14_t21_mem1', length=1, delay_cost=1)
	t14_t21_mem1 += INPUT_mem_r
	S += t14_t21_mem1 <= t14_t21

	new_TZ_t0_t2 = S.Task('new_TZ_t0_t2', length=1, delay_cost=1)
	new_TZ_t0_t2 += alt(ADD)

	new_TZ_t0_t2_mem0 = S.Task('new_TZ_t0_t2_mem0', length=1, delay_cost=1)
	new_TZ_t0_t2_mem0 += INPUT_mem_r
	S += new_TZ_t0_t2_mem0 <= new_TZ_t0_t2

	new_TZ_t0_t2_mem1 = S.Task('new_TZ_t0_t2_mem1', length=1, delay_cost=1)
	new_TZ_t0_t2_mem1 += INPUT_mem_r
	S += new_TZ_t0_t2_mem1 <= new_TZ_t0_t2

	new_TZ_t1_t2 = S.Task('new_TZ_t1_t2', length=1, delay_cost=1)
	new_TZ_t1_t2 += alt(ADD)

	new_TZ_t1_t2_mem0 = S.Task('new_TZ_t1_t2_mem0', length=1, delay_cost=1)
	new_TZ_t1_t2_mem0 += INPUT_mem_r
	S += new_TZ_t1_t2_mem0 <= new_TZ_t1_t2

	new_TZ_t1_t2_mem1 = S.Task('new_TZ_t1_t2_mem1', length=1, delay_cost=1)
	new_TZ_t1_t2_mem1 += INPUT_mem_r
	S += new_TZ_t1_t2_mem1 <= new_TZ_t1_t2

	new_TZ_t20 = S.Task('new_TZ_t20', length=1, delay_cost=1)
	new_TZ_t20 += alt(ADD)

	new_TZ_t20_mem0 = S.Task('new_TZ_t20_mem0', length=1, delay_cost=1)
	new_TZ_t20_mem0 += INPUT_mem_r
	S += new_TZ_t20_mem0 <= new_TZ_t20

	new_TZ_t20_mem1 = S.Task('new_TZ_t20_mem1', length=1, delay_cost=1)
	new_TZ_t20_mem1 += INPUT_mem_r
	S += new_TZ_t20_mem1 <= new_TZ_t20

	new_TZ_t21 = S.Task('new_TZ_t21', length=1, delay_cost=1)
	new_TZ_t21 += alt(ADD)

	new_TZ_t21_mem0 = S.Task('new_TZ_t21_mem0', length=1, delay_cost=1)
	new_TZ_t21_mem0 += INPUT_mem_r
	S += new_TZ_t21_mem0 <= new_TZ_t21

	new_TZ_t21_mem1 = S.Task('new_TZ_t21_mem1', length=1, delay_cost=1)
	new_TZ_t21_mem1 += INPUT_mem_r
	S += new_TZ_t21_mem1 <= new_TZ_t21

	t16_t0_t2 = S.Task('t16_t0_t2', length=1, delay_cost=1)
	t16_t0_t2 += alt(ADD)

	t16_t0_t2_mem0 = S.Task('t16_t0_t2_mem0', length=1, delay_cost=1)
	t16_t0_t2_mem0 += INPUT_mem_r
	S += t16_t0_t2_mem0 <= t16_t0_t2

	t16_t0_t2_mem1 = S.Task('t16_t0_t2_mem1', length=1, delay_cost=1)
	t16_t0_t2_mem1 += INPUT_mem_r
	S += t16_t0_t2_mem1 <= t16_t0_t2

	t16_t1_t2 = S.Task('t16_t1_t2', length=1, delay_cost=1)
	t16_t1_t2 += alt(ADD)

	t16_t1_t2_mem0 = S.Task('t16_t1_t2_mem0', length=1, delay_cost=1)
	t16_t1_t2_mem0 += INPUT_mem_r
	S += t16_t1_t2_mem0 <= t16_t1_t2

	t16_t1_t2_mem1 = S.Task('t16_t1_t2_mem1', length=1, delay_cost=1)
	t16_t1_t2_mem1 += INPUT_mem_r
	S += t16_t1_t2_mem1 <= t16_t1_t2

	t16_t20 = S.Task('t16_t20', length=1, delay_cost=1)
	t16_t20 += alt(ADD)

	t16_t20_mem0 = S.Task('t16_t20_mem0', length=1, delay_cost=1)
	t16_t20_mem0 += INPUT_mem_r
	S += t16_t20_mem0 <= t16_t20

	t16_t20_mem1 = S.Task('t16_t20_mem1', length=1, delay_cost=1)
	t16_t20_mem1 += INPUT_mem_r
	S += t16_t20_mem1 <= t16_t20

	t16_t21 = S.Task('t16_t21', length=1, delay_cost=1)
	t16_t21 += alt(ADD)

	t16_t21_mem0 = S.Task('t16_t21_mem0', length=1, delay_cost=1)
	t16_t21_mem0 += INPUT_mem_r
	S += t16_t21_mem0 <= t16_t21

	t16_t21_mem1 = S.Task('t16_t21_mem1', length=1, delay_cost=1)
	t16_t21_mem1 += INPUT_mem_r
	S += t16_t21_mem1 <= t16_t21

	t17_t0_t2 = S.Task('t17_t0_t2', length=1, delay_cost=1)
	t17_t0_t2 += alt(ADD)

	t17_t0_t2_mem0 = S.Task('t17_t0_t2_mem0', length=1, delay_cost=1)
	t17_t0_t2_mem0 += INPUT_mem_r
	S += t17_t0_t2_mem0 <= t17_t0_t2

	t17_t0_t2_mem1 = S.Task('t17_t0_t2_mem1', length=1, delay_cost=1)
	t17_t0_t2_mem1 += INPUT_mem_r
	S += t17_t0_t2_mem1 <= t17_t0_t2

	t17_t1_t2 = S.Task('t17_t1_t2', length=1, delay_cost=1)
	t17_t1_t2 += alt(ADD)

	t17_t1_t2_mem0 = S.Task('t17_t1_t2_mem0', length=1, delay_cost=1)
	t17_t1_t2_mem0 += INPUT_mem_r
	S += t17_t1_t2_mem0 <= t17_t1_t2

	t17_t1_t2_mem1 = S.Task('t17_t1_t2_mem1', length=1, delay_cost=1)
	t17_t1_t2_mem1 += INPUT_mem_r
	S += t17_t1_t2_mem1 <= t17_t1_t2

	t17_t20 = S.Task('t17_t20', length=1, delay_cost=1)
	t17_t20 += alt(ADD)

	t17_t20_mem0 = S.Task('t17_t20_mem0', length=1, delay_cost=1)
	t17_t20_mem0 += INPUT_mem_r
	S += t17_t20_mem0 <= t17_t20

	t17_t20_mem1 = S.Task('t17_t20_mem1', length=1, delay_cost=1)
	t17_t20_mem1 += INPUT_mem_r
	S += t17_t20_mem1 <= t17_t20

	t17_t21 = S.Task('t17_t21', length=1, delay_cost=1)
	t17_t21 += alt(ADD)

	t17_t21_mem0 = S.Task('t17_t21_mem0', length=1, delay_cost=1)
	t17_t21_mem0 += INPUT_mem_r
	S += t17_t21_mem0 <= t17_t21

	t17_t21_mem1 = S.Task('t17_t21_mem1', length=1, delay_cost=1)
	t17_t21_mem1 += INPUT_mem_r
	S += t17_t21_mem1 <= t17_t21

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/PADD_mul1_add4/PADD_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

