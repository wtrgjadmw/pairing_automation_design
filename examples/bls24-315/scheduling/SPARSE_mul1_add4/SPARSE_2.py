from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 172
	S = Scenario("SPARSE_2", horizon=horizon)

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

	t1_t0_t1_in = S.Task('t1_t0_t1_in', length=1, delay_cost=1)
	S += t1_t0_t1_in >= 1
	t1_t0_t1_in += MUL_in[0]

	t1_t0_t1_mem0 = S.Task('t1_t0_t1_mem0', length=1, delay_cost=1)
	S += t1_t0_t1_mem0 >= 1
	t1_t0_t1_mem0 += INPUT_mem_r

	t1_t0_t1_mem1 = S.Task('t1_t0_t1_mem1', length=1, delay_cost=1)
	S += t1_t0_t1_mem1 >= 1
	t1_t0_t1_mem1 += INPUT_mem_r

	t2_t1_t1 = S.Task('t2_t1_t1', length=7, delay_cost=1)
	S += t2_t1_t1 >= 1
	t2_t1_t1 += MUL[0]

	t1_t0_t0_in = S.Task('t1_t0_t0_in', length=1, delay_cost=1)
	S += t1_t0_t0_in >= 2
	t1_t0_t0_in += MUL_in[0]

	t1_t0_t0_mem0 = S.Task('t1_t0_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_t0_mem0 >= 2
	t1_t0_t0_mem0 += INPUT_mem_r

	t1_t0_t0_mem1 = S.Task('t1_t0_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_t0_mem1 >= 2
	t1_t0_t0_mem1 += INPUT_mem_r

	t1_t0_t1 = S.Task('t1_t0_t1', length=7, delay_cost=1)
	S += t1_t0_t1 >= 2
	t1_t0_t1 += MUL[0]

	t1_t0_t0 = S.Task('t1_t0_t0', length=7, delay_cost=1)
	S += t1_t0_t0 >= 3
	t1_t0_t0 += MUL[0]

	t2_t0_t1_in = S.Task('t2_t0_t1_in', length=1, delay_cost=1)
	S += t2_t0_t1_in >= 3
	t2_t0_t1_in += MUL_in[0]

	t2_t0_t1_mem0 = S.Task('t2_t0_t1_mem0', length=1, delay_cost=1)
	S += t2_t0_t1_mem0 >= 3
	t2_t0_t1_mem0 += INPUT_mem_r

	t2_t0_t1_mem1 = S.Task('t2_t0_t1_mem1', length=1, delay_cost=1)
	S += t2_t0_t1_mem1 >= 3
	t2_t0_t1_mem1 += INPUT_mem_r

	t1_t1_t1_in = S.Task('t1_t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_t1_in >= 4
	t1_t1_t1_in += MUL_in[0]

	t1_t1_t1_mem0 = S.Task('t1_t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_t1_mem0 >= 4
	t1_t1_t1_mem0 += INPUT_mem_r

	t1_t1_t1_mem1 = S.Task('t1_t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_t1_mem1 >= 4
	t1_t1_t1_mem1 += INPUT_mem_r

	t2_t0_t1 = S.Task('t2_t0_t1', length=7, delay_cost=1)
	S += t2_t0_t1 >= 4
	t2_t0_t1 += MUL[0]

	t1_t1_t0_in = S.Task('t1_t1_t0_in', length=1, delay_cost=1)
	S += t1_t1_t0_in >= 5
	t1_t1_t0_in += MUL_in[0]

	t1_t1_t0_mem0 = S.Task('t1_t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t1_t0_mem0 >= 5
	t1_t1_t0_mem0 += INPUT_mem_r

	t1_t1_t0_mem1 = S.Task('t1_t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t1_t0_mem1 >= 5
	t1_t1_t0_mem1 += INPUT_mem_r

	t1_t1_t1 = S.Task('t1_t1_t1', length=7, delay_cost=1)
	S += t1_t1_t1 >= 5
	t1_t1_t1 += MUL[0]

	t0_t1_t0_in = S.Task('t0_t1_t0_in', length=1, delay_cost=1)
	S += t0_t1_t0_in >= 6
	t0_t1_t0_in += MUL_in[0]

	t0_t1_t0_mem0 = S.Task('t0_t1_t0_mem0', length=1, delay_cost=1)
	S += t0_t1_t0_mem0 >= 6
	t0_t1_t0_mem0 += INPUT_mem_r

	t0_t1_t0_mem1 = S.Task('t0_t1_t0_mem1', length=1, delay_cost=1)
	S += t0_t1_t0_mem1 >= 6
	t0_t1_t0_mem1 += INPUT_mem_r

	t1_t1_t0 = S.Task('t1_t1_t0', length=7, delay_cost=1)
	S += t1_t1_t0 >= 6
	t1_t1_t0 += MUL[0]

	t0_t1_t0 = S.Task('t0_t1_t0', length=7, delay_cost=1)
	S += t0_t1_t0 >= 7
	t0_t1_t0 += MUL[0]

	t2_t0_t0_in = S.Task('t2_t0_t0_in', length=1, delay_cost=1)
	S += t2_t0_t0_in >= 7
	t2_t0_t0_in += MUL_in[0]

	t2_t0_t0_mem0 = S.Task('t2_t0_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_t0_mem0 >= 7
	t2_t0_t0_mem0 += INPUT_mem_r

	t2_t0_t0_mem1 = S.Task('t2_t0_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_t0_mem1 >= 7
	t2_t0_t0_mem1 += INPUT_mem_r

	t0_t0_t0_in = S.Task('t0_t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_t0_in >= 8
	t0_t0_t0_in += MUL_in[0]

	t0_t0_t0_mem0 = S.Task('t0_t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_t0_mem0 >= 8
	t0_t0_t0_mem0 += INPUT_mem_r

	t0_t0_t0_mem1 = S.Task('t0_t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_t0_mem1 >= 8
	t0_t0_t0_mem1 += INPUT_mem_r

	t2_t0_t0 = S.Task('t2_t0_t0', length=7, delay_cost=1)
	S += t2_t0_t0 >= 8
	t2_t0_t0 += MUL[0]

	t0_t0_t0 = S.Task('t0_t0_t0', length=7, delay_cost=1)
	S += t0_t0_t0 >= 9
	t0_t0_t0 += MUL[0]

	t2_t1_t0_in = S.Task('t2_t1_t0_in', length=1, delay_cost=1)
	S += t2_t1_t0_in >= 9
	t2_t1_t0_in += MUL_in[0]

	t2_t1_t0_mem0 = S.Task('t2_t1_t0_mem0', length=1, delay_cost=1)
	S += t2_t1_t0_mem0 >= 9
	t2_t1_t0_mem0 += INPUT_mem_r

	t2_t1_t0_mem1 = S.Task('t2_t1_t0_mem1', length=1, delay_cost=1)
	S += t2_t1_t0_mem1 >= 9
	t2_t1_t0_mem1 += INPUT_mem_r

	t0_t1_t1_in = S.Task('t0_t1_t1_in', length=1, delay_cost=1)
	S += t0_t1_t1_in >= 10
	t0_t1_t1_in += MUL_in[0]

	t0_t1_t1_mem0 = S.Task('t0_t1_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_t1_mem0 >= 10
	t0_t1_t1_mem0 += INPUT_mem_r

	t0_t1_t1_mem1 = S.Task('t0_t1_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_t1_mem1 >= 10
	t0_t1_t1_mem1 += INPUT_mem_r

	t2_t1_t0 = S.Task('t2_t1_t0', length=7, delay_cost=1)
	S += t2_t1_t0 >= 10
	t2_t1_t0 += MUL[0]

	t0_t0_t1_in = S.Task('t0_t0_t1_in', length=1, delay_cost=1)
	S += t0_t0_t1_in >= 11
	t0_t0_t1_in += MUL_in[0]

	t0_t0_t1_mem0 = S.Task('t0_t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t0_t1_mem0 >= 11
	t0_t0_t1_mem0 += INPUT_mem_r

	t0_t0_t1_mem1 = S.Task('t0_t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t0_t1_mem1 >= 11
	t0_t0_t1_mem1 += INPUT_mem_r

	t0_t1_t1 = S.Task('t0_t1_t1', length=7, delay_cost=1)
	S += t0_t1_t1 >= 11
	t0_t1_t1 += MUL[0]

	t0_t0_t1 = S.Task('t0_t0_t1', length=7, delay_cost=1)
	S += t0_t0_t1 >= 12
	t0_t0_t1 += MUL[0]

	t0_t0_t2_mem0 = S.Task('t0_t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t0_t2_mem0 >= 12
	t0_t0_t2_mem0 += INPUT_mem_r

	t0_t0_t2_mem1 = S.Task('t0_t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t0_t2_mem1 >= 12
	t0_t0_t2_mem1 += INPUT_mem_r

	t0_t0_t2 = S.Task('t0_t0_t2', length=1, delay_cost=1)
	S += t0_t0_t2 >= 13
	t0_t0_t2 += ADD[1]

	t2_t0_t2_mem0 = S.Task('t2_t0_t2_mem0', length=1, delay_cost=1)
	S += t2_t0_t2_mem0 >= 13
	t2_t0_t2_mem0 += INPUT_mem_r

	t2_t0_t2_mem1 = S.Task('t2_t0_t2_mem1', length=1, delay_cost=1)
	S += t2_t0_t2_mem1 >= 13
	t2_t0_t2_mem1 += INPUT_mem_r

	t0_t0_t3_mem0 = S.Task('t0_t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t0_t3_mem0 >= 14
	t0_t0_t3_mem0 += INPUT_mem_r

	t0_t0_t3_mem1 = S.Task('t0_t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t0_t3_mem1 >= 14
	t0_t0_t3_mem1 += INPUT_mem_r

	t2_t0_t2 = S.Task('t2_t0_t2', length=1, delay_cost=1)
	S += t2_t0_t2 >= 14
	t2_t0_t2 += ADD[3]

	t0_t0_t3 = S.Task('t0_t0_t3', length=1, delay_cost=1)
	S += t0_t0_t3 >= 15
	t0_t0_t3 += ADD[0]

	t1_t30_mem0 = S.Task('t1_t30_mem0', length=1, delay_cost=1)
	S += t1_t30_mem0 >= 15
	t1_t30_mem0 += INPUT_mem_r

	t1_t30_mem1 = S.Task('t1_t30_mem1', length=1, delay_cost=1)
	S += t1_t30_mem1 >= 15
	t1_t30_mem1 += INPUT_mem_r

	t1_t20_mem0 = S.Task('t1_t20_mem0', length=1, delay_cost=1)
	S += t1_t20_mem0 >= 16
	t1_t20_mem0 += INPUT_mem_r

	t1_t20_mem1 = S.Task('t1_t20_mem1', length=1, delay_cost=1)
	S += t1_t20_mem1 >= 16
	t1_t20_mem1 += INPUT_mem_r

	t1_t30 = S.Task('t1_t30', length=1, delay_cost=1)
	S += t1_t30 >= 16
	t1_t30 += ADD[0]

	t1_t20 = S.Task('t1_t20', length=1, delay_cost=1)
	S += t1_t20 >= 17
	t1_t20 += ADD[3]

	t1_t21_mem0 = S.Task('t1_t21_mem0', length=1, delay_cost=1)
	S += t1_t21_mem0 >= 17
	t1_t21_mem0 += INPUT_mem_r

	t1_t21_mem1 = S.Task('t1_t21_mem1', length=1, delay_cost=1)
	S += t1_t21_mem1 >= 17
	t1_t21_mem1 += INPUT_mem_r

	t1_t21 = S.Task('t1_t21', length=1, delay_cost=1)
	S += t1_t21 >= 18
	t1_t21 += ADD[0]

	t2_t0_t3_mem0 = S.Task('t2_t0_t3_mem0', length=1, delay_cost=1)
	S += t2_t0_t3_mem0 >= 18
	t2_t0_t3_mem0 += INPUT_mem_r

	t2_t0_t3_mem1 = S.Task('t2_t0_t3_mem1', length=1, delay_cost=1)
	S += t2_t0_t3_mem1 >= 18
	t2_t0_t3_mem1 += INPUT_mem_r

	t0_t21_mem0 = S.Task('t0_t21_mem0', length=1, delay_cost=1)
	S += t0_t21_mem0 >= 19
	t0_t21_mem0 += INPUT_mem_r

	t0_t21_mem1 = S.Task('t0_t21_mem1', length=1, delay_cost=1)
	S += t0_t21_mem1 >= 19
	t0_t21_mem1 += INPUT_mem_r

	t2_t0_t3 = S.Task('t2_t0_t3', length=1, delay_cost=1)
	S += t2_t0_t3 >= 19
	t2_t0_t3 += ADD[1]

	t0_t21 = S.Task('t0_t21', length=1, delay_cost=1)
	S += t0_t21 >= 20
	t0_t21 += ADD[3]

	t1_t1_t3_mem0 = S.Task('t1_t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t1_t3_mem0 >= 20
	t1_t1_t3_mem0 += INPUT_mem_r

	t1_t1_t3_mem1 = S.Task('t1_t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t1_t3_mem1 >= 20
	t1_t1_t3_mem1 += INPUT_mem_r

	t0_t1_t2_mem0 = S.Task('t0_t1_t2_mem0', length=1, delay_cost=1)
	S += t0_t1_t2_mem0 >= 21
	t0_t1_t2_mem0 += INPUT_mem_r

	t0_t1_t2_mem1 = S.Task('t0_t1_t2_mem1', length=1, delay_cost=1)
	S += t0_t1_t2_mem1 >= 21
	t0_t1_t2_mem1 += INPUT_mem_r

	t1_t1_t3 = S.Task('t1_t1_t3', length=1, delay_cost=1)
	S += t1_t1_t3 >= 21
	t1_t1_t3 += ADD[1]

	t0_t1_t2 = S.Task('t0_t1_t2', length=1, delay_cost=1)
	S += t0_t1_t2 >= 22
	t0_t1_t2 += ADD[0]

	t0_t20_mem0 = S.Task('t0_t20_mem0', length=1, delay_cost=1)
	S += t0_t20_mem0 >= 22
	t0_t20_mem0 += INPUT_mem_r

	t0_t20_mem1 = S.Task('t0_t20_mem1', length=1, delay_cost=1)
	S += t0_t20_mem1 >= 22
	t0_t20_mem1 += INPUT_mem_r

	t0_t20 = S.Task('t0_t20', length=1, delay_cost=1)
	S += t0_t20 >= 23
	t0_t20 += ADD[0]

	t1_t31_mem0 = S.Task('t1_t31_mem0', length=1, delay_cost=1)
	S += t1_t31_mem0 >= 23
	t1_t31_mem0 += INPUT_mem_r

	t1_t31_mem1 = S.Task('t1_t31_mem1', length=1, delay_cost=1)
	S += t1_t31_mem1 >= 23
	t1_t31_mem1 += INPUT_mem_r

	t0_t1_t3_mem0 = S.Task('t0_t1_t3_mem0', length=1, delay_cost=1)
	S += t0_t1_t3_mem0 >= 24
	t0_t1_t3_mem0 += INPUT_mem_r

	t0_t1_t3_mem1 = S.Task('t0_t1_t3_mem1', length=1, delay_cost=1)
	S += t0_t1_t3_mem1 >= 24
	t0_t1_t3_mem1 += INPUT_mem_r

	t1_t31 = S.Task('t1_t31', length=1, delay_cost=1)
	S += t1_t31 >= 24
	t1_t31 += ADD[0]

	t0_t1_t3 = S.Task('t0_t1_t3', length=1, delay_cost=1)
	S += t0_t1_t3 >= 25
	t0_t1_t3 += ADD[0]

	t1_t1_t2_mem0 = S.Task('t1_t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t1_t2_mem0 >= 25
	t1_t1_t2_mem0 += INPUT_mem_r

	t1_t1_t2_mem1 = S.Task('t1_t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t1_t2_mem1 >= 25
	t1_t1_t2_mem1 += INPUT_mem_r

	t1_t0_t3_mem0 = S.Task('t1_t0_t3_mem0', length=1, delay_cost=1)
	S += t1_t0_t3_mem0 >= 26
	t1_t0_t3_mem0 += INPUT_mem_r

	t1_t0_t3_mem1 = S.Task('t1_t0_t3_mem1', length=1, delay_cost=1)
	S += t1_t0_t3_mem1 >= 26
	t1_t0_t3_mem1 += INPUT_mem_r

	t1_t1_t2 = S.Task('t1_t1_t2', length=1, delay_cost=1)
	S += t1_t1_t2 >= 26
	t1_t1_t2 += ADD[1]

	t1_t0_t2_mem0 = S.Task('t1_t0_t2_mem0', length=1, delay_cost=1)
	S += t1_t0_t2_mem0 >= 27
	t1_t0_t2_mem0 += INPUT_mem_r

	t1_t0_t2_mem1 = S.Task('t1_t0_t2_mem1', length=1, delay_cost=1)
	S += t1_t0_t2_mem1 >= 27
	t1_t0_t2_mem1 += INPUT_mem_r

	t1_t0_t3 = S.Task('t1_t0_t3', length=1, delay_cost=1)
	S += t1_t0_t3 >= 27
	t1_t0_t3 += ADD[0]

	t0_t31_mem0 = S.Task('t0_t31_mem0', length=1, delay_cost=1)
	S += t0_t31_mem0 >= 28
	t0_t31_mem0 += INPUT_mem_r

	t0_t31_mem1 = S.Task('t0_t31_mem1', length=1, delay_cost=1)
	S += t0_t31_mem1 >= 28
	t0_t31_mem1 += INPUT_mem_r

	t1_t0_t2 = S.Task('t1_t0_t2', length=1, delay_cost=1)
	S += t1_t0_t2 >= 28
	t1_t0_t2 += ADD[2]

	t0_t30_mem0 = S.Task('t0_t30_mem0', length=1, delay_cost=1)
	S += t0_t30_mem0 >= 29
	t0_t30_mem0 += INPUT_mem_r

	t0_t30_mem1 = S.Task('t0_t30_mem1', length=1, delay_cost=1)
	S += t0_t30_mem1 >= 29
	t0_t30_mem1 += INPUT_mem_r

	t0_t31 = S.Task('t0_t31', length=1, delay_cost=1)
	S += t0_t31 >= 29
	t0_t31 += ADD[0]

	t0_t30 = S.Task('t0_t30', length=1, delay_cost=1)
	S += t0_t30 >= 30
	t0_t30 += ADD[1]

	t4_t1_t1_t0_in = S.Task('t4_t1_t1_t0_in', length=1, delay_cost=1)
	S += t4_t1_t1_t0_in >= 30
	t4_t1_t1_t0_in += MUL_in[0]

	t4_t1_t1_t0_mem0 = S.Task('t4_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_t0_mem0 >= 30
	t4_t1_t1_t0_mem0 += INPUT_mem_r

	t4_t1_t1_t0_mem1 = S.Task('t4_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_t0_mem1 >= 30
	t4_t1_t1_t0_mem1 += INPUT_mem_r

	t4_t1_t1_t0 = S.Task('t4_t1_t1_t0', length=7, delay_cost=1)
	S += t4_t1_t1_t0 >= 31
	t4_t1_t1_t0 += MUL[0]

	t4_t1_t1_t1_in = S.Task('t4_t1_t1_t1_in', length=1, delay_cost=1)
	S += t4_t1_t1_t1_in >= 31
	t4_t1_t1_t1_in += MUL_in[0]

	t4_t1_t1_t1_mem0 = S.Task('t4_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_t1_mem0 >= 31
	t4_t1_t1_t1_mem0 += INPUT_mem_r

	t4_t1_t1_t1_mem1 = S.Task('t4_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_t1_mem1 >= 31
	t4_t1_t1_t1_mem1 += INPUT_mem_r

	t4_t0_t1_t1_in = S.Task('t4_t0_t1_t1_in', length=1, delay_cost=1)
	S += t4_t0_t1_t1_in >= 32
	t4_t0_t1_t1_in += MUL_in[0]

	t4_t0_t1_t1_mem0 = S.Task('t4_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_t1_mem0 >= 32
	t4_t0_t1_t1_mem0 += INPUT_mem_r

	t4_t0_t1_t1_mem1 = S.Task('t4_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_t1_mem1 >= 32
	t4_t0_t1_t1_mem1 += INPUT_mem_r

	t4_t1_t1_t1 = S.Task('t4_t1_t1_t1', length=7, delay_cost=1)
	S += t4_t1_t1_t1 >= 32
	t4_t1_t1_t1 += MUL[0]

	t4_t0_t1_t0_in = S.Task('t4_t0_t1_t0_in', length=1, delay_cost=1)
	S += t4_t0_t1_t0_in >= 33
	t4_t0_t1_t0_in += MUL_in[0]

	t4_t0_t1_t0_mem0 = S.Task('t4_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_t0_mem0 >= 33
	t4_t0_t1_t0_mem0 += INPUT_mem_r

	t4_t0_t1_t0_mem1 = S.Task('t4_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_t0_mem1 >= 33
	t4_t0_t1_t0_mem1 += INPUT_mem_r

	t4_t0_t1_t1 = S.Task('t4_t0_t1_t1', length=7, delay_cost=1)
	S += t4_t0_t1_t1 >= 33
	t4_t0_t1_t1 += MUL[0]

	t4_t0_t1_t0 = S.Task('t4_t0_t1_t0', length=7, delay_cost=1)
	S += t4_t0_t1_t0 >= 34
	t4_t0_t1_t0 += MUL[0]

	t4_t1_t0_t1_in = S.Task('t4_t1_t0_t1_in', length=1, delay_cost=1)
	S += t4_t1_t0_t1_in >= 34
	t4_t1_t0_t1_in += MUL_in[0]

	t4_t1_t0_t1_mem0 = S.Task('t4_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_t1_mem0 >= 34
	t4_t1_t0_t1_mem0 += INPUT_mem_r

	t4_t1_t0_t1_mem1 = S.Task('t4_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_t1_mem1 >= 34
	t4_t1_t0_t1_mem1 += INPUT_mem_r

	t4_t1_t0_t0_in = S.Task('t4_t1_t0_t0_in', length=1, delay_cost=1)
	S += t4_t1_t0_t0_in >= 35
	t4_t1_t0_t0_in += MUL_in[0]

	t4_t1_t0_t0_mem0 = S.Task('t4_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_t0_mem0 >= 35
	t4_t1_t0_t0_mem0 += INPUT_mem_r

	t4_t1_t0_t0_mem1 = S.Task('t4_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_t0_mem1 >= 35
	t4_t1_t0_t0_mem1 += INPUT_mem_r

	t4_t1_t0_t1 = S.Task('t4_t1_t0_t1', length=7, delay_cost=1)
	S += t4_t1_t0_t1 >= 35
	t4_t1_t0_t1 += MUL[0]

	t4_t0_t0_t1_in = S.Task('t4_t0_t0_t1_in', length=1, delay_cost=1)
	S += t4_t0_t0_t1_in >= 36
	t4_t0_t0_t1_in += MUL_in[0]

	t4_t0_t0_t1_mem0 = S.Task('t4_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_t1_mem0 >= 36
	t4_t0_t0_t1_mem0 += INPUT_mem_r

	t4_t0_t0_t1_mem1 = S.Task('t4_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_t1_mem1 >= 36
	t4_t0_t0_t1_mem1 += INPUT_mem_r

	t4_t1_t0_t0 = S.Task('t4_t1_t0_t0', length=7, delay_cost=1)
	S += t4_t1_t0_t0 >= 36
	t4_t1_t0_t0 += MUL[0]

	t4_t0_t0_t0_in = S.Task('t4_t0_t0_t0_in', length=1, delay_cost=1)
	S += t4_t0_t0_t0_in >= 37
	t4_t0_t0_t0_in += MUL_in[0]

	t4_t0_t0_t0_mem0 = S.Task('t4_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_t0_mem0 >= 37
	t4_t0_t0_t0_mem0 += INPUT_mem_r

	t4_t0_t0_t0_mem1 = S.Task('t4_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_t0_mem1 >= 37
	t4_t0_t0_t0_mem1 += INPUT_mem_r

	t4_t0_t0_t1 = S.Task('t4_t0_t0_t1', length=7, delay_cost=1)
	S += t4_t0_t0_t1 >= 37
	t4_t0_t0_t1 += MUL[0]

	t4_t0_t0_t0 = S.Task('t4_t0_t0_t0', length=7, delay_cost=1)
	S += t4_t0_t0_t0 >= 38
	t4_t0_t0_t0 += MUL[0]

	t4_t0_t31_mem0 = S.Task('t4_t0_t31_mem0', length=1, delay_cost=1)
	S += t4_t0_t31_mem0 >= 38
	t4_t0_t31_mem0 += INPUT_mem_r

	t4_t0_t31_mem1 = S.Task('t4_t0_t31_mem1', length=1, delay_cost=1)
	S += t4_t0_t31_mem1 >= 38
	t4_t0_t31_mem1 += INPUT_mem_r

	t4_t0_t31 = S.Task('t4_t0_t31', length=1, delay_cost=1)
	S += t4_t0_t31 >= 39
	t4_t0_t31 += ADD[0]

	t4_t1_t0_t2_mem0 = S.Task('t4_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_t2_mem0 >= 39
	t4_t1_t0_t2_mem0 += INPUT_mem_r

	t4_t1_t0_t2_mem1 = S.Task('t4_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_t2_mem1 >= 39
	t4_t1_t0_t2_mem1 += INPUT_mem_r

	t4_t1_t0_t2 = S.Task('t4_t1_t0_t2', length=1, delay_cost=1)
	S += t4_t1_t0_t2 >= 40
	t4_t1_t0_t2 += ADD[0]

	t4_t1_t30_mem0 = S.Task('t4_t1_t30_mem0', length=1, delay_cost=1)
	S += t4_t1_t30_mem0 >= 40
	t4_t1_t30_mem0 += INPUT_mem_r

	t4_t1_t30_mem1 = S.Task('t4_t1_t30_mem1', length=1, delay_cost=1)
	S += t4_t1_t30_mem1 >= 40
	t4_t1_t30_mem1 += INPUT_mem_r

	t4_t0_t30_mem0 = S.Task('t4_t0_t30_mem0', length=1, delay_cost=1)
	S += t4_t0_t30_mem0 >= 41
	t4_t0_t30_mem0 += INPUT_mem_r

	t4_t0_t30_mem1 = S.Task('t4_t0_t30_mem1', length=1, delay_cost=1)
	S += t4_t0_t30_mem1 >= 41
	t4_t0_t30_mem1 += INPUT_mem_r

	t4_t1_t30 = S.Task('t4_t1_t30', length=1, delay_cost=1)
	S += t4_t1_t30 >= 41
	t4_t1_t30 += ADD[3]

	t4_t0_t20_mem0 = S.Task('t4_t0_t20_mem0', length=1, delay_cost=1)
	S += t4_t0_t20_mem0 >= 42
	t4_t0_t20_mem0 += INPUT_mem_r

	t4_t0_t20_mem1 = S.Task('t4_t0_t20_mem1', length=1, delay_cost=1)
	S += t4_t0_t20_mem1 >= 42
	t4_t0_t20_mem1 += INPUT_mem_r

	t4_t0_t30 = S.Task('t4_t0_t30', length=1, delay_cost=1)
	S += t4_t0_t30 >= 42
	t4_t0_t30 += ADD[3]

	t2_t21_mem0 = S.Task('t2_t21_mem0', length=1, delay_cost=1)
	S += t2_t21_mem0 >= 43
	t2_t21_mem0 += INPUT_mem_r

	t2_t21_mem1 = S.Task('t2_t21_mem1', length=1, delay_cost=1)
	S += t2_t21_mem1 >= 43
	t2_t21_mem1 += INPUT_mem_r

	t4_t0_t20 = S.Task('t4_t0_t20', length=1, delay_cost=1)
	S += t4_t0_t20 >= 43
	t4_t0_t20 += ADD[0]

	t2_t1_t3_mem0 = S.Task('t2_t1_t3_mem0', length=1, delay_cost=1)
	S += t2_t1_t3_mem0 >= 44
	t2_t1_t3_mem0 += INPUT_mem_r

	t2_t1_t3_mem1 = S.Task('t2_t1_t3_mem1', length=1, delay_cost=1)
	S += t2_t1_t3_mem1 >= 44
	t2_t1_t3_mem1 += INPUT_mem_r

	t2_t21 = S.Task('t2_t21', length=1, delay_cost=1)
	S += t2_t21 >= 44
	t2_t21 += ADD[1]

	t2_t1_t3 = S.Task('t2_t1_t3', length=1, delay_cost=1)
	S += t2_t1_t3 >= 45
	t2_t1_t3 += ADD[0]

	t4_t1_t31_mem0 = S.Task('t4_t1_t31_mem0', length=1, delay_cost=1)
	S += t4_t1_t31_mem0 >= 45
	t4_t1_t31_mem0 += INPUT_mem_r

	t4_t1_t31_mem1 = S.Task('t4_t1_t31_mem1', length=1, delay_cost=1)
	S += t4_t1_t31_mem1 >= 45
	t4_t1_t31_mem1 += INPUT_mem_r

	t2_t30_mem0 = S.Task('t2_t30_mem0', length=1, delay_cost=1)
	S += t2_t30_mem0 >= 46
	t2_t30_mem0 += INPUT_mem_r

	t2_t30_mem1 = S.Task('t2_t30_mem1', length=1, delay_cost=1)
	S += t2_t30_mem1 >= 46
	t2_t30_mem1 += INPUT_mem_r

	t4_t1_t31 = S.Task('t4_t1_t31', length=1, delay_cost=1)
	S += t4_t1_t31 >= 46
	t4_t1_t31 += ADD[0]

	t2_t30 = S.Task('t2_t30', length=1, delay_cost=1)
	S += t2_t30 >= 47
	t2_t30 += ADD[1]

	t4_t0_t1_t3_mem0 = S.Task('t4_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_t3_mem0 >= 47
	t4_t0_t1_t3_mem0 += INPUT_mem_r

	t4_t0_t1_t3_mem1 = S.Task('t4_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_t3_mem1 >= 47
	t4_t0_t1_t3_mem1 += INPUT_mem_r

	t4_t0_t1_t3 = S.Task('t4_t0_t1_t3', length=1, delay_cost=1)
	S += t4_t0_t1_t3 >= 48
	t4_t0_t1_t3 += ADD[0]

	t4_t1_t21_mem0 = S.Task('t4_t1_t21_mem0', length=1, delay_cost=1)
	S += t4_t1_t21_mem0 >= 48
	t4_t1_t21_mem0 += INPUT_mem_r

	t4_t1_t21_mem1 = S.Task('t4_t1_t21_mem1', length=1, delay_cost=1)
	S += t4_t1_t21_mem1 >= 48
	t4_t1_t21_mem1 += INPUT_mem_r

	t4_t1_t1_t2_mem0 = S.Task('t4_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_t2_mem0 >= 49
	t4_t1_t1_t2_mem0 += INPUT_mem_r

	t4_t1_t1_t2_mem1 = S.Task('t4_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_t2_mem1 >= 49
	t4_t1_t1_t2_mem1 += INPUT_mem_r

	t4_t1_t21 = S.Task('t4_t1_t21', length=1, delay_cost=1)
	S += t4_t1_t21 >= 49
	t4_t1_t21 += ADD[0]

	t4_t1_t1_t2 = S.Task('t4_t1_t1_t2', length=1, delay_cost=1)
	S += t4_t1_t1_t2 >= 50
	t4_t1_t1_t2 += ADD[1]

	t4_t1_t1_t3_mem0 = S.Task('t4_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_t3_mem0 >= 50
	t4_t1_t1_t3_mem0 += INPUT_mem_r

	t4_t1_t1_t3_mem1 = S.Task('t4_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_t3_mem1 >= 50
	t4_t1_t1_t3_mem1 += INPUT_mem_r

	t2_t1_t2_mem0 = S.Task('t2_t1_t2_mem0', length=1, delay_cost=1)
	S += t2_t1_t2_mem0 >= 51
	t2_t1_t2_mem0 += INPUT_mem_r

	t2_t1_t2_mem1 = S.Task('t2_t1_t2_mem1', length=1, delay_cost=1)
	S += t2_t1_t2_mem1 >= 51
	t2_t1_t2_mem1 += INPUT_mem_r

	t4_t1_t1_t3 = S.Task('t4_t1_t1_t3', length=1, delay_cost=1)
	S += t4_t1_t1_t3 >= 51
	t4_t1_t1_t3 += ADD[0]

	t2_t1_t2 = S.Task('t2_t1_t2', length=1, delay_cost=1)
	S += t2_t1_t2 >= 52
	t2_t1_t2 += ADD[3]

	t2_t20_mem0 = S.Task('t2_t20_mem0', length=1, delay_cost=1)
	S += t2_t20_mem0 >= 52
	t2_t20_mem0 += INPUT_mem_r

	t2_t20_mem1 = S.Task('t2_t20_mem1', length=1, delay_cost=1)
	S += t2_t20_mem1 >= 52
	t2_t20_mem1 += INPUT_mem_r

	t2_t20 = S.Task('t2_t20', length=1, delay_cost=1)
	S += t2_t20 >= 53
	t2_t20 += ADD[0]

	t4_t0_t21_mem0 = S.Task('t4_t0_t21_mem0', length=1, delay_cost=1)
	S += t4_t0_t21_mem0 >= 53
	t4_t0_t21_mem0 += INPUT_mem_r

	t4_t0_t21_mem1 = S.Task('t4_t0_t21_mem1', length=1, delay_cost=1)
	S += t4_t0_t21_mem1 >= 53
	t4_t0_t21_mem1 += INPUT_mem_r

	t4_t0_t21 = S.Task('t4_t0_t21', length=1, delay_cost=1)
	S += t4_t0_t21 >= 54
	t4_t0_t21 += ADD[0]

	t4_t1_t0_t3_mem0 = S.Task('t4_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_t3_mem0 >= 54
	t4_t1_t0_t3_mem0 += INPUT_mem_r

	t4_t1_t0_t3_mem1 = S.Task('t4_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_t3_mem1 >= 54
	t4_t1_t0_t3_mem1 += INPUT_mem_r

	t4_t1_t0_t3 = S.Task('t4_t1_t0_t3', length=1, delay_cost=1)
	S += t4_t1_t0_t3 >= 55
	t4_t1_t0_t3 += ADD[2]

	t4_t1_t20_mem0 = S.Task('t4_t1_t20_mem0', length=1, delay_cost=1)
	S += t4_t1_t20_mem0 >= 55
	t4_t1_t20_mem0 += INPUT_mem_r

	t4_t1_t20_mem1 = S.Task('t4_t1_t20_mem1', length=1, delay_cost=1)
	S += t4_t1_t20_mem1 >= 55
	t4_t1_t20_mem1 += INPUT_mem_r

	t4_t0_t1_t2_mem0 = S.Task('t4_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_t2_mem0 >= 56
	t4_t0_t1_t2_mem0 += INPUT_mem_r

	t4_t0_t1_t2_mem1 = S.Task('t4_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_t2_mem1 >= 56
	t4_t0_t1_t2_mem1 += INPUT_mem_r

	t4_t1_t20 = S.Task('t4_t1_t20', length=1, delay_cost=1)
	S += t4_t1_t20 >= 56
	t4_t1_t20 += ADD[1]

	t4_t0_t0_t3_mem0 = S.Task('t4_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_t3_mem0 >= 57
	t4_t0_t0_t3_mem0 += INPUT_mem_r

	t4_t0_t0_t3_mem1 = S.Task('t4_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_t3_mem1 >= 57
	t4_t0_t0_t3_mem1 += INPUT_mem_r

	t4_t0_t1_t2 = S.Task('t4_t0_t1_t2', length=1, delay_cost=1)
	S += t4_t0_t1_t2 >= 57
	t4_t0_t1_t2 += ADD[2]

	t4_t0_t0_t2_mem0 = S.Task('t4_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_t2_mem0 >= 58
	t4_t0_t0_t2_mem0 += INPUT_mem_r

	t4_t0_t0_t2_mem1 = S.Task('t4_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_t2_mem1 >= 58
	t4_t0_t0_t2_mem1 += INPUT_mem_r

	t4_t0_t0_t3 = S.Task('t4_t0_t0_t3', length=1, delay_cost=1)
	S += t4_t0_t0_t3 >= 58
	t4_t0_t0_t3 += ADD[3]

	t2_t31_mem0 = S.Task('t2_t31_mem0', length=1, delay_cost=1)
	S += t2_t31_mem0 >= 59
	t2_t31_mem0 += INPUT_mem_r

	t2_t31_mem1 = S.Task('t2_t31_mem1', length=1, delay_cost=1)
	S += t2_t31_mem1 >= 59
	t2_t31_mem1 += INPUT_mem_r

	t4_t0_t0_t2 = S.Task('t4_t0_t0_t2', length=1, delay_cost=1)
	S += t4_t0_t0_t2 >= 59
	t4_t0_t0_t2 += ADD[2]

	t2_t31 = S.Task('t2_t31', length=1, delay_cost=1)
	S += t2_t31 >= 60
	t2_t31 += ADD[0]


	# new tasks
	t4_t2_t0_t0_in = S.Task('t4_t2_t0_t0_in', length=1, delay_cost=1)
	t4_t2_t0_t0_in += alt(MUL_in)
	t4_t2_t0_t0 = S.Task('t4_t2_t0_t0', length=7, delay_cost=1)
	t4_t2_t0_t0 += alt(MUL)
	S += t4_t2_t0_t0>=t4_t2_t0_t0_in

	t4_t2_t0_t0_mem0 = S.Task('t4_t2_t0_t0_mem0', length=1, delay_cost=1)
	t4_t2_t0_t0_mem0 += INPUT_mem_r
	S += t4_t2_t0_t0_mem0 <= t4_t2_t0_t0

	t4_t2_t0_t0_mem1 = S.Task('t4_t2_t0_t0_mem1', length=1, delay_cost=1)
	t4_t2_t0_t0_mem1 += INPUT_mem_r
	S += t4_t2_t0_t0_mem1 <= t4_t2_t0_t0

	t4_t2_t0_t1_in = S.Task('t4_t2_t0_t1_in', length=1, delay_cost=1)
	t4_t2_t0_t1_in += alt(MUL_in)
	t4_t2_t0_t1 = S.Task('t4_t2_t0_t1', length=7, delay_cost=1)
	t4_t2_t0_t1 += alt(MUL)
	S += t4_t2_t0_t1>=t4_t2_t0_t1_in

	t4_t2_t0_t1_mem0 = S.Task('t4_t2_t0_t1_mem0', length=1, delay_cost=1)
	t4_t2_t0_t1_mem0 += INPUT_mem_r
	S += t4_t2_t0_t1_mem0 <= t4_t2_t0_t1

	t4_t2_t0_t1_mem1 = S.Task('t4_t2_t0_t1_mem1', length=1, delay_cost=1)
	t4_t2_t0_t1_mem1 += INPUT_mem_r
	S += t4_t2_t0_t1_mem1 <= t4_t2_t0_t1

	t4_t2_t0_t2 = S.Task('t4_t2_t0_t2', length=1, delay_cost=1)
	t4_t2_t0_t2 += alt(ADD)

	t4_t2_t0_t2_mem0 = S.Task('t4_t2_t0_t2_mem0', length=1, delay_cost=1)
	t4_t2_t0_t2_mem0 += INPUT_mem_r
	S += t4_t2_t0_t2_mem0 <= t4_t2_t0_t2

	t4_t2_t0_t2_mem1 = S.Task('t4_t2_t0_t2_mem1', length=1, delay_cost=1)
	t4_t2_t0_t2_mem1 += INPUT_mem_r
	S += t4_t2_t0_t2_mem1 <= t4_t2_t0_t2

	t4_t2_t0_t3 = S.Task('t4_t2_t0_t3', length=1, delay_cost=1)
	t4_t2_t0_t3 += alt(ADD)

	t4_t2_t0_t3_mem0 = S.Task('t4_t2_t0_t3_mem0', length=1, delay_cost=1)
	t4_t2_t0_t3_mem0 += INPUT_mem_r
	S += t4_t2_t0_t3_mem0 <= t4_t2_t0_t3

	t4_t2_t0_t3_mem1 = S.Task('t4_t2_t0_t3_mem1', length=1, delay_cost=1)
	t4_t2_t0_t3_mem1 += INPUT_mem_r
	S += t4_t2_t0_t3_mem1 <= t4_t2_t0_t3

	t4_t2_t1_t0_in = S.Task('t4_t2_t1_t0_in', length=1, delay_cost=1)
	t4_t2_t1_t0_in += alt(MUL_in)
	t4_t2_t1_t0 = S.Task('t4_t2_t1_t0', length=7, delay_cost=1)
	t4_t2_t1_t0 += alt(MUL)
	S += t4_t2_t1_t0>=t4_t2_t1_t0_in

	t4_t2_t1_t0_mem0 = S.Task('t4_t2_t1_t0_mem0', length=1, delay_cost=1)
	t4_t2_t1_t0_mem0 += INPUT_mem_r
	S += t4_t2_t1_t0_mem0 <= t4_t2_t1_t0

	t4_t2_t1_t0_mem1 = S.Task('t4_t2_t1_t0_mem1', length=1, delay_cost=1)
	t4_t2_t1_t0_mem1 += INPUT_mem_r
	S += t4_t2_t1_t0_mem1 <= t4_t2_t1_t0

	t4_t2_t1_t1_in = S.Task('t4_t2_t1_t1_in', length=1, delay_cost=1)
	t4_t2_t1_t1_in += alt(MUL_in)
	t4_t2_t1_t1 = S.Task('t4_t2_t1_t1', length=7, delay_cost=1)
	t4_t2_t1_t1 += alt(MUL)
	S += t4_t2_t1_t1>=t4_t2_t1_t1_in

	t4_t2_t1_t1_mem0 = S.Task('t4_t2_t1_t1_mem0', length=1, delay_cost=1)
	t4_t2_t1_t1_mem0 += INPUT_mem_r
	S += t4_t2_t1_t1_mem0 <= t4_t2_t1_t1

	t4_t2_t1_t1_mem1 = S.Task('t4_t2_t1_t1_mem1', length=1, delay_cost=1)
	t4_t2_t1_t1_mem1 += INPUT_mem_r
	S += t4_t2_t1_t1_mem1 <= t4_t2_t1_t1

	t4_t2_t1_t2 = S.Task('t4_t2_t1_t2', length=1, delay_cost=1)
	t4_t2_t1_t2 += alt(ADD)

	t4_t2_t1_t2_mem0 = S.Task('t4_t2_t1_t2_mem0', length=1, delay_cost=1)
	t4_t2_t1_t2_mem0 += INPUT_mem_r
	S += t4_t2_t1_t2_mem0 <= t4_t2_t1_t2

	t4_t2_t1_t2_mem1 = S.Task('t4_t2_t1_t2_mem1', length=1, delay_cost=1)
	t4_t2_t1_t2_mem1 += INPUT_mem_r
	S += t4_t2_t1_t2_mem1 <= t4_t2_t1_t2

	t4_t2_t1_t3 = S.Task('t4_t2_t1_t3', length=1, delay_cost=1)
	t4_t2_t1_t3 += alt(ADD)

	t4_t2_t1_t3_mem0 = S.Task('t4_t2_t1_t3_mem0', length=1, delay_cost=1)
	t4_t2_t1_t3_mem0 += INPUT_mem_r
	S += t4_t2_t1_t3_mem0 <= t4_t2_t1_t3

	t4_t2_t1_t3_mem1 = S.Task('t4_t2_t1_t3_mem1', length=1, delay_cost=1)
	t4_t2_t1_t3_mem1 += INPUT_mem_r
	S += t4_t2_t1_t3_mem1 <= t4_t2_t1_t3

	t4_t2_t20 = S.Task('t4_t2_t20', length=1, delay_cost=1)
	t4_t2_t20 += alt(ADD)

	t4_t2_t20_mem0 = S.Task('t4_t2_t20_mem0', length=1, delay_cost=1)
	t4_t2_t20_mem0 += INPUT_mem_r
	S += t4_t2_t20_mem0 <= t4_t2_t20

	t4_t2_t20_mem1 = S.Task('t4_t2_t20_mem1', length=1, delay_cost=1)
	t4_t2_t20_mem1 += INPUT_mem_r
	S += t4_t2_t20_mem1 <= t4_t2_t20

	t4_t2_t21 = S.Task('t4_t2_t21', length=1, delay_cost=1)
	t4_t2_t21 += alt(ADD)

	t4_t2_t21_mem0 = S.Task('t4_t2_t21_mem0', length=1, delay_cost=1)
	t4_t2_t21_mem0 += INPUT_mem_r
	S += t4_t2_t21_mem0 <= t4_t2_t21

	t4_t2_t21_mem1 = S.Task('t4_t2_t21_mem1', length=1, delay_cost=1)
	t4_t2_t21_mem1 += INPUT_mem_r
	S += t4_t2_t21_mem1 <= t4_t2_t21

	t4_t2_t30 = S.Task('t4_t2_t30', length=1, delay_cost=1)
	t4_t2_t30 += alt(ADD)

	t4_t2_t30_mem0 = S.Task('t4_t2_t30_mem0', length=1, delay_cost=1)
	t4_t2_t30_mem0 += INPUT_mem_r
	S += t4_t2_t30_mem0 <= t4_t2_t30

	t4_t2_t30_mem1 = S.Task('t4_t2_t30_mem1', length=1, delay_cost=1)
	t4_t2_t30_mem1 += INPUT_mem_r
	S += t4_t2_t30_mem1 <= t4_t2_t30

	t4_t2_t31 = S.Task('t4_t2_t31', length=1, delay_cost=1)
	t4_t2_t31 += alt(ADD)

	t4_t2_t31_mem0 = S.Task('t4_t2_t31_mem0', length=1, delay_cost=1)
	t4_t2_t31_mem0 += INPUT_mem_r
	S += t4_t2_t31_mem0 <= t4_t2_t31

	t4_t2_t31_mem1 = S.Task('t4_t2_t31_mem1', length=1, delay_cost=1)
	t4_t2_t31_mem1 += INPUT_mem_r
	S += t4_t2_t31_mem1 <= t4_t2_t31

	t4_t400 = S.Task('t4_t400', length=1, delay_cost=1)
	t4_t400 += alt(ADD)

	t4_t400_mem0 = S.Task('t4_t400_mem0', length=1, delay_cost=1)
	t4_t400_mem0 += INPUT_mem_r
	S += t4_t400_mem0 <= t4_t400

	t4_t400_mem1 = S.Task('t4_t400_mem1', length=1, delay_cost=1)
	t4_t400_mem1 += INPUT_mem_r
	S += t4_t400_mem1 <= t4_t400

	t4_t401 = S.Task('t4_t401', length=1, delay_cost=1)
	t4_t401 += alt(ADD)

	t4_t401_mem0 = S.Task('t4_t401_mem0', length=1, delay_cost=1)
	t4_t401_mem0 += INPUT_mem_r
	S += t4_t401_mem0 <= t4_t401

	t4_t401_mem1 = S.Task('t4_t401_mem1', length=1, delay_cost=1)
	t4_t401_mem1 += INPUT_mem_r
	S += t4_t401_mem1 <= t4_t401

	t4_t410 = S.Task('t4_t410', length=1, delay_cost=1)
	t4_t410 += alt(ADD)

	t4_t410_mem0 = S.Task('t4_t410_mem0', length=1, delay_cost=1)
	t4_t410_mem0 += INPUT_mem_r
	S += t4_t410_mem0 <= t4_t410

	t4_t410_mem1 = S.Task('t4_t410_mem1', length=1, delay_cost=1)
	t4_t410_mem1 += INPUT_mem_r
	S += t4_t410_mem1 <= t4_t410

	t4_t411 = S.Task('t4_t411', length=1, delay_cost=1)
	t4_t411 += alt(ADD)

	t4_t411_mem0 = S.Task('t4_t411_mem0', length=1, delay_cost=1)
	t4_t411_mem0 += INPUT_mem_r
	S += t4_t411_mem0 <= t4_t411

	t4_t411_mem1 = S.Task('t4_t411_mem1', length=1, delay_cost=1)
	t4_t411_mem1 += INPUT_mem_r
	S += t4_t411_mem1 <= t4_t411

	t4_t500 = S.Task('t4_t500', length=1, delay_cost=1)
	t4_t500 += alt(ADD)

	t4_t500_mem0 = S.Task('t4_t500_mem0', length=1, delay_cost=1)
	t4_t500_mem0 += INPUT_mem_r
	S += t4_t500_mem0 <= t4_t500

	t4_t500_mem1 = S.Task('t4_t500_mem1', length=1, delay_cost=1)
	t4_t500_mem1 += INPUT_mem_r
	S += t4_t500_mem1 <= t4_t500

	t4_t501 = S.Task('t4_t501', length=1, delay_cost=1)
	t4_t501 += alt(ADD)

	t4_t501_mem0 = S.Task('t4_t501_mem0', length=1, delay_cost=1)
	t4_t501_mem0 += INPUT_mem_r
	S += t4_t501_mem0 <= t4_t501

	t4_t501_mem1 = S.Task('t4_t501_mem1', length=1, delay_cost=1)
	t4_t501_mem1 += INPUT_mem_r
	S += t4_t501_mem1 <= t4_t501

	t4_t510 = S.Task('t4_t510', length=1, delay_cost=1)
	t4_t510 += alt(ADD)

	t4_t510_mem0 = S.Task('t4_t510_mem0', length=1, delay_cost=1)
	t4_t510_mem0 += INPUT_mem_r
	S += t4_t510_mem0 <= t4_t510

	t4_t510_mem1 = S.Task('t4_t510_mem1', length=1, delay_cost=1)
	t4_t510_mem1 += INPUT_mem_r
	S += t4_t510_mem1 <= t4_t510

	t4_t511 = S.Task('t4_t511', length=1, delay_cost=1)
	t4_t511 += alt(ADD)

	t4_t511_mem0 = S.Task('t4_t511_mem0', length=1, delay_cost=1)
	t4_t511_mem0 += INPUT_mem_r
	S += t4_t511_mem0 <= t4_t511

	t4_t511_mem1 = S.Task('t4_t511_mem1', length=1, delay_cost=1)
	t4_t511_mem1 += INPUT_mem_r
	S += t4_t511_mem1 <= t4_t511

	t4_t8_t0_t0_in = S.Task('t4_t8_t0_t0_in', length=1, delay_cost=1)
	t4_t8_t0_t0_in += alt(MUL_in)
	t4_t8_t0_t0 = S.Task('t4_t8_t0_t0', length=7, delay_cost=1)
	t4_t8_t0_t0 += alt(MUL)
	S += t4_t8_t0_t0>=t4_t8_t0_t0_in

	t4_t8_t0_t0_mem0 = S.Task('t4_t8_t0_t0_mem0', length=1, delay_cost=1)
	t4_t8_t0_t0_mem0 += INPUT_mem_r
	S += t4_t8_t0_t0_mem0 <= t4_t8_t0_t0

	t4_t8_t0_t0_mem1 = S.Task('t4_t8_t0_t0_mem1', length=1, delay_cost=1)
	t4_t8_t0_t0_mem1 += INPUT_mem_r
	S += t4_t8_t0_t0_mem1 <= t4_t8_t0_t0

	t4_t8_t0_t1_in = S.Task('t4_t8_t0_t1_in', length=1, delay_cost=1)
	t4_t8_t0_t1_in += alt(MUL_in)
	t4_t8_t0_t1 = S.Task('t4_t8_t0_t1', length=7, delay_cost=1)
	t4_t8_t0_t1 += alt(MUL)
	S += t4_t8_t0_t1>=t4_t8_t0_t1_in

	t4_t8_t0_t1_mem0 = S.Task('t4_t8_t0_t1_mem0', length=1, delay_cost=1)
	t4_t8_t0_t1_mem0 += INPUT_mem_r
	S += t4_t8_t0_t1_mem0 <= t4_t8_t0_t1

	t4_t8_t0_t1_mem1 = S.Task('t4_t8_t0_t1_mem1', length=1, delay_cost=1)
	t4_t8_t0_t1_mem1 += INPUT_mem_r
	S += t4_t8_t0_t1_mem1 <= t4_t8_t0_t1

	t4_t8_t0_t2 = S.Task('t4_t8_t0_t2', length=1, delay_cost=1)
	t4_t8_t0_t2 += alt(ADD)

	t4_t8_t0_t2_mem0 = S.Task('t4_t8_t0_t2_mem0', length=1, delay_cost=1)
	t4_t8_t0_t2_mem0 += INPUT_mem_r
	S += t4_t8_t0_t2_mem0 <= t4_t8_t0_t2

	t4_t8_t0_t2_mem1 = S.Task('t4_t8_t0_t2_mem1', length=1, delay_cost=1)
	t4_t8_t0_t2_mem1 += INPUT_mem_r
	S += t4_t8_t0_t2_mem1 <= t4_t8_t0_t2

	t4_t8_t0_t3 = S.Task('t4_t8_t0_t3', length=1, delay_cost=1)
	t4_t8_t0_t3 += alt(ADD)

	t4_t8_t0_t3_mem0 = S.Task('t4_t8_t0_t3_mem0', length=1, delay_cost=1)
	t4_t8_t0_t3_mem0 += INPUT_mem_r
	S += t4_t8_t0_t3_mem0 <= t4_t8_t0_t3

	t4_t8_t0_t3_mem1 = S.Task('t4_t8_t0_t3_mem1', length=1, delay_cost=1)
	t4_t8_t0_t3_mem1 += INPUT_mem_r
	S += t4_t8_t0_t3_mem1 <= t4_t8_t0_t3

	t4_t8_t1_t0_in = S.Task('t4_t8_t1_t0_in', length=1, delay_cost=1)
	t4_t8_t1_t0_in += alt(MUL_in)
	t4_t8_t1_t0 = S.Task('t4_t8_t1_t0', length=7, delay_cost=1)
	t4_t8_t1_t0 += alt(MUL)
	S += t4_t8_t1_t0>=t4_t8_t1_t0_in

	t4_t8_t1_t0_mem0 = S.Task('t4_t8_t1_t0_mem0', length=1, delay_cost=1)
	t4_t8_t1_t0_mem0 += INPUT_mem_r
	S += t4_t8_t1_t0_mem0 <= t4_t8_t1_t0

	t4_t8_t1_t0_mem1 = S.Task('t4_t8_t1_t0_mem1', length=1, delay_cost=1)
	t4_t8_t1_t0_mem1 += INPUT_mem_r
	S += t4_t8_t1_t0_mem1 <= t4_t8_t1_t0

	t4_t8_t1_t1_in = S.Task('t4_t8_t1_t1_in', length=1, delay_cost=1)
	t4_t8_t1_t1_in += alt(MUL_in)
	t4_t8_t1_t1 = S.Task('t4_t8_t1_t1', length=7, delay_cost=1)
	t4_t8_t1_t1 += alt(MUL)
	S += t4_t8_t1_t1>=t4_t8_t1_t1_in

	t4_t8_t1_t1_mem0 = S.Task('t4_t8_t1_t1_mem0', length=1, delay_cost=1)
	t4_t8_t1_t1_mem0 += INPUT_mem_r
	S += t4_t8_t1_t1_mem0 <= t4_t8_t1_t1

	t4_t8_t1_t1_mem1 = S.Task('t4_t8_t1_t1_mem1', length=1, delay_cost=1)
	t4_t8_t1_t1_mem1 += INPUT_mem_r
	S += t4_t8_t1_t1_mem1 <= t4_t8_t1_t1

	t4_t8_t1_t2 = S.Task('t4_t8_t1_t2', length=1, delay_cost=1)
	t4_t8_t1_t2 += alt(ADD)

	t4_t8_t1_t2_mem0 = S.Task('t4_t8_t1_t2_mem0', length=1, delay_cost=1)
	t4_t8_t1_t2_mem0 += INPUT_mem_r
	S += t4_t8_t1_t2_mem0 <= t4_t8_t1_t2

	t4_t8_t1_t2_mem1 = S.Task('t4_t8_t1_t2_mem1', length=1, delay_cost=1)
	t4_t8_t1_t2_mem1 += INPUT_mem_r
	S += t4_t8_t1_t2_mem1 <= t4_t8_t1_t2

	t4_t8_t1_t3 = S.Task('t4_t8_t1_t3', length=1, delay_cost=1)
	t4_t8_t1_t3 += alt(ADD)

	t4_t8_t1_t3_mem0 = S.Task('t4_t8_t1_t3_mem0', length=1, delay_cost=1)
	t4_t8_t1_t3_mem0 += INPUT_mem_r
	S += t4_t8_t1_t3_mem0 <= t4_t8_t1_t3

	t4_t8_t1_t3_mem1 = S.Task('t4_t8_t1_t3_mem1', length=1, delay_cost=1)
	t4_t8_t1_t3_mem1 += INPUT_mem_r
	S += t4_t8_t1_t3_mem1 <= t4_t8_t1_t3

	t4_t8_t20 = S.Task('t4_t8_t20', length=1, delay_cost=1)
	t4_t8_t20 += alt(ADD)

	t4_t8_t20_mem0 = S.Task('t4_t8_t20_mem0', length=1, delay_cost=1)
	t4_t8_t20_mem0 += INPUT_mem_r
	S += t4_t8_t20_mem0 <= t4_t8_t20

	t4_t8_t20_mem1 = S.Task('t4_t8_t20_mem1', length=1, delay_cost=1)
	t4_t8_t20_mem1 += INPUT_mem_r
	S += t4_t8_t20_mem1 <= t4_t8_t20

	t4_t8_t21 = S.Task('t4_t8_t21', length=1, delay_cost=1)
	t4_t8_t21 += alt(ADD)

	t4_t8_t21_mem0 = S.Task('t4_t8_t21_mem0', length=1, delay_cost=1)
	t4_t8_t21_mem0 += INPUT_mem_r
	S += t4_t8_t21_mem0 <= t4_t8_t21

	t4_t8_t21_mem1 = S.Task('t4_t8_t21_mem1', length=1, delay_cost=1)
	t4_t8_t21_mem1 += INPUT_mem_r
	S += t4_t8_t21_mem1 <= t4_t8_t21

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/SPARSE_mul1_add4/SPARSE_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

