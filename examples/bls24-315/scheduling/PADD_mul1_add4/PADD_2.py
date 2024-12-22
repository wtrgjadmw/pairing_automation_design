from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 139
	S = Scenario("PADD_2", horizon=horizon)

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

	new_TZ_t20_mem0 = S.Task('new_TZ_t20_mem0', length=1, delay_cost=1)
	S += new_TZ_t20_mem0 >= 30
	new_TZ_t20_mem0 += INPUT_mem_r

	new_TZ_t20_mem1 = S.Task('new_TZ_t20_mem1', length=1, delay_cost=1)
	S += new_TZ_t20_mem1 >= 30
	new_TZ_t20_mem1 += INPUT_mem_r

	t2_t0_t2 = S.Task('t2_t0_t2', length=1, delay_cost=1)
	S += t2_t0_t2 >= 30
	t2_t0_t2 += ADD[2]

	new_TZ_t1_t2_mem0 = S.Task('new_TZ_t1_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t1_t2_mem0 >= 31
	new_TZ_t1_t2_mem0 += INPUT_mem_r

	new_TZ_t1_t2_mem1 = S.Task('new_TZ_t1_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t1_t2_mem1 >= 31
	new_TZ_t1_t2_mem1 += INPUT_mem_r

	new_TZ_t20 = S.Task('new_TZ_t20', length=1, delay_cost=1)
	S += new_TZ_t20 >= 31
	new_TZ_t20 += ADD[1]

	new_TZ_t1_t2 = S.Task('new_TZ_t1_t2', length=1, delay_cost=1)
	S += new_TZ_t1_t2 >= 32
	new_TZ_t1_t2 += ADD[0]

	new_TZ_t21_mem0 = S.Task('new_TZ_t21_mem0', length=1, delay_cost=1)
	S += new_TZ_t21_mem0 >= 32
	new_TZ_t21_mem0 += INPUT_mem_r

	new_TZ_t21_mem1 = S.Task('new_TZ_t21_mem1', length=1, delay_cost=1)
	S += new_TZ_t21_mem1 >= 32
	new_TZ_t21_mem1 += INPUT_mem_r

	new_TZ_t21 = S.Task('new_TZ_t21', length=1, delay_cost=1)
	S += new_TZ_t21 >= 33
	new_TZ_t21 += ADD[3]

	t9_t20_mem0 = S.Task('t9_t20_mem0', length=1, delay_cost=1)
	S += t9_t20_mem0 >= 33
	t9_t20_mem0 += INPUT_mem_r

	t9_t20_mem1 = S.Task('t9_t20_mem1', length=1, delay_cost=1)
	S += t9_t20_mem1 >= 33
	t9_t20_mem1 += INPUT_mem_r

	t16_t0_t2_mem0 = S.Task('t16_t0_t2_mem0', length=1, delay_cost=1)
	S += t16_t0_t2_mem0 >= 34
	t16_t0_t2_mem0 += INPUT_mem_r

	t16_t0_t2_mem1 = S.Task('t16_t0_t2_mem1', length=1, delay_cost=1)
	S += t16_t0_t2_mem1 >= 34
	t16_t0_t2_mem1 += INPUT_mem_r

	t9_t20 = S.Task('t9_t20', length=1, delay_cost=1)
	S += t9_t20 >= 34
	t9_t20 += ADD[2]

	t16_t0_t2 = S.Task('t16_t0_t2', length=1, delay_cost=1)
	S += t16_t0_t2 >= 35
	t16_t0_t2 += ADD[2]

	t16_t1_t2_mem0 = S.Task('t16_t1_t2_mem0', length=1, delay_cost=1)
	S += t16_t1_t2_mem0 >= 35
	t16_t1_t2_mem0 += INPUT_mem_r

	t16_t1_t2_mem1 = S.Task('t16_t1_t2_mem1', length=1, delay_cost=1)
	S += t16_t1_t2_mem1 >= 35
	t16_t1_t2_mem1 += INPUT_mem_r

	t16_t1_t2 = S.Task('t16_t1_t2', length=1, delay_cost=1)
	S += t16_t1_t2 >= 36
	t16_t1_t2 += ADD[2]

	t16_t20_mem0 = S.Task('t16_t20_mem0', length=1, delay_cost=1)
	S += t16_t20_mem0 >= 36
	t16_t20_mem0 += INPUT_mem_r

	t16_t20_mem1 = S.Task('t16_t20_mem1', length=1, delay_cost=1)
	S += t16_t20_mem1 >= 36
	t16_t20_mem1 += INPUT_mem_r

	t16_t20 = S.Task('t16_t20', length=1, delay_cost=1)
	S += t16_t20 >= 37
	t16_t20 += ADD[2]

	t16_t21_mem0 = S.Task('t16_t21_mem0', length=1, delay_cost=1)
	S += t16_t21_mem0 >= 37
	t16_t21_mem0 += INPUT_mem_r

	t16_t21_mem1 = S.Task('t16_t21_mem1', length=1, delay_cost=1)
	S += t16_t21_mem1 >= 37
	t16_t21_mem1 += INPUT_mem_r

	t16_t21 = S.Task('t16_t21', length=1, delay_cost=1)
	S += t16_t21 >= 38
	t16_t21 += ADD[2]

	t17_t0_t2_mem0 = S.Task('t17_t0_t2_mem0', length=1, delay_cost=1)
	S += t17_t0_t2_mem0 >= 38
	t17_t0_t2_mem0 += INPUT_mem_r

	t17_t0_t2_mem1 = S.Task('t17_t0_t2_mem1', length=1, delay_cost=1)
	S += t17_t0_t2_mem1 >= 38
	t17_t0_t2_mem1 += INPUT_mem_r

	t17_t0_t2 = S.Task('t17_t0_t2', length=1, delay_cost=1)
	S += t17_t0_t2 >= 39
	t17_t0_t2 += ADD[1]

	t17_t1_t2_mem0 = S.Task('t17_t1_t2_mem0', length=1, delay_cost=1)
	S += t17_t1_t2_mem0 >= 39
	t17_t1_t2_mem0 += INPUT_mem_r

	t17_t1_t2_mem1 = S.Task('t17_t1_t2_mem1', length=1, delay_cost=1)
	S += t17_t1_t2_mem1 >= 39
	t17_t1_t2_mem1 += INPUT_mem_r

	t17_t1_t2 = S.Task('t17_t1_t2', length=1, delay_cost=1)
	S += t17_t1_t2 >= 40
	t17_t1_t2 += ADD[2]

	t17_t20_mem0 = S.Task('t17_t20_mem0', length=1, delay_cost=1)
	S += t17_t20_mem0 >= 40
	t17_t20_mem0 += INPUT_mem_r

	t17_t20_mem1 = S.Task('t17_t20_mem1', length=1, delay_cost=1)
	S += t17_t20_mem1 >= 40
	t17_t20_mem1 += INPUT_mem_r

	t17_t20 = S.Task('t17_t20', length=1, delay_cost=1)
	S += t17_t20 >= 41
	t17_t20 += ADD[2]

	t17_t21_mem0 = S.Task('t17_t21_mem0', length=1, delay_cost=1)
	S += t17_t21_mem0 >= 41
	t17_t21_mem0 += INPUT_mem_r

	t17_t21_mem1 = S.Task('t17_t21_mem1', length=1, delay_cost=1)
	S += t17_t21_mem1 >= 41
	t17_t21_mem1 += INPUT_mem_r

	t17_t21 = S.Task('t17_t21', length=1, delay_cost=1)
	S += t17_t21 >= 42
	t17_t21 += ADD[0]

	t9_t21_mem0 = S.Task('t9_t21_mem0', length=1, delay_cost=1)
	S += t9_t21_mem0 >= 42
	t9_t21_mem0 += INPUT_mem_r

	t9_t21_mem1 = S.Task('t9_t21_mem1', length=1, delay_cost=1)
	S += t9_t21_mem1 >= 42
	t9_t21_mem1 += INPUT_mem_r

	new_TZ_t0_t2_mem0 = S.Task('new_TZ_t0_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t0_t2_mem0 >= 43
	new_TZ_t0_t2_mem0 += INPUT_mem_r

	new_TZ_t0_t2_mem1 = S.Task('new_TZ_t0_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t0_t2_mem1 >= 43
	new_TZ_t0_t2_mem1 += INPUT_mem_r

	t9_t21 = S.Task('t9_t21', length=1, delay_cost=1)
	S += t9_t21 >= 43
	t9_t21 += ADD[0]

	new_TZ_t0_t2 = S.Task('new_TZ_t0_t2', length=1, delay_cost=1)
	S += new_TZ_t0_t2 >= 44
	new_TZ_t0_t2 += ADD[0]

	t14_t1_t2_mem0 = S.Task('t14_t1_t2_mem0', length=1, delay_cost=1)
	S += t14_t1_t2_mem0 >= 44
	t14_t1_t2_mem0 += INPUT_mem_r

	t14_t1_t2_mem1 = S.Task('t14_t1_t2_mem1', length=1, delay_cost=1)
	S += t14_t1_t2_mem1 >= 44
	t14_t1_t2_mem1 += INPUT_mem_r

	t14_t0_t2_mem0 = S.Task('t14_t0_t2_mem0', length=1, delay_cost=1)
	S += t14_t0_t2_mem0 >= 45
	t14_t0_t2_mem0 += INPUT_mem_r

	t14_t0_t2_mem1 = S.Task('t14_t0_t2_mem1', length=1, delay_cost=1)
	S += t14_t0_t2_mem1 >= 45
	t14_t0_t2_mem1 += INPUT_mem_r

	t14_t1_t2 = S.Task('t14_t1_t2', length=1, delay_cost=1)
	S += t14_t1_t2 >= 45
	t14_t1_t2 += ADD[0]

	t14_t0_t2 = S.Task('t14_t0_t2', length=1, delay_cost=1)
	S += t14_t0_t2 >= 46
	t14_t0_t2 += ADD[1]

	t14_t20_mem0 = S.Task('t14_t20_mem0', length=1, delay_cost=1)
	S += t14_t20_mem0 >= 46
	t14_t20_mem0 += INPUT_mem_r

	t14_t20_mem1 = S.Task('t14_t20_mem1', length=1, delay_cost=1)
	S += t14_t20_mem1 >= 46
	t14_t20_mem1 += INPUT_mem_r

	t14_t20 = S.Task('t14_t20', length=1, delay_cost=1)
	S += t14_t20 >= 47
	t14_t20 += ADD[1]

	t14_t21_mem0 = S.Task('t14_t21_mem0', length=1, delay_cost=1)
	S += t14_t21_mem0 >= 47
	t14_t21_mem0 += INPUT_mem_r

	t14_t21_mem1 = S.Task('t14_t21_mem1', length=1, delay_cost=1)
	S += t14_t21_mem1 >= 47
	t14_t21_mem1 += INPUT_mem_r

	t14_t21 = S.Task('t14_t21', length=1, delay_cost=1)
	S += t14_t21 >= 48
	t14_t21 += ADD[2]


	# new tasks
	t0_t0_t4_in = S.Task('t0_t0_t4_in', length=1, delay_cost=1)
	t0_t0_t4_in += alt(MUL_in)
	t0_t0_t4 = S.Task('t0_t0_t4', length=7, delay_cost=1)
	t0_t0_t4 += alt(MUL)
	S += t0_t0_t4>=t0_t0_t4_in

	t0_t0_t4_mem0 = S.Task('t0_t0_t4_mem0', length=1, delay_cost=1)
	t0_t0_t4_mem0 += ADD_mem[0]
	S += 11 < t0_t0_t4_mem0
	S += t0_t0_t4_mem0 <= t0_t0_t4

	t0_t0_t4_mem1 = S.Task('t0_t0_t4_mem1', length=1, delay_cost=1)
	t0_t0_t4_mem1 += ADD_mem[3]
	S += 25 < t0_t0_t4_mem1
	S += t0_t0_t4_mem1 <= t0_t0_t4

	t0_t0_s00 = S.Task('t0_t0_s00', length=1, delay_cost=1)
	t0_t0_s00 += alt(ADD)

	t0_t0_s00_mem0 = S.Task('t0_t0_s00_mem0', length=1, delay_cost=1)
	t0_t0_s00_mem0 += MUL_mem[0]
	S += 13 < t0_t0_s00_mem0
	S += t0_t0_s00_mem0 <= t0_t0_s00

	t0_t0_t5 = S.Task('t0_t0_t5', length=1, delay_cost=1)
	t0_t0_t5 += alt(ADD)

	t0_t0_t5_mem0 = S.Task('t0_t0_t5_mem0', length=1, delay_cost=1)
	t0_t0_t5_mem0 += MUL_mem[0]
	S += 14 < t0_t0_t5_mem0
	S += t0_t0_t5_mem0 <= t0_t0_t5

	t0_t0_t5_mem1 = S.Task('t0_t0_t5_mem1', length=1, delay_cost=1)
	t0_t0_t5_mem1 += MUL_mem[0]
	S += 13 < t0_t0_t5_mem1
	S += t0_t0_t5_mem1 <= t0_t0_t5

	t0_t1_t4_in = S.Task('t0_t1_t4_in', length=1, delay_cost=1)
	t0_t1_t4_in += alt(MUL_in)
	t0_t1_t4 = S.Task('t0_t1_t4', length=7, delay_cost=1)
	t0_t1_t4 += alt(MUL)
	S += t0_t1_t4>=t0_t1_t4_in

	t0_t1_t4_mem0 = S.Task('t0_t1_t4_mem0', length=1, delay_cost=1)
	t0_t1_t4_mem0 += ADD_mem[0]
	S += 23 < t0_t1_t4_mem0
	S += t0_t1_t4_mem0 <= t0_t1_t4

	t0_t1_t4_mem1 = S.Task('t0_t1_t4_mem1', length=1, delay_cost=1)
	t0_t1_t4_mem1 += ADD_mem[0]
	S += 21 < t0_t1_t4_mem1
	S += t0_t1_t4_mem1 <= t0_t1_t4

	t0_t1_s00 = S.Task('t0_t1_s00', length=1, delay_cost=1)
	t0_t1_s00 += alt(ADD)

	t0_t1_s00_mem0 = S.Task('t0_t1_s00_mem0', length=1, delay_cost=1)
	t0_t1_s00_mem0 += MUL_mem[0]
	S += 8 < t0_t1_s00_mem0
	S += t0_t1_s00_mem0 <= t0_t1_s00

	t0_t1_t5 = S.Task('t0_t1_t5', length=1, delay_cost=1)
	t0_t1_t5 += alt(ADD)

	t0_t1_t5_mem0 = S.Task('t0_t1_t5_mem0', length=1, delay_cost=1)
	t0_t1_t5_mem0 += MUL_mem[0]
	S += 12 < t0_t1_t5_mem0
	S += t0_t1_t5_mem0 <= t0_t1_t5

	t0_t1_t5_mem1 = S.Task('t0_t1_t5_mem1', length=1, delay_cost=1)
	t0_t1_t5_mem1 += MUL_mem[0]
	S += 8 < t0_t1_t5_mem1
	S += t0_t1_t5_mem1 <= t0_t1_t5

	t0_t4_t0_in = S.Task('t0_t4_t0_in', length=1, delay_cost=1)
	t0_t4_t0_in += alt(MUL_in)
	t0_t4_t0 = S.Task('t0_t4_t0', length=7, delay_cost=1)
	t0_t4_t0 += alt(MUL)
	S += t0_t4_t0>=t0_t4_t0_in

	t0_t4_t0_mem0 = S.Task('t0_t4_t0_mem0', length=1, delay_cost=1)
	t0_t4_t0_mem0 += ADD_mem[0]
	S += 10 < t0_t4_t0_mem0
	S += t0_t4_t0_mem0 <= t0_t4_t0

	t0_t4_t0_mem1 = S.Task('t0_t4_t0_mem1', length=1, delay_cost=1)
	t0_t4_t0_mem1 += ADD_mem[0]
	S += 22 < t0_t4_t0_mem1
	S += t0_t4_t0_mem1 <= t0_t4_t0

	t0_t4_t1_in = S.Task('t0_t4_t1_in', length=1, delay_cost=1)
	t0_t4_t1_in += alt(MUL_in)
	t0_t4_t1 = S.Task('t0_t4_t1', length=7, delay_cost=1)
	t0_t4_t1 += alt(MUL)
	S += t0_t4_t1>=t0_t4_t1_in

	t0_t4_t1_mem0 = S.Task('t0_t4_t1_mem0', length=1, delay_cost=1)
	t0_t4_t1_mem0 += ADD_mem[0]
	S += 12 < t0_t4_t1_mem0
	S += t0_t4_t1_mem0 <= t0_t4_t1

	t0_t4_t1_mem1 = S.Task('t0_t4_t1_mem1', length=1, delay_cost=1)
	t0_t4_t1_mem1 += ADD_mem[2]
	S += 15 < t0_t4_t1_mem1
	S += t0_t4_t1_mem1 <= t0_t4_t1

	t0_t4_t2 = S.Task('t0_t4_t2', length=1, delay_cost=1)
	t0_t4_t2 += alt(ADD)

	t0_t4_t2_mem0 = S.Task('t0_t4_t2_mem0', length=1, delay_cost=1)
	t0_t4_t2_mem0 += ADD_mem[0]
	S += 10 < t0_t4_t2_mem0
	S += t0_t4_t2_mem0 <= t0_t4_t2

	t0_t4_t2_mem1 = S.Task('t0_t4_t2_mem1', length=1, delay_cost=1)
	t0_t4_t2_mem1 += ADD_mem[0]
	S += 12 < t0_t4_t2_mem1
	S += t0_t4_t2_mem1 <= t0_t4_t2

	t0_t4_t3 = S.Task('t0_t4_t3', length=1, delay_cost=1)
	t0_t4_t3 += alt(ADD)

	t0_t4_t3_mem0 = S.Task('t0_t4_t3_mem0', length=1, delay_cost=1)
	t0_t4_t3_mem0 += ADD_mem[0]
	S += 22 < t0_t4_t3_mem0
	S += t0_t4_t3_mem0 <= t0_t4_t3

	t0_t4_t3_mem1 = S.Task('t0_t4_t3_mem1', length=1, delay_cost=1)
	t0_t4_t3_mem1 += ADD_mem[2]
	S += 15 < t0_t4_t3_mem1
	S += t0_t4_t3_mem1 <= t0_t4_t3

	t2_t0_t4_in = S.Task('t2_t0_t4_in', length=1, delay_cost=1)
	t2_t0_t4_in += alt(MUL_in)
	t2_t0_t4 = S.Task('t2_t0_t4', length=7, delay_cost=1)
	t2_t0_t4 += alt(MUL)
	S += t2_t0_t4>=t2_t0_t4_in

	t2_t0_t4_mem0 = S.Task('t2_t0_t4_mem0', length=1, delay_cost=1)
	t2_t0_t4_mem0 += ADD_mem[2]
	S += 30 < t2_t0_t4_mem0
	S += t2_t0_t4_mem0 <= t2_t0_t4

	t2_t0_t4_mem1 = S.Task('t2_t0_t4_mem1', length=1, delay_cost=1)
	t2_t0_t4_mem1 += ADD_mem[3]
	S += 29 < t2_t0_t4_mem1
	S += t2_t0_t4_mem1 <= t2_t0_t4

	t2_t0_s00 = S.Task('t2_t0_s00', length=1, delay_cost=1)
	t2_t0_s00 += alt(ADD)

	t2_t0_s00_mem0 = S.Task('t2_t0_s00_mem0', length=1, delay_cost=1)
	t2_t0_s00_mem0 += MUL_mem[0]
	S += 9 < t2_t0_s00_mem0
	S += t2_t0_s00_mem0 <= t2_t0_s00

	t2_t0_t5 = S.Task('t2_t0_t5', length=1, delay_cost=1)
	t2_t0_t5 += alt(ADD)

	t2_t0_t5_mem0 = S.Task('t2_t0_t5_mem0', length=1, delay_cost=1)
	t2_t0_t5_mem0 += MUL_mem[0]
	S += 10 < t2_t0_t5_mem0
	S += t2_t0_t5_mem0 <= t2_t0_t5

	t2_t0_t5_mem1 = S.Task('t2_t0_t5_mem1', length=1, delay_cost=1)
	t2_t0_t5_mem1 += MUL_mem[0]
	S += 9 < t2_t0_t5_mem1
	S += t2_t0_t5_mem1 <= t2_t0_t5

	t2_t1_t4_in = S.Task('t2_t1_t4_in', length=1, delay_cost=1)
	t2_t1_t4_in += alt(MUL_in)
	t2_t1_t4 = S.Task('t2_t1_t4', length=7, delay_cost=1)
	t2_t1_t4 += alt(MUL)
	S += t2_t1_t4>=t2_t1_t4_in

	t2_t1_t4_mem0 = S.Task('t2_t1_t4_mem0', length=1, delay_cost=1)
	t2_t1_t4_mem0 += ADD_mem[0]
	S += 28 < t2_t1_t4_mem0
	S += t2_t1_t4_mem0 <= t2_t1_t4

	t2_t1_t4_mem1 = S.Task('t2_t1_t4_mem1', length=1, delay_cost=1)
	t2_t1_t4_mem1 += ADD_mem[0]
	S += 27 < t2_t1_t4_mem1
	S += t2_t1_t4_mem1 <= t2_t1_t4

	t2_t1_s00 = S.Task('t2_t1_s00', length=1, delay_cost=1)
	t2_t1_s00 += alt(ADD)

	t2_t1_s00_mem0 = S.Task('t2_t1_s00_mem0', length=1, delay_cost=1)
	t2_t1_s00_mem0 += MUL_mem[0]
	S += 7 < t2_t1_s00_mem0
	S += t2_t1_s00_mem0 <= t2_t1_s00

	t2_t1_t5 = S.Task('t2_t1_t5', length=1, delay_cost=1)
	t2_t1_t5 += alt(ADD)

	t2_t1_t5_mem0 = S.Task('t2_t1_t5_mem0', length=1, delay_cost=1)
	t2_t1_t5_mem0 += MUL_mem[0]
	S += 11 < t2_t1_t5_mem0
	S += t2_t1_t5_mem0 <= t2_t1_t5

	t2_t1_t5_mem1 = S.Task('t2_t1_t5_mem1', length=1, delay_cost=1)
	t2_t1_t5_mem1 += MUL_mem[0]
	S += 7 < t2_t1_t5_mem1
	S += t2_t1_t5_mem1 <= t2_t1_t5

	t2_t4_t0_in = S.Task('t2_t4_t0_in', length=1, delay_cost=1)
	t2_t4_t0_in += alt(MUL_in)
	t2_t4_t0 = S.Task('t2_t4_t0', length=7, delay_cost=1)
	t2_t4_t0 += alt(MUL)
	S += t2_t4_t0>=t2_t4_t0_in

	t2_t4_t0_mem0 = S.Task('t2_t4_t0_mem0', length=1, delay_cost=1)
	t2_t4_t0_mem0 += ADD_mem[2]
	S += 26 < t2_t4_t0_mem0
	S += t2_t4_t0_mem0 <= t2_t4_t0

	t2_t4_t0_mem1 = S.Task('t2_t4_t0_mem1', length=1, delay_cost=1)
	t2_t4_t0_mem1 += ADD_mem[0]
	S += 16 < t2_t4_t0_mem1
	S += t2_t4_t0_mem1 <= t2_t4_t0

	t2_t4_t1_in = S.Task('t2_t4_t1_in', length=1, delay_cost=1)
	t2_t4_t1_in += alt(MUL_in)
	t2_t4_t1 = S.Task('t2_t4_t1', length=7, delay_cost=1)
	t2_t4_t1 += alt(MUL)
	S += t2_t4_t1>=t2_t4_t1_in

	t2_t4_t1_mem0 = S.Task('t2_t4_t1_mem0', length=1, delay_cost=1)
	t2_t4_t1_mem0 += ADD_mem[0]
	S += 18 < t2_t4_t1_mem0
	S += t2_t4_t1_mem0 <= t2_t4_t1

	t2_t4_t1_mem1 = S.Task('t2_t4_t1_mem1', length=1, delay_cost=1)
	t2_t4_t1_mem1 += ADD_mem[0]
	S += 14 < t2_t4_t1_mem1
	S += t2_t4_t1_mem1 <= t2_t4_t1

	t2_t4_t2 = S.Task('t2_t4_t2', length=1, delay_cost=1)
	t2_t4_t2 += alt(ADD)

	t2_t4_t2_mem0 = S.Task('t2_t4_t2_mem0', length=1, delay_cost=1)
	t2_t4_t2_mem0 += ADD_mem[2]
	S += 26 < t2_t4_t2_mem0
	S += t2_t4_t2_mem0 <= t2_t4_t2

	t2_t4_t2_mem1 = S.Task('t2_t4_t2_mem1', length=1, delay_cost=1)
	t2_t4_t2_mem1 += ADD_mem[0]
	S += 18 < t2_t4_t2_mem1
	S += t2_t4_t2_mem1 <= t2_t4_t2

	t2_t4_t3 = S.Task('t2_t4_t3', length=1, delay_cost=1)
	t2_t4_t3 += alt(ADD)

	t2_t4_t3_mem0 = S.Task('t2_t4_t3_mem0', length=1, delay_cost=1)
	t2_t4_t3_mem0 += ADD_mem[0]
	S += 16 < t2_t4_t3_mem0
	S += t2_t4_t3_mem0 <= t2_t4_t3

	t2_t4_t3_mem1 = S.Task('t2_t4_t3_mem1', length=1, delay_cost=1)
	t2_t4_t3_mem1 += ADD_mem[0]
	S += 14 < t2_t4_t3_mem1
	S += t2_t4_t3_mem1 <= t2_t4_t3

	t7_t4_t2 = S.Task('t7_t4_t2', length=1, delay_cost=1)
	t7_t4_t2 += alt(ADD)

	t7_t4_t2_mem0 = S.Task('t7_t4_t2_mem0', length=1, delay_cost=1)
	t7_t4_t2_mem0 += ADD_mem[0]
	S += 13 < t7_t4_t2_mem0
	S += t7_t4_t2_mem0 <= t7_t4_t2

	t7_t4_t2_mem1 = S.Task('t7_t4_t2_mem1', length=1, delay_cost=1)
	t7_t4_t2_mem1 += ADD_mem[0]
	S += 20 < t7_t4_t2_mem1
	S += t7_t4_t2_mem1 <= t7_t4_t2

	t9_t4_t2 = S.Task('t9_t4_t2', length=1, delay_cost=1)
	t9_t4_t2 += alt(ADD)

	t9_t4_t2_mem0 = S.Task('t9_t4_t2_mem0', length=1, delay_cost=1)
	t9_t4_t2_mem0 += ADD_mem[2]
	S += 34 < t9_t4_t2_mem0
	S += t9_t4_t2_mem0 <= t9_t4_t2

	t9_t4_t2_mem1 = S.Task('t9_t4_t2_mem1', length=1, delay_cost=1)
	t9_t4_t2_mem1 += ADD_mem[0]
	S += 43 < t9_t4_t2_mem1
	S += t9_t4_t2_mem1 <= t9_t4_t2

	t14_t4_t2 = S.Task('t14_t4_t2', length=1, delay_cost=1)
	t14_t4_t2 += alt(ADD)

	t14_t4_t2_mem0 = S.Task('t14_t4_t2_mem0', length=1, delay_cost=1)
	t14_t4_t2_mem0 += ADD_mem[1]
	S += 47 < t14_t4_t2_mem0
	S += t14_t4_t2_mem0 <= t14_t4_t2

	t14_t4_t2_mem1 = S.Task('t14_t4_t2_mem1', length=1, delay_cost=1)
	t14_t4_t2_mem1 += ADD_mem[2]
	S += 48 < t14_t4_t2_mem1
	S += t14_t4_t2_mem1 <= t14_t4_t2

	new_TZ_t4_t2 = S.Task('new_TZ_t4_t2', length=1, delay_cost=1)
	new_TZ_t4_t2 += alt(ADD)

	new_TZ_t4_t2_mem0 = S.Task('new_TZ_t4_t2_mem0', length=1, delay_cost=1)
	new_TZ_t4_t2_mem0 += ADD_mem[1]
	S += 31 < new_TZ_t4_t2_mem0
	S += new_TZ_t4_t2_mem0 <= new_TZ_t4_t2

	new_TZ_t4_t2_mem1 = S.Task('new_TZ_t4_t2_mem1', length=1, delay_cost=1)
	new_TZ_t4_t2_mem1 += ADD_mem[3]
	S += 33 < new_TZ_t4_t2_mem1
	S += new_TZ_t4_t2_mem1 <= new_TZ_t4_t2

	t16_t4_t2 = S.Task('t16_t4_t2', length=1, delay_cost=1)
	t16_t4_t2 += alt(ADD)

	t16_t4_t2_mem0 = S.Task('t16_t4_t2_mem0', length=1, delay_cost=1)
	t16_t4_t2_mem0 += ADD_mem[2]
	S += 37 < t16_t4_t2_mem0
	S += t16_t4_t2_mem0 <= t16_t4_t2

	t16_t4_t2_mem1 = S.Task('t16_t4_t2_mem1', length=1, delay_cost=1)
	t16_t4_t2_mem1 += ADD_mem[2]
	S += 38 < t16_t4_t2_mem1
	S += t16_t4_t2_mem1 <= t16_t4_t2

	t17_t4_t2 = S.Task('t17_t4_t2', length=1, delay_cost=1)
	t17_t4_t2 += alt(ADD)

	t17_t4_t2_mem0 = S.Task('t17_t4_t2_mem0', length=1, delay_cost=1)
	t17_t4_t2_mem0 += ADD_mem[2]
	S += 41 < t17_t4_t2_mem0
	S += t17_t4_t2_mem0 <= t17_t4_t2

	t17_t4_t2_mem1 = S.Task('t17_t4_t2_mem1', length=1, delay_cost=1)
	t17_t4_t2_mem1 += ADD_mem[0]
	S += 42 < t17_t4_t2_mem1
	S += t17_t4_t2_mem1 <= t17_t4_t2

	t0_t0_s01 = S.Task('t0_t0_s01', length=1, delay_cost=1)
	t0_t0_s01 += alt(ADD)

	t0_t0_s01_mem0 = S.Task('t0_t0_s01_mem0', length=1, delay_cost=1)
	t0_t0_s01_mem0 += alt(ADD_mem)
	S += (t0_t0_s00*ADD[0])-1 < t0_t0_s01_mem0*ADD_mem[0]
	S += (t0_t0_s00*ADD[1])-1 < t0_t0_s01_mem0*ADD_mem[1]
	S += (t0_t0_s00*ADD[2])-1 < t0_t0_s01_mem0*ADD_mem[2]
	S += (t0_t0_s00*ADD[3])-1 < t0_t0_s01_mem0*ADD_mem[3]
	S += t0_t0_s01_mem0 <= t0_t0_s01

	t0_t0_s01_mem1 = S.Task('t0_t0_s01_mem1', length=1, delay_cost=1)
	t0_t0_s01_mem1 += MUL_mem[0]
	S += 13 < t0_t0_s01_mem1
	S += t0_t0_s01_mem1 <= t0_t0_s01

	t0_t01 = S.Task('t0_t01', length=1, delay_cost=1)
	t0_t01 += alt(ADD)

	t0_t01_mem0 = S.Task('t0_t01_mem0', length=1, delay_cost=1)
	t0_t01_mem0 += alt(MUL_mem)
	S += (t0_t0_t4*MUL[0])-1 < t0_t01_mem0*MUL_mem[0]
	S += t0_t01_mem0 <= t0_t01

	t0_t01_mem1 = S.Task('t0_t01_mem1', length=1, delay_cost=1)
	t0_t01_mem1 += alt(ADD_mem)
	S += (t0_t0_t5*ADD[0])-1 < t0_t01_mem1*ADD_mem[0]
	S += (t0_t0_t5*ADD[1])-1 < t0_t01_mem1*ADD_mem[1]
	S += (t0_t0_t5*ADD[2])-1 < t0_t01_mem1*ADD_mem[2]
	S += (t0_t0_t5*ADD[3])-1 < t0_t01_mem1*ADD_mem[3]
	S += t0_t01_mem1 <= t0_t01

	t0_t1_s01 = S.Task('t0_t1_s01', length=1, delay_cost=1)
	t0_t1_s01 += alt(ADD)

	t0_t1_s01_mem0 = S.Task('t0_t1_s01_mem0', length=1, delay_cost=1)
	t0_t1_s01_mem0 += alt(ADD_mem)
	S += (t0_t1_s00*ADD[0])-1 < t0_t1_s01_mem0*ADD_mem[0]
	S += (t0_t1_s00*ADD[1])-1 < t0_t1_s01_mem0*ADD_mem[1]
	S += (t0_t1_s00*ADD[2])-1 < t0_t1_s01_mem0*ADD_mem[2]
	S += (t0_t1_s00*ADD[3])-1 < t0_t1_s01_mem0*ADD_mem[3]
	S += t0_t1_s01_mem0 <= t0_t1_s01

	t0_t1_s01_mem1 = S.Task('t0_t1_s01_mem1', length=1, delay_cost=1)
	t0_t1_s01_mem1 += MUL_mem[0]
	S += 8 < t0_t1_s01_mem1
	S += t0_t1_s01_mem1 <= t0_t1_s01

	t0_t11 = S.Task('t0_t11', length=1, delay_cost=1)
	t0_t11 += alt(ADD)

	t0_t11_mem0 = S.Task('t0_t11_mem0', length=1, delay_cost=1)
	t0_t11_mem0 += alt(MUL_mem)
	S += (t0_t1_t4*MUL[0])-1 < t0_t11_mem0*MUL_mem[0]
	S += t0_t11_mem0 <= t0_t11

	t0_t11_mem1 = S.Task('t0_t11_mem1', length=1, delay_cost=1)
	t0_t11_mem1 += alt(ADD_mem)
	S += (t0_t1_t5*ADD[0])-1 < t0_t11_mem1*ADD_mem[0]
	S += (t0_t1_t5*ADD[1])-1 < t0_t11_mem1*ADD_mem[1]
	S += (t0_t1_t5*ADD[2])-1 < t0_t11_mem1*ADD_mem[2]
	S += (t0_t1_t5*ADD[3])-1 < t0_t11_mem1*ADD_mem[3]
	S += t0_t11_mem1 <= t0_t11

	t0_t4_t4_in = S.Task('t0_t4_t4_in', length=1, delay_cost=1)
	t0_t4_t4_in += alt(MUL_in)
	t0_t4_t4 = S.Task('t0_t4_t4', length=7, delay_cost=1)
	t0_t4_t4 += alt(MUL)
	S += t0_t4_t4>=t0_t4_t4_in

	t0_t4_t4_mem0 = S.Task('t0_t4_t4_mem0', length=1, delay_cost=1)
	t0_t4_t4_mem0 += alt(ADD_mem)
	S += (t0_t4_t2*ADD[0])-1 < t0_t4_t4_mem0*ADD_mem[0]
	S += (t0_t4_t2*ADD[1])-1 < t0_t4_t4_mem0*ADD_mem[1]
	S += (t0_t4_t2*ADD[2])-1 < t0_t4_t4_mem0*ADD_mem[2]
	S += (t0_t4_t2*ADD[3])-1 < t0_t4_t4_mem0*ADD_mem[3]
	S += t0_t4_t4_mem0 <= t0_t4_t4

	t0_t4_t4_mem1 = S.Task('t0_t4_t4_mem1', length=1, delay_cost=1)
	t0_t4_t4_mem1 += alt(ADD_mem)
	S += (t0_t4_t3*ADD[0])-1 < t0_t4_t4_mem1*ADD_mem[0]
	S += (t0_t4_t3*ADD[1])-1 < t0_t4_t4_mem1*ADD_mem[1]
	S += (t0_t4_t3*ADD[2])-1 < t0_t4_t4_mem1*ADD_mem[2]
	S += (t0_t4_t3*ADD[3])-1 < t0_t4_t4_mem1*ADD_mem[3]
	S += t0_t4_t4_mem1 <= t0_t4_t4

	t0_t4_s00 = S.Task('t0_t4_s00', length=1, delay_cost=1)
	t0_t4_s00 += alt(ADD)

	t0_t4_s00_mem0 = S.Task('t0_t4_s00_mem0', length=1, delay_cost=1)
	t0_t4_s00_mem0 += alt(MUL_mem)
	S += (t0_t4_t1*MUL[0])-1 < t0_t4_s00_mem0*MUL_mem[0]
	S += t0_t4_s00_mem0 <= t0_t4_s00

	t0_t4_t5 = S.Task('t0_t4_t5', length=1, delay_cost=1)
	t0_t4_t5 += alt(ADD)

	t0_t4_t5_mem0 = S.Task('t0_t4_t5_mem0', length=1, delay_cost=1)
	t0_t4_t5_mem0 += alt(MUL_mem)
	S += (t0_t4_t0*MUL[0])-1 < t0_t4_t5_mem0*MUL_mem[0]
	S += t0_t4_t5_mem0 <= t0_t4_t5

	t0_t4_t5_mem1 = S.Task('t0_t4_t5_mem1', length=1, delay_cost=1)
	t0_t4_t5_mem1 += alt(MUL_mem)
	S += (t0_t4_t1*MUL[0])-1 < t0_t4_t5_mem1*MUL_mem[0]
	S += t0_t4_t5_mem1 <= t0_t4_t5

	t2_t0_s01 = S.Task('t2_t0_s01', length=1, delay_cost=1)
	t2_t0_s01 += alt(ADD)

	t2_t0_s01_mem0 = S.Task('t2_t0_s01_mem0', length=1, delay_cost=1)
	t2_t0_s01_mem0 += alt(ADD_mem)
	S += (t2_t0_s00*ADD[0])-1 < t2_t0_s01_mem0*ADD_mem[0]
	S += (t2_t0_s00*ADD[1])-1 < t2_t0_s01_mem0*ADD_mem[1]
	S += (t2_t0_s00*ADD[2])-1 < t2_t0_s01_mem0*ADD_mem[2]
	S += (t2_t0_s00*ADD[3])-1 < t2_t0_s01_mem0*ADD_mem[3]
	S += t2_t0_s01_mem0 <= t2_t0_s01

	t2_t0_s01_mem1 = S.Task('t2_t0_s01_mem1', length=1, delay_cost=1)
	t2_t0_s01_mem1 += MUL_mem[0]
	S += 9 < t2_t0_s01_mem1
	S += t2_t0_s01_mem1 <= t2_t0_s01

	t2_t01 = S.Task('t2_t01', length=1, delay_cost=1)
	t2_t01 += alt(ADD)

	t2_t01_mem0 = S.Task('t2_t01_mem0', length=1, delay_cost=1)
	t2_t01_mem0 += alt(MUL_mem)
	S += (t2_t0_t4*MUL[0])-1 < t2_t01_mem0*MUL_mem[0]
	S += t2_t01_mem0 <= t2_t01

	t2_t01_mem1 = S.Task('t2_t01_mem1', length=1, delay_cost=1)
	t2_t01_mem1 += alt(ADD_mem)
	S += (t2_t0_t5*ADD[0])-1 < t2_t01_mem1*ADD_mem[0]
	S += (t2_t0_t5*ADD[1])-1 < t2_t01_mem1*ADD_mem[1]
	S += (t2_t0_t5*ADD[2])-1 < t2_t01_mem1*ADD_mem[2]
	S += (t2_t0_t5*ADD[3])-1 < t2_t01_mem1*ADD_mem[3]
	S += t2_t01_mem1 <= t2_t01

	t2_t1_s01 = S.Task('t2_t1_s01', length=1, delay_cost=1)
	t2_t1_s01 += alt(ADD)

	t2_t1_s01_mem0 = S.Task('t2_t1_s01_mem0', length=1, delay_cost=1)
	t2_t1_s01_mem0 += alt(ADD_mem)
	S += (t2_t1_s00*ADD[0])-1 < t2_t1_s01_mem0*ADD_mem[0]
	S += (t2_t1_s00*ADD[1])-1 < t2_t1_s01_mem0*ADD_mem[1]
	S += (t2_t1_s00*ADD[2])-1 < t2_t1_s01_mem0*ADD_mem[2]
	S += (t2_t1_s00*ADD[3])-1 < t2_t1_s01_mem0*ADD_mem[3]
	S += t2_t1_s01_mem0 <= t2_t1_s01

	t2_t1_s01_mem1 = S.Task('t2_t1_s01_mem1', length=1, delay_cost=1)
	t2_t1_s01_mem1 += MUL_mem[0]
	S += 7 < t2_t1_s01_mem1
	S += t2_t1_s01_mem1 <= t2_t1_s01

	t2_t11 = S.Task('t2_t11', length=1, delay_cost=1)
	t2_t11 += alt(ADD)

	t2_t11_mem0 = S.Task('t2_t11_mem0', length=1, delay_cost=1)
	t2_t11_mem0 += alt(MUL_mem)
	S += (t2_t1_t4*MUL[0])-1 < t2_t11_mem0*MUL_mem[0]
	S += t2_t11_mem0 <= t2_t11

	t2_t11_mem1 = S.Task('t2_t11_mem1', length=1, delay_cost=1)
	t2_t11_mem1 += alt(ADD_mem)
	S += (t2_t1_t5*ADD[0])-1 < t2_t11_mem1*ADD_mem[0]
	S += (t2_t1_t5*ADD[1])-1 < t2_t11_mem1*ADD_mem[1]
	S += (t2_t1_t5*ADD[2])-1 < t2_t11_mem1*ADD_mem[2]
	S += (t2_t1_t5*ADD[3])-1 < t2_t11_mem1*ADD_mem[3]
	S += t2_t11_mem1 <= t2_t11

	t2_t4_t4_in = S.Task('t2_t4_t4_in', length=1, delay_cost=1)
	t2_t4_t4_in += alt(MUL_in)
	t2_t4_t4 = S.Task('t2_t4_t4', length=7, delay_cost=1)
	t2_t4_t4 += alt(MUL)
	S += t2_t4_t4>=t2_t4_t4_in

	t2_t4_t4_mem0 = S.Task('t2_t4_t4_mem0', length=1, delay_cost=1)
	t2_t4_t4_mem0 += alt(ADD_mem)
	S += (t2_t4_t2*ADD[0])-1 < t2_t4_t4_mem0*ADD_mem[0]
	S += (t2_t4_t2*ADD[1])-1 < t2_t4_t4_mem0*ADD_mem[1]
	S += (t2_t4_t2*ADD[2])-1 < t2_t4_t4_mem0*ADD_mem[2]
	S += (t2_t4_t2*ADD[3])-1 < t2_t4_t4_mem0*ADD_mem[3]
	S += t2_t4_t4_mem0 <= t2_t4_t4

	t2_t4_t4_mem1 = S.Task('t2_t4_t4_mem1', length=1, delay_cost=1)
	t2_t4_t4_mem1 += alt(ADD_mem)
	S += (t2_t4_t3*ADD[0])-1 < t2_t4_t4_mem1*ADD_mem[0]
	S += (t2_t4_t3*ADD[1])-1 < t2_t4_t4_mem1*ADD_mem[1]
	S += (t2_t4_t3*ADD[2])-1 < t2_t4_t4_mem1*ADD_mem[2]
	S += (t2_t4_t3*ADD[3])-1 < t2_t4_t4_mem1*ADD_mem[3]
	S += t2_t4_t4_mem1 <= t2_t4_t4

	t2_t4_s00 = S.Task('t2_t4_s00', length=1, delay_cost=1)
	t2_t4_s00 += alt(ADD)

	t2_t4_s00_mem0 = S.Task('t2_t4_s00_mem0', length=1, delay_cost=1)
	t2_t4_s00_mem0 += alt(MUL_mem)
	S += (t2_t4_t1*MUL[0])-1 < t2_t4_s00_mem0*MUL_mem[0]
	S += t2_t4_s00_mem0 <= t2_t4_s00

	t2_t4_t5 = S.Task('t2_t4_t5', length=1, delay_cost=1)
	t2_t4_t5 += alt(ADD)

	t2_t4_t5_mem0 = S.Task('t2_t4_t5_mem0', length=1, delay_cost=1)
	t2_t4_t5_mem0 += alt(MUL_mem)
	S += (t2_t4_t0*MUL[0])-1 < t2_t4_t5_mem0*MUL_mem[0]
	S += t2_t4_t5_mem0 <= t2_t4_t5

	t2_t4_t5_mem1 = S.Task('t2_t4_t5_mem1', length=1, delay_cost=1)
	t2_t4_t5_mem1 += alt(MUL_mem)
	S += (t2_t4_t1*MUL[0])-1 < t2_t4_t5_mem1*MUL_mem[0]
	S += t2_t4_t5_mem1 <= t2_t4_t5

	t0_t0_s02 = S.Task('t0_t0_s02', length=1, delay_cost=1)
	t0_t0_s02 += alt(ADD)

	t0_t0_s02_mem0 = S.Task('t0_t0_s02_mem0', length=1, delay_cost=1)
	t0_t0_s02_mem0 += alt(ADD_mem)
	S += (t0_t0_s01*ADD[0])-1 < t0_t0_s02_mem0*ADD_mem[0]
	S += (t0_t0_s01*ADD[1])-1 < t0_t0_s02_mem0*ADD_mem[1]
	S += (t0_t0_s01*ADD[2])-1 < t0_t0_s02_mem0*ADD_mem[2]
	S += (t0_t0_s01*ADD[3])-1 < t0_t0_s02_mem0*ADD_mem[3]
	S += t0_t0_s02_mem0 <= t0_t0_s02

	t0_t1_s02 = S.Task('t0_t1_s02', length=1, delay_cost=1)
	t0_t1_s02 += alt(ADD)

	t0_t1_s02_mem0 = S.Task('t0_t1_s02_mem0', length=1, delay_cost=1)
	t0_t1_s02_mem0 += alt(ADD_mem)
	S += (t0_t1_s01*ADD[0])-1 < t0_t1_s02_mem0*ADD_mem[0]
	S += (t0_t1_s01*ADD[1])-1 < t0_t1_s02_mem0*ADD_mem[1]
	S += (t0_t1_s01*ADD[2])-1 < t0_t1_s02_mem0*ADD_mem[2]
	S += (t0_t1_s01*ADD[3])-1 < t0_t1_s02_mem0*ADD_mem[3]
	S += t0_t1_s02_mem0 <= t0_t1_s02

	t0_t4_s01 = S.Task('t0_t4_s01', length=1, delay_cost=1)
	t0_t4_s01 += alt(ADD)

	t0_t4_s01_mem0 = S.Task('t0_t4_s01_mem0', length=1, delay_cost=1)
	t0_t4_s01_mem0 += alt(ADD_mem)
	S += (t0_t4_s00*ADD[0])-1 < t0_t4_s01_mem0*ADD_mem[0]
	S += (t0_t4_s00*ADD[1])-1 < t0_t4_s01_mem0*ADD_mem[1]
	S += (t0_t4_s00*ADD[2])-1 < t0_t4_s01_mem0*ADD_mem[2]
	S += (t0_t4_s00*ADD[3])-1 < t0_t4_s01_mem0*ADD_mem[3]
	S += t0_t4_s01_mem0 <= t0_t4_s01

	t0_t4_s01_mem1 = S.Task('t0_t4_s01_mem1', length=1, delay_cost=1)
	t0_t4_s01_mem1 += alt(MUL_mem)
	S += (t0_t4_t1*MUL[0])-1 < t0_t4_s01_mem1*MUL_mem[0]
	S += t0_t4_s01_mem1 <= t0_t4_s01

	t0_t41 = S.Task('t0_t41', length=1, delay_cost=1)
	t0_t41 += alt(ADD)

	t0_t41_mem0 = S.Task('t0_t41_mem0', length=1, delay_cost=1)
	t0_t41_mem0 += alt(MUL_mem)
	S += (t0_t4_t4*MUL[0])-1 < t0_t41_mem0*MUL_mem[0]
	S += t0_t41_mem0 <= t0_t41

	t0_t41_mem1 = S.Task('t0_t41_mem1', length=1, delay_cost=1)
	t0_t41_mem1 += alt(ADD_mem)
	S += (t0_t4_t5*ADD[0])-1 < t0_t41_mem1*ADD_mem[0]
	S += (t0_t4_t5*ADD[1])-1 < t0_t41_mem1*ADD_mem[1]
	S += (t0_t4_t5*ADD[2])-1 < t0_t41_mem1*ADD_mem[2]
	S += (t0_t4_t5*ADD[3])-1 < t0_t41_mem1*ADD_mem[3]
	S += t0_t41_mem1 <= t0_t41

	t0_s0_y1_0 = S.Task('t0_s0_y1_0', length=1, delay_cost=1)
	t0_s0_y1_0 += alt(ADD)

	t0_s0_y1_0_mem0 = S.Task('t0_s0_y1_0_mem0', length=1, delay_cost=1)
	t0_s0_y1_0_mem0 += alt(ADD_mem)
	S += (t0_t11*ADD[0])-1 < t0_s0_y1_0_mem0*ADD_mem[0]
	S += (t0_t11*ADD[1])-1 < t0_s0_y1_0_mem0*ADD_mem[1]
	S += (t0_t11*ADD[2])-1 < t0_s0_y1_0_mem0*ADD_mem[2]
	S += (t0_t11*ADD[3])-1 < t0_s0_y1_0_mem0*ADD_mem[3]
	S += t0_s0_y1_0_mem0 <= t0_s0_y1_0

	t0_t51 = S.Task('t0_t51', length=1, delay_cost=1)
	t0_t51 += alt(ADD)

	t0_t51_mem0 = S.Task('t0_t51_mem0', length=1, delay_cost=1)
	t0_t51_mem0 += alt(ADD_mem)
	S += (t0_t01*ADD[0])-1 < t0_t51_mem0*ADD_mem[0]
	S += (t0_t01*ADD[1])-1 < t0_t51_mem0*ADD_mem[1]
	S += (t0_t01*ADD[2])-1 < t0_t51_mem0*ADD_mem[2]
	S += (t0_t01*ADD[3])-1 < t0_t51_mem0*ADD_mem[3]
	S += t0_t51_mem0 <= t0_t51

	t0_t51_mem1 = S.Task('t0_t51_mem1', length=1, delay_cost=1)
	t0_t51_mem1 += alt(ADD_mem)
	S += (t0_t11*ADD[0])-1 < t0_t51_mem1*ADD_mem[0]
	S += (t0_t11*ADD[1])-1 < t0_t51_mem1*ADD_mem[1]
	S += (t0_t11*ADD[2])-1 < t0_t51_mem1*ADD_mem[2]
	S += (t0_t11*ADD[3])-1 < t0_t51_mem1*ADD_mem[3]
	S += t0_t51_mem1 <= t0_t51

	t2_t0_s02 = S.Task('t2_t0_s02', length=1, delay_cost=1)
	t2_t0_s02 += alt(ADD)

	t2_t0_s02_mem0 = S.Task('t2_t0_s02_mem0', length=1, delay_cost=1)
	t2_t0_s02_mem0 += alt(ADD_mem)
	S += (t2_t0_s01*ADD[0])-1 < t2_t0_s02_mem0*ADD_mem[0]
	S += (t2_t0_s01*ADD[1])-1 < t2_t0_s02_mem0*ADD_mem[1]
	S += (t2_t0_s01*ADD[2])-1 < t2_t0_s02_mem0*ADD_mem[2]
	S += (t2_t0_s01*ADD[3])-1 < t2_t0_s02_mem0*ADD_mem[3]
	S += t2_t0_s02_mem0 <= t2_t0_s02

	t2_t1_s02 = S.Task('t2_t1_s02', length=1, delay_cost=1)
	t2_t1_s02 += alt(ADD)

	t2_t1_s02_mem0 = S.Task('t2_t1_s02_mem0', length=1, delay_cost=1)
	t2_t1_s02_mem0 += alt(ADD_mem)
	S += (t2_t1_s01*ADD[0])-1 < t2_t1_s02_mem0*ADD_mem[0]
	S += (t2_t1_s01*ADD[1])-1 < t2_t1_s02_mem0*ADD_mem[1]
	S += (t2_t1_s01*ADD[2])-1 < t2_t1_s02_mem0*ADD_mem[2]
	S += (t2_t1_s01*ADD[3])-1 < t2_t1_s02_mem0*ADD_mem[3]
	S += t2_t1_s02_mem0 <= t2_t1_s02

	t2_t4_s01 = S.Task('t2_t4_s01', length=1, delay_cost=1)
	t2_t4_s01 += alt(ADD)

	t2_t4_s01_mem0 = S.Task('t2_t4_s01_mem0', length=1, delay_cost=1)
	t2_t4_s01_mem0 += alt(ADD_mem)
	S += (t2_t4_s00*ADD[0])-1 < t2_t4_s01_mem0*ADD_mem[0]
	S += (t2_t4_s00*ADD[1])-1 < t2_t4_s01_mem0*ADD_mem[1]
	S += (t2_t4_s00*ADD[2])-1 < t2_t4_s01_mem0*ADD_mem[2]
	S += (t2_t4_s00*ADD[3])-1 < t2_t4_s01_mem0*ADD_mem[3]
	S += t2_t4_s01_mem0 <= t2_t4_s01

	t2_t4_s01_mem1 = S.Task('t2_t4_s01_mem1', length=1, delay_cost=1)
	t2_t4_s01_mem1 += alt(MUL_mem)
	S += (t2_t4_t1*MUL[0])-1 < t2_t4_s01_mem1*MUL_mem[0]
	S += t2_t4_s01_mem1 <= t2_t4_s01

	t2_t41 = S.Task('t2_t41', length=1, delay_cost=1)
	t2_t41 += alt(ADD)

	t2_t41_mem0 = S.Task('t2_t41_mem0', length=1, delay_cost=1)
	t2_t41_mem0 += alt(MUL_mem)
	S += (t2_t4_t4*MUL[0])-1 < t2_t41_mem0*MUL_mem[0]
	S += t2_t41_mem0 <= t2_t41

	t2_t41_mem1 = S.Task('t2_t41_mem1', length=1, delay_cost=1)
	t2_t41_mem1 += alt(ADD_mem)
	S += (t2_t4_t5*ADD[0])-1 < t2_t41_mem1*ADD_mem[0]
	S += (t2_t4_t5*ADD[1])-1 < t2_t41_mem1*ADD_mem[1]
	S += (t2_t4_t5*ADD[2])-1 < t2_t41_mem1*ADD_mem[2]
	S += (t2_t4_t5*ADD[3])-1 < t2_t41_mem1*ADD_mem[3]
	S += t2_t41_mem1 <= t2_t41

	t2_s0_y1_0 = S.Task('t2_s0_y1_0', length=1, delay_cost=1)
	t2_s0_y1_0 += alt(ADD)

	t2_s0_y1_0_mem0 = S.Task('t2_s0_y1_0_mem0', length=1, delay_cost=1)
	t2_s0_y1_0_mem0 += alt(ADD_mem)
	S += (t2_t11*ADD[0])-1 < t2_s0_y1_0_mem0*ADD_mem[0]
	S += (t2_t11*ADD[1])-1 < t2_s0_y1_0_mem0*ADD_mem[1]
	S += (t2_t11*ADD[2])-1 < t2_s0_y1_0_mem0*ADD_mem[2]
	S += (t2_t11*ADD[3])-1 < t2_s0_y1_0_mem0*ADD_mem[3]
	S += t2_s0_y1_0_mem0 <= t2_s0_y1_0

	t2_t51 = S.Task('t2_t51', length=1, delay_cost=1)
	t2_t51 += alt(ADD)

	t2_t51_mem0 = S.Task('t2_t51_mem0', length=1, delay_cost=1)
	t2_t51_mem0 += alt(ADD_mem)
	S += (t2_t01*ADD[0])-1 < t2_t51_mem0*ADD_mem[0]
	S += (t2_t01*ADD[1])-1 < t2_t51_mem0*ADD_mem[1]
	S += (t2_t01*ADD[2])-1 < t2_t51_mem0*ADD_mem[2]
	S += (t2_t01*ADD[3])-1 < t2_t51_mem0*ADD_mem[3]
	S += t2_t51_mem0 <= t2_t51

	t2_t51_mem1 = S.Task('t2_t51_mem1', length=1, delay_cost=1)
	t2_t51_mem1 += alt(ADD_mem)
	S += (t2_t11*ADD[0])-1 < t2_t51_mem1*ADD_mem[0]
	S += (t2_t11*ADD[1])-1 < t2_t51_mem1*ADD_mem[1]
	S += (t2_t11*ADD[2])-1 < t2_t51_mem1*ADD_mem[2]
	S += (t2_t11*ADD[3])-1 < t2_t51_mem1*ADD_mem[3]
	S += t2_t51_mem1 <= t2_t51

	t0_t0_s03 = S.Task('t0_t0_s03', length=1, delay_cost=1)
	t0_t0_s03 += alt(ADD)

	t0_t0_s03_mem0 = S.Task('t0_t0_s03_mem0', length=1, delay_cost=1)
	t0_t0_s03_mem0 += alt(ADD_mem)
	S += (t0_t0_s02*ADD[0])-1 < t0_t0_s03_mem0*ADD_mem[0]
	S += (t0_t0_s02*ADD[1])-1 < t0_t0_s03_mem0*ADD_mem[1]
	S += (t0_t0_s02*ADD[2])-1 < t0_t0_s03_mem0*ADD_mem[2]
	S += (t0_t0_s02*ADD[3])-1 < t0_t0_s03_mem0*ADD_mem[3]
	S += t0_t0_s03_mem0 <= t0_t0_s03

	t0_t1_s03 = S.Task('t0_t1_s03', length=1, delay_cost=1)
	t0_t1_s03 += alt(ADD)

	t0_t1_s03_mem0 = S.Task('t0_t1_s03_mem0', length=1, delay_cost=1)
	t0_t1_s03_mem0 += alt(ADD_mem)
	S += (t0_t1_s02*ADD[0])-1 < t0_t1_s03_mem0*ADD_mem[0]
	S += (t0_t1_s02*ADD[1])-1 < t0_t1_s03_mem0*ADD_mem[1]
	S += (t0_t1_s02*ADD[2])-1 < t0_t1_s03_mem0*ADD_mem[2]
	S += (t0_t1_s02*ADD[3])-1 < t0_t1_s03_mem0*ADD_mem[3]
	S += t0_t1_s03_mem0 <= t0_t1_s03

	t0_t4_s02 = S.Task('t0_t4_s02', length=1, delay_cost=1)
	t0_t4_s02 += alt(ADD)

	t0_t4_s02_mem0 = S.Task('t0_t4_s02_mem0', length=1, delay_cost=1)
	t0_t4_s02_mem0 += alt(ADD_mem)
	S += (t0_t4_s01*ADD[0])-1 < t0_t4_s02_mem0*ADD_mem[0]
	S += (t0_t4_s01*ADD[1])-1 < t0_t4_s02_mem0*ADD_mem[1]
	S += (t0_t4_s01*ADD[2])-1 < t0_t4_s02_mem0*ADD_mem[2]
	S += (t0_t4_s01*ADD[3])-1 < t0_t4_s02_mem0*ADD_mem[3]
	S += t0_t4_s02_mem0 <= t0_t4_s02

	t0_s0_y1_1 = S.Task('t0_s0_y1_1', length=1, delay_cost=1)
	t0_s0_y1_1 += alt(ADD)

	t0_s0_y1_1_mem0 = S.Task('t0_s0_y1_1_mem0', length=1, delay_cost=1)
	t0_s0_y1_1_mem0 += alt(ADD_mem)
	S += (t0_s0_y1_0*ADD[0])-1 < t0_s0_y1_1_mem0*ADD_mem[0]
	S += (t0_s0_y1_0*ADD[1])-1 < t0_s0_y1_1_mem0*ADD_mem[1]
	S += (t0_s0_y1_0*ADD[2])-1 < t0_s0_y1_1_mem0*ADD_mem[2]
	S += (t0_s0_y1_0*ADD[3])-1 < t0_s0_y1_1_mem0*ADD_mem[3]
	S += t0_s0_y1_1_mem0 <= t0_s0_y1_1

	t0_s0_y1_1_mem1 = S.Task('t0_s0_y1_1_mem1', length=1, delay_cost=1)
	t0_s0_y1_1_mem1 += alt(ADD_mem)
	S += (t0_t11*ADD[0])-1 < t0_s0_y1_1_mem1*ADD_mem[0]
	S += (t0_t11*ADD[1])-1 < t0_s0_y1_1_mem1*ADD_mem[1]
	S += (t0_t11*ADD[2])-1 < t0_s0_y1_1_mem1*ADD_mem[2]
	S += (t0_t11*ADD[3])-1 < t0_s0_y1_1_mem1*ADD_mem[3]
	S += t0_s0_y1_1_mem1 <= t0_s0_y1_1

	t011 = S.Task('t011', length=1, delay_cost=1)
	t011 += alt(ADD)

	t011_mem0 = S.Task('t011_mem0', length=1, delay_cost=1)
	t011_mem0 += alt(ADD_mem)
	S += (t0_t41*ADD[0])-1 < t011_mem0*ADD_mem[0]
	S += (t0_t41*ADD[1])-1 < t011_mem0*ADD_mem[1]
	S += (t0_t41*ADD[2])-1 < t011_mem0*ADD_mem[2]
	S += (t0_t41*ADD[3])-1 < t011_mem0*ADD_mem[3]
	S += t011_mem0 <= t011

	t011_mem1 = S.Task('t011_mem1', length=1, delay_cost=1)
	t011_mem1 += alt(ADD_mem)
	S += (t0_t51*ADD[0])-1 < t011_mem1*ADD_mem[0]
	S += (t0_t51*ADD[1])-1 < t011_mem1*ADD_mem[1]
	S += (t0_t51*ADD[2])-1 < t011_mem1*ADD_mem[2]
	S += (t0_t51*ADD[3])-1 < t011_mem1*ADD_mem[3]
	S += t011_mem1 <= t011

	t2_t0_s03 = S.Task('t2_t0_s03', length=1, delay_cost=1)
	t2_t0_s03 += alt(ADD)

	t2_t0_s03_mem0 = S.Task('t2_t0_s03_mem0', length=1, delay_cost=1)
	t2_t0_s03_mem0 += alt(ADD_mem)
	S += (t2_t0_s02*ADD[0])-1 < t2_t0_s03_mem0*ADD_mem[0]
	S += (t2_t0_s02*ADD[1])-1 < t2_t0_s03_mem0*ADD_mem[1]
	S += (t2_t0_s02*ADD[2])-1 < t2_t0_s03_mem0*ADD_mem[2]
	S += (t2_t0_s02*ADD[3])-1 < t2_t0_s03_mem0*ADD_mem[3]
	S += t2_t0_s03_mem0 <= t2_t0_s03

	t2_t1_s03 = S.Task('t2_t1_s03', length=1, delay_cost=1)
	t2_t1_s03 += alt(ADD)

	t2_t1_s03_mem0 = S.Task('t2_t1_s03_mem0', length=1, delay_cost=1)
	t2_t1_s03_mem0 += alt(ADD_mem)
	S += (t2_t1_s02*ADD[0])-1 < t2_t1_s03_mem0*ADD_mem[0]
	S += (t2_t1_s02*ADD[1])-1 < t2_t1_s03_mem0*ADD_mem[1]
	S += (t2_t1_s02*ADD[2])-1 < t2_t1_s03_mem0*ADD_mem[2]
	S += (t2_t1_s02*ADD[3])-1 < t2_t1_s03_mem0*ADD_mem[3]
	S += t2_t1_s03_mem0 <= t2_t1_s03

	t2_t4_s02 = S.Task('t2_t4_s02', length=1, delay_cost=1)
	t2_t4_s02 += alt(ADD)

	t2_t4_s02_mem0 = S.Task('t2_t4_s02_mem0', length=1, delay_cost=1)
	t2_t4_s02_mem0 += alt(ADD_mem)
	S += (t2_t4_s01*ADD[0])-1 < t2_t4_s02_mem0*ADD_mem[0]
	S += (t2_t4_s01*ADD[1])-1 < t2_t4_s02_mem0*ADD_mem[1]
	S += (t2_t4_s01*ADD[2])-1 < t2_t4_s02_mem0*ADD_mem[2]
	S += (t2_t4_s01*ADD[3])-1 < t2_t4_s02_mem0*ADD_mem[3]
	S += t2_t4_s02_mem0 <= t2_t4_s02

	t2_s0_y1_1 = S.Task('t2_s0_y1_1', length=1, delay_cost=1)
	t2_s0_y1_1 += alt(ADD)

	t2_s0_y1_1_mem0 = S.Task('t2_s0_y1_1_mem0', length=1, delay_cost=1)
	t2_s0_y1_1_mem0 += alt(ADD_mem)
	S += (t2_s0_y1_0*ADD[0])-1 < t2_s0_y1_1_mem0*ADD_mem[0]
	S += (t2_s0_y1_0*ADD[1])-1 < t2_s0_y1_1_mem0*ADD_mem[1]
	S += (t2_s0_y1_0*ADD[2])-1 < t2_s0_y1_1_mem0*ADD_mem[2]
	S += (t2_s0_y1_0*ADD[3])-1 < t2_s0_y1_1_mem0*ADD_mem[3]
	S += t2_s0_y1_1_mem0 <= t2_s0_y1_1

	t2_s0_y1_1_mem1 = S.Task('t2_s0_y1_1_mem1', length=1, delay_cost=1)
	t2_s0_y1_1_mem1 += alt(ADD_mem)
	S += (t2_t11*ADD[0])-1 < t2_s0_y1_1_mem1*ADD_mem[0]
	S += (t2_t11*ADD[1])-1 < t2_s0_y1_1_mem1*ADD_mem[1]
	S += (t2_t11*ADD[2])-1 < t2_s0_y1_1_mem1*ADD_mem[2]
	S += (t2_t11*ADD[3])-1 < t2_s0_y1_1_mem1*ADD_mem[3]
	S += t2_s0_y1_1_mem1 <= t2_s0_y1_1

	t211 = S.Task('t211', length=1, delay_cost=1)
	t211 += alt(ADD)

	t211_mem0 = S.Task('t211_mem0', length=1, delay_cost=1)
	t211_mem0 += alt(ADD_mem)
	S += (t2_t41*ADD[0])-1 < t211_mem0*ADD_mem[0]
	S += (t2_t41*ADD[1])-1 < t211_mem0*ADD_mem[1]
	S += (t2_t41*ADD[2])-1 < t211_mem0*ADD_mem[2]
	S += (t2_t41*ADD[3])-1 < t211_mem0*ADD_mem[3]
	S += t211_mem0 <= t211

	t211_mem1 = S.Task('t211_mem1', length=1, delay_cost=1)
	t211_mem1 += alt(ADD_mem)
	S += (t2_t51*ADD[0])-1 < t211_mem1*ADD_mem[0]
	S += (t2_t51*ADD[1])-1 < t211_mem1*ADD_mem[1]
	S += (t2_t51*ADD[2])-1 < t211_mem1*ADD_mem[2]
	S += (t2_t51*ADD[3])-1 < t211_mem1*ADD_mem[3]
	S += t211_mem1 <= t211

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/PADD_mul1_add4/PADD_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

