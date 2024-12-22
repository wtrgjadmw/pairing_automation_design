from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 158
	S = Scenario("SQR012345_3", horizon=horizon)

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
	t3_t1_t1_in = S.Task('t3_t1_t1_in', length=1, delay_cost=1)
	S += t3_t1_t1_in >= 0
	t3_t1_t1_in += MUL_in[0]

	t3_t1_t1_mem0 = S.Task('t3_t1_t1_mem0', length=1, delay_cost=1)
	S += t3_t1_t1_mem0 >= 0
	t3_t1_t1_mem0 += INPUT_mem_r

	t3_t1_t1_mem1 = S.Task('t3_t1_t1_mem1', length=1, delay_cost=1)
	S += t3_t1_t1_mem1 >= 0
	t3_t1_t1_mem1 += INPUT_mem_r

	t3_t1_t0_in = S.Task('t3_t1_t0_in', length=1, delay_cost=1)
	S += t3_t1_t0_in >= 1
	t3_t1_t0_in += MUL_in[0]

	t3_t1_t0_mem0 = S.Task('t3_t1_t0_mem0', length=1, delay_cost=1)
	S += t3_t1_t0_mem0 >= 1
	t3_t1_t0_mem0 += INPUT_mem_r

	t3_t1_t0_mem1 = S.Task('t3_t1_t0_mem1', length=1, delay_cost=1)
	S += t3_t1_t0_mem1 >= 1
	t3_t1_t0_mem1 += INPUT_mem_r

	t3_t1_t1 = S.Task('t3_t1_t1', length=7, delay_cost=1)
	S += t3_t1_t1 >= 1
	t3_t1_t1 += MUL[0]

	t3_t0_t1_in = S.Task('t3_t0_t1_in', length=1, delay_cost=1)
	S += t3_t0_t1_in >= 2
	t3_t0_t1_in += MUL_in[0]

	t3_t0_t1_mem0 = S.Task('t3_t0_t1_mem0', length=1, delay_cost=1)
	S += t3_t0_t1_mem0 >= 2
	t3_t0_t1_mem0 += INPUT_mem_r

	t3_t0_t1_mem1 = S.Task('t3_t0_t1_mem1', length=1, delay_cost=1)
	S += t3_t0_t1_mem1 >= 2
	t3_t0_t1_mem1 += INPUT_mem_r

	t3_t1_t0 = S.Task('t3_t1_t0', length=7, delay_cost=1)
	S += t3_t1_t0 >= 2
	t3_t1_t0 += MUL[0]

	t3_t0_t0_in = S.Task('t3_t0_t0_in', length=1, delay_cost=1)
	S += t3_t0_t0_in >= 3
	t3_t0_t0_in += MUL_in[0]

	t3_t0_t0_mem0 = S.Task('t3_t0_t0_mem0', length=1, delay_cost=1)
	S += t3_t0_t0_mem0 >= 3
	t3_t0_t0_mem0 += INPUT_mem_r

	t3_t0_t0_mem1 = S.Task('t3_t0_t0_mem1', length=1, delay_cost=1)
	S += t3_t0_t0_mem1 >= 3
	t3_t0_t0_mem1 += INPUT_mem_r

	t3_t0_t1 = S.Task('t3_t0_t1', length=7, delay_cost=1)
	S += t3_t0_t1 >= 3
	t3_t0_t1 += MUL[0]

	t0_t3_t1_in = S.Task('t0_t3_t1_in', length=1, delay_cost=1)
	S += t0_t3_t1_in >= 4
	t0_t3_t1_in += MUL_in[0]

	t0_t3_t1_mem0 = S.Task('t0_t3_t1_mem0', length=1, delay_cost=1)
	S += t0_t3_t1_mem0 >= 4
	t0_t3_t1_mem0 += INPUT_mem_r

	t0_t3_t1_mem1 = S.Task('t0_t3_t1_mem1', length=1, delay_cost=1)
	S += t0_t3_t1_mem1 >= 4
	t0_t3_t1_mem1 += INPUT_mem_r

	t3_t0_t0 = S.Task('t3_t0_t0', length=7, delay_cost=1)
	S += t3_t0_t0 >= 4
	t3_t0_t0 += MUL[0]

	t0_t3_t0_in = S.Task('t0_t3_t0_in', length=1, delay_cost=1)
	S += t0_t3_t0_in >= 5
	t0_t3_t0_in += MUL_in[0]

	t0_t3_t0_mem0 = S.Task('t0_t3_t0_mem0', length=1, delay_cost=1)
	S += t0_t3_t0_mem0 >= 5
	t0_t3_t0_mem0 += INPUT_mem_r

	t0_t3_t0_mem1 = S.Task('t0_t3_t0_mem1', length=1, delay_cost=1)
	S += t0_t3_t0_mem1 >= 5
	t0_t3_t0_mem1 += INPUT_mem_r

	t0_t3_t1 = S.Task('t0_t3_t1', length=7, delay_cost=1)
	S += t0_t3_t1 >= 5
	t0_t3_t1 += MUL[0]

	t0_a1__y1_0_mem0 = S.Task('t0_a1__y1_0_mem0', length=1, delay_cost=1)
	S += t0_a1__y1_0_mem0 >= 6
	t0_a1__y1_0_mem0 += INPUT_mem_r

	t0_t3_t0 = S.Task('t0_t3_t0', length=7, delay_cost=1)
	S += t0_t3_t0 >= 6
	t0_t3_t0 += MUL[0]

	t4_a1__y1_0_mem0 = S.Task('t4_a1__y1_0_mem0', length=1, delay_cost=1)
	S += t4_a1__y1_0_mem0 >= 6
	t4_a1__y1_0_mem0 += INPUT_mem_r

	t0_a1__y1_0 = S.Task('t0_a1__y1_0', length=1, delay_cost=1)
	S += t0_a1__y1_0 >= 7
	t0_a1__y1_0 += ADD[1]

	t4_a1__y1_0 = S.Task('t4_a1__y1_0', length=1, delay_cost=1)
	S += t4_a1__y1_0 >= 7
	t4_a1__y1_0 += ADD[0]

	t4_t3_t1_in = S.Task('t4_t3_t1_in', length=1, delay_cost=1)
	S += t4_t3_t1_in >= 7
	t4_t3_t1_in += MUL_in[0]

	t4_t3_t1_mem0 = S.Task('t4_t3_t1_mem0', length=1, delay_cost=1)
	S += t4_t3_t1_mem0 >= 7
	t4_t3_t1_mem0 += INPUT_mem_r

	t4_t3_t1_mem1 = S.Task('t4_t3_t1_mem1', length=1, delay_cost=1)
	S += t4_t3_t1_mem1 >= 7
	t4_t3_t1_mem1 += INPUT_mem_r

	t4_t3_t0_in = S.Task('t4_t3_t0_in', length=1, delay_cost=1)
	S += t4_t3_t0_in >= 8
	t4_t3_t0_in += MUL_in[0]

	t4_t3_t0_mem0 = S.Task('t4_t3_t0_mem0', length=1, delay_cost=1)
	S += t4_t3_t0_mem0 >= 8
	t4_t3_t0_mem0 += INPUT_mem_r

	t4_t3_t0_mem1 = S.Task('t4_t3_t0_mem1', length=1, delay_cost=1)
	S += t4_t3_t0_mem1 >= 8
	t4_t3_t0_mem1 += INPUT_mem_r

	t4_t3_t1 = S.Task('t4_t3_t1', length=7, delay_cost=1)
	S += t4_t3_t1 >= 8
	t4_t3_t1 += MUL[0]

	t3_t20_mem0 = S.Task('t3_t20_mem0', length=1, delay_cost=1)
	S += t3_t20_mem0 >= 9
	t3_t20_mem0 += INPUT_mem_r

	t3_t20_mem1 = S.Task('t3_t20_mem1', length=1, delay_cost=1)
	S += t3_t20_mem1 >= 9
	t3_t20_mem1 += INPUT_mem_r

	t4_t3_t0 = S.Task('t4_t3_t0', length=7, delay_cost=1)
	S += t4_t3_t0 >= 9
	t4_t3_t0 += MUL[0]

	t0_t3_t2_mem0 = S.Task('t0_t3_t2_mem0', length=1, delay_cost=1)
	S += t0_t3_t2_mem0 >= 10
	t0_t3_t2_mem0 += INPUT_mem_r

	t0_t3_t2_mem1 = S.Task('t0_t3_t2_mem1', length=1, delay_cost=1)
	S += t0_t3_t2_mem1 >= 10
	t0_t3_t2_mem1 += INPUT_mem_r

	t3_t20 = S.Task('t3_t20', length=1, delay_cost=1)
	S += t3_t20 >= 10
	t3_t20 += ADD[0]

	t0_t11_mem0 = S.Task('t0_t11_mem0', length=1, delay_cost=1)
	S += t0_t11_mem0 >= 11
	t0_t11_mem0 += INPUT_mem_r

	t0_t11_mem1 = S.Task('t0_t11_mem1', length=1, delay_cost=1)
	S += t0_t11_mem1 >= 11
	t0_t11_mem1 += INPUT_mem_r

	t0_t3_t2 = S.Task('t0_t3_t2', length=1, delay_cost=1)
	S += t0_t3_t2 >= 11
	t0_t3_t2 += ADD[0]

	t0_t11 = S.Task('t0_t11', length=1, delay_cost=1)
	S += t0_t11 >= 12
	t0_t11 += ADD[0]

	t3_t31_mem0 = S.Task('t3_t31_mem0', length=1, delay_cost=1)
	S += t3_t31_mem0 >= 12
	t3_t31_mem0 += INPUT_mem_r

	t3_t31_mem1 = S.Task('t3_t31_mem1', length=1, delay_cost=1)
	S += t3_t31_mem1 >= 12
	t3_t31_mem1 += INPUT_mem_r

	t3_t30_mem0 = S.Task('t3_t30_mem0', length=1, delay_cost=1)
	S += t3_t30_mem0 >= 13
	t3_t30_mem0 += INPUT_mem_r

	t3_t30_mem1 = S.Task('t3_t30_mem1', length=1, delay_cost=1)
	S += t3_t30_mem1 >= 13
	t3_t30_mem1 += INPUT_mem_r

	t3_t31 = S.Task('t3_t31', length=1, delay_cost=1)
	S += t3_t31 >= 13
	t3_t31 += ADD[3]

	t0_t3_t3_mem0 = S.Task('t0_t3_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_t3_mem0 >= 14
	t0_t3_t3_mem0 += INPUT_mem_r

	t0_t3_t3_mem1 = S.Task('t0_t3_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_t3_mem1 >= 14
	t0_t3_t3_mem1 += INPUT_mem_r

	t3_t30 = S.Task('t3_t30', length=1, delay_cost=1)
	S += t3_t30 >= 14
	t3_t30 += ADD[3]

	t0_t01_mem0 = S.Task('t0_t01_mem0', length=1, delay_cost=1)
	S += t0_t01_mem0 >= 15
	t0_t01_mem0 += INPUT_mem_r

	t0_t01_mem1 = S.Task('t0_t01_mem1', length=1, delay_cost=1)
	S += t0_t01_mem1 >= 15
	t0_t01_mem1 += INPUT_mem_r

	t0_t3_t3 = S.Task('t0_t3_t3', length=1, delay_cost=1)
	S += t0_t3_t3 >= 15
	t0_t3_t3 += ADD[0]

	t0_t01 = S.Task('t0_t01', length=1, delay_cost=1)
	S += t0_t01 >= 16
	t0_t01 += ADD[1]

	t3_t0_t3_mem0 = S.Task('t3_t0_t3_mem0', length=1, delay_cost=1)
	S += t3_t0_t3_mem0 >= 16
	t3_t0_t3_mem0 += INPUT_mem_r

	t3_t0_t3_mem1 = S.Task('t3_t0_t3_mem1', length=1, delay_cost=1)
	S += t3_t0_t3_mem1 >= 16
	t3_t0_t3_mem1 += INPUT_mem_r

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 17
	t111_mem0 += INPUT_mem_r

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 17
	t111_mem1 += INPUT_mem_r

	t3_t0_t3 = S.Task('t3_t0_t3', length=1, delay_cost=1)
	S += t3_t0_t3 >= 17
	t3_t0_t3 += ADD[0]

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 18
	t111 += ADD[3]

	t3_t21_mem0 = S.Task('t3_t21_mem0', length=1, delay_cost=1)
	S += t3_t21_mem0 >= 18
	t3_t21_mem0 += INPUT_mem_r

	t3_t21_mem1 = S.Task('t3_t21_mem1', length=1, delay_cost=1)
	S += t3_t21_mem1 >= 18
	t3_t21_mem1 += INPUT_mem_r

	t3_t1_t2_mem0 = S.Task('t3_t1_t2_mem0', length=1, delay_cost=1)
	S += t3_t1_t2_mem0 >= 19
	t3_t1_t2_mem0 += INPUT_mem_r

	t3_t1_t2_mem1 = S.Task('t3_t1_t2_mem1', length=1, delay_cost=1)
	S += t3_t1_t2_mem1 >= 19
	t3_t1_t2_mem1 += INPUT_mem_r

	t3_t21 = S.Task('t3_t21', length=1, delay_cost=1)
	S += t3_t21 >= 19
	t3_t21 += ADD[3]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 20
	t101_mem0 += INPUT_mem_r

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 20
	t101_mem1 += INPUT_mem_r

	t3_t1_t2 = S.Task('t3_t1_t2', length=1, delay_cost=1)
	S += t3_t1_t2 >= 20
	t3_t1_t2 += ADD[2]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 21
	t101 += ADD[2]

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	S += t4_t10_mem0 >= 21
	t4_t10_mem0 += INPUT_mem_r

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	S += t4_t10_mem1 >= 21
	t4_t10_mem1 += INPUT_mem_r

	t3_t0_t2_mem0 = S.Task('t3_t0_t2_mem0', length=1, delay_cost=1)
	S += t3_t0_t2_mem0 >= 22
	t3_t0_t2_mem0 += INPUT_mem_r

	t3_t0_t2_mem1 = S.Task('t3_t0_t2_mem1', length=1, delay_cost=1)
	S += t3_t0_t2_mem1 >= 22
	t3_t0_t2_mem1 += INPUT_mem_r

	t4_t10 = S.Task('t4_t10', length=1, delay_cost=1)
	S += t4_t10 >= 22
	t4_t10 += ADD[0]

	t3_t0_t2 = S.Task('t3_t0_t2', length=1, delay_cost=1)
	S += t3_t0_t2 >= 23
	t3_t0_t2 += ADD[1]

	t3_t1_t3_mem0 = S.Task('t3_t1_t3_mem0', length=1, delay_cost=1)
	S += t3_t1_t3_mem0 >= 23
	t3_t1_t3_mem0 += INPUT_mem_r

	t3_t1_t3_mem1 = S.Task('t3_t1_t3_mem1', length=1, delay_cost=1)
	S += t3_t1_t3_mem1 >= 23
	t3_t1_t3_mem1 += INPUT_mem_r

	t3_t1_t3 = S.Task('t3_t1_t3', length=1, delay_cost=1)
	S += t3_t1_t3 >= 24
	t3_t1_t3 += ADD[0]

	t4_t01_mem0 = S.Task('t4_t01_mem0', length=1, delay_cost=1)
	S += t4_t01_mem0 >= 24
	t4_t01_mem0 += INPUT_mem_r

	t4_t01_mem1 = S.Task('t4_t01_mem1', length=1, delay_cost=1)
	S += t4_t01_mem1 >= 24
	t4_t01_mem1 += INPUT_mem_r

	t4_t01 = S.Task('t4_t01', length=1, delay_cost=1)
	S += t4_t01 >= 25
	t4_t01 += ADD[0]

	t4_t11_mem0 = S.Task('t4_t11_mem0', length=1, delay_cost=1)
	S += t4_t11_mem0 >= 25
	t4_t11_mem0 += INPUT_mem_r

	t4_t11_mem1 = S.Task('t4_t11_mem1', length=1, delay_cost=1)
	S += t4_t11_mem1 >= 25
	t4_t11_mem1 += INPUT_mem_r

	t0_t10_mem0 = S.Task('t0_t10_mem0', length=1, delay_cost=1)
	S += t0_t10_mem0 >= 26
	t0_t10_mem0 += INPUT_mem_r

	t0_t10_mem1 = S.Task('t0_t10_mem1', length=1, delay_cost=1)
	S += t0_t10_mem1 >= 26
	t0_t10_mem1 += INPUT_mem_r

	t4_t11 = S.Task('t4_t11', length=1, delay_cost=1)
	S += t4_t11 >= 26
	t4_t11 += ADD[1]

	t0_t10 = S.Task('t0_t10', length=1, delay_cost=1)
	S += t0_t10 >= 27
	t0_t10 += ADD[0]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 27
	t110_mem0 += INPUT_mem_r

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 27
	t110_mem1 += INPUT_mem_r

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 28
	t100_mem0 += INPUT_mem_r

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 28
	t100_mem1 += INPUT_mem_r

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 28
	t110 += ADD[2]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 29
	t100 += ADD[0]

	t6_t1_t1_in = S.Task('t6_t1_t1_in', length=1, delay_cost=1)
	S += t6_t1_t1_in >= 29
	t6_t1_t1_in += MUL_in[0]

	t6_t1_t1_mem0 = S.Task('t6_t1_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_t1_mem0 >= 29
	t6_t1_t1_mem0 += INPUT_mem_r

	t6_t1_t1_mem1 = S.Task('t6_t1_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_t1_mem1 >= 29
	t6_t1_t1_mem1 += INPUT_mem_r

	t6_t1_t1 = S.Task('t6_t1_t1', length=7, delay_cost=1)
	S += t6_t1_t1 >= 30
	t6_t1_t1 += MUL[0]

	t7_t0_t1_in = S.Task('t7_t0_t1_in', length=1, delay_cost=1)
	S += t7_t0_t1_in >= 30
	t7_t0_t1_in += MUL_in[0]

	t7_t0_t1_mem0 = S.Task('t7_t0_t1_mem0', length=1, delay_cost=1)
	S += t7_t0_t1_mem0 >= 30
	t7_t0_t1_mem0 += INPUT_mem_r

	t7_t0_t1_mem1 = S.Task('t7_t0_t1_mem1', length=1, delay_cost=1)
	S += t7_t0_t1_mem1 >= 30
	t7_t0_t1_mem1 += INPUT_mem_r

	t6_t0_t1_in = S.Task('t6_t0_t1_in', length=1, delay_cost=1)
	S += t6_t0_t1_in >= 31
	t6_t0_t1_in += MUL_in[0]

	t6_t0_t1_mem0 = S.Task('t6_t0_t1_mem0', length=1, delay_cost=1)
	S += t6_t0_t1_mem0 >= 31
	t6_t0_t1_mem0 += INPUT_mem_r

	t6_t0_t1_mem1 = S.Task('t6_t0_t1_mem1', length=1, delay_cost=1)
	S += t6_t0_t1_mem1 >= 31
	t6_t0_t1_mem1 += INPUT_mem_r

	t7_t0_t1 = S.Task('t7_t0_t1', length=7, delay_cost=1)
	S += t7_t0_t1 >= 31
	t7_t0_t1 += MUL[0]

	t6_t0_t0_in = S.Task('t6_t0_t0_in', length=1, delay_cost=1)
	S += t6_t0_t0_in >= 32
	t6_t0_t0_in += MUL_in[0]

	t6_t0_t0_mem0 = S.Task('t6_t0_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_t0_mem0 >= 32
	t6_t0_t0_mem0 += INPUT_mem_r

	t6_t0_t0_mem1 = S.Task('t6_t0_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_t0_mem1 >= 32
	t6_t0_t0_mem1 += INPUT_mem_r

	t6_t0_t1 = S.Task('t6_t0_t1', length=7, delay_cost=1)
	S += t6_t0_t1 >= 32
	t6_t0_t1 += MUL[0]

	t6_t0_t0 = S.Task('t6_t0_t0', length=7, delay_cost=1)
	S += t6_t0_t0 >= 33
	t6_t0_t0 += MUL[0]

	t7_t0_t0_in = S.Task('t7_t0_t0_in', length=1, delay_cost=1)
	S += t7_t0_t0_in >= 33
	t7_t0_t0_in += MUL_in[0]

	t7_t0_t0_mem0 = S.Task('t7_t0_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_t0_mem0 >= 33
	t7_t0_t0_mem0 += INPUT_mem_r

	t7_t0_t0_mem1 = S.Task('t7_t0_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_t0_mem1 >= 33
	t7_t0_t0_mem1 += INPUT_mem_r

	t6_t1_t0_in = S.Task('t6_t1_t0_in', length=1, delay_cost=1)
	S += t6_t1_t0_in >= 34
	t6_t1_t0_in += MUL_in[0]

	t6_t1_t0_mem0 = S.Task('t6_t1_t0_mem0', length=1, delay_cost=1)
	S += t6_t1_t0_mem0 >= 34
	t6_t1_t0_mem0 += INPUT_mem_r

	t6_t1_t0_mem1 = S.Task('t6_t1_t0_mem1', length=1, delay_cost=1)
	S += t6_t1_t0_mem1 >= 34
	t6_t1_t0_mem1 += INPUT_mem_r

	t7_t0_t0 = S.Task('t7_t0_t0', length=7, delay_cost=1)
	S += t7_t0_t0 >= 34
	t7_t0_t0 += MUL[0]

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	S += t5_t1_t1_in >= 35
	t5_t1_t1_in += MUL_in[0]

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_t1_mem0 >= 35
	t5_t1_t1_mem0 += INPUT_mem_r

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_t1_mem1 >= 35
	t5_t1_t1_mem1 += INPUT_mem_r

	t6_t1_t0 = S.Task('t6_t1_t0', length=7, delay_cost=1)
	S += t6_t1_t0 >= 35
	t6_t1_t0 += MUL[0]

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	S += t5_t1_t0_in >= 36
	t5_t1_t0_in += MUL_in[0]

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	S += t5_t1_t0_mem0 >= 36
	t5_t1_t0_mem0 += INPUT_mem_r

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	S += t5_t1_t0_mem1 >= 36
	t5_t1_t0_mem1 += INPUT_mem_r

	t5_t1_t1 = S.Task('t5_t1_t1', length=7, delay_cost=1)
	S += t5_t1_t1 >= 36
	t5_t1_t1 += MUL[0]

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	S += t5_t0_t1_in >= 37
	t5_t0_t1_in += MUL_in[0]

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	S += t5_t0_t1_mem0 >= 37
	t5_t0_t1_mem0 += INPUT_mem_r

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	S += t5_t0_t1_mem1 >= 37
	t5_t0_t1_mem1 += INPUT_mem_r

	t5_t1_t0 = S.Task('t5_t1_t0', length=7, delay_cost=1)
	S += t5_t1_t0 >= 37
	t5_t1_t0 += MUL[0]

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	S += t5_t0_t0_in >= 38
	t5_t0_t0_in += MUL_in[0]

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_t0_mem0 >= 38
	t5_t0_t0_mem0 += INPUT_mem_r

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_t0_mem1 >= 38
	t5_t0_t0_mem1 += INPUT_mem_r

	t5_t0_t1 = S.Task('t5_t0_t1', length=7, delay_cost=1)
	S += t5_t0_t1 >= 38
	t5_t0_t1 += MUL[0]

	t5_t0_t0 = S.Task('t5_t0_t0', length=7, delay_cost=1)
	S += t5_t0_t0 >= 39
	t5_t0_t0 += MUL[0]

	t6_t31_mem0 = S.Task('t6_t31_mem0', length=1, delay_cost=1)
	S += t6_t31_mem0 >= 39
	t6_t31_mem0 += INPUT_mem_r

	t6_t31_mem1 = S.Task('t6_t31_mem1', length=1, delay_cost=1)
	S += t6_t31_mem1 >= 39
	t6_t31_mem1 += INPUT_mem_r

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	S += t5_t0_t3_mem0 >= 40
	t5_t0_t3_mem0 += INPUT_mem_r

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	S += t5_t0_t3_mem1 >= 40
	t5_t0_t3_mem1 += INPUT_mem_r

	t6_t31 = S.Task('t6_t31', length=1, delay_cost=1)
	S += t6_t31 >= 40
	t6_t31 += ADD[2]

	t5_t0_t3 = S.Task('t5_t0_t3', length=1, delay_cost=1)
	S += t5_t0_t3 >= 41
	t5_t0_t3 += ADD[0]

	t7_t0_t3_mem0 = S.Task('t7_t0_t3_mem0', length=1, delay_cost=1)
	S += t7_t0_t3_mem0 >= 41
	t7_t0_t3_mem0 += INPUT_mem_r

	t7_t0_t3_mem1 = S.Task('t7_t0_t3_mem1', length=1, delay_cost=1)
	S += t7_t0_t3_mem1 >= 41
	t7_t0_t3_mem1 += INPUT_mem_r

	t6_t30_mem0 = S.Task('t6_t30_mem0', length=1, delay_cost=1)
	S += t6_t30_mem0 >= 42
	t6_t30_mem0 += INPUT_mem_r

	t6_t30_mem1 = S.Task('t6_t30_mem1', length=1, delay_cost=1)
	S += t6_t30_mem1 >= 42
	t6_t30_mem1 += INPUT_mem_r

	t7_t0_t3 = S.Task('t7_t0_t3', length=1, delay_cost=1)
	S += t7_t0_t3 >= 42
	t7_t0_t3 += ADD[0]

	t6_t30 = S.Task('t6_t30', length=1, delay_cost=1)
	S += t6_t30 >= 43
	t6_t30 += ADD[0]

	t7_t0_t2_mem0 = S.Task('t7_t0_t2_mem0', length=1, delay_cost=1)
	S += t7_t0_t2_mem0 >= 43
	t7_t0_t2_mem0 += INPUT_mem_r

	t7_t0_t2_mem1 = S.Task('t7_t0_t2_mem1', length=1, delay_cost=1)
	S += t7_t0_t2_mem1 >= 43
	t7_t0_t2_mem1 += INPUT_mem_r

	t4_t3_t3_mem0 = S.Task('t4_t3_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_t3_mem0 >= 44
	t4_t3_t3_mem0 += INPUT_mem_r

	t4_t3_t3_mem1 = S.Task('t4_t3_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_t3_mem1 >= 44
	t4_t3_t3_mem1 += INPUT_mem_r

	t7_t0_t2 = S.Task('t7_t0_t2', length=1, delay_cost=1)
	S += t7_t0_t2 >= 44
	t7_t0_t2 += ADD[1]

	t4_t3_t3 = S.Task('t4_t3_t3', length=1, delay_cost=1)
	S += t4_t3_t3 >= 45
	t4_t3_t3 += ADD[1]

	t5_t20_mem0 = S.Task('t5_t20_mem0', length=1, delay_cost=1)
	S += t5_t20_mem0 >= 45
	t5_t20_mem0 += INPUT_mem_r

	t5_t20_mem1 = S.Task('t5_t20_mem1', length=1, delay_cost=1)
	S += t5_t20_mem1 >= 45
	t5_t20_mem1 += INPUT_mem_r

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	S += t5_t1_t3_mem0 >= 46
	t5_t1_t3_mem0 += INPUT_mem_r

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	S += t5_t1_t3_mem1 >= 46
	t5_t1_t3_mem1 += INPUT_mem_r

	t5_t20 = S.Task('t5_t20', length=1, delay_cost=1)
	S += t5_t20 >= 46
	t5_t20 += ADD[1]

	t5_t1_t3 = S.Task('t5_t1_t3', length=1, delay_cost=1)
	S += t5_t1_t3 >= 47
	t5_t1_t3 += ADD[1]

	t6_t21_mem0 = S.Task('t6_t21_mem0', length=1, delay_cost=1)
	S += t6_t21_mem0 >= 47
	t6_t21_mem0 += INPUT_mem_r

	t6_t21_mem1 = S.Task('t6_t21_mem1', length=1, delay_cost=1)
	S += t6_t21_mem1 >= 47
	t6_t21_mem1 += INPUT_mem_r

	t6_t20_mem0 = S.Task('t6_t20_mem0', length=1, delay_cost=1)
	S += t6_t20_mem0 >= 48
	t6_t20_mem0 += INPUT_mem_r

	t6_t20_mem1 = S.Task('t6_t20_mem1', length=1, delay_cost=1)
	S += t6_t20_mem1 >= 48
	t6_t20_mem1 += INPUT_mem_r

	t6_t21 = S.Task('t6_t21', length=1, delay_cost=1)
	S += t6_t21 >= 48
	t6_t21 += ADD[3]

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	S += t5_t1_t2_mem0 >= 49
	t5_t1_t2_mem0 += INPUT_mem_r

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	S += t5_t1_t2_mem1 >= 49
	t5_t1_t2_mem1 += INPUT_mem_r

	t6_t20 = S.Task('t6_t20', length=1, delay_cost=1)
	S += t6_t20 >= 49
	t6_t20 += ADD[0]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 50
	t5_t0_t2_mem0 += INPUT_mem_r

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 50
	t5_t0_t2_mem1 += INPUT_mem_r

	t5_t1_t2 = S.Task('t5_t1_t2', length=1, delay_cost=1)
	S += t5_t1_t2 >= 50
	t5_t1_t2 += ADD[0]

	t5_t0_t2 = S.Task('t5_t0_t2', length=1, delay_cost=1)
	S += t5_t0_t2 >= 51
	t5_t0_t2 += ADD[0]

	t6_t1_t3_mem0 = S.Task('t6_t1_t3_mem0', length=1, delay_cost=1)
	S += t6_t1_t3_mem0 >= 51
	t6_t1_t3_mem0 += INPUT_mem_r

	t6_t1_t3_mem1 = S.Task('t6_t1_t3_mem1', length=1, delay_cost=1)
	S += t6_t1_t3_mem1 >= 51
	t6_t1_t3_mem1 += INPUT_mem_r

	t6_t1_t2_mem0 = S.Task('t6_t1_t2_mem0', length=1, delay_cost=1)
	S += t6_t1_t2_mem0 >= 52
	t6_t1_t2_mem0 += INPUT_mem_r

	t6_t1_t2_mem1 = S.Task('t6_t1_t2_mem1', length=1, delay_cost=1)
	S += t6_t1_t2_mem1 >= 52
	t6_t1_t2_mem1 += INPUT_mem_r

	t6_t1_t3 = S.Task('t6_t1_t3', length=1, delay_cost=1)
	S += t6_t1_t3 >= 52
	t6_t1_t3 += ADD[0]

	t6_t0_t3_mem0 = S.Task('t6_t0_t3_mem0', length=1, delay_cost=1)
	S += t6_t0_t3_mem0 >= 53
	t6_t0_t3_mem0 += INPUT_mem_r

	t6_t0_t3_mem1 = S.Task('t6_t0_t3_mem1', length=1, delay_cost=1)
	S += t6_t0_t3_mem1 >= 53
	t6_t0_t3_mem1 += INPUT_mem_r

	t6_t1_t2 = S.Task('t6_t1_t2', length=1, delay_cost=1)
	S += t6_t1_t2 >= 53
	t6_t1_t2 += ADD[0]

	t4_t3_t2_mem0 = S.Task('t4_t3_t2_mem0', length=1, delay_cost=1)
	S += t4_t3_t2_mem0 >= 54
	t4_t3_t2_mem0 += INPUT_mem_r

	t4_t3_t2_mem1 = S.Task('t4_t3_t2_mem1', length=1, delay_cost=1)
	S += t4_t3_t2_mem1 >= 54
	t4_t3_t2_mem1 += INPUT_mem_r

	t6_t0_t3 = S.Task('t6_t0_t3', length=1, delay_cost=1)
	S += t6_t0_t3 >= 54
	t6_t0_t3 += ADD[3]

	t4_t3_t2 = S.Task('t4_t3_t2', length=1, delay_cost=1)
	S += t4_t3_t2 >= 55
	t4_t3_t2 += ADD[0]

	t6_t0_t2_mem0 = S.Task('t6_t0_t2_mem0', length=1, delay_cost=1)
	S += t6_t0_t2_mem0 >= 55
	t6_t0_t2_mem0 += INPUT_mem_r

	t6_t0_t2_mem1 = S.Task('t6_t0_t2_mem1', length=1, delay_cost=1)
	S += t6_t0_t2_mem1 >= 55
	t6_t0_t2_mem1 += INPUT_mem_r

	t5_t31_mem0 = S.Task('t5_t31_mem0', length=1, delay_cost=1)
	S += t5_t31_mem0 >= 56
	t5_t31_mem0 += INPUT_mem_r

	t5_t31_mem1 = S.Task('t5_t31_mem1', length=1, delay_cost=1)
	S += t5_t31_mem1 >= 56
	t5_t31_mem1 += INPUT_mem_r

	t6_t0_t2 = S.Task('t6_t0_t2', length=1, delay_cost=1)
	S += t6_t0_t2 >= 56
	t6_t0_t2 += ADD[0]

	t5_t30_mem0 = S.Task('t5_t30_mem0', length=1, delay_cost=1)
	S += t5_t30_mem0 >= 57
	t5_t30_mem0 += INPUT_mem_r

	t5_t30_mem1 = S.Task('t5_t30_mem1', length=1, delay_cost=1)
	S += t5_t30_mem1 >= 57
	t5_t30_mem1 += INPUT_mem_r

	t5_t31 = S.Task('t5_t31', length=1, delay_cost=1)
	S += t5_t31 >= 57
	t5_t31 += ADD[1]

	t5_t21_mem0 = S.Task('t5_t21_mem0', length=1, delay_cost=1)
	S += t5_t21_mem0 >= 58
	t5_t21_mem0 += INPUT_mem_r

	t5_t21_mem1 = S.Task('t5_t21_mem1', length=1, delay_cost=1)
	S += t5_t21_mem1 >= 58
	t5_t21_mem1 += INPUT_mem_r

	t5_t30 = S.Task('t5_t30', length=1, delay_cost=1)
	S += t5_t30 >= 58
	t5_t30 += ADD[0]

	t5_t21 = S.Task('t5_t21', length=1, delay_cost=1)
	S += t5_t21 >= 59
	t5_t21 += ADD[0]

	t7_t1_t0_in = S.Task('t7_t1_t0_in', length=1, delay_cost=1)
	S += t7_t1_t0_in >= 59
	t7_t1_t0_in += MUL_in[0]

	t7_t1_t0_mem0 = S.Task('t7_t1_t0_mem0', length=1, delay_cost=1)
	S += t7_t1_t0_mem0 >= 59
	t7_t1_t0_mem0 += INPUT_mem_r

	t7_t1_t0_mem1 = S.Task('t7_t1_t0_mem1', length=1, delay_cost=1)
	S += t7_t1_t0_mem1 >= 59
	t7_t1_t0_mem1 += INPUT_mem_r

	t7_t1_t0 = S.Task('t7_t1_t0', length=7, delay_cost=1)
	S += t7_t1_t0 >= 60
	t7_t1_t0 += MUL[0]

	t7_t1_t1_in = S.Task('t7_t1_t1_in', length=1, delay_cost=1)
	S += t7_t1_t1_in >= 60
	t7_t1_t1_in += MUL_in[0]

	t7_t1_t1_mem0 = S.Task('t7_t1_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_t1_mem0 >= 60
	t7_t1_t1_mem0 += INPUT_mem_r

	t7_t1_t1_mem1 = S.Task('t7_t1_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_t1_mem1 >= 60
	t7_t1_t1_mem1 += INPUT_mem_r

	t7_t1_t1 = S.Task('t7_t1_t1', length=7, delay_cost=1)
	S += t7_t1_t1 >= 61
	t7_t1_t1 += MUL[0]

	t7_t1_t2_mem0 = S.Task('t7_t1_t2_mem0', length=1, delay_cost=1)
	S += t7_t1_t2_mem0 >= 61
	t7_t1_t2_mem0 += INPUT_mem_r

	t7_t1_t2_mem1 = S.Task('t7_t1_t2_mem1', length=1, delay_cost=1)
	S += t7_t1_t2_mem1 >= 61
	t7_t1_t2_mem1 += INPUT_mem_r

	t7_t1_t2 = S.Task('t7_t1_t2', length=1, delay_cost=1)
	S += t7_t1_t2 >= 62
	t7_t1_t2 += ADD[2]

	t7_t1_t3_mem0 = S.Task('t7_t1_t3_mem0', length=1, delay_cost=1)
	S += t7_t1_t3_mem0 >= 62
	t7_t1_t3_mem0 += INPUT_mem_r

	t7_t1_t3_mem1 = S.Task('t7_t1_t3_mem1', length=1, delay_cost=1)
	S += t7_t1_t3_mem1 >= 62
	t7_t1_t3_mem1 += INPUT_mem_r

	t7_t1_t3 = S.Task('t7_t1_t3', length=1, delay_cost=1)
	S += t7_t1_t3 >= 63
	t7_t1_t3 += ADD[0]

	t7_t21_mem0 = S.Task('t7_t21_mem0', length=1, delay_cost=1)
	S += t7_t21_mem0 >= 63
	t7_t21_mem0 += INPUT_mem_r

	t7_t21_mem1 = S.Task('t7_t21_mem1', length=1, delay_cost=1)
	S += t7_t21_mem1 >= 63
	t7_t21_mem1 += INPUT_mem_r

	t7_t20_mem0 = S.Task('t7_t20_mem0', length=1, delay_cost=1)
	S += t7_t20_mem0 >= 64
	t7_t20_mem0 += INPUT_mem_r

	t7_t20_mem1 = S.Task('t7_t20_mem1', length=1, delay_cost=1)
	S += t7_t20_mem1 >= 64
	t7_t20_mem1 += INPUT_mem_r

	t7_t21 = S.Task('t7_t21', length=1, delay_cost=1)
	S += t7_t21 >= 64
	t7_t21 += ADD[3]

	t7_t20 = S.Task('t7_t20', length=1, delay_cost=1)
	S += t7_t20 >= 65
	t7_t20 += ADD[1]

	t7_t30_mem0 = S.Task('t7_t30_mem0', length=1, delay_cost=1)
	S += t7_t30_mem0 >= 65
	t7_t30_mem0 += INPUT_mem_r

	t7_t30_mem1 = S.Task('t7_t30_mem1', length=1, delay_cost=1)
	S += t7_t30_mem1 >= 65
	t7_t30_mem1 += INPUT_mem_r

	t7_t30 = S.Task('t7_t30', length=1, delay_cost=1)
	S += t7_t30 >= 66
	t7_t30 += ADD[2]

	t7_t31_mem0 = S.Task('t7_t31_mem0', length=1, delay_cost=1)
	S += t7_t31_mem0 >= 66
	t7_t31_mem0 += INPUT_mem_r

	t7_t31_mem1 = S.Task('t7_t31_mem1', length=1, delay_cost=1)
	S += t7_t31_mem1 >= 66
	t7_t31_mem1 += INPUT_mem_r

	t7_t31 = S.Task('t7_t31', length=1, delay_cost=1)
	S += t7_t31 >= 67
	t7_t31 += ADD[1]


	# new tasks
	t0_a1__y1_1 = S.Task('t0_a1__y1_1', length=1, delay_cost=1)
	t0_a1__y1_1 += alt(ADD)

	t0_a1__y1_1_mem0 = S.Task('t0_a1__y1_1_mem0', length=1, delay_cost=1)
	t0_a1__y1_1_mem0 += ADD_mem[1]
	S += 7 < t0_a1__y1_1_mem0
	S += t0_a1__y1_1_mem0 <= t0_a1__y1_1

	t0_a1__y1_1_mem1 = S.Task('t0_a1__y1_1_mem1', length=1, delay_cost=1)
	t0_a1__y1_1_mem1 += INPUT_mem_r
	S += t0_a1__y1_1_mem1 <= t0_a1__y1_1

	t0_t2_t1_in = S.Task('t0_t2_t1_in', length=1, delay_cost=1)
	t0_t2_t1_in += alt(MUL_in)
	t0_t2_t1 = S.Task('t0_t2_t1', length=7, delay_cost=1)
	t0_t2_t1 += alt(MUL)
	S += t0_t2_t1>=t0_t2_t1_in

	t0_t2_t1_mem0 = S.Task('t0_t2_t1_mem0', length=1, delay_cost=1)
	t0_t2_t1_mem0 += ADD_mem[1]
	S += 16 < t0_t2_t1_mem0
	S += t0_t2_t1_mem0 <= t0_t2_t1

	t0_t2_t1_mem1 = S.Task('t0_t2_t1_mem1', length=1, delay_cost=1)
	t0_t2_t1_mem1 += ADD_mem[0]
	S += 12 < t0_t2_t1_mem1
	S += t0_t2_t1_mem1 <= t0_t2_t1

	t0_t2_t3 = S.Task('t0_t2_t3', length=1, delay_cost=1)
	t0_t2_t3 += alt(ADD)

	t0_t2_t3_mem0 = S.Task('t0_t2_t3_mem0', length=1, delay_cost=1)
	t0_t2_t3_mem0 += ADD_mem[0]
	S += 27 < t0_t2_t3_mem0
	S += t0_t2_t3_mem0 <= t0_t2_t3

	t0_t2_t3_mem1 = S.Task('t0_t2_t3_mem1', length=1, delay_cost=1)
	t0_t2_t3_mem1 += ADD_mem[0]
	S += 12 < t0_t2_t3_mem1
	S += t0_t2_t3_mem1 <= t0_t2_t3

	t0_t3_t4_in = S.Task('t0_t3_t4_in', length=1, delay_cost=1)
	t0_t3_t4_in += alt(MUL_in)
	t0_t3_t4 = S.Task('t0_t3_t4', length=7, delay_cost=1)
	t0_t3_t4 += alt(MUL)
	S += t0_t3_t4>=t0_t3_t4_in

	t0_t3_t4_mem0 = S.Task('t0_t3_t4_mem0', length=1, delay_cost=1)
	t0_t3_t4_mem0 += ADD_mem[0]
	S += 11 < t0_t3_t4_mem0
	S += t0_t3_t4_mem0 <= t0_t3_t4

	t0_t3_t4_mem1 = S.Task('t0_t3_t4_mem1', length=1, delay_cost=1)
	t0_t3_t4_mem1 += ADD_mem[0]
	S += 15 < t0_t3_t4_mem1
	S += t0_t3_t4_mem1 <= t0_t3_t4

	t0_t3_s00 = S.Task('t0_t3_s00', length=1, delay_cost=1)
	t0_t3_s00 += alt(ADD)

	t0_t3_s00_mem0 = S.Task('t0_t3_s00_mem0', length=1, delay_cost=1)
	t0_t3_s00_mem0 += MUL_mem[0]
	S += 11 < t0_t3_s00_mem0
	S += t0_t3_s00_mem0 <= t0_t3_s00

	t0_t3_t5 = S.Task('t0_t3_t5', length=1, delay_cost=1)
	t0_t3_t5 += alt(ADD)

	t0_t3_t5_mem0 = S.Task('t0_t3_t5_mem0', length=1, delay_cost=1)
	t0_t3_t5_mem0 += MUL_mem[0]
	S += 12 < t0_t3_t5_mem0
	S += t0_t3_t5_mem0 <= t0_t3_t5

	t0_t3_t5_mem1 = S.Task('t0_t3_t5_mem1', length=1, delay_cost=1)
	t0_t3_t5_mem1 += MUL_mem[0]
	S += 11 < t0_t3_t5_mem1
	S += t0_t3_t5_mem1 <= t0_t3_t5

	t200 = S.Task('t200', length=1, delay_cost=1)
	t200 += alt(ADD)

	t200_mem0 = S.Task('t200_mem0', length=1, delay_cost=1)
	t200_mem0 += ADD_mem[0]
	S += 29 < t200_mem0
	S += t200_mem0 <= t200

	t200_mem1 = S.Task('t200_mem1', length=1, delay_cost=1)
	t200_mem1 += INPUT_mem_r
	S += t200_mem1 <= t200

	t201 = S.Task('t201', length=1, delay_cost=1)
	t201 += alt(ADD)

	t201_mem0 = S.Task('t201_mem0', length=1, delay_cost=1)
	t201_mem0 += ADD_mem[2]
	S += 21 < t201_mem0
	S += t201_mem0 <= t201

	t201_mem1 = S.Task('t201_mem1', length=1, delay_cost=1)
	t201_mem1 += INPUT_mem_r
	S += t201_mem1 <= t201

	t210 = S.Task('t210', length=1, delay_cost=1)
	t210 += alt(ADD)

	t210_mem0 = S.Task('t210_mem0', length=1, delay_cost=1)
	t210_mem0 += ADD_mem[2]
	S += 28 < t210_mem0
	S += t210_mem0 <= t210

	t210_mem1 = S.Task('t210_mem1', length=1, delay_cost=1)
	t210_mem1 += INPUT_mem_r
	S += t210_mem1 <= t210

	t211 = S.Task('t211', length=1, delay_cost=1)
	t211 += alt(ADD)

	t211_mem0 = S.Task('t211_mem0', length=1, delay_cost=1)
	t211_mem0 += ADD_mem[3]
	S += 18 < t211_mem0
	S += t211_mem0 <= t211

	t211_mem1 = S.Task('t211_mem1', length=1, delay_cost=1)
	t211_mem1 += INPUT_mem_r
	S += t211_mem1 <= t211

	t800 = S.Task('t800', length=1, delay_cost=1)
	t800 += alt(ADD)

	t800_mem0 = S.Task('t800_mem0', length=1, delay_cost=1)
	t800_mem0 += ADD_mem[0]
	S += 29 < t800_mem0
	S += t800_mem0 <= t800

	t800_mem1 = S.Task('t800_mem1', length=1, delay_cost=1)
	t800_mem1 += INPUT_mem_r
	S += t800_mem1 <= t800

	t801 = S.Task('t801', length=1, delay_cost=1)
	t801 += alt(ADD)

	t801_mem0 = S.Task('t801_mem0', length=1, delay_cost=1)
	t801_mem0 += ADD_mem[2]
	S += 21 < t801_mem0
	S += t801_mem0 <= t801

	t801_mem1 = S.Task('t801_mem1', length=1, delay_cost=1)
	t801_mem1 += INPUT_mem_r
	S += t801_mem1 <= t801

	t810 = S.Task('t810', length=1, delay_cost=1)
	t810 += alt(ADD)

	t810_mem0 = S.Task('t810_mem0', length=1, delay_cost=1)
	t810_mem0 += ADD_mem[2]
	S += 28 < t810_mem0
	S += t810_mem0 <= t810

	t810_mem1 = S.Task('t810_mem1', length=1, delay_cost=1)
	t810_mem1 += INPUT_mem_r
	S += t810_mem1 <= t810

	t811 = S.Task('t811', length=1, delay_cost=1)
	t811 += alt(ADD)

	t811_mem0 = S.Task('t811_mem0', length=1, delay_cost=1)
	t811_mem0 += ADD_mem[3]
	S += 18 < t811_mem0
	S += t811_mem0 <= t811

	t811_mem1 = S.Task('t811_mem1', length=1, delay_cost=1)
	t811_mem1 += INPUT_mem_r
	S += t811_mem1 <= t811

	t3_t0_t4_in = S.Task('t3_t0_t4_in', length=1, delay_cost=1)
	t3_t0_t4_in += alt(MUL_in)
	t3_t0_t4 = S.Task('t3_t0_t4', length=7, delay_cost=1)
	t3_t0_t4 += alt(MUL)
	S += t3_t0_t4>=t3_t0_t4_in

	t3_t0_t4_mem0 = S.Task('t3_t0_t4_mem0', length=1, delay_cost=1)
	t3_t0_t4_mem0 += ADD_mem[1]
	S += 23 < t3_t0_t4_mem0
	S += t3_t0_t4_mem0 <= t3_t0_t4

	t3_t0_t4_mem1 = S.Task('t3_t0_t4_mem1', length=1, delay_cost=1)
	t3_t0_t4_mem1 += ADD_mem[0]
	S += 17 < t3_t0_t4_mem1
	S += t3_t0_t4_mem1 <= t3_t0_t4

	t3_t0_s00 = S.Task('t3_t0_s00', length=1, delay_cost=1)
	t3_t0_s00 += alt(ADD)

	t3_t0_s00_mem0 = S.Task('t3_t0_s00_mem0', length=1, delay_cost=1)
	t3_t0_s00_mem0 += MUL_mem[0]
	S += 9 < t3_t0_s00_mem0
	S += t3_t0_s00_mem0 <= t3_t0_s00

	t3_t0_t5 = S.Task('t3_t0_t5', length=1, delay_cost=1)
	t3_t0_t5 += alt(ADD)

	t3_t0_t5_mem0 = S.Task('t3_t0_t5_mem0', length=1, delay_cost=1)
	t3_t0_t5_mem0 += MUL_mem[0]
	S += 10 < t3_t0_t5_mem0
	S += t3_t0_t5_mem0 <= t3_t0_t5

	t3_t0_t5_mem1 = S.Task('t3_t0_t5_mem1', length=1, delay_cost=1)
	t3_t0_t5_mem1 += MUL_mem[0]
	S += 9 < t3_t0_t5_mem1
	S += t3_t0_t5_mem1 <= t3_t0_t5

	t3_t1_t4_in = S.Task('t3_t1_t4_in', length=1, delay_cost=1)
	t3_t1_t4_in += alt(MUL_in)
	t3_t1_t4 = S.Task('t3_t1_t4', length=7, delay_cost=1)
	t3_t1_t4 += alt(MUL)
	S += t3_t1_t4>=t3_t1_t4_in

	t3_t1_t4_mem0 = S.Task('t3_t1_t4_mem0', length=1, delay_cost=1)
	t3_t1_t4_mem0 += ADD_mem[2]
	S += 20 < t3_t1_t4_mem0
	S += t3_t1_t4_mem0 <= t3_t1_t4

	t3_t1_t4_mem1 = S.Task('t3_t1_t4_mem1', length=1, delay_cost=1)
	t3_t1_t4_mem1 += ADD_mem[0]
	S += 24 < t3_t1_t4_mem1
	S += t3_t1_t4_mem1 <= t3_t1_t4

	t3_t1_s00 = S.Task('t3_t1_s00', length=1, delay_cost=1)
	t3_t1_s00 += alt(ADD)

	t3_t1_s00_mem0 = S.Task('t3_t1_s00_mem0', length=1, delay_cost=1)
	t3_t1_s00_mem0 += MUL_mem[0]
	S += 7 < t3_t1_s00_mem0
	S += t3_t1_s00_mem0 <= t3_t1_s00

	t3_t1_t5 = S.Task('t3_t1_t5', length=1, delay_cost=1)
	t3_t1_t5 += alt(ADD)

	t3_t1_t5_mem0 = S.Task('t3_t1_t5_mem0', length=1, delay_cost=1)
	t3_t1_t5_mem0 += MUL_mem[0]
	S += 8 < t3_t1_t5_mem0
	S += t3_t1_t5_mem0 <= t3_t1_t5

	t3_t1_t5_mem1 = S.Task('t3_t1_t5_mem1', length=1, delay_cost=1)
	t3_t1_t5_mem1 += MUL_mem[0]
	S += 7 < t3_t1_t5_mem1
	S += t3_t1_t5_mem1 <= t3_t1_t5

	t3_t4_t0_in = S.Task('t3_t4_t0_in', length=1, delay_cost=1)
	t3_t4_t0_in += alt(MUL_in)
	t3_t4_t0 = S.Task('t3_t4_t0', length=7, delay_cost=1)
	t3_t4_t0 += alt(MUL)
	S += t3_t4_t0>=t3_t4_t0_in

	t3_t4_t0_mem0 = S.Task('t3_t4_t0_mem0', length=1, delay_cost=1)
	t3_t4_t0_mem0 += ADD_mem[0]
	S += 10 < t3_t4_t0_mem0
	S += t3_t4_t0_mem0 <= t3_t4_t0

	t3_t4_t0_mem1 = S.Task('t3_t4_t0_mem1', length=1, delay_cost=1)
	t3_t4_t0_mem1 += ADD_mem[3]
	S += 14 < t3_t4_t0_mem1
	S += t3_t4_t0_mem1 <= t3_t4_t0

	t3_t4_t1_in = S.Task('t3_t4_t1_in', length=1, delay_cost=1)
	t3_t4_t1_in += alt(MUL_in)
	t3_t4_t1 = S.Task('t3_t4_t1', length=7, delay_cost=1)
	t3_t4_t1 += alt(MUL)
	S += t3_t4_t1>=t3_t4_t1_in

	t3_t4_t1_mem0 = S.Task('t3_t4_t1_mem0', length=1, delay_cost=1)
	t3_t4_t1_mem0 += ADD_mem[3]
	S += 19 < t3_t4_t1_mem0
	S += t3_t4_t1_mem0 <= t3_t4_t1

	t3_t4_t1_mem1 = S.Task('t3_t4_t1_mem1', length=1, delay_cost=1)
	t3_t4_t1_mem1 += ADD_mem[3]
	S += 13 < t3_t4_t1_mem1
	S += t3_t4_t1_mem1 <= t3_t4_t1

	t3_t4_t2 = S.Task('t3_t4_t2', length=1, delay_cost=1)
	t3_t4_t2 += alt(ADD)

	t3_t4_t2_mem0 = S.Task('t3_t4_t2_mem0', length=1, delay_cost=1)
	t3_t4_t2_mem0 += ADD_mem[0]
	S += 10 < t3_t4_t2_mem0
	S += t3_t4_t2_mem0 <= t3_t4_t2

	t3_t4_t2_mem1 = S.Task('t3_t4_t2_mem1', length=1, delay_cost=1)
	t3_t4_t2_mem1 += ADD_mem[3]
	S += 19 < t3_t4_t2_mem1
	S += t3_t4_t2_mem1 <= t3_t4_t2

	t3_t4_t3 = S.Task('t3_t4_t3', length=1, delay_cost=1)
	t3_t4_t3 += alt(ADD)

	t3_t4_t3_mem0 = S.Task('t3_t4_t3_mem0', length=1, delay_cost=1)
	t3_t4_t3_mem0 += ADD_mem[3]
	S += 14 < t3_t4_t3_mem0
	S += t3_t4_t3_mem0 <= t3_t4_t3

	t3_t4_t3_mem1 = S.Task('t3_t4_t3_mem1', length=1, delay_cost=1)
	t3_t4_t3_mem1 += ADD_mem[3]
	S += 13 < t3_t4_t3_mem1
	S += t3_t4_t3_mem1 <= t3_t4_t3

	t4_a1__y1_1 = S.Task('t4_a1__y1_1', length=1, delay_cost=1)
	t4_a1__y1_1 += alt(ADD)

	t4_a1__y1_1_mem0 = S.Task('t4_a1__y1_1_mem0', length=1, delay_cost=1)
	t4_a1__y1_1_mem0 += ADD_mem[0]
	S += 7 < t4_a1__y1_1_mem0
	S += t4_a1__y1_1_mem0 <= t4_a1__y1_1

	t4_a1__y1_1_mem1 = S.Task('t4_a1__y1_1_mem1', length=1, delay_cost=1)
	t4_a1__y1_1_mem1 += INPUT_mem_r
	S += t4_a1__y1_1_mem1 <= t4_a1__y1_1

	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	t4_t2_t1_in += alt(MUL_in)
	t4_t2_t1 = S.Task('t4_t2_t1', length=7, delay_cost=1)
	t4_t2_t1 += alt(MUL)
	S += t4_t2_t1>=t4_t2_t1_in

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	t4_t2_t1_mem0 += ADD_mem[0]
	S += 25 < t4_t2_t1_mem0
	S += t4_t2_t1_mem0 <= t4_t2_t1

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	t4_t2_t1_mem1 += ADD_mem[1]
	S += 26 < t4_t2_t1_mem1
	S += t4_t2_t1_mem1 <= t4_t2_t1

	t4_t2_t3 = S.Task('t4_t2_t3', length=1, delay_cost=1)
	t4_t2_t3 += alt(ADD)

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	t4_t2_t3_mem0 += ADD_mem[0]
	S += 22 < t4_t2_t3_mem0
	S += t4_t2_t3_mem0 <= t4_t2_t3

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	t4_t2_t3_mem1 += ADD_mem[1]
	S += 26 < t4_t2_t3_mem1
	S += t4_t2_t3_mem1 <= t4_t2_t3

	t4_t3_t4_in = S.Task('t4_t3_t4_in', length=1, delay_cost=1)
	t4_t3_t4_in += alt(MUL_in)
	t4_t3_t4 = S.Task('t4_t3_t4', length=7, delay_cost=1)
	t4_t3_t4 += alt(MUL)
	S += t4_t3_t4>=t4_t3_t4_in

	t4_t3_t4_mem0 = S.Task('t4_t3_t4_mem0', length=1, delay_cost=1)
	t4_t3_t4_mem0 += ADD_mem[0]
	S += 55 < t4_t3_t4_mem0
	S += t4_t3_t4_mem0 <= t4_t3_t4

	t4_t3_t4_mem1 = S.Task('t4_t3_t4_mem1', length=1, delay_cost=1)
	t4_t3_t4_mem1 += ADD_mem[1]
	S += 45 < t4_t3_t4_mem1
	S += t4_t3_t4_mem1 <= t4_t3_t4

	t4_t3_s00 = S.Task('t4_t3_s00', length=1, delay_cost=1)
	t4_t3_s00 += alt(ADD)

	t4_t3_s00_mem0 = S.Task('t4_t3_s00_mem0', length=1, delay_cost=1)
	t4_t3_s00_mem0 += MUL_mem[0]
	S += 14 < t4_t3_s00_mem0
	S += t4_t3_s00_mem0 <= t4_t3_s00

	t4_t3_t5 = S.Task('t4_t3_t5', length=1, delay_cost=1)
	t4_t3_t5 += alt(ADD)

	t4_t3_t5_mem0 = S.Task('t4_t3_t5_mem0', length=1, delay_cost=1)
	t4_t3_t5_mem0 += MUL_mem[0]
	S += 15 < t4_t3_t5_mem0
	S += t4_t3_t5_mem0 <= t4_t3_t5

	t4_t3_t5_mem1 = S.Task('t4_t3_t5_mem1', length=1, delay_cost=1)
	t4_t3_t5_mem1 += MUL_mem[0]
	S += 14 < t4_t3_t5_mem1
	S += t4_t3_t5_mem1 <= t4_t3_t5

	t5_t0_t4_in = S.Task('t5_t0_t4_in', length=1, delay_cost=1)
	t5_t0_t4_in += alt(MUL_in)
	t5_t0_t4 = S.Task('t5_t0_t4', length=7, delay_cost=1)
	t5_t0_t4 += alt(MUL)
	S += t5_t0_t4>=t5_t0_t4_in

	t5_t0_t4_mem0 = S.Task('t5_t0_t4_mem0', length=1, delay_cost=1)
	t5_t0_t4_mem0 += ADD_mem[0]
	S += 51 < t5_t0_t4_mem0
	S += t5_t0_t4_mem0 <= t5_t0_t4

	t5_t0_t4_mem1 = S.Task('t5_t0_t4_mem1', length=1, delay_cost=1)
	t5_t0_t4_mem1 += ADD_mem[0]
	S += 41 < t5_t0_t4_mem1
	S += t5_t0_t4_mem1 <= t5_t0_t4

	t5_t0_s00 = S.Task('t5_t0_s00', length=1, delay_cost=1)
	t5_t0_s00 += alt(ADD)

	t5_t0_s00_mem0 = S.Task('t5_t0_s00_mem0', length=1, delay_cost=1)
	t5_t0_s00_mem0 += MUL_mem[0]
	S += 44 < t5_t0_s00_mem0
	S += t5_t0_s00_mem0 <= t5_t0_s00

	t5_t0_t5 = S.Task('t5_t0_t5', length=1, delay_cost=1)
	t5_t0_t5 += alt(ADD)

	t5_t0_t5_mem0 = S.Task('t5_t0_t5_mem0', length=1, delay_cost=1)
	t5_t0_t5_mem0 += MUL_mem[0]
	S += 45 < t5_t0_t5_mem0
	S += t5_t0_t5_mem0 <= t5_t0_t5

	t5_t0_t5_mem1 = S.Task('t5_t0_t5_mem1', length=1, delay_cost=1)
	t5_t0_t5_mem1 += MUL_mem[0]
	S += 44 < t5_t0_t5_mem1
	S += t5_t0_t5_mem1 <= t5_t0_t5

	t5_t1_t4_in = S.Task('t5_t1_t4_in', length=1, delay_cost=1)
	t5_t1_t4_in += alt(MUL_in)
	t5_t1_t4 = S.Task('t5_t1_t4', length=7, delay_cost=1)
	t5_t1_t4 += alt(MUL)
	S += t5_t1_t4>=t5_t1_t4_in

	t5_t1_t4_mem0 = S.Task('t5_t1_t4_mem0', length=1, delay_cost=1)
	t5_t1_t4_mem0 += ADD_mem[0]
	S += 50 < t5_t1_t4_mem0
	S += t5_t1_t4_mem0 <= t5_t1_t4

	t5_t1_t4_mem1 = S.Task('t5_t1_t4_mem1', length=1, delay_cost=1)
	t5_t1_t4_mem1 += ADD_mem[1]
	S += 47 < t5_t1_t4_mem1
	S += t5_t1_t4_mem1 <= t5_t1_t4

	t5_t1_s00 = S.Task('t5_t1_s00', length=1, delay_cost=1)
	t5_t1_s00 += alt(ADD)

	t5_t1_s00_mem0 = S.Task('t5_t1_s00_mem0', length=1, delay_cost=1)
	t5_t1_s00_mem0 += MUL_mem[0]
	S += 42 < t5_t1_s00_mem0
	S += t5_t1_s00_mem0 <= t5_t1_s00

	t5_t1_t5 = S.Task('t5_t1_t5', length=1, delay_cost=1)
	t5_t1_t5 += alt(ADD)

	t5_t1_t5_mem0 = S.Task('t5_t1_t5_mem0', length=1, delay_cost=1)
	t5_t1_t5_mem0 += MUL_mem[0]
	S += 43 < t5_t1_t5_mem0
	S += t5_t1_t5_mem0 <= t5_t1_t5

	t5_t1_t5_mem1 = S.Task('t5_t1_t5_mem1', length=1, delay_cost=1)
	t5_t1_t5_mem1 += MUL_mem[0]
	S += 42 < t5_t1_t5_mem1
	S += t5_t1_t5_mem1 <= t5_t1_t5

	t5_t4_t0_in = S.Task('t5_t4_t0_in', length=1, delay_cost=1)
	t5_t4_t0_in += alt(MUL_in)
	t5_t4_t0 = S.Task('t5_t4_t0', length=7, delay_cost=1)
	t5_t4_t0 += alt(MUL)
	S += t5_t4_t0>=t5_t4_t0_in

	t5_t4_t0_mem0 = S.Task('t5_t4_t0_mem0', length=1, delay_cost=1)
	t5_t4_t0_mem0 += ADD_mem[1]
	S += 46 < t5_t4_t0_mem0
	S += t5_t4_t0_mem0 <= t5_t4_t0

	t5_t4_t0_mem1 = S.Task('t5_t4_t0_mem1', length=1, delay_cost=1)
	t5_t4_t0_mem1 += ADD_mem[0]
	S += 58 < t5_t4_t0_mem1
	S += t5_t4_t0_mem1 <= t5_t4_t0

	t5_t4_t1_in = S.Task('t5_t4_t1_in', length=1, delay_cost=1)
	t5_t4_t1_in += alt(MUL_in)
	t5_t4_t1 = S.Task('t5_t4_t1', length=7, delay_cost=1)
	t5_t4_t1 += alt(MUL)
	S += t5_t4_t1>=t5_t4_t1_in

	t5_t4_t1_mem0 = S.Task('t5_t4_t1_mem0', length=1, delay_cost=1)
	t5_t4_t1_mem0 += ADD_mem[0]
	S += 59 < t5_t4_t1_mem0
	S += t5_t4_t1_mem0 <= t5_t4_t1

	t5_t4_t1_mem1 = S.Task('t5_t4_t1_mem1', length=1, delay_cost=1)
	t5_t4_t1_mem1 += ADD_mem[1]
	S += 57 < t5_t4_t1_mem1
	S += t5_t4_t1_mem1 <= t5_t4_t1

	t5_t4_t2 = S.Task('t5_t4_t2', length=1, delay_cost=1)
	t5_t4_t2 += alt(ADD)

	t5_t4_t2_mem0 = S.Task('t5_t4_t2_mem0', length=1, delay_cost=1)
	t5_t4_t2_mem0 += ADD_mem[1]
	S += 46 < t5_t4_t2_mem0
	S += t5_t4_t2_mem0 <= t5_t4_t2

	t5_t4_t2_mem1 = S.Task('t5_t4_t2_mem1', length=1, delay_cost=1)
	t5_t4_t2_mem1 += ADD_mem[0]
	S += 59 < t5_t4_t2_mem1
	S += t5_t4_t2_mem1 <= t5_t4_t2

	t5_t4_t3 = S.Task('t5_t4_t3', length=1, delay_cost=1)
	t5_t4_t3 += alt(ADD)

	t5_t4_t3_mem0 = S.Task('t5_t4_t3_mem0', length=1, delay_cost=1)
	t5_t4_t3_mem0 += ADD_mem[0]
	S += 58 < t5_t4_t3_mem0
	S += t5_t4_t3_mem0 <= t5_t4_t3

	t5_t4_t3_mem1 = S.Task('t5_t4_t3_mem1', length=1, delay_cost=1)
	t5_t4_t3_mem1 += ADD_mem[1]
	S += 57 < t5_t4_t3_mem1
	S += t5_t4_t3_mem1 <= t5_t4_t3

	t6_t0_t4_in = S.Task('t6_t0_t4_in', length=1, delay_cost=1)
	t6_t0_t4_in += alt(MUL_in)
	t6_t0_t4 = S.Task('t6_t0_t4', length=7, delay_cost=1)
	t6_t0_t4 += alt(MUL)
	S += t6_t0_t4>=t6_t0_t4_in

	t6_t0_t4_mem0 = S.Task('t6_t0_t4_mem0', length=1, delay_cost=1)
	t6_t0_t4_mem0 += ADD_mem[0]
	S += 56 < t6_t0_t4_mem0
	S += t6_t0_t4_mem0 <= t6_t0_t4

	t6_t0_t4_mem1 = S.Task('t6_t0_t4_mem1', length=1, delay_cost=1)
	t6_t0_t4_mem1 += ADD_mem[3]
	S += 54 < t6_t0_t4_mem1
	S += t6_t0_t4_mem1 <= t6_t0_t4

	t6_t0_s00 = S.Task('t6_t0_s00', length=1, delay_cost=1)
	t6_t0_s00 += alt(ADD)

	t6_t0_s00_mem0 = S.Task('t6_t0_s00_mem0', length=1, delay_cost=1)
	t6_t0_s00_mem0 += MUL_mem[0]
	S += 38 < t6_t0_s00_mem0
	S += t6_t0_s00_mem0 <= t6_t0_s00

	t6_t0_t5 = S.Task('t6_t0_t5', length=1, delay_cost=1)
	t6_t0_t5 += alt(ADD)

	t6_t0_t5_mem0 = S.Task('t6_t0_t5_mem0', length=1, delay_cost=1)
	t6_t0_t5_mem0 += MUL_mem[0]
	S += 39 < t6_t0_t5_mem0
	S += t6_t0_t5_mem0 <= t6_t0_t5

	t6_t0_t5_mem1 = S.Task('t6_t0_t5_mem1', length=1, delay_cost=1)
	t6_t0_t5_mem1 += MUL_mem[0]
	S += 38 < t6_t0_t5_mem1
	S += t6_t0_t5_mem1 <= t6_t0_t5

	t6_t1_t4_in = S.Task('t6_t1_t4_in', length=1, delay_cost=1)
	t6_t1_t4_in += alt(MUL_in)
	t6_t1_t4 = S.Task('t6_t1_t4', length=7, delay_cost=1)
	t6_t1_t4 += alt(MUL)
	S += t6_t1_t4>=t6_t1_t4_in

	t6_t1_t4_mem0 = S.Task('t6_t1_t4_mem0', length=1, delay_cost=1)
	t6_t1_t4_mem0 += ADD_mem[0]
	S += 53 < t6_t1_t4_mem0
	S += t6_t1_t4_mem0 <= t6_t1_t4

	t6_t1_t4_mem1 = S.Task('t6_t1_t4_mem1', length=1, delay_cost=1)
	t6_t1_t4_mem1 += ADD_mem[0]
	S += 52 < t6_t1_t4_mem1
	S += t6_t1_t4_mem1 <= t6_t1_t4

	t6_t1_s00 = S.Task('t6_t1_s00', length=1, delay_cost=1)
	t6_t1_s00 += alt(ADD)

	t6_t1_s00_mem0 = S.Task('t6_t1_s00_mem0', length=1, delay_cost=1)
	t6_t1_s00_mem0 += MUL_mem[0]
	S += 36 < t6_t1_s00_mem0
	S += t6_t1_s00_mem0 <= t6_t1_s00

	t6_t1_t5 = S.Task('t6_t1_t5', length=1, delay_cost=1)
	t6_t1_t5 += alt(ADD)

	t6_t1_t5_mem0 = S.Task('t6_t1_t5_mem0', length=1, delay_cost=1)
	t6_t1_t5_mem0 += MUL_mem[0]
	S += 41 < t6_t1_t5_mem0
	S += t6_t1_t5_mem0 <= t6_t1_t5

	t6_t1_t5_mem1 = S.Task('t6_t1_t5_mem1', length=1, delay_cost=1)
	t6_t1_t5_mem1 += MUL_mem[0]
	S += 36 < t6_t1_t5_mem1
	S += t6_t1_t5_mem1 <= t6_t1_t5

	t6_t4_t0_in = S.Task('t6_t4_t0_in', length=1, delay_cost=1)
	t6_t4_t0_in += alt(MUL_in)
	t6_t4_t0 = S.Task('t6_t4_t0', length=7, delay_cost=1)
	t6_t4_t0 += alt(MUL)
	S += t6_t4_t0>=t6_t4_t0_in

	t6_t4_t0_mem0 = S.Task('t6_t4_t0_mem0', length=1, delay_cost=1)
	t6_t4_t0_mem0 += ADD_mem[0]
	S += 49 < t6_t4_t0_mem0
	S += t6_t4_t0_mem0 <= t6_t4_t0

	t6_t4_t0_mem1 = S.Task('t6_t4_t0_mem1', length=1, delay_cost=1)
	t6_t4_t0_mem1 += ADD_mem[0]
	S += 43 < t6_t4_t0_mem1
	S += t6_t4_t0_mem1 <= t6_t4_t0

	t6_t4_t1_in = S.Task('t6_t4_t1_in', length=1, delay_cost=1)
	t6_t4_t1_in += alt(MUL_in)
	t6_t4_t1 = S.Task('t6_t4_t1', length=7, delay_cost=1)
	t6_t4_t1 += alt(MUL)
	S += t6_t4_t1>=t6_t4_t1_in

	t6_t4_t1_mem0 = S.Task('t6_t4_t1_mem0', length=1, delay_cost=1)
	t6_t4_t1_mem0 += ADD_mem[3]
	S += 48 < t6_t4_t1_mem0
	S += t6_t4_t1_mem0 <= t6_t4_t1

	t6_t4_t1_mem1 = S.Task('t6_t4_t1_mem1', length=1, delay_cost=1)
	t6_t4_t1_mem1 += ADD_mem[2]
	S += 40 < t6_t4_t1_mem1
	S += t6_t4_t1_mem1 <= t6_t4_t1

	t6_t4_t2 = S.Task('t6_t4_t2', length=1, delay_cost=1)
	t6_t4_t2 += alt(ADD)

	t6_t4_t2_mem0 = S.Task('t6_t4_t2_mem0', length=1, delay_cost=1)
	t6_t4_t2_mem0 += ADD_mem[0]
	S += 49 < t6_t4_t2_mem0
	S += t6_t4_t2_mem0 <= t6_t4_t2

	t6_t4_t2_mem1 = S.Task('t6_t4_t2_mem1', length=1, delay_cost=1)
	t6_t4_t2_mem1 += ADD_mem[3]
	S += 48 < t6_t4_t2_mem1
	S += t6_t4_t2_mem1 <= t6_t4_t2

	t6_t4_t3 = S.Task('t6_t4_t3', length=1, delay_cost=1)
	t6_t4_t3 += alt(ADD)

	t6_t4_t3_mem0 = S.Task('t6_t4_t3_mem0', length=1, delay_cost=1)
	t6_t4_t3_mem0 += ADD_mem[0]
	S += 43 < t6_t4_t3_mem0
	S += t6_t4_t3_mem0 <= t6_t4_t3

	t6_t4_t3_mem1 = S.Task('t6_t4_t3_mem1', length=1, delay_cost=1)
	t6_t4_t3_mem1 += ADD_mem[2]
	S += 40 < t6_t4_t3_mem1
	S += t6_t4_t3_mem1 <= t6_t4_t3

	t7_t0_t4_in = S.Task('t7_t0_t4_in', length=1, delay_cost=1)
	t7_t0_t4_in += alt(MUL_in)
	t7_t0_t4 = S.Task('t7_t0_t4', length=7, delay_cost=1)
	t7_t0_t4 += alt(MUL)
	S += t7_t0_t4>=t7_t0_t4_in

	t7_t0_t4_mem0 = S.Task('t7_t0_t4_mem0', length=1, delay_cost=1)
	t7_t0_t4_mem0 += ADD_mem[1]
	S += 44 < t7_t0_t4_mem0
	S += t7_t0_t4_mem0 <= t7_t0_t4

	t7_t0_t4_mem1 = S.Task('t7_t0_t4_mem1', length=1, delay_cost=1)
	t7_t0_t4_mem1 += ADD_mem[0]
	S += 42 < t7_t0_t4_mem1
	S += t7_t0_t4_mem1 <= t7_t0_t4

	t7_t0_s00 = S.Task('t7_t0_s00', length=1, delay_cost=1)
	t7_t0_s00 += alt(ADD)

	t7_t0_s00_mem0 = S.Task('t7_t0_s00_mem0', length=1, delay_cost=1)
	t7_t0_s00_mem0 += MUL_mem[0]
	S += 37 < t7_t0_s00_mem0
	S += t7_t0_s00_mem0 <= t7_t0_s00

	t7_t0_t5 = S.Task('t7_t0_t5', length=1, delay_cost=1)
	t7_t0_t5 += alt(ADD)

	t7_t0_t5_mem0 = S.Task('t7_t0_t5_mem0', length=1, delay_cost=1)
	t7_t0_t5_mem0 += MUL_mem[0]
	S += 40 < t7_t0_t5_mem0
	S += t7_t0_t5_mem0 <= t7_t0_t5

	t7_t0_t5_mem1 = S.Task('t7_t0_t5_mem1', length=1, delay_cost=1)
	t7_t0_t5_mem1 += MUL_mem[0]
	S += 37 < t7_t0_t5_mem1
	S += t7_t0_t5_mem1 <= t7_t0_t5

	t7_t1_t4_in = S.Task('t7_t1_t4_in', length=1, delay_cost=1)
	t7_t1_t4_in += alt(MUL_in)
	t7_t1_t4 = S.Task('t7_t1_t4', length=7, delay_cost=1)
	t7_t1_t4 += alt(MUL)
	S += t7_t1_t4>=t7_t1_t4_in

	t7_t1_t4_mem0 = S.Task('t7_t1_t4_mem0', length=1, delay_cost=1)
	t7_t1_t4_mem0 += ADD_mem[2]
	S += 62 < t7_t1_t4_mem0
	S += t7_t1_t4_mem0 <= t7_t1_t4

	t7_t1_t4_mem1 = S.Task('t7_t1_t4_mem1', length=1, delay_cost=1)
	t7_t1_t4_mem1 += ADD_mem[0]
	S += 63 < t7_t1_t4_mem1
	S += t7_t1_t4_mem1 <= t7_t1_t4

	t7_t1_s00 = S.Task('t7_t1_s00', length=1, delay_cost=1)
	t7_t1_s00 += alt(ADD)

	t7_t1_s00_mem0 = S.Task('t7_t1_s00_mem0', length=1, delay_cost=1)
	t7_t1_s00_mem0 += MUL_mem[0]
	S += 67 < t7_t1_s00_mem0
	S += t7_t1_s00_mem0 <= t7_t1_s00

	t7_t1_t5 = S.Task('t7_t1_t5', length=1, delay_cost=1)
	t7_t1_t5 += alt(ADD)

	t7_t1_t5_mem0 = S.Task('t7_t1_t5_mem0', length=1, delay_cost=1)
	t7_t1_t5_mem0 += MUL_mem[0]
	S += 66 < t7_t1_t5_mem0
	S += t7_t1_t5_mem0 <= t7_t1_t5

	t7_t1_t5_mem1 = S.Task('t7_t1_t5_mem1', length=1, delay_cost=1)
	t7_t1_t5_mem1 += MUL_mem[0]
	S += 67 < t7_t1_t5_mem1
	S += t7_t1_t5_mem1 <= t7_t1_t5

	t7_t4_t0_in = S.Task('t7_t4_t0_in', length=1, delay_cost=1)
	t7_t4_t0_in += alt(MUL_in)
	t7_t4_t0 = S.Task('t7_t4_t0', length=7, delay_cost=1)
	t7_t4_t0 += alt(MUL)
	S += t7_t4_t0>=t7_t4_t0_in

	t7_t4_t0_mem0 = S.Task('t7_t4_t0_mem0', length=1, delay_cost=1)
	t7_t4_t0_mem0 += ADD_mem[1]
	S += 65 < t7_t4_t0_mem0
	S += t7_t4_t0_mem0 <= t7_t4_t0

	t7_t4_t0_mem1 = S.Task('t7_t4_t0_mem1', length=1, delay_cost=1)
	t7_t4_t0_mem1 += ADD_mem[2]
	S += 66 < t7_t4_t0_mem1
	S += t7_t4_t0_mem1 <= t7_t4_t0

	t7_t4_t1_in = S.Task('t7_t4_t1_in', length=1, delay_cost=1)
	t7_t4_t1_in += alt(MUL_in)
	t7_t4_t1 = S.Task('t7_t4_t1', length=7, delay_cost=1)
	t7_t4_t1 += alt(MUL)
	S += t7_t4_t1>=t7_t4_t1_in

	t7_t4_t1_mem0 = S.Task('t7_t4_t1_mem0', length=1, delay_cost=1)
	t7_t4_t1_mem0 += ADD_mem[3]
	S += 64 < t7_t4_t1_mem0
	S += t7_t4_t1_mem0 <= t7_t4_t1

	t7_t4_t1_mem1 = S.Task('t7_t4_t1_mem1', length=1, delay_cost=1)
	t7_t4_t1_mem1 += ADD_mem[1]
	S += 67 < t7_t4_t1_mem1
	S += t7_t4_t1_mem1 <= t7_t4_t1

	t7_t4_t2 = S.Task('t7_t4_t2', length=1, delay_cost=1)
	t7_t4_t2 += alt(ADD)

	t7_t4_t2_mem0 = S.Task('t7_t4_t2_mem0', length=1, delay_cost=1)
	t7_t4_t2_mem0 += ADD_mem[1]
	S += 65 < t7_t4_t2_mem0
	S += t7_t4_t2_mem0 <= t7_t4_t2

	t7_t4_t2_mem1 = S.Task('t7_t4_t2_mem1', length=1, delay_cost=1)
	t7_t4_t2_mem1 += ADD_mem[3]
	S += 64 < t7_t4_t2_mem1
	S += t7_t4_t2_mem1 <= t7_t4_t2

	t7_t4_t3 = S.Task('t7_t4_t3', length=1, delay_cost=1)
	t7_t4_t3 += alt(ADD)

	t7_t4_t3_mem0 = S.Task('t7_t4_t3_mem0', length=1, delay_cost=1)
	t7_t4_t3_mem0 += ADD_mem[2]
	S += 66 < t7_t4_t3_mem0
	S += t7_t4_t3_mem0 <= t7_t4_t3

	t7_t4_t3_mem1 = S.Task('t7_t4_t3_mem1', length=1, delay_cost=1)
	t7_t4_t3_mem1 += ADD_mem[1]
	S += 67 < t7_t4_t3_mem1
	S += t7_t4_t3_mem1 <= t7_t4_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/SQR012345_mul1_add4/SQR012345_3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

