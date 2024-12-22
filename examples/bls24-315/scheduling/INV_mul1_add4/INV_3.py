from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 236
	S = Scenario("INV_3", horizon=horizon)

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
	c_aa_t0_t0_t0_in = S.Task('c_aa_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_aa_t0_t0_t0_in >= 0
	c_aa_t0_t0_t0_in += MUL_in[0]

	c_aa_t0_t0_t0_mem0 = S.Task('c_aa_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t0_t0_mem0 >= 0
	c_aa_t0_t0_t0_mem0 += INPUT_mem_r

	c_aa_t0_t0_t0 = S.Task('c_aa_t0_t0_t0', length=7, delay_cost=1)
	S += c_aa_t0_t0_t0 >= 1
	c_aa_t0_t0_t0 += MUL[0]

	c_aa_t0_t0_t2_mem0 = S.Task('c_aa_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t0_t2_mem0 >= 1
	c_aa_t0_t0_t2_mem0 += INPUT_mem_r

	c_aa_t0_t0_t2_mem1 = S.Task('c_aa_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t0_t0_t2_mem1 >= 1
	c_aa_t0_t0_t2_mem1 += INPUT_mem_r

	c_aa_t0_t0_t2 = S.Task('c_aa_t0_t0_t2', length=1, delay_cost=1)
	S += c_aa_t0_t0_t2 >= 2
	c_aa_t0_t0_t2 += ADD[0]

	c_aa_t0_t21_mem0 = S.Task('c_aa_t0_t21_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t21_mem0 >= 2
	c_aa_t0_t21_mem0 += INPUT_mem_r

	c_aa_t0_t21_mem1 = S.Task('c_aa_t0_t21_mem1', length=1, delay_cost=1)
	S += c_aa_t0_t21_mem1 >= 2
	c_aa_t0_t21_mem1 += INPUT_mem_r

	c_aa_t0_t21 = S.Task('c_aa_t0_t21', length=1, delay_cost=1)
	S += c_aa_t0_t21 >= 3
	c_aa_t0_t21 += ADD[2]

	c_aa_t0_t30_mem0 = S.Task('c_aa_t0_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t30_mem0 >= 3
	c_aa_t0_t30_mem0 += INPUT_mem_r

	c_aa_t0_t30_mem1 = S.Task('c_aa_t0_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t0_t30_mem1 >= 3
	c_aa_t0_t30_mem1 += INPUT_mem_r

	c_aa_t0_t30 = S.Task('c_aa_t0_t30', length=1, delay_cost=1)
	S += c_aa_t0_t30 >= 4
	c_aa_t0_t30 += ADD[3]

	c_aa_t0_t31_mem0 = S.Task('c_aa_t0_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t31_mem0 >= 4
	c_aa_t0_t31_mem0 += INPUT_mem_r

	c_aa_t0_t31_mem1 = S.Task('c_aa_t0_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t0_t31_mem1 >= 4
	c_aa_t0_t31_mem1 += INPUT_mem_r

	c_aa_t0_t31 = S.Task('c_aa_t0_t31', length=1, delay_cost=1)
	S += c_aa_t0_t31 >= 5
	c_aa_t0_t31 += ADD[0]

	c_aa_t1_t0_t2_mem0 = S.Task('c_aa_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t0_t2_mem0 >= 5
	c_aa_t1_t0_t2_mem0 += INPUT_mem_r

	c_aa_t1_t0_t2_mem1 = S.Task('c_aa_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t1_t0_t2_mem1 >= 5
	c_aa_t1_t0_t2_mem1 += INPUT_mem_r

	c_aa_t1_t0_t2 = S.Task('c_aa_t1_t0_t2', length=1, delay_cost=1)
	S += c_aa_t1_t0_t2 >= 6
	c_aa_t1_t0_t2 += ADD[3]

	c_aa_t1_t0_t3_mem0 = S.Task('c_aa_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t0_t3_mem0 >= 6
	c_aa_t1_t0_t3_mem0 += INPUT_mem_r

	c_aa_t1_t0_t3_mem1 = S.Task('c_aa_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t1_t0_t3_mem1 >= 6
	c_aa_t1_t0_t3_mem1 += INPUT_mem_r

	c_aa_t1_t0_t3 = S.Task('c_aa_t1_t0_t3', length=1, delay_cost=1)
	S += c_aa_t1_t0_t3 >= 7
	c_aa_t1_t0_t3 += ADD[0]

	c_aa_t1_t1_t2_mem0 = S.Task('c_aa_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t1_t2_mem0 >= 7
	c_aa_t1_t1_t2_mem0 += INPUT_mem_r

	c_aa_t1_t1_t2_mem1 = S.Task('c_aa_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t1_t1_t2_mem1 >= 7
	c_aa_t1_t1_t2_mem1 += INPUT_mem_r

	c_aa_t0_t0_t3_mem0 = S.Task('c_aa_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t0_t3_mem0 >= 8
	c_aa_t0_t0_t3_mem0 += INPUT_mem_r

	c_aa_t0_t0_t3_mem1 = S.Task('c_aa_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t0_t0_t3_mem1 >= 8
	c_aa_t0_t0_t3_mem1 += INPUT_mem_r

	c_aa_t1_t1_t2 = S.Task('c_aa_t1_t1_t2', length=1, delay_cost=1)
	S += c_aa_t1_t1_t2 >= 8
	c_aa_t1_t1_t2 += ADD[0]

	c_aa_t0_t0_t1_in = S.Task('c_aa_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_aa_t0_t0_t1_in >= 9
	c_aa_t0_t0_t1_in += MUL_in[0]

	c_aa_t0_t0_t1_mem0 = S.Task('c_aa_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t0_t1_mem0 >= 9
	c_aa_t0_t0_t1_mem0 += INPUT_mem_r

	c_aa_t0_t0_t3 = S.Task('c_aa_t0_t0_t3', length=1, delay_cost=1)
	S += c_aa_t0_t0_t3 >= 9
	c_aa_t0_t0_t3 += ADD[0]

	c_aa_t0_t0_t1 = S.Task('c_aa_t0_t0_t1', length=7, delay_cost=1)
	S += c_aa_t0_t0_t1 >= 10
	c_aa_t0_t0_t1 += MUL[0]

	c_aa_t1_t1_t3_mem0 = S.Task('c_aa_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t1_t3_mem0 >= 10
	c_aa_t1_t1_t3_mem0 += INPUT_mem_r

	c_aa_t1_t1_t3_mem1 = S.Task('c_aa_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t1_t1_t3_mem1 >= 10
	c_aa_t1_t1_t3_mem1 += INPUT_mem_r

	c_aa_t1_t1_t3 = S.Task('c_aa_t1_t1_t3', length=1, delay_cost=1)
	S += c_aa_t1_t1_t3 >= 11
	c_aa_t1_t1_t3 += ADD[0]

	c_aa_t1_t20_mem0 = S.Task('c_aa_t1_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t20_mem0 >= 11
	c_aa_t1_t20_mem0 += INPUT_mem_r

	c_aa_t1_t20_mem1 = S.Task('c_aa_t1_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t1_t20_mem1 >= 11
	c_aa_t1_t20_mem1 += INPUT_mem_r

	c_aa_t1_t20 = S.Task('c_aa_t1_t20', length=1, delay_cost=1)
	S += c_aa_t1_t20 >= 12
	c_aa_t1_t20 += ADD[0]

	c_aa_t1_t21_mem0 = S.Task('c_aa_t1_t21_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t21_mem0 >= 12
	c_aa_t1_t21_mem0 += INPUT_mem_r

	c_aa_t1_t21_mem1 = S.Task('c_aa_t1_t21_mem1', length=1, delay_cost=1)
	S += c_aa_t1_t21_mem1 >= 12
	c_aa_t1_t21_mem1 += INPUT_mem_r

	c_aa_t1_t21 = S.Task('c_aa_t1_t21', length=1, delay_cost=1)
	S += c_aa_t1_t21 >= 13
	c_aa_t1_t21 += ADD[0]

	c_aa_t1_t30_mem0 = S.Task('c_aa_t1_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t30_mem0 >= 13
	c_aa_t1_t30_mem0 += INPUT_mem_r

	c_aa_t1_t30_mem1 = S.Task('c_aa_t1_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t1_t30_mem1 >= 13
	c_aa_t1_t30_mem1 += INPUT_mem_r

	c_aa_t1_t30 = S.Task('c_aa_t1_t30', length=1, delay_cost=1)
	S += c_aa_t1_t30 >= 14
	c_aa_t1_t30 += ADD[0]

	c_aa_t1_t31_mem0 = S.Task('c_aa_t1_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t31_mem0 >= 14
	c_aa_t1_t31_mem0 += INPUT_mem_r

	c_aa_t1_t31_mem1 = S.Task('c_aa_t1_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t1_t31_mem1 >= 14
	c_aa_t1_t31_mem1 += INPUT_mem_r

	c_aa_t1_t31 = S.Task('c_aa_t1_t31', length=1, delay_cost=1)
	S += c_aa_t1_t31 >= 15
	c_aa_t1_t31 += ADD[2]

	c_aa_t2_t0_t2_mem0 = S.Task('c_aa_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_t2_mem0 >= 15
	c_aa_t2_t0_t2_mem0 += INPUT_mem_r

	c_aa_t2_t0_t2_mem1 = S.Task('c_aa_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_t2_mem1 >= 15
	c_aa_t2_t0_t2_mem1 += INPUT_mem_r

	c_aa_t2_t0_t2 = S.Task('c_aa_t2_t0_t2', length=1, delay_cost=1)
	S += c_aa_t2_t0_t2 >= 16
	c_aa_t2_t0_t2 += ADD[0]

	c_aa_t2_t0_t3_mem0 = S.Task('c_aa_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_t3_mem0 >= 16
	c_aa_t2_t0_t3_mem0 += INPUT_mem_r

	c_aa_t2_t0_t3_mem1 = S.Task('c_aa_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_t3_mem1 >= 16
	c_aa_t2_t0_t3_mem1 += INPUT_mem_r

	c_aa_t0_t1_t3_mem0 = S.Task('c_aa_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t1_t3_mem0 >= 17
	c_aa_t0_t1_t3_mem0 += INPUT_mem_r

	c_aa_t0_t1_t3_mem1 = S.Task('c_aa_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t0_t1_t3_mem1 >= 17
	c_aa_t0_t1_t3_mem1 += INPUT_mem_r

	c_aa_t2_t0_t3 = S.Task('c_aa_t2_t0_t3', length=1, delay_cost=1)
	S += c_aa_t2_t0_t3 >= 17
	c_aa_t2_t0_t3 += ADD[0]

	c_aa_t0_t1_t3 = S.Task('c_aa_t0_t1_t3', length=1, delay_cost=1)
	S += c_aa_t0_t1_t3 >= 18
	c_aa_t0_t1_t3 += ADD[1]

	c_aa_t0_t20_mem0 = S.Task('c_aa_t0_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t20_mem0 >= 18
	c_aa_t0_t20_mem0 += INPUT_mem_r

	c_aa_t0_t20_mem1 = S.Task('c_aa_t0_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t0_t20_mem1 >= 18
	c_aa_t0_t20_mem1 += INPUT_mem_r

	c_aa_t0_t20 = S.Task('c_aa_t0_t20', length=1, delay_cost=1)
	S += c_aa_t0_t20 >= 19
	c_aa_t0_t20 += ADD[3]

	c_aa_t2_t0_t1_in = S.Task('c_aa_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_t1_in >= 19
	c_aa_t2_t0_t1_in += MUL_in[0]

	c_aa_t2_t0_t1_mem0 = S.Task('c_aa_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_t1_mem0 >= 19
	c_aa_t2_t0_t1_mem0 += INPUT_mem_r

	c_aa_t2_t0_t0_in = S.Task('c_aa_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_t0_in >= 20
	c_aa_t2_t0_t0_in += MUL_in[0]

	c_aa_t2_t0_t0_mem0 = S.Task('c_aa_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_t0_mem0 >= 20
	c_aa_t2_t0_t0_mem0 += INPUT_mem_r

	c_aa_t2_t0_t1 = S.Task('c_aa_t2_t0_t1', length=7, delay_cost=1)
	S += c_aa_t2_t0_t1 >= 20
	c_aa_t2_t0_t1 += MUL[0]

	c_aa_t1_t1_t1_in = S.Task('c_aa_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_aa_t1_t1_t1_in >= 21
	c_aa_t1_t1_t1_in += MUL_in[0]

	c_aa_t1_t1_t1_mem0 = S.Task('c_aa_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t1_t1_mem0 >= 21
	c_aa_t1_t1_t1_mem0 += INPUT_mem_r

	c_aa_t2_t0_t0 = S.Task('c_aa_t2_t0_t0', length=7, delay_cost=1)
	S += c_aa_t2_t0_t0 >= 21
	c_aa_t2_t0_t0 += MUL[0]

	c_aa_t1_t1_t0_in = S.Task('c_aa_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_aa_t1_t1_t0_in >= 22
	c_aa_t1_t1_t0_in += MUL_in[0]

	c_aa_t1_t1_t0_mem0 = S.Task('c_aa_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t1_t0_mem0 >= 22
	c_aa_t1_t1_t0_mem0 += INPUT_mem_r

	c_aa_t1_t1_t1 = S.Task('c_aa_t1_t1_t1', length=7, delay_cost=1)
	S += c_aa_t1_t1_t1 >= 22
	c_aa_t1_t1_t1 += MUL[0]

	c_aa_t1_t0_t1_in = S.Task('c_aa_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_aa_t1_t0_t1_in >= 23
	c_aa_t1_t0_t1_in += MUL_in[0]

	c_aa_t1_t0_t1_mem0 = S.Task('c_aa_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t0_t1_mem0 >= 23
	c_aa_t1_t0_t1_mem0 += INPUT_mem_r

	c_aa_t1_t1_t0 = S.Task('c_aa_t1_t1_t0', length=7, delay_cost=1)
	S += c_aa_t1_t1_t0 >= 23
	c_aa_t1_t1_t0 += MUL[0]

	c_aa_t1_t0_t0_in = S.Task('c_aa_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_aa_t1_t0_t0_in >= 24
	c_aa_t1_t0_t0_in += MUL_in[0]

	c_aa_t1_t0_t0_mem0 = S.Task('c_aa_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t1_t0_t0_mem0 >= 24
	c_aa_t1_t0_t0_mem0 += INPUT_mem_r

	c_aa_t1_t0_t1 = S.Task('c_aa_t1_t0_t1', length=7, delay_cost=1)
	S += c_aa_t1_t0_t1 >= 24
	c_aa_t1_t0_t1 += MUL[0]

	c_aa_t0_t1_t1_in = S.Task('c_aa_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_aa_t0_t1_t1_in >= 25
	c_aa_t0_t1_t1_in += MUL_in[0]

	c_aa_t0_t1_t1_mem0 = S.Task('c_aa_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t1_t1_mem0 >= 25
	c_aa_t0_t1_t1_mem0 += INPUT_mem_r

	c_aa_t1_t0_t0 = S.Task('c_aa_t1_t0_t0', length=7, delay_cost=1)
	S += c_aa_t1_t0_t0 >= 25
	c_aa_t1_t0_t0 += MUL[0]

	c_aa_t0_t1_t1 = S.Task('c_aa_t0_t1_t1', length=7, delay_cost=1)
	S += c_aa_t0_t1_t1 >= 26
	c_aa_t0_t1_t1 += MUL[0]

	c_aa_t0_t1_t2_mem0 = S.Task('c_aa_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t1_t2_mem0 >= 26
	c_aa_t0_t1_t2_mem0 += INPUT_mem_r

	c_aa_t0_t1_t2_mem1 = S.Task('c_aa_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t0_t1_t2_mem1 >= 26
	c_aa_t0_t1_t2_mem1 += INPUT_mem_r

	c_aa_t0_t1_t2 = S.Task('c_aa_t0_t1_t2', length=1, delay_cost=1)
	S += c_aa_t0_t1_t2 >= 27
	c_aa_t0_t1_t2 += ADD[3]

	c_aa_t2_t1_t1_in = S.Task('c_aa_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_t1_in >= 27
	c_aa_t2_t1_t1_in += MUL_in[0]

	c_aa_t2_t1_t1_mem0 = S.Task('c_aa_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_t1_mem0 >= 27
	c_aa_t2_t1_t1_mem0 += INPUT_mem_r

	c_aa_t0_t1_t0_in = S.Task('c_aa_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_aa_t0_t1_t0_in >= 28
	c_aa_t0_t1_t0_in += MUL_in[0]

	c_aa_t0_t1_t0_mem0 = S.Task('c_aa_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t0_t1_t0_mem0 >= 28
	c_aa_t0_t1_t0_mem0 += INPUT_mem_r

	c_aa_t2_t1_t1 = S.Task('c_aa_t2_t1_t1', length=7, delay_cost=1)
	S += c_aa_t2_t1_t1 >= 28
	c_aa_t2_t1_t1 += MUL[0]

	c_aa_t0_t1_t0 = S.Task('c_aa_t0_t1_t0', length=7, delay_cost=1)
	S += c_aa_t0_t1_t0 >= 29
	c_aa_t0_t1_t0 += MUL[0]

	c_aa_t2_t1_t0_in = S.Task('c_aa_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_t0_in >= 29
	c_aa_t2_t1_t0_in += MUL_in[0]

	c_aa_t2_t1_t0_mem0 = S.Task('c_aa_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_t0_mem0 >= 29
	c_aa_t2_t1_t0_mem0 += INPUT_mem_r

	c_aa_t2_t1_t0 = S.Task('c_aa_t2_t1_t0', length=7, delay_cost=1)
	S += c_aa_t2_t1_t0 >= 30
	c_aa_t2_t1_t0 += MUL[0]

	c_aa_t5100_mem0 = S.Task('c_aa_t5100_mem0', length=1, delay_cost=1)
	S += c_aa_t5100_mem0 >= 30
	c_aa_t5100_mem0 += INPUT_mem_r

	c_aa_t5100_mem1 = S.Task('c_aa_t5100_mem1', length=1, delay_cost=1)
	S += c_aa_t5100_mem1 >= 30
	c_aa_t5100_mem1 += INPUT_mem_r

	c_aa_t4110_mem0 = S.Task('c_aa_t4110_mem0', length=1, delay_cost=1)
	S += c_aa_t4110_mem0 >= 31
	c_aa_t4110_mem0 += INPUT_mem_r

	c_aa_t4110_mem1 = S.Task('c_aa_t4110_mem1', length=1, delay_cost=1)
	S += c_aa_t4110_mem1 >= 31
	c_aa_t4110_mem1 += INPUT_mem_r

	c_aa_t5100 = S.Task('c_aa_t5100', length=1, delay_cost=1)
	S += c_aa_t5100 >= 31
	c_aa_t5100 += ADD[0]

	c_aa_t4110 = S.Task('c_aa_t4110', length=1, delay_cost=1)
	S += c_aa_t4110 >= 32
	c_aa_t4110 += ADD[0]

	c_aa_t5110_mem0 = S.Task('c_aa_t5110_mem0', length=1, delay_cost=1)
	S += c_aa_t5110_mem0 >= 32
	c_aa_t5110_mem0 += INPUT_mem_r

	c_aa_t5110_mem1 = S.Task('c_aa_t5110_mem1', length=1, delay_cost=1)
	S += c_aa_t5110_mem1 >= 32
	c_aa_t5110_mem1 += INPUT_mem_r

	c_aa_t4111_mem0 = S.Task('c_aa_t4111_mem0', length=1, delay_cost=1)
	S += c_aa_t4111_mem0 >= 33
	c_aa_t4111_mem0 += INPUT_mem_r

	c_aa_t4111_mem1 = S.Task('c_aa_t4111_mem1', length=1, delay_cost=1)
	S += c_aa_t4111_mem1 >= 33
	c_aa_t4111_mem1 += INPUT_mem_r

	c_aa_t5110 = S.Task('c_aa_t5110', length=1, delay_cost=1)
	S += c_aa_t5110 >= 33
	c_aa_t5110 += ADD[0]

	c_aa_t3000_mem0 = S.Task('c_aa_t3000_mem0', length=1, delay_cost=1)
	S += c_aa_t3000_mem0 >= 34
	c_aa_t3000_mem0 += INPUT_mem_r

	c_aa_t3000_mem1 = S.Task('c_aa_t3000_mem1', length=1, delay_cost=1)
	S += c_aa_t3000_mem1 >= 34
	c_aa_t3000_mem1 += INPUT_mem_r

	c_aa_t4111 = S.Task('c_aa_t4111', length=1, delay_cost=1)
	S += c_aa_t4111 >= 34
	c_aa_t4111 += ADD[0]

	c_aa_t3000 = S.Task('c_aa_t3000', length=1, delay_cost=1)
	S += c_aa_t3000 >= 35
	c_aa_t3000 += ADD[1]

	c_aa_t3110_mem0 = S.Task('c_aa_t3110_mem0', length=1, delay_cost=1)
	S += c_aa_t3110_mem0 >= 35
	c_aa_t3110_mem0 += INPUT_mem_r

	c_aa_t3110_mem1 = S.Task('c_aa_t3110_mem1', length=1, delay_cost=1)
	S += c_aa_t3110_mem1 >= 35
	c_aa_t3110_mem1 += INPUT_mem_r

	c_aa_t3010_mem0 = S.Task('c_aa_t3010_mem0', length=1, delay_cost=1)
	S += c_aa_t3010_mem0 >= 36
	c_aa_t3010_mem0 += INPUT_mem_r

	c_aa_t3010_mem1 = S.Task('c_aa_t3010_mem1', length=1, delay_cost=1)
	S += c_aa_t3010_mem1 >= 36
	c_aa_t3010_mem1 += INPUT_mem_r

	c_aa_t3110 = S.Task('c_aa_t3110', length=1, delay_cost=1)
	S += c_aa_t3110 >= 36
	c_aa_t3110 += ADD[3]

	c_aa_t3010 = S.Task('c_aa_t3010', length=1, delay_cost=1)
	S += c_aa_t3010 >= 37
	c_aa_t3010 += ADD[2]

	c_aa_t5000_mem0 = S.Task('c_aa_t5000_mem0', length=1, delay_cost=1)
	S += c_aa_t5000_mem0 >= 37
	c_aa_t5000_mem0 += INPUT_mem_r

	c_aa_t5000_mem1 = S.Task('c_aa_t5000_mem1', length=1, delay_cost=1)
	S += c_aa_t5000_mem1 >= 37
	c_aa_t5000_mem1 += INPUT_mem_r

	c_aa_t2_t1_t3_mem0 = S.Task('c_aa_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_t3_mem0 >= 38
	c_aa_t2_t1_t3_mem0 += INPUT_mem_r

	c_aa_t2_t1_t3_mem1 = S.Task('c_aa_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_t3_mem1 >= 38
	c_aa_t2_t1_t3_mem1 += INPUT_mem_r

	c_aa_t5000 = S.Task('c_aa_t5000', length=1, delay_cost=1)
	S += c_aa_t5000 >= 38
	c_aa_t5000 += ADD[2]

	c_aa_t2_t1_t3 = S.Task('c_aa_t2_t1_t3', length=1, delay_cost=1)
	S += c_aa_t2_t1_t3 >= 39
	c_aa_t2_t1_t3 += ADD[3]

	c_aa_t2_t31_mem0 = S.Task('c_aa_t2_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t31_mem0 >= 39
	c_aa_t2_t31_mem0 += INPUT_mem_r

	c_aa_t2_t31_mem1 = S.Task('c_aa_t2_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t31_mem1 >= 39
	c_aa_t2_t31_mem1 += INPUT_mem_r

	c_aa_t2_t20_mem0 = S.Task('c_aa_t2_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t20_mem0 >= 40
	c_aa_t2_t20_mem0 += INPUT_mem_r

	c_aa_t2_t20_mem1 = S.Task('c_aa_t2_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t20_mem1 >= 40
	c_aa_t2_t20_mem1 += INPUT_mem_r

	c_aa_t2_t31 = S.Task('c_aa_t2_t31', length=1, delay_cost=1)
	S += c_aa_t2_t31 >= 40
	c_aa_t2_t31 += ADD[0]

	c_aa_t2_t20 = S.Task('c_aa_t2_t20', length=1, delay_cost=1)
	S += c_aa_t2_t20 >= 41
	c_aa_t2_t20 += ADD[0]

	c_aa_t4101_mem0 = S.Task('c_aa_t4101_mem0', length=1, delay_cost=1)
	S += c_aa_t4101_mem0 >= 41
	c_aa_t4101_mem0 += INPUT_mem_r

	c_aa_t4101_mem1 = S.Task('c_aa_t4101_mem1', length=1, delay_cost=1)
	S += c_aa_t4101_mem1 >= 41
	c_aa_t4101_mem1 += INPUT_mem_r

	c_aa_t3100_mem0 = S.Task('c_aa_t3100_mem0', length=1, delay_cost=1)
	S += c_aa_t3100_mem0 >= 42
	c_aa_t3100_mem0 += INPUT_mem_r

	c_aa_t3100_mem1 = S.Task('c_aa_t3100_mem1', length=1, delay_cost=1)
	S += c_aa_t3100_mem1 >= 42
	c_aa_t3100_mem1 += INPUT_mem_r

	c_aa_t4101 = S.Task('c_aa_t4101', length=1, delay_cost=1)
	S += c_aa_t4101 >= 42
	c_aa_t4101 += ADD[1]

	c_aa_t3100 = S.Task('c_aa_t3100', length=1, delay_cost=1)
	S += c_aa_t3100 >= 43
	c_aa_t3100 += ADD[3]

	c_aa_t3111_mem0 = S.Task('c_aa_t3111_mem0', length=1, delay_cost=1)
	S += c_aa_t3111_mem0 >= 43
	c_aa_t3111_mem0 += INPUT_mem_r

	c_aa_t3111_mem1 = S.Task('c_aa_t3111_mem1', length=1, delay_cost=1)
	S += c_aa_t3111_mem1 >= 43
	c_aa_t3111_mem1 += INPUT_mem_r

	c_aa_t3101_mem0 = S.Task('c_aa_t3101_mem0', length=1, delay_cost=1)
	S += c_aa_t3101_mem0 >= 44
	c_aa_t3101_mem0 += INPUT_mem_r

	c_aa_t3101_mem1 = S.Task('c_aa_t3101_mem1', length=1, delay_cost=1)
	S += c_aa_t3101_mem1 >= 44
	c_aa_t3101_mem1 += INPUT_mem_r

	c_aa_t3111 = S.Task('c_aa_t3111', length=1, delay_cost=1)
	S += c_aa_t3111 >= 44
	c_aa_t3111 += ADD[0]

	c_aa_t2_t1_t2_mem0 = S.Task('c_aa_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_t2_mem0 >= 45
	c_aa_t2_t1_t2_mem0 += INPUT_mem_r

	c_aa_t2_t1_t2_mem1 = S.Task('c_aa_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_t2_mem1 >= 45
	c_aa_t2_t1_t2_mem1 += INPUT_mem_r

	c_aa_t3101 = S.Task('c_aa_t3101', length=1, delay_cost=1)
	S += c_aa_t3101 >= 45
	c_aa_t3101 += ADD[3]

	c_aa_t2_t1_t2 = S.Task('c_aa_t2_t1_t2', length=1, delay_cost=1)
	S += c_aa_t2_t1_t2 >= 46
	c_aa_t2_t1_t2 += ADD[1]

	c_aa_t4010_mem0 = S.Task('c_aa_t4010_mem0', length=1, delay_cost=1)
	S += c_aa_t4010_mem0 >= 46
	c_aa_t4010_mem0 += INPUT_mem_r

	c_aa_t4010_mem1 = S.Task('c_aa_t4010_mem1', length=1, delay_cost=1)
	S += c_aa_t4010_mem1 >= 46
	c_aa_t4010_mem1 += INPUT_mem_r

	c_aa_t4010 = S.Task('c_aa_t4010', length=1, delay_cost=1)
	S += c_aa_t4010 >= 47
	c_aa_t4010 += ADD[0]

	c_aa_t5010_mem0 = S.Task('c_aa_t5010_mem0', length=1, delay_cost=1)
	S += c_aa_t5010_mem0 >= 47
	c_aa_t5010_mem0 += INPUT_mem_r

	c_aa_t5010_mem1 = S.Task('c_aa_t5010_mem1', length=1, delay_cost=1)
	S += c_aa_t5010_mem1 >= 47
	c_aa_t5010_mem1 += INPUT_mem_r

	c_aa_t3001_mem0 = S.Task('c_aa_t3001_mem0', length=1, delay_cost=1)
	S += c_aa_t3001_mem0 >= 48
	c_aa_t3001_mem0 += INPUT_mem_r

	c_aa_t3001_mem1 = S.Task('c_aa_t3001_mem1', length=1, delay_cost=1)
	S += c_aa_t3001_mem1 >= 48
	c_aa_t3001_mem1 += INPUT_mem_r

	c_aa_t5010 = S.Task('c_aa_t5010', length=1, delay_cost=1)
	S += c_aa_t5010 >= 48
	c_aa_t5010 += ADD[0]

	c_aa_t3001 = S.Task('c_aa_t3001', length=1, delay_cost=1)
	S += c_aa_t3001 >= 49
	c_aa_t3001 += ADD[2]

	c_aa_t4011_mem0 = S.Task('c_aa_t4011_mem0', length=1, delay_cost=1)
	S += c_aa_t4011_mem0 >= 49
	c_aa_t4011_mem0 += INPUT_mem_r

	c_aa_t4011_mem1 = S.Task('c_aa_t4011_mem1', length=1, delay_cost=1)
	S += c_aa_t4011_mem1 >= 49
	c_aa_t4011_mem1 += INPUT_mem_r

	c_aa_t4011 = S.Task('c_aa_t4011', length=1, delay_cost=1)
	S += c_aa_t4011 >= 50
	c_aa_t4011 += ADD[2]

	c_aa_t5001_mem0 = S.Task('c_aa_t5001_mem0', length=1, delay_cost=1)
	S += c_aa_t5001_mem0 >= 50
	c_aa_t5001_mem0 += INPUT_mem_r

	c_aa_t5001_mem1 = S.Task('c_aa_t5001_mem1', length=1, delay_cost=1)
	S += c_aa_t5001_mem1 >= 50
	c_aa_t5001_mem1 += INPUT_mem_r

	c_aa_t3011_mem0 = S.Task('c_aa_t3011_mem0', length=1, delay_cost=1)
	S += c_aa_t3011_mem0 >= 51
	c_aa_t3011_mem0 += INPUT_mem_r

	c_aa_t3011_mem1 = S.Task('c_aa_t3011_mem1', length=1, delay_cost=1)
	S += c_aa_t3011_mem1 >= 51
	c_aa_t3011_mem1 += INPUT_mem_r

	c_aa_t5001 = S.Task('c_aa_t5001', length=1, delay_cost=1)
	S += c_aa_t5001 >= 51
	c_aa_t5001 += ADD[0]

	c_aa_t3011 = S.Task('c_aa_t3011', length=1, delay_cost=1)
	S += c_aa_t3011 >= 52
	c_aa_t3011 += ADD[3]

	c_aa_t4000_mem0 = S.Task('c_aa_t4000_mem0', length=1, delay_cost=1)
	S += c_aa_t4000_mem0 >= 52
	c_aa_t4000_mem0 += INPUT_mem_r

	c_aa_t4000_mem1 = S.Task('c_aa_t4000_mem1', length=1, delay_cost=1)
	S += c_aa_t4000_mem1 >= 52
	c_aa_t4000_mem1 += INPUT_mem_r

	c_aa_t4000 = S.Task('c_aa_t4000', length=1, delay_cost=1)
	S += c_aa_t4000 >= 53
	c_aa_t4000 += ADD[3]

	c_aa_t4001_mem0 = S.Task('c_aa_t4001_mem0', length=1, delay_cost=1)
	S += c_aa_t4001_mem0 >= 53
	c_aa_t4001_mem0 += INPUT_mem_r

	c_aa_t4001_mem1 = S.Task('c_aa_t4001_mem1', length=1, delay_cost=1)
	S += c_aa_t4001_mem1 >= 53
	c_aa_t4001_mem1 += INPUT_mem_r

	c_aa_t2_t21_mem0 = S.Task('c_aa_t2_t21_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t21_mem0 >= 54
	c_aa_t2_t21_mem0 += INPUT_mem_r

	c_aa_t2_t21_mem1 = S.Task('c_aa_t2_t21_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t21_mem1 >= 54
	c_aa_t2_t21_mem1 += INPUT_mem_r

	c_aa_t4001 = S.Task('c_aa_t4001', length=1, delay_cost=1)
	S += c_aa_t4001 >= 54
	c_aa_t4001 += ADD[3]

	c_aa_t2_t21 = S.Task('c_aa_t2_t21', length=1, delay_cost=1)
	S += c_aa_t2_t21 >= 55
	c_aa_t2_t21 += ADD[0]

	c_aa_t5011_mem0 = S.Task('c_aa_t5011_mem0', length=1, delay_cost=1)
	S += c_aa_t5011_mem0 >= 55
	c_aa_t5011_mem0 += INPUT_mem_r

	c_aa_t5011_mem1 = S.Task('c_aa_t5011_mem1', length=1, delay_cost=1)
	S += c_aa_t5011_mem1 >= 55
	c_aa_t5011_mem1 += INPUT_mem_r

	c_aa_t5011 = S.Task('c_aa_t5011', length=1, delay_cost=1)
	S += c_aa_t5011 >= 56
	c_aa_t5011 += ADD[2]

	c_aa_t5101_mem0 = S.Task('c_aa_t5101_mem0', length=1, delay_cost=1)
	S += c_aa_t5101_mem0 >= 56
	c_aa_t5101_mem0 += INPUT_mem_r

	c_aa_t5101_mem1 = S.Task('c_aa_t5101_mem1', length=1, delay_cost=1)
	S += c_aa_t5101_mem1 >= 56
	c_aa_t5101_mem1 += INPUT_mem_r

	c_aa_t5101 = S.Task('c_aa_t5101', length=1, delay_cost=1)
	S += c_aa_t5101 >= 57
	c_aa_t5101 += ADD[0]

	c_aa_t5111_mem0 = S.Task('c_aa_t5111_mem0', length=1, delay_cost=1)
	S += c_aa_t5111_mem0 >= 57
	c_aa_t5111_mem0 += INPUT_mem_r

	c_aa_t5111_mem1 = S.Task('c_aa_t5111_mem1', length=1, delay_cost=1)
	S += c_aa_t5111_mem1 >= 57
	c_aa_t5111_mem1 += INPUT_mem_r

	c_aa_t4100_mem0 = S.Task('c_aa_t4100_mem0', length=1, delay_cost=1)
	S += c_aa_t4100_mem0 >= 58
	c_aa_t4100_mem0 += INPUT_mem_r

	c_aa_t4100_mem1 = S.Task('c_aa_t4100_mem1', length=1, delay_cost=1)
	S += c_aa_t4100_mem1 >= 58
	c_aa_t4100_mem1 += INPUT_mem_r

	c_aa_t5111 = S.Task('c_aa_t5111', length=1, delay_cost=1)
	S += c_aa_t5111 >= 58
	c_aa_t5111 += ADD[0]

	c_aa_t2_t30_mem0 = S.Task('c_aa_t2_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t30_mem0 >= 59
	c_aa_t2_t30_mem0 += INPUT_mem_r

	c_aa_t2_t30_mem1 = S.Task('c_aa_t2_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t30_mem1 >= 59
	c_aa_t2_t30_mem1 += INPUT_mem_r

	c_aa_t4100 = S.Task('c_aa_t4100', length=1, delay_cost=1)
	S += c_aa_t4100 >= 59
	c_aa_t4100 += ADD[0]

	c_aa_t2_t30 = S.Task('c_aa_t2_t30', length=1, delay_cost=1)
	S += c_aa_t2_t30 >= 60
	c_aa_t2_t30 += ADD[0]

	c_bb_t0_t20_mem0 = S.Task('c_bb_t0_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t20_mem0 >= 60
	c_bb_t0_t20_mem0 += INPUT_mem_r

	c_bb_t0_t20_mem1 = S.Task('c_bb_t0_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t0_t20_mem1 >= 60
	c_bb_t0_t20_mem1 += INPUT_mem_r

	c_bb_t0_t20 = S.Task('c_bb_t0_t20', length=1, delay_cost=1)
	S += c_bb_t0_t20 >= 61
	c_bb_t0_t20 += ADD[2]

	c_bb_t0_t21_mem0 = S.Task('c_bb_t0_t21_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t21_mem0 >= 61
	c_bb_t0_t21_mem0 += INPUT_mem_r

	c_bb_t0_t21_mem1 = S.Task('c_bb_t0_t21_mem1', length=1, delay_cost=1)
	S += c_bb_t0_t21_mem1 >= 61
	c_bb_t0_t21_mem1 += INPUT_mem_r

	c_bb_t0_t21 = S.Task('c_bb_t0_t21', length=1, delay_cost=1)
	S += c_bb_t0_t21 >= 62
	c_bb_t0_t21 += ADD[0]

	c_bb_t0_t30_mem0 = S.Task('c_bb_t0_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t30_mem0 >= 62
	c_bb_t0_t30_mem0 += INPUT_mem_r

	c_bb_t0_t30_mem1 = S.Task('c_bb_t0_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t0_t30_mem1 >= 62
	c_bb_t0_t30_mem1 += INPUT_mem_r

	c_bb_t0_t30 = S.Task('c_bb_t0_t30', length=1, delay_cost=1)
	S += c_bb_t0_t30 >= 63
	c_bb_t0_t30 += ADD[2]

	c_bb_t0_t31_mem0 = S.Task('c_bb_t0_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t31_mem0 >= 63
	c_bb_t0_t31_mem0 += INPUT_mem_r

	c_bb_t0_t31_mem1 = S.Task('c_bb_t0_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t0_t31_mem1 >= 63
	c_bb_t0_t31_mem1 += INPUT_mem_r

	c_bb_t0_t31 = S.Task('c_bb_t0_t31', length=1, delay_cost=1)
	S += c_bb_t0_t31 >= 64
	c_bb_t0_t31 += ADD[0]

	c_bb_t1_t0_t2_mem0 = S.Task('c_bb_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t0_t2_mem0 >= 64
	c_bb_t1_t0_t2_mem0 += INPUT_mem_r

	c_bb_t1_t0_t2_mem1 = S.Task('c_bb_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t1_t0_t2_mem1 >= 64
	c_bb_t1_t0_t2_mem1 += INPUT_mem_r

	c_bb_t1_t0_t2 = S.Task('c_bb_t1_t0_t2', length=1, delay_cost=1)
	S += c_bb_t1_t0_t2 >= 65
	c_bb_t1_t0_t2 += ADD[0]

	c_bb_t1_t0_t3_mem0 = S.Task('c_bb_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t0_t3_mem0 >= 65
	c_bb_t1_t0_t3_mem0 += INPUT_mem_r

	c_bb_t1_t0_t3_mem1 = S.Task('c_bb_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t1_t0_t3_mem1 >= 65
	c_bb_t1_t0_t3_mem1 += INPUT_mem_r

	c_bb_t0_t0_t2_mem0 = S.Task('c_bb_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t0_t2_mem0 >= 66
	c_bb_t0_t0_t2_mem0 += INPUT_mem_r

	c_bb_t0_t0_t2_mem1 = S.Task('c_bb_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t0_t0_t2_mem1 >= 66
	c_bb_t0_t0_t2_mem1 += INPUT_mem_r

	c_bb_t1_t0_t3 = S.Task('c_bb_t1_t0_t3', length=1, delay_cost=1)
	S += c_bb_t1_t0_t3 >= 66
	c_bb_t1_t0_t3 += ADD[2]

	c_bb_t0_t0_t2 = S.Task('c_bb_t0_t0_t2', length=1, delay_cost=1)
	S += c_bb_t0_t0_t2 >= 67
	c_bb_t0_t0_t2 += ADD[1]

	c_bb_t1_t1_t2_mem0 = S.Task('c_bb_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t1_t2_mem0 >= 67
	c_bb_t1_t1_t2_mem0 += INPUT_mem_r

	c_bb_t1_t1_t2_mem1 = S.Task('c_bb_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t1_t1_t2_mem1 >= 67
	c_bb_t1_t1_t2_mem1 += INPUT_mem_r

	c_bb_t1_t1_t2 = S.Task('c_bb_t1_t1_t2', length=1, delay_cost=1)
	S += c_bb_t1_t1_t2 >= 68
	c_bb_t1_t1_t2 += ADD[1]

	c_bb_t1_t1_t3_mem0 = S.Task('c_bb_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t1_t3_mem0 >= 68
	c_bb_t1_t1_t3_mem0 += INPUT_mem_r

	c_bb_t1_t1_t3_mem1 = S.Task('c_bb_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t1_t1_t3_mem1 >= 68
	c_bb_t1_t1_t3_mem1 += INPUT_mem_r

	c_bb_t1_t1_t3 = S.Task('c_bb_t1_t1_t3', length=1, delay_cost=1)
	S += c_bb_t1_t1_t3 >= 69
	c_bb_t1_t1_t3 += ADD[3]

	c_bb_t1_t20_mem0 = S.Task('c_bb_t1_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t20_mem0 >= 69
	c_bb_t1_t20_mem0 += INPUT_mem_r

	c_bb_t1_t20_mem1 = S.Task('c_bb_t1_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t1_t20_mem1 >= 69
	c_bb_t1_t20_mem1 += INPUT_mem_r

	c_bb_t1_t20 = S.Task('c_bb_t1_t20', length=1, delay_cost=1)
	S += c_bb_t1_t20 >= 70
	c_bb_t1_t20 += ADD[2]

	c_bb_t1_t21_mem0 = S.Task('c_bb_t1_t21_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t21_mem0 >= 70
	c_bb_t1_t21_mem0 += INPUT_mem_r

	c_bb_t1_t21_mem1 = S.Task('c_bb_t1_t21_mem1', length=1, delay_cost=1)
	S += c_bb_t1_t21_mem1 >= 70
	c_bb_t1_t21_mem1 += INPUT_mem_r

	c_bb_t1_t21 = S.Task('c_bb_t1_t21', length=1, delay_cost=1)
	S += c_bb_t1_t21 >= 71
	c_bb_t1_t21 += ADD[0]

	c_bb_t1_t30_mem0 = S.Task('c_bb_t1_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t30_mem0 >= 71
	c_bb_t1_t30_mem0 += INPUT_mem_r

	c_bb_t1_t30_mem1 = S.Task('c_bb_t1_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t1_t30_mem1 >= 71
	c_bb_t1_t30_mem1 += INPUT_mem_r

	c_bb_t1_t30 = S.Task('c_bb_t1_t30', length=1, delay_cost=1)
	S += c_bb_t1_t30 >= 72
	c_bb_t1_t30 += ADD[3]

	c_bb_t1_t31_mem0 = S.Task('c_bb_t1_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t31_mem0 >= 72
	c_bb_t1_t31_mem0 += INPUT_mem_r

	c_bb_t1_t31_mem1 = S.Task('c_bb_t1_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t1_t31_mem1 >= 72
	c_bb_t1_t31_mem1 += INPUT_mem_r

	c_bb_t1_t31 = S.Task('c_bb_t1_t31', length=1, delay_cost=1)
	S += c_bb_t1_t31 >= 73
	c_bb_t1_t31 += ADD[1]

	c_bb_t2_t0_t2_mem0 = S.Task('c_bb_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_t2_mem0 >= 73
	c_bb_t2_t0_t2_mem0 += INPUT_mem_r

	c_bb_t2_t0_t2_mem1 = S.Task('c_bb_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_t2_mem1 >= 73
	c_bb_t2_t0_t2_mem1 += INPUT_mem_r

	c_bb_t2_t0_t2 = S.Task('c_bb_t2_t0_t2', length=1, delay_cost=1)
	S += c_bb_t2_t0_t2 >= 74
	c_bb_t2_t0_t2 += ADD[3]

	c_bb_t2_t0_t3_mem0 = S.Task('c_bb_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_t3_mem0 >= 74
	c_bb_t2_t0_t3_mem0 += INPUT_mem_r

	c_bb_t2_t0_t3_mem1 = S.Task('c_bb_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_t3_mem1 >= 74
	c_bb_t2_t0_t3_mem1 += INPUT_mem_r

	c_bb_t0_t0_t3_mem0 = S.Task('c_bb_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t0_t3_mem0 >= 75
	c_bb_t0_t0_t3_mem0 += INPUT_mem_r

	c_bb_t0_t0_t3_mem1 = S.Task('c_bb_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t0_t0_t3_mem1 >= 75
	c_bb_t0_t0_t3_mem1 += INPUT_mem_r

	c_bb_t2_t0_t3 = S.Task('c_bb_t2_t0_t3', length=1, delay_cost=1)
	S += c_bb_t2_t0_t3 >= 75
	c_bb_t2_t0_t3 += ADD[0]

	c_bb_t0_t0_t3 = S.Task('c_bb_t0_t0_t3', length=1, delay_cost=1)
	S += c_bb_t0_t0_t3 >= 76
	c_bb_t0_t0_t3 += ADD[0]

	c_bb_t0_t1_t2_mem0 = S.Task('c_bb_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t1_t2_mem0 >= 76
	c_bb_t0_t1_t2_mem0 += INPUT_mem_r

	c_bb_t0_t1_t2_mem1 = S.Task('c_bb_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t0_t1_t2_mem1 >= 76
	c_bb_t0_t1_t2_mem1 += INPUT_mem_r

	c_bb_t0_t1_t2 = S.Task('c_bb_t0_t1_t2', length=1, delay_cost=1)
	S += c_bb_t0_t1_t2 >= 77
	c_bb_t0_t1_t2 += ADD[1]

	c_bb_t0_t1_t3_mem0 = S.Task('c_bb_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t1_t3_mem0 >= 77
	c_bb_t0_t1_t3_mem0 += INPUT_mem_r

	c_bb_t0_t1_t3_mem1 = S.Task('c_bb_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t0_t1_t3_mem1 >= 77
	c_bb_t0_t1_t3_mem1 += INPUT_mem_r

	c_bb_t0_t1_t3 = S.Task('c_bb_t0_t1_t3', length=1, delay_cost=1)
	S += c_bb_t0_t1_t3 >= 78
	c_bb_t0_t1_t3 += ADD[0]

	c_bb_t1_t1_t1_in = S.Task('c_bb_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_bb_t1_t1_t1_in >= 78
	c_bb_t1_t1_t1_in += MUL_in[0]

	c_bb_t1_t1_t1_mem0 = S.Task('c_bb_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t1_t1_mem0 >= 78
	c_bb_t1_t1_t1_mem0 += INPUT_mem_r

	c_bb_t1_t1_t0_in = S.Task('c_bb_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_bb_t1_t1_t0_in >= 79
	c_bb_t1_t1_t0_in += MUL_in[0]

	c_bb_t1_t1_t0_mem0 = S.Task('c_bb_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t1_t0_mem0 >= 79
	c_bb_t1_t1_t0_mem0 += INPUT_mem_r

	c_bb_t1_t1_t1 = S.Task('c_bb_t1_t1_t1', length=7, delay_cost=1)
	S += c_bb_t1_t1_t1 >= 79
	c_bb_t1_t1_t1 += MUL[0]

	c_bb_t1_t0_t1_in = S.Task('c_bb_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_bb_t1_t0_t1_in >= 80
	c_bb_t1_t0_t1_in += MUL_in[0]

	c_bb_t1_t0_t1_mem0 = S.Task('c_bb_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t0_t1_mem0 >= 80
	c_bb_t1_t0_t1_mem0 += INPUT_mem_r

	c_bb_t1_t1_t0 = S.Task('c_bb_t1_t1_t0', length=7, delay_cost=1)
	S += c_bb_t1_t1_t0 >= 80
	c_bb_t1_t1_t0 += MUL[0]

	c_bb_t1_t0_t0_in = S.Task('c_bb_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_bb_t1_t0_t0_in >= 81
	c_bb_t1_t0_t0_in += MUL_in[0]

	c_bb_t1_t0_t0_mem0 = S.Task('c_bb_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t1_t0_t0_mem0 >= 81
	c_bb_t1_t0_t0_mem0 += INPUT_mem_r

	c_bb_t1_t0_t1 = S.Task('c_bb_t1_t0_t1', length=7, delay_cost=1)
	S += c_bb_t1_t0_t1 >= 81
	c_bb_t1_t0_t1 += MUL[0]

	c_bb_t0_t1_t1_in = S.Task('c_bb_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_bb_t0_t1_t1_in >= 82
	c_bb_t0_t1_t1_in += MUL_in[0]

	c_bb_t0_t1_t1_mem0 = S.Task('c_bb_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t1_t1_mem0 >= 82
	c_bb_t0_t1_t1_mem0 += INPUT_mem_r

	c_bb_t1_t0_t0 = S.Task('c_bb_t1_t0_t0', length=7, delay_cost=1)
	S += c_bb_t1_t0_t0 >= 82
	c_bb_t1_t0_t0 += MUL[0]

	c_bb_t0_t1_t0_in = S.Task('c_bb_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_bb_t0_t1_t0_in >= 83
	c_bb_t0_t1_t0_in += MUL_in[0]

	c_bb_t0_t1_t0_mem0 = S.Task('c_bb_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t1_t0_mem0 >= 83
	c_bb_t0_t1_t0_mem0 += INPUT_mem_r

	c_bb_t0_t1_t1 = S.Task('c_bb_t0_t1_t1', length=7, delay_cost=1)
	S += c_bb_t0_t1_t1 >= 83
	c_bb_t0_t1_t1 += MUL[0]

	c_bb_t0_t0_t1_in = S.Task('c_bb_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_bb_t0_t0_t1_in >= 84
	c_bb_t0_t0_t1_in += MUL_in[0]

	c_bb_t0_t0_t1_mem0 = S.Task('c_bb_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t0_t1_mem0 >= 84
	c_bb_t0_t0_t1_mem0 += INPUT_mem_r

	c_bb_t0_t1_t0 = S.Task('c_bb_t0_t1_t0', length=7, delay_cost=1)
	S += c_bb_t0_t1_t0 >= 84
	c_bb_t0_t1_t0 += MUL[0]

	c_bb_t0_t0_t1 = S.Task('c_bb_t0_t0_t1', length=7, delay_cost=1)
	S += c_bb_t0_t0_t1 >= 85
	c_bb_t0_t0_t1 += MUL[0]

	c_bb_t2_t1_t1_in = S.Task('c_bb_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_t1_in >= 85
	c_bb_t2_t1_t1_in += MUL_in[0]

	c_bb_t2_t1_t1_mem0 = S.Task('c_bb_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_t1_mem0 >= 85
	c_bb_t2_t1_t1_mem0 += INPUT_mem_r

	c_bb_t2_t1_t0_in = S.Task('c_bb_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_t0_in >= 86
	c_bb_t2_t1_t0_in += MUL_in[0]

	c_bb_t2_t1_t0_mem0 = S.Task('c_bb_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_t0_mem0 >= 86
	c_bb_t2_t1_t0_mem0 += INPUT_mem_r

	c_bb_t2_t1_t1 = S.Task('c_bb_t2_t1_t1', length=7, delay_cost=1)
	S += c_bb_t2_t1_t1 >= 86
	c_bb_t2_t1_t1 += MUL[0]

	c_bb_t2_t0_t1_in = S.Task('c_bb_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_t1_in >= 87
	c_bb_t2_t0_t1_in += MUL_in[0]

	c_bb_t2_t0_t1_mem0 = S.Task('c_bb_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_t1_mem0 >= 87
	c_bb_t2_t0_t1_mem0 += INPUT_mem_r

	c_bb_t2_t1_t0 = S.Task('c_bb_t2_t1_t0', length=7, delay_cost=1)
	S += c_bb_t2_t1_t0 >= 87
	c_bb_t2_t1_t0 += MUL[0]

	c_bb_t0_t0_t0_in = S.Task('c_bb_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_bb_t0_t0_t0_in >= 88
	c_bb_t0_t0_t0_in += MUL_in[0]

	c_bb_t0_t0_t0_mem0 = S.Task('c_bb_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t0_t0_t0_mem0 >= 88
	c_bb_t0_t0_t0_mem0 += INPUT_mem_r

	c_bb_t2_t0_t1 = S.Task('c_bb_t2_t0_t1', length=7, delay_cost=1)
	S += c_bb_t2_t0_t1 >= 88
	c_bb_t2_t0_t1 += MUL[0]

	c_bb_t0_t0_t0 = S.Task('c_bb_t0_t0_t0', length=7, delay_cost=1)
	S += c_bb_t0_t0_t0 >= 89
	c_bb_t0_t0_t0 += MUL[0]

	c_bb_t2_t0_t0_in = S.Task('c_bb_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_t0_in >= 89
	c_bb_t2_t0_t0_in += MUL_in[0]

	c_bb_t2_t0_t0_mem0 = S.Task('c_bb_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_t0_mem0 >= 89
	c_bb_t2_t0_t0_mem0 += INPUT_mem_r

	c_bb_t2_t0_t0 = S.Task('c_bb_t2_t0_t0', length=7, delay_cost=1)
	S += c_bb_t2_t0_t0 >= 90
	c_bb_t2_t0_t0 += MUL[0]


	# new tasks
	c_bb_t2_t1_t2 = S.Task('c_bb_t2_t1_t2', length=1, delay_cost=1)
	c_bb_t2_t1_t2 += alt(ADD)

	c_bb_t2_t1_t2_mem0 = S.Task('c_bb_t2_t1_t2_mem0', length=1, delay_cost=1)
	c_bb_t2_t1_t2_mem0 += INPUT_mem_r
	S += c_bb_t2_t1_t2_mem0 <= c_bb_t2_t1_t2

	c_bb_t2_t1_t2_mem1 = S.Task('c_bb_t2_t1_t2_mem1', length=1, delay_cost=1)
	c_bb_t2_t1_t2_mem1 += INPUT_mem_r
	S += c_bb_t2_t1_t2_mem1 <= c_bb_t2_t1_t2

	c_bb_t2_t1_t3 = S.Task('c_bb_t2_t1_t3', length=1, delay_cost=1)
	c_bb_t2_t1_t3 += alt(ADD)

	c_bb_t2_t1_t3_mem0 = S.Task('c_bb_t2_t1_t3_mem0', length=1, delay_cost=1)
	c_bb_t2_t1_t3_mem0 += INPUT_mem_r
	S += c_bb_t2_t1_t3_mem0 <= c_bb_t2_t1_t3

	c_bb_t2_t1_t3_mem1 = S.Task('c_bb_t2_t1_t3_mem1', length=1, delay_cost=1)
	c_bb_t2_t1_t3_mem1 += INPUT_mem_r
	S += c_bb_t2_t1_t3_mem1 <= c_bb_t2_t1_t3

	c_bb_t2_t20 = S.Task('c_bb_t2_t20', length=1, delay_cost=1)
	c_bb_t2_t20 += alt(ADD)

	c_bb_t2_t20_mem0 = S.Task('c_bb_t2_t20_mem0', length=1, delay_cost=1)
	c_bb_t2_t20_mem0 += INPUT_mem_r
	S += c_bb_t2_t20_mem0 <= c_bb_t2_t20

	c_bb_t2_t20_mem1 = S.Task('c_bb_t2_t20_mem1', length=1, delay_cost=1)
	c_bb_t2_t20_mem1 += INPUT_mem_r
	S += c_bb_t2_t20_mem1 <= c_bb_t2_t20

	c_bb_t2_t21 = S.Task('c_bb_t2_t21', length=1, delay_cost=1)
	c_bb_t2_t21 += alt(ADD)

	c_bb_t2_t21_mem0 = S.Task('c_bb_t2_t21_mem0', length=1, delay_cost=1)
	c_bb_t2_t21_mem0 += INPUT_mem_r
	S += c_bb_t2_t21_mem0 <= c_bb_t2_t21

	c_bb_t2_t21_mem1 = S.Task('c_bb_t2_t21_mem1', length=1, delay_cost=1)
	c_bb_t2_t21_mem1 += INPUT_mem_r
	S += c_bb_t2_t21_mem1 <= c_bb_t2_t21

	c_bb_t2_t30 = S.Task('c_bb_t2_t30', length=1, delay_cost=1)
	c_bb_t2_t30 += alt(ADD)

	c_bb_t2_t30_mem0 = S.Task('c_bb_t2_t30_mem0', length=1, delay_cost=1)
	c_bb_t2_t30_mem0 += INPUT_mem_r
	S += c_bb_t2_t30_mem0 <= c_bb_t2_t30

	c_bb_t2_t30_mem1 = S.Task('c_bb_t2_t30_mem1', length=1, delay_cost=1)
	c_bb_t2_t30_mem1 += INPUT_mem_r
	S += c_bb_t2_t30_mem1 <= c_bb_t2_t30

	c_bb_t2_t31 = S.Task('c_bb_t2_t31', length=1, delay_cost=1)
	c_bb_t2_t31 += alt(ADD)

	c_bb_t2_t31_mem0 = S.Task('c_bb_t2_t31_mem0', length=1, delay_cost=1)
	c_bb_t2_t31_mem0 += INPUT_mem_r
	S += c_bb_t2_t31_mem0 <= c_bb_t2_t31

	c_bb_t2_t31_mem1 = S.Task('c_bb_t2_t31_mem1', length=1, delay_cost=1)
	c_bb_t2_t31_mem1 += INPUT_mem_r
	S += c_bb_t2_t31_mem1 <= c_bb_t2_t31

	c_bb_t3000 = S.Task('c_bb_t3000', length=1, delay_cost=1)
	c_bb_t3000 += alt(ADD)

	c_bb_t3000_mem0 = S.Task('c_bb_t3000_mem0', length=1, delay_cost=1)
	c_bb_t3000_mem0 += INPUT_mem_r
	S += c_bb_t3000_mem0 <= c_bb_t3000

	c_bb_t3000_mem1 = S.Task('c_bb_t3000_mem1', length=1, delay_cost=1)
	c_bb_t3000_mem1 += INPUT_mem_r
	S += c_bb_t3000_mem1 <= c_bb_t3000

	c_bb_t3001 = S.Task('c_bb_t3001', length=1, delay_cost=1)
	c_bb_t3001 += alt(ADD)

	c_bb_t3001_mem0 = S.Task('c_bb_t3001_mem0', length=1, delay_cost=1)
	c_bb_t3001_mem0 += INPUT_mem_r
	S += c_bb_t3001_mem0 <= c_bb_t3001

	c_bb_t3001_mem1 = S.Task('c_bb_t3001_mem1', length=1, delay_cost=1)
	c_bb_t3001_mem1 += INPUT_mem_r
	S += c_bb_t3001_mem1 <= c_bb_t3001

	c_bb_t3010 = S.Task('c_bb_t3010', length=1, delay_cost=1)
	c_bb_t3010 += alt(ADD)

	c_bb_t3010_mem0 = S.Task('c_bb_t3010_mem0', length=1, delay_cost=1)
	c_bb_t3010_mem0 += INPUT_mem_r
	S += c_bb_t3010_mem0 <= c_bb_t3010

	c_bb_t3010_mem1 = S.Task('c_bb_t3010_mem1', length=1, delay_cost=1)
	c_bb_t3010_mem1 += INPUT_mem_r
	S += c_bb_t3010_mem1 <= c_bb_t3010

	c_bb_t3011 = S.Task('c_bb_t3011', length=1, delay_cost=1)
	c_bb_t3011 += alt(ADD)

	c_bb_t3011_mem0 = S.Task('c_bb_t3011_mem0', length=1, delay_cost=1)
	c_bb_t3011_mem0 += INPUT_mem_r
	S += c_bb_t3011_mem0 <= c_bb_t3011

	c_bb_t3011_mem1 = S.Task('c_bb_t3011_mem1', length=1, delay_cost=1)
	c_bb_t3011_mem1 += INPUT_mem_r
	S += c_bb_t3011_mem1 <= c_bb_t3011

	c_bb_t3100 = S.Task('c_bb_t3100', length=1, delay_cost=1)
	c_bb_t3100 += alt(ADD)

	c_bb_t3100_mem0 = S.Task('c_bb_t3100_mem0', length=1, delay_cost=1)
	c_bb_t3100_mem0 += INPUT_mem_r
	S += c_bb_t3100_mem0 <= c_bb_t3100

	c_bb_t3100_mem1 = S.Task('c_bb_t3100_mem1', length=1, delay_cost=1)
	c_bb_t3100_mem1 += INPUT_mem_r
	S += c_bb_t3100_mem1 <= c_bb_t3100

	c_bb_t3101 = S.Task('c_bb_t3101', length=1, delay_cost=1)
	c_bb_t3101 += alt(ADD)

	c_bb_t3101_mem0 = S.Task('c_bb_t3101_mem0', length=1, delay_cost=1)
	c_bb_t3101_mem0 += INPUT_mem_r
	S += c_bb_t3101_mem0 <= c_bb_t3101

	c_bb_t3101_mem1 = S.Task('c_bb_t3101_mem1', length=1, delay_cost=1)
	c_bb_t3101_mem1 += INPUT_mem_r
	S += c_bb_t3101_mem1 <= c_bb_t3101

	c_bb_t3110 = S.Task('c_bb_t3110', length=1, delay_cost=1)
	c_bb_t3110 += alt(ADD)

	c_bb_t3110_mem0 = S.Task('c_bb_t3110_mem0', length=1, delay_cost=1)
	c_bb_t3110_mem0 += INPUT_mem_r
	S += c_bb_t3110_mem0 <= c_bb_t3110

	c_bb_t3110_mem1 = S.Task('c_bb_t3110_mem1', length=1, delay_cost=1)
	c_bb_t3110_mem1 += INPUT_mem_r
	S += c_bb_t3110_mem1 <= c_bb_t3110

	c_bb_t3111 = S.Task('c_bb_t3111', length=1, delay_cost=1)
	c_bb_t3111 += alt(ADD)

	c_bb_t3111_mem0 = S.Task('c_bb_t3111_mem0', length=1, delay_cost=1)
	c_bb_t3111_mem0 += INPUT_mem_r
	S += c_bb_t3111_mem0 <= c_bb_t3111

	c_bb_t3111_mem1 = S.Task('c_bb_t3111_mem1', length=1, delay_cost=1)
	c_bb_t3111_mem1 += INPUT_mem_r
	S += c_bb_t3111_mem1 <= c_bb_t3111

	c_bb_t4000 = S.Task('c_bb_t4000', length=1, delay_cost=1)
	c_bb_t4000 += alt(ADD)

	c_bb_t4000_mem0 = S.Task('c_bb_t4000_mem0', length=1, delay_cost=1)
	c_bb_t4000_mem0 += INPUT_mem_r
	S += c_bb_t4000_mem0 <= c_bb_t4000

	c_bb_t4000_mem1 = S.Task('c_bb_t4000_mem1', length=1, delay_cost=1)
	c_bb_t4000_mem1 += INPUT_mem_r
	S += c_bb_t4000_mem1 <= c_bb_t4000

	c_bb_t4001 = S.Task('c_bb_t4001', length=1, delay_cost=1)
	c_bb_t4001 += alt(ADD)

	c_bb_t4001_mem0 = S.Task('c_bb_t4001_mem0', length=1, delay_cost=1)
	c_bb_t4001_mem0 += INPUT_mem_r
	S += c_bb_t4001_mem0 <= c_bb_t4001

	c_bb_t4001_mem1 = S.Task('c_bb_t4001_mem1', length=1, delay_cost=1)
	c_bb_t4001_mem1 += INPUT_mem_r
	S += c_bb_t4001_mem1 <= c_bb_t4001

	c_bb_t4010 = S.Task('c_bb_t4010', length=1, delay_cost=1)
	c_bb_t4010 += alt(ADD)

	c_bb_t4010_mem0 = S.Task('c_bb_t4010_mem0', length=1, delay_cost=1)
	c_bb_t4010_mem0 += INPUT_mem_r
	S += c_bb_t4010_mem0 <= c_bb_t4010

	c_bb_t4010_mem1 = S.Task('c_bb_t4010_mem1', length=1, delay_cost=1)
	c_bb_t4010_mem1 += INPUT_mem_r
	S += c_bb_t4010_mem1 <= c_bb_t4010

	c_bb_t4011 = S.Task('c_bb_t4011', length=1, delay_cost=1)
	c_bb_t4011 += alt(ADD)

	c_bb_t4011_mem0 = S.Task('c_bb_t4011_mem0', length=1, delay_cost=1)
	c_bb_t4011_mem0 += INPUT_mem_r
	S += c_bb_t4011_mem0 <= c_bb_t4011

	c_bb_t4011_mem1 = S.Task('c_bb_t4011_mem1', length=1, delay_cost=1)
	c_bb_t4011_mem1 += INPUT_mem_r
	S += c_bb_t4011_mem1 <= c_bb_t4011

	c_bb_t4100 = S.Task('c_bb_t4100', length=1, delay_cost=1)
	c_bb_t4100 += alt(ADD)

	c_bb_t4100_mem0 = S.Task('c_bb_t4100_mem0', length=1, delay_cost=1)
	c_bb_t4100_mem0 += INPUT_mem_r
	S += c_bb_t4100_mem0 <= c_bb_t4100

	c_bb_t4100_mem1 = S.Task('c_bb_t4100_mem1', length=1, delay_cost=1)
	c_bb_t4100_mem1 += INPUT_mem_r
	S += c_bb_t4100_mem1 <= c_bb_t4100

	c_bb_t4101 = S.Task('c_bb_t4101', length=1, delay_cost=1)
	c_bb_t4101 += alt(ADD)

	c_bb_t4101_mem0 = S.Task('c_bb_t4101_mem0', length=1, delay_cost=1)
	c_bb_t4101_mem0 += INPUT_mem_r
	S += c_bb_t4101_mem0 <= c_bb_t4101

	c_bb_t4101_mem1 = S.Task('c_bb_t4101_mem1', length=1, delay_cost=1)
	c_bb_t4101_mem1 += INPUT_mem_r
	S += c_bb_t4101_mem1 <= c_bb_t4101

	c_bb_t4110 = S.Task('c_bb_t4110', length=1, delay_cost=1)
	c_bb_t4110 += alt(ADD)

	c_bb_t4110_mem0 = S.Task('c_bb_t4110_mem0', length=1, delay_cost=1)
	c_bb_t4110_mem0 += INPUT_mem_r
	S += c_bb_t4110_mem0 <= c_bb_t4110

	c_bb_t4110_mem1 = S.Task('c_bb_t4110_mem1', length=1, delay_cost=1)
	c_bb_t4110_mem1 += INPUT_mem_r
	S += c_bb_t4110_mem1 <= c_bb_t4110

	c_bb_t4111 = S.Task('c_bb_t4111', length=1, delay_cost=1)
	c_bb_t4111 += alt(ADD)

	c_bb_t4111_mem0 = S.Task('c_bb_t4111_mem0', length=1, delay_cost=1)
	c_bb_t4111_mem0 += INPUT_mem_r
	S += c_bb_t4111_mem0 <= c_bb_t4111

	c_bb_t4111_mem1 = S.Task('c_bb_t4111_mem1', length=1, delay_cost=1)
	c_bb_t4111_mem1 += INPUT_mem_r
	S += c_bb_t4111_mem1 <= c_bb_t4111

	c_bb_t5000 = S.Task('c_bb_t5000', length=1, delay_cost=1)
	c_bb_t5000 += alt(ADD)

	c_bb_t5000_mem0 = S.Task('c_bb_t5000_mem0', length=1, delay_cost=1)
	c_bb_t5000_mem0 += INPUT_mem_r
	S += c_bb_t5000_mem0 <= c_bb_t5000

	c_bb_t5000_mem1 = S.Task('c_bb_t5000_mem1', length=1, delay_cost=1)
	c_bb_t5000_mem1 += INPUT_mem_r
	S += c_bb_t5000_mem1 <= c_bb_t5000

	c_bb_t5001 = S.Task('c_bb_t5001', length=1, delay_cost=1)
	c_bb_t5001 += alt(ADD)

	c_bb_t5001_mem0 = S.Task('c_bb_t5001_mem0', length=1, delay_cost=1)
	c_bb_t5001_mem0 += INPUT_mem_r
	S += c_bb_t5001_mem0 <= c_bb_t5001

	c_bb_t5001_mem1 = S.Task('c_bb_t5001_mem1', length=1, delay_cost=1)
	c_bb_t5001_mem1 += INPUT_mem_r
	S += c_bb_t5001_mem1 <= c_bb_t5001

	c_bb_t5010 = S.Task('c_bb_t5010', length=1, delay_cost=1)
	c_bb_t5010 += alt(ADD)

	c_bb_t5010_mem0 = S.Task('c_bb_t5010_mem0', length=1, delay_cost=1)
	c_bb_t5010_mem0 += INPUT_mem_r
	S += c_bb_t5010_mem0 <= c_bb_t5010

	c_bb_t5010_mem1 = S.Task('c_bb_t5010_mem1', length=1, delay_cost=1)
	c_bb_t5010_mem1 += INPUT_mem_r
	S += c_bb_t5010_mem1 <= c_bb_t5010

	c_bb_t5011 = S.Task('c_bb_t5011', length=1, delay_cost=1)
	c_bb_t5011 += alt(ADD)

	c_bb_t5011_mem0 = S.Task('c_bb_t5011_mem0', length=1, delay_cost=1)
	c_bb_t5011_mem0 += INPUT_mem_r
	S += c_bb_t5011_mem0 <= c_bb_t5011

	c_bb_t5011_mem1 = S.Task('c_bb_t5011_mem1', length=1, delay_cost=1)
	c_bb_t5011_mem1 += INPUT_mem_r
	S += c_bb_t5011_mem1 <= c_bb_t5011

	c_bb_t5100 = S.Task('c_bb_t5100', length=1, delay_cost=1)
	c_bb_t5100 += alt(ADD)

	c_bb_t5100_mem0 = S.Task('c_bb_t5100_mem0', length=1, delay_cost=1)
	c_bb_t5100_mem0 += INPUT_mem_r
	S += c_bb_t5100_mem0 <= c_bb_t5100

	c_bb_t5100_mem1 = S.Task('c_bb_t5100_mem1', length=1, delay_cost=1)
	c_bb_t5100_mem1 += INPUT_mem_r
	S += c_bb_t5100_mem1 <= c_bb_t5100

	c_bb_t5101 = S.Task('c_bb_t5101', length=1, delay_cost=1)
	c_bb_t5101 += alt(ADD)

	c_bb_t5101_mem0 = S.Task('c_bb_t5101_mem0', length=1, delay_cost=1)
	c_bb_t5101_mem0 += INPUT_mem_r
	S += c_bb_t5101_mem0 <= c_bb_t5101

	c_bb_t5101_mem1 = S.Task('c_bb_t5101_mem1', length=1, delay_cost=1)
	c_bb_t5101_mem1 += INPUT_mem_r
	S += c_bb_t5101_mem1 <= c_bb_t5101

	c_bb_t5110 = S.Task('c_bb_t5110', length=1, delay_cost=1)
	c_bb_t5110 += alt(ADD)

	c_bb_t5110_mem0 = S.Task('c_bb_t5110_mem0', length=1, delay_cost=1)
	c_bb_t5110_mem0 += INPUT_mem_r
	S += c_bb_t5110_mem0 <= c_bb_t5110

	c_bb_t5110_mem1 = S.Task('c_bb_t5110_mem1', length=1, delay_cost=1)
	c_bb_t5110_mem1 += INPUT_mem_r
	S += c_bb_t5110_mem1 <= c_bb_t5110

	c_bb_t5111 = S.Task('c_bb_t5111', length=1, delay_cost=1)
	c_bb_t5111 += alt(ADD)

	c_bb_t5111_mem0 = S.Task('c_bb_t5111_mem0', length=1, delay_cost=1)
	c_bb_t5111_mem0 += INPUT_mem_r
	S += c_bb_t5111_mem0 <= c_bb_t5111

	c_bb_t5111_mem1 = S.Task('c_bb_t5111_mem1', length=1, delay_cost=1)
	c_bb_t5111_mem1 += INPUT_mem_r
	S += c_bb_t5111_mem1 <= c_bb_t5111

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/INV_mul1_add4/INV_3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

