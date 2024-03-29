from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 129
	S = Scenario("PDBL_2", horizon=horizon)

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
	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 0
	t10_t1_in += MUL_in[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 0
	t10_t1_mem0 += INPUT_mem_r

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 0
	t10_t1_mem1 += INPUT_mem_r

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 1
	t10_t0_in += MUL_in[0]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 1
	t10_t0_mem0 += INPUT_mem_r

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 1
	t10_t0_mem1 += INPUT_mem_r

	t10_t1 = S.Task('t10_t1', length=7, delay_cost=1)
	S += t10_t1 >= 1
	t10_t1 += MUL[0]

	t10_t0 = S.Task('t10_t0', length=7, delay_cost=1)
	S += t10_t0 >= 2
	t10_t0 += MUL[0]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 2
	t1_t3_in += MUL_in[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 2
	t1_t3_mem0 += INPUT_mem_r

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 2
	t1_t3_mem1 += INPUT_mem_r

	t1_t3 = S.Task('t1_t3', length=7, delay_cost=1)
	S += t1_t3 >= 3
	t1_t3 += MUL[0]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 3
	t5_t1_in += MUL_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 3
	t5_t1_mem0 += INPUT_mem_r

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 3
	t5_t1_mem1 += INPUT_mem_r

	t5_t1 = S.Task('t5_t1', length=7, delay_cost=1)
	S += t5_t1 >= 4
	t5_t1 += MUL[0]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 4
	t7_t3_in += MUL_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 4
	t7_t3_mem0 += INPUT_mem_r

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 4
	t7_t3_mem1 += INPUT_mem_r

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 5
	t5_t0_in += MUL_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 5
	t5_t0_mem0 += INPUT_mem_r

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 5
	t5_t0_mem1 += INPUT_mem_r

	t7_t3 = S.Task('t7_t3', length=7, delay_cost=1)
	S += t7_t3 >= 5
	t7_t3 += MUL[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 6
	t0_t3_in += MUL_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 6
	t0_t3_mem0 += INPUT_mem_r

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 6
	t0_t3_mem1 += INPUT_mem_r

	t5_t0 = S.Task('t5_t0', length=7, delay_cost=1)
	S += t5_t0 >= 6
	t5_t0 += MUL[0]

	t0_t3 = S.Task('t0_t3', length=7, delay_cost=1)
	S += t0_t3 >= 7
	t0_t3 += MUL[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 7
	t2_t2_mem0 += INPUT_mem_r

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 7
	t2_t2_mem1 += INPUT_mem_r

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 8
	t100_mem0 += MUL_mem[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 8
	t100_mem1 += MUL_mem[0]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 8
	t2_t2 += ADD[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 8
	t5_t3_mem0 += INPUT_mem_r

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 8
	t5_t3_mem1 += INPUT_mem_r

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 9
	t100 += ADD[1]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 9
	t110_mem0 += ADD_mem[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 9
	t11_mem0 += MUL_mem[0]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 9
	t1_t5_mem0 += MUL_mem[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 9
	t5_t2_mem0 += INPUT_mem_r

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 9
	t5_t2_mem1 += INPUT_mem_r

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	S += t5_t3 >= 9
	t5_t3 += ADD[0]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 10
	t10_t5_mem0 += MUL_mem[0]

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	S += t10_t5_mem1 >= 10
	t10_t5_mem1 += MUL_mem[0]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 10
	t11 += ADD[1]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 10
	t110 += ADD[3]

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	S += t1_t5 >= 10
	t1_t5 += ADD[2]

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	S += t5_t2 >= 10
	t5_t2 += ADD[0]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 10
	t5_t4_in += MUL_in[0]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 10
	t5_t4_mem0 += ADD_mem[0]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 10
	t5_t4_mem1 += ADD_mem[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 10
	t7_t0_mem0 += INPUT_mem_r

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 10
	t7_t0_mem1 += INPUT_mem_r

	t10_t5 = S.Task('t10_t5', length=1, delay_cost=1)
	S += t10_t5 >= 11
	t10_t5 += ADD[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 11
	t1_t1_mem0 += INPUT_mem_r

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 11
	t1_t1_mem1 += INPUT_mem_r

	t5_t4 = S.Task('t5_t4', length=7, delay_cost=1)
	S += t5_t4 >= 11
	t5_t4 += MUL[0]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 11
	t71_mem0 += MUL_mem[0]

	t7_t0 = S.Task('t7_t0', length=1, delay_cost=1)
	S += t7_t0 >= 11
	t7_t0 += ADD[1]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 11
	t7_t5_mem0 += MUL_mem[0]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 12
	t10_t2_mem0 += INPUT_mem_r

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 12
	t10_t2_mem1 += INPUT_mem_r

	t1_t1 = S.Task('t1_t1', length=1, delay_cost=1)
	S += t1_t1 >= 12
	t1_t1 += ADD[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 12
	t50_mem0 += MUL_mem[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 12
	t50_mem1 += MUL_mem[0]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 12
	t71 += ADD[2]

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	S += t7_t5 >= 12
	t7_t5 += ADD[1]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 12
	t81_mem0 += ADD_mem[2]

	t10_t2 = S.Task('t10_t2', length=1, delay_cost=1)
	S += t10_t2 >= 13
	t10_t2 += ADD[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 13
	t1_t0_mem0 += INPUT_mem_r

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 13
	t1_t0_mem1 += INPUT_mem_r

	t50 = S.Task('t50', length=1, delay_cost=1)
	S += t50 >= 13
	t50 += ADD[1]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 13
	t5_t5_mem0 += MUL_mem[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 13
	t5_t5_mem1 += MUL_mem[0]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 13
	t60_mem0 += ADD_mem[1]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 13
	t81 += ADD[2]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 13
	t91_mem0 += ADD_mem[2]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 13
	t91_mem1 += ADD_mem[2]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 14
	t01_mem0 += MUL_mem[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 14
	t0_t5_mem0 += MUL_mem[0]

	t1_t0 = S.Task('t1_t0', length=1, delay_cost=1)
	S += t1_t0 >= 14
	t1_t0 += ADD[2]

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	S += t1_t2_in >= 14
	t1_t2_in += MUL_in[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 14
	t1_t2_mem0 += ADD_mem[2]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 14
	t1_t2_mem1 += ADD_mem[0]

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 14
	t5_t5 += ADD[3]

	t60 = S.Task('t60', length=1, delay_cost=1)
	S += t60 >= 14
	t60 += ADD[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 14
	t7_t1_mem0 += INPUT_mem_r

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 14
	t7_t1_mem1 += INPUT_mem_r

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 14
	t91 += ADD[1]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 15
	t01 += ADD[1]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 15
	t0_t5 += ADD[3]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 15
	t10_t3_mem0 += INPUT_mem_r

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 15
	t10_t3_mem1 += INPUT_mem_r

	t1_t2 = S.Task('t1_t2', length=7, delay_cost=1)
	S += t1_t2 >= 15
	t1_t2 += MUL[0]

	t7_t1 = S.Task('t7_t1', length=1, delay_cost=1)
	S += t7_t1 >= 15
	t7_t1 += ADD[0]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 15
	t7_t2_in += MUL_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 15
	t7_t2_mem0 += ADD_mem[1]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 15
	t7_t2_mem1 += ADD_mem[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 16
	t0_t0_mem0 += INPUT_mem_r

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 16
	t0_t0_mem1 += INPUT_mem_r

	t10_t3 = S.Task('t10_t3', length=1, delay_cost=1)
	S += t10_t3 >= 16
	t10_t3 += ADD[2]

	t10_t4_in = S.Task('t10_t4_in', length=1, delay_cost=1)
	S += t10_t4_in >= 16
	t10_t4_in += MUL_in[0]

	t10_t4_mem0 = S.Task('t10_t4_mem0', length=1, delay_cost=1)
	S += t10_t4_mem0 >= 16
	t10_t4_mem0 += ADD_mem[0]

	t10_t4_mem1 = S.Task('t10_t4_mem1', length=1, delay_cost=1)
	S += t10_t4_mem1 >= 16
	t10_t4_mem1 += ADD_mem[2]

	t7_t2 = S.Task('t7_t2', length=7, delay_cost=1)
	S += t7_t2 >= 16
	t7_t2 += MUL[0]

	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	S += t0_t0 >= 17
	t0_t0 += ADD[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 17
	t0_t1_mem0 += INPUT_mem_r

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 17
	t0_t1_mem1 += INPUT_mem_r

	t10_t4 = S.Task('t10_t4', length=7, delay_cost=1)
	S += t10_t4 >= 17
	t10_t4 += MUL[0]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 17
	t51_mem0 += MUL_mem[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 17
	t51_mem1 += ADD_mem[3]

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	S += t0_t1 >= 18
	t0_t1 += ADD[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 18
	t0_t2_in += MUL_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 18
	t0_t2_mem0 += ADD_mem[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 18
	t0_t2_mem1 += ADD_mem[1]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 18
	t51 += ADD[0]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 18
	t61_mem0 += ADD_mem[0]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 19
	new_TX_t3_mem0 += ADD_mem[0]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 19
	new_TX_t3_mem1 += ADD_mem[0]

	t0_t2 = S.Task('t0_t2', length=7, delay_cost=1)
	S += t0_t2 >= 19
	t0_t2 += MUL[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 19
	t2_t1_in += MUL_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 19
	t2_t1_mem0 += INPUT_mem_r

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 19
	t2_t1_mem1 += ADD_mem[1]

	t61 = S.Task('t61', length=1, delay_cost=1)
	S += t61 >= 19
	t61 += ADD[0]

	new_TX_t3 = S.Task('new_TX_t3', length=1, delay_cost=1)
	S += new_TX_t3 >= 20
	new_TX_t3 += ADD[3]

	t2_t1 = S.Task('t2_t1', length=7, delay_cost=1)
	S += t2_t1 >= 20
	t2_t1 += MUL[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 21
	t10_mem0 += MUL_mem[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 21
	t10_mem1 += ADD_mem[2]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 22
	t10 += ADD[0]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 22
	t2_t0_in += MUL_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 22
	t2_t0_mem0 += INPUT_mem_r

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 22
	t2_t0_mem1 += ADD_mem[0]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 22
	t2_t3_mem0 += ADD_mem[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 22
	t2_t3_mem1 += ADD_mem[1]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 22
	t70_mem0 += MUL_mem[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 22
	t70_mem1 += ADD_mem[1]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 23
	t101_mem0 += MUL_mem[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 23
	t101_mem1 += ADD_mem[0]

	t2_t0 = S.Task('t2_t0', length=7, delay_cost=1)
	S += t2_t0 >= 23
	t2_t0 += MUL[0]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 23
	t2_t3 += ADD[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 23
	t2_t4_in += MUL_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 23
	t2_t4_mem0 += ADD_mem[0]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 23
	t2_t4_mem1 += ADD_mem[1]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 23
	t70 += ADD[3]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 23
	t80_mem0 += ADD_mem[3]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 24
	t101 += ADD[1]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 24
	t111_mem0 += ADD_mem[1]

	t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
	S += t2_t4 >= 24
	t2_t4 += MUL[0]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 24
	t80 += ADD[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 24
	t90_mem0 += ADD_mem[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 24
	t90_mem1 += ADD_mem[3]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 25
	t00_mem0 += MUL_mem[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 25
	t00_mem1 += ADD_mem[3]

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 25
	t111 += ADD[0]

	t12_t1_in = S.Task('t12_t1_in', length=1, delay_cost=1)
	S += t12_t1_in >= 25
	t12_t1_in += MUL_in[0]

	t12_t1_mem0 = S.Task('t12_t1_mem0', length=1, delay_cost=1)
	S += t12_t1_mem0 >= 25
	t12_t1_mem0 += ADD_mem[1]

	t12_t1_mem1 = S.Task('t12_t1_mem1', length=1, delay_cost=1)
	S += t12_t1_mem1 >= 25
	t12_t1_mem1 += ADD_mem[0]

	t12_t3_mem0 = S.Task('t12_t3_mem0', length=1, delay_cost=1)
	S += t12_t3_mem0 >= 25
	t12_t3_mem0 += ADD_mem[3]

	t12_t3_mem1 = S.Task('t12_t3_mem1', length=1, delay_cost=1)
	S += t12_t3_mem1 >= 25
	t12_t3_mem1 += ADD_mem[0]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 25
	t90 += ADD[2]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 26
	t00 += ADD[2]

	t12_t0_in = S.Task('t12_t0_in', length=1, delay_cost=1)
	S += t12_t0_in >= 26
	t12_t0_in += MUL_in[0]

	t12_t0_mem0 = S.Task('t12_t0_mem0', length=1, delay_cost=1)
	S += t12_t0_mem0 >= 26
	t12_t0_mem0 += ADD_mem[2]

	t12_t0_mem1 = S.Task('t12_t0_mem1', length=1, delay_cost=1)
	S += t12_t0_mem1 >= 26
	t12_t0_mem1 += ADD_mem[3]

	t12_t1 = S.Task('t12_t1', length=7, delay_cost=1)
	S += t12_t1 >= 26
	t12_t1 += MUL[0]

	t12_t2_mem0 = S.Task('t12_t2_mem0', length=1, delay_cost=1)
	S += t12_t2_mem0 >= 26
	t12_t2_mem0 += ADD_mem[2]

	t12_t2_mem1 = S.Task('t12_t2_mem1', length=1, delay_cost=1)
	S += t12_t2_mem1 >= 26
	t12_t2_mem1 += ADD_mem[1]

	t12_t3 = S.Task('t12_t3', length=1, delay_cost=1)
	S += t12_t3 >= 26
	t12_t3 += ADD[3]

	t12_t0 = S.Task('t12_t0', length=7, delay_cost=1)
	S += t12_t0 >= 27
	t12_t0 += MUL[0]

	t12_t2 = S.Task('t12_t2', length=1, delay_cost=1)
	S += t12_t2 >= 27
	t12_t2 += ADD[0]

	t12_t4_in = S.Task('t12_t4_in', length=1, delay_cost=1)
	S += t12_t4_in >= 27
	t12_t4_in += MUL_in[0]

	t12_t4_mem0 = S.Task('t12_t4_mem0', length=1, delay_cost=1)
	S += t12_t4_mem0 >= 27
	t12_t4_mem0 += ADD_mem[0]

	t12_t4_mem1 = S.Task('t12_t4_mem1', length=1, delay_cost=1)
	S += t12_t4_mem1 >= 27
	t12_t4_mem1 += ADD_mem[3]

	t18_t0_mem0 = S.Task('t18_t0_mem0', length=1, delay_cost=1)
	S += t18_t0_mem0 >= 27
	t18_t0_mem0 += ADD_mem[2]

	t18_t0_mem1 = S.Task('t18_t0_mem1', length=1, delay_cost=1)
	S += t18_t0_mem1 >= 27
	t18_t0_mem1 += ADD_mem[1]

	t18_t1_mem0 = S.Task('t18_t1_mem0', length=1, delay_cost=1)
	S += t18_t1_mem0 >= 27
	t18_t1_mem0 += ADD_mem[2]

	t18_t1_mem1 = S.Task('t18_t1_mem1', length=1, delay_cost=1)
	S += t18_t1_mem1 >= 27
	t18_t1_mem1 += ADD_mem[1]

	t12_t4 = S.Task('t12_t4', length=7, delay_cost=1)
	S += t12_t4 >= 28
	t12_t4 += MUL[0]

	t18_t0 = S.Task('t18_t0', length=1, delay_cost=1)
	S += t18_t0 >= 28
	t18_t0 += ADD[3]

	t18_t1 = S.Task('t18_t1', length=1, delay_cost=1)
	S += t18_t1 >= 28
	t18_t1 += ADD[0]

	t18_t3_in = S.Task('t18_t3_in', length=1, delay_cost=1)
	S += t18_t3_in >= 28
	t18_t3_in += MUL_in[0]

	t18_t3_mem0 = S.Task('t18_t3_mem0', length=1, delay_cost=1)
	S += t18_t3_mem0 >= 28
	t18_t3_mem0 += ADD_mem[2]

	t18_t3_mem1 = S.Task('t18_t3_mem1', length=1, delay_cost=1)
	S += t18_t3_mem1 >= 28
	t18_t3_mem1 += ADD_mem[1]

	t18_t2_in = S.Task('t18_t2_in', length=1, delay_cost=1)
	S += t18_t2_in >= 29
	t18_t2_in += MUL_in[0]

	t18_t2_mem0 = S.Task('t18_t2_mem0', length=1, delay_cost=1)
	S += t18_t2_mem0 >= 29
	t18_t2_mem0 += ADD_mem[3]

	t18_t2_mem1 = S.Task('t18_t2_mem1', length=1, delay_cost=1)
	S += t18_t2_mem1 >= 29
	t18_t2_mem1 += ADD_mem[0]

	t18_t3 = S.Task('t18_t3', length=7, delay_cost=1)
	S += t18_t3 >= 29
	t18_t3 += MUL[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 29
	t20_mem0 += MUL_mem[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 29
	t20_mem1 += MUL_mem[0]

	t18_t2 = S.Task('t18_t2', length=7, delay_cost=1)
	S += t18_t2 >= 30
	t18_t2 += MUL[0]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 30
	t20 += ADD[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 30
	t2_t5_mem0 += MUL_mem[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 30
	t2_t5_mem1 += MUL_mem[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 30
	t30_mem0 += ADD_mem[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 31
	t21_mem0 += MUL_mem[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 31
	t21_mem1 += ADD_mem[0]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 31
	t2_t5 += ADD[0]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 31
	t30 += ADD[2]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 31
	t40_mem0 += ADD_mem[2]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 31
	t40_mem1 += ADD_mem[0]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 32
	c000_mem0 += ADD_mem[2]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 32
	c000_mem1 += ADD_mem[1]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 32
	t140_mem0 += ADD_mem[1]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 32
	t21 += ADD[2]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 32
	t31_mem0 += ADD_mem[2]

	t40 = S.Task('t40', length=1, delay_cost=1)
	S += t40 >= 32
	t40 += ADD[1]

	c000 = S.Task('c000', length=1, delay_cost=1)
	S += c000 >= 33
	c000 += ADD[3]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 33
	t120_mem0 += MUL_mem[0]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 33
	t120_mem1 += MUL_mem[0]

	t140 = S.Task('t140', length=1, delay_cost=1)
	S += t140 >= 33
	t140 += ADD[0]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 33
	t150_mem0 += ADD_mem[3]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 33
	t150_mem1 += ADD_mem[0]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 33
	t160_mem0 += ADD_mem[2]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 33
	t160_mem1 += ADD_mem[3]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 33
	t31 += ADD[1]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 33
	t41_mem0 += ADD_mem[1]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 33
	t41_mem1 += ADD_mem[2]

	b30_mem0 = S.Task('b30_mem0', length=1, delay_cost=1)
	S += b30_mem0 >= 34
	b30_mem0 += ADD_mem[0]

	b30_mem1 = S.Task('b30_mem1', length=1, delay_cost=1)
	S += b30_mem1 >= 34
	b30_mem1 += ADD_mem[1]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 34
	c001_mem0 += ADD_mem[1]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 34
	c001_mem1 += ADD_mem[3]

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 34
	new_TX_t0_in += MUL_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 34
	new_TX_t0_mem0 += ADD_mem[2]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 34
	new_TX_t0_mem1 += ADD_mem[0]

	t120 = S.Task('t120', length=1, delay_cost=1)
	S += t120 >= 34
	t120 += ADD[1]

	t12_t5_mem0 = S.Task('t12_t5_mem0', length=1, delay_cost=1)
	S += t12_t5_mem0 >= 34
	t12_t5_mem0 += MUL_mem[0]

	t12_t5_mem1 = S.Task('t12_t5_mem1', length=1, delay_cost=1)
	S += t12_t5_mem1 >= 34
	t12_t5_mem1 += MUL_mem[0]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 34
	t141_mem0 += ADD_mem[3]

	t150 = S.Task('t150', length=1, delay_cost=1)
	S += t150 >= 34
	t150 += ADD[2]

	t160 = S.Task('t160', length=1, delay_cost=1)
	S += t160 >= 34
	t160 += ADD[0]

	t41 = S.Task('t41', length=1, delay_cost=1)
	S += t41 >= 34
	t41 += ADD[3]

	b30 = S.Task('b30', length=1, delay_cost=1)
	S += b30 >= 35
	b30 += ADD[3]

	b31_mem0 = S.Task('b31_mem0', length=1, delay_cost=1)
	S += b31_mem0 >= 35
	b31_mem0 += ADD_mem[2]

	b31_mem1 = S.Task('b31_mem1', length=1, delay_cost=1)
	S += b31_mem1 >= 35
	b31_mem1 += ADD_mem[3]

	c001 = S.Task('c001', length=1, delay_cost=1)
	S += c001 >= 35
	c001 += ADD[1]

	new_TX_t0 = S.Task('new_TX_t0', length=7, delay_cost=1)
	S += new_TX_t0 >= 35
	new_TX_t0 += MUL[0]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 35
	t121_mem0 += MUL_mem[0]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 35
	t121_mem1 += ADD_mem[0]

	t12_t5 = S.Task('t12_t5', length=1, delay_cost=1)
	S += t12_t5 >= 35
	t12_t5 += ADD[0]

	t141 = S.Task('t141', length=1, delay_cost=1)
	S += t141 >= 35
	t141 += ADD[2]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 35
	t161_mem0 += ADD_mem[1]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 35
	t161_mem1 += ADD_mem[1]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 35
	t17_t0_in += MUL_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 35
	t17_t0_mem0 += ADD_mem[3]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 35
	t17_t0_mem1 += ADD_mem[0]

	t18_t5_mem0 = S.Task('t18_t5_mem0', length=1, delay_cost=1)
	S += t18_t5_mem0 >= 35
	t18_t5_mem0 += MUL_mem[0]

	b31 = S.Task('b31', length=1, delay_cost=1)
	S += b31 >= 36
	b31 += ADD[0]

	t121 = S.Task('t121', length=1, delay_cost=1)
	S += t121 >= 36
	t121 += ADD[2]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 36
	t131_mem0 += ADD_mem[2]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	S += t151_mem0 >= 36
	t151_mem0 += ADD_mem[1]

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	S += t151_mem1 >= 36
	t151_mem1 += ADD_mem[2]

	t161 = S.Task('t161', length=1, delay_cost=1)
	S += t161 >= 36
	t161 += ADD[3]

	t17_t0 = S.Task('t17_t0', length=7, delay_cost=1)
	S += t17_t0 >= 36
	t17_t0 += MUL[0]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	S += t180_mem0 >= 36
	t180_mem0 += MUL_mem[0]

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	S += t180_mem1 >= 36
	t180_mem1 += ADD_mem[1]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 36
	t181_mem0 += MUL_mem[0]

	t18_t5 = S.Task('t18_t5', length=1, delay_cost=1)
	S += t18_t5 >= 36
	t18_t5 += ADD[1]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 37
	t130_mem0 += ADD_mem[1]

	t131 = S.Task('t131', length=1, delay_cost=1)
	S += t131 >= 37
	t131 += ADD[2]

	t151 = S.Task('t151', length=1, delay_cost=1)
	S += t151 >= 37
	t151 += ADD[3]

	t180 = S.Task('t180', length=1, delay_cost=1)
	S += t180 >= 37
	t180 += ADD[1]

	t181 = S.Task('t181', length=1, delay_cost=1)
	S += t181 >= 37
	t181 += ADD[0]

	t130 = S.Task('t130', length=1, delay_cost=1)
	S += t130 >= 38
	t130 += ADD[3]


	# new tasks
	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	new_TX_t1_in += alt(MUL_in)
	new_TX_t1 = S.Task('new_TX_t1', length=7, delay_cost=1)
	new_TX_t1 += alt(MUL)
	S += new_TX_t1>=new_TX_t1_in

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	new_TX_t1_mem0 += ADD_mem[3]
	S += 37 < new_TX_t1_mem0
	S += new_TX_t1_mem0 <= new_TX_t1

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	new_TX_t1_mem1 += ADD_mem[0]
	S += 19 < new_TX_t1_mem1
	S += new_TX_t1_mem1 <= new_TX_t1

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	new_TX_t2 += alt(ADD)

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	new_TX_t2_mem0 += ADD_mem[2]
	S += 34 < new_TX_t2_mem0
	S += new_TX_t2_mem0 <= new_TX_t2

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	new_TX_t2_mem1 += ADD_mem[3]
	S += 37 < new_TX_t2_mem1
	S += new_TX_t2_mem1 <= new_TX_t2

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	t17_t1_in += alt(MUL_in)
	t17_t1 = S.Task('t17_t1', length=7, delay_cost=1)
	t17_t1 += alt(MUL)
	S += t17_t1>=t17_t1_in

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	t17_t1_mem0 += ADD_mem[0]
	S += 36 < t17_t1_mem0
	S += t17_t1_mem0 <= t17_t1

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	t17_t1_mem1 += ADD_mem[3]
	S += 36 < t17_t1_mem1
	S += t17_t1_mem1 <= t17_t1

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	t17_t2 += alt(ADD)

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	t17_t2_mem0 += ADD_mem[3]
	S += 35 < t17_t2_mem0
	S += t17_t2_mem0 <= t17_t2

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	t17_t2_mem1 += ADD_mem[0]
	S += 36 < t17_t2_mem1
	S += t17_t2_mem1 <= t17_t2

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	t17_t3 += alt(ADD)

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	t17_t3_mem0 += ADD_mem[0]
	S += 34 < t17_t3_mem0
	S += t17_t3_mem0 <= t17_t3

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	t17_t3_mem1 += ADD_mem[3]
	S += 36 < t17_t3_mem1
	S += t17_t3_mem1 <= t17_t3

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	new_TX_t4_in += alt(MUL_in)
	new_TX_t4 = S.Task('new_TX_t4', length=7, delay_cost=1)
	new_TX_t4 += alt(MUL)
	S += new_TX_t4>=new_TX_t4_in

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	new_TX_t4_mem0 += alt(ADD_mem)
	S += (new_TX_t2*ADD[0])-1 < new_TX_t4_mem0*ADD_mem[0]
	S += (new_TX_t2*ADD[1])-1 < new_TX_t4_mem0*ADD_mem[1]
	S += (new_TX_t2*ADD[2])-1 < new_TX_t4_mem0*ADD_mem[2]
	S += (new_TX_t2*ADD[3])-1 < new_TX_t4_mem0*ADD_mem[3]
	S += new_TX_t4_mem0 <= new_TX_t4

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	new_TX_t4_mem1 += ADD_mem[3]
	S += 20 < new_TX_t4_mem1
	S += new_TX_t4_mem1 <= new_TX_t4

	new_TX_t5 = S.Task('new_TX_t5', length=1, delay_cost=1)
	new_TX_t5 += alt(ADD)

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	new_TX_t5_mem0 += MUL_mem[0]
	S += 41 < new_TX_t5_mem0
	S += new_TX_t5_mem0 <= new_TX_t5

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	new_TX_t5_mem1 += alt(MUL_mem)
	S += (new_TX_t1*MUL[0])-1 < new_TX_t5_mem1*MUL_mem[0]
	S += new_TX_t5_mem1 <= new_TX_t5

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	t17_t4_in += alt(MUL_in)
	t17_t4 = S.Task('t17_t4', length=7, delay_cost=1)
	t17_t4 += alt(MUL)
	S += t17_t4>=t17_t4_in

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	t17_t4_mem0 += alt(ADD_mem)
	S += (t17_t2*ADD[0])-1 < t17_t4_mem0*ADD_mem[0]
	S += (t17_t2*ADD[1])-1 < t17_t4_mem0*ADD_mem[1]
	S += (t17_t2*ADD[2])-1 < t17_t4_mem0*ADD_mem[2]
	S += (t17_t2*ADD[3])-1 < t17_t4_mem0*ADD_mem[3]
	S += t17_t4_mem0 <= t17_t4

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	t17_t4_mem1 += alt(ADD_mem)
	S += (t17_t3*ADD[0])-1 < t17_t4_mem1*ADD_mem[0]
	S += (t17_t3*ADD[1])-1 < t17_t4_mem1*ADD_mem[1]
	S += (t17_t3*ADD[2])-1 < t17_t4_mem1*ADD_mem[2]
	S += (t17_t3*ADD[3])-1 < t17_t4_mem1*ADD_mem[3]
	S += t17_t4_mem1 <= t17_t4

	t170 = S.Task('t170', length=1, delay_cost=1)
	t170 += alt(ADD)

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	t170_mem0 += MUL_mem[0]
	S += 42 < t170_mem0
	S += t170_mem0 <= t170

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	t170_mem1 += alt(MUL_mem)
	S += (t17_t1*MUL[0])-1 < t170_mem1*MUL_mem[0]
	S += t170_mem1 <= t170

	t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
	t17_t5 += alt(ADD)

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	t17_t5_mem0 += MUL_mem[0]
	S += 42 < t17_t5_mem0
	S += t17_t5_mem0 <= t17_t5

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	t17_t5_mem1 += alt(MUL_mem)
	S += (t17_t1*MUL[0])-1 < t17_t5_mem1*MUL_mem[0]
	S += t17_t5_mem1 <= t17_t5

	t171 = S.Task('t171', length=1, delay_cost=1)
	t171 += alt(ADD)

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += alt(MUL_mem)
	S += (t17_t4*MUL[0])-1 < t171_mem0*MUL_mem[0]
	S += t171_mem0 <= t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += alt(ADD_mem)
	S += (t17_t5*ADD[0])-1 < t171_mem1*ADD_mem[0]
	S += (t17_t5*ADD[1])-1 < t171_mem1*ADD_mem[1]
	S += (t17_t5*ADD[2])-1 < t171_mem1*ADD_mem[2]
	S += (t17_t5*ADD[3])-1 < t171_mem1*ADD_mem[3]
	S += t171_mem1 <= t171

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MUL_in)
	c010 = S.Task('c010', length=7, delay_cost=1)
	c010 += alt(MUL)
	S += c010>=c010_in

	S += 0<c010

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += ADD_mem[3]
	S += 10 < c010_mem0
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += INPUT_mem_r
	S += c010_mem1 <= c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(INPUT_mem_w)
	S += c010-1 <= c010_w

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MUL_in)
	c011 = S.Task('c011', length=7, delay_cost=1)
	c011 += alt(MUL)
	S += c011>=c011_in

	S += 0<c011

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += ADD_mem[0]
	S += 25 < c011_mem0
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += INPUT_mem_r
	S += c011_mem1 <= c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(INPUT_mem_w)
	S += c011-1 <= c011_w

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MUL_in)
	c201 = S.Task('c201', length=7, delay_cost=1)
	c201 += alt(MUL)
	S += c201>=c201_in

	S += 0<c201

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += ADD_mem[1]
	S += 14 < c201_mem0
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += INPUT_mem_r
	S += c201_mem1 <= c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(INPUT_mem_w)
	S += c201-1 <= c201_w

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MUL_in)
	c200 = S.Task('c200', length=7, delay_cost=1)
	c200 += alt(MUL)
	S += c200>=c200_in

	S += 0<c200

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += ADD_mem[2]
	S += 25 < c200_mem0
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += INPUT_mem_r
	S += c200_mem1 <= c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(INPUT_mem_w)
	S += c200-1 <= c200_w

	new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
	new_TZ0 += alt(ADD)

	S += 16<new_TZ0

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	new_TZ0_mem0 += ADD_mem[3]
	S += 38 < new_TZ0_mem0
	S += new_TZ0_mem0 <= new_TZ0

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	new_TZ0_w += alt(INPUT_mem_w)
	S += new_TZ0-1 <= new_TZ0_w

	new_TZ1 = S.Task('new_TZ1', length=1, delay_cost=1)
	new_TZ1 += alt(ADD)

	S += 16<new_TZ1

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	new_TZ1_mem0 += ADD_mem[2]
	S += 37 < new_TZ1_mem0
	S += new_TZ1_mem0 <= new_TZ1

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	new_TZ1_w += alt(INPUT_mem_w)
	S += new_TZ1-1 <= new_TZ1_w

	new_TX0 = S.Task('new_TX0', length=1, delay_cost=1)
	new_TX0 += alt(ADD)

	S += 15<new_TX0

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	new_TX0_mem0 += MUL_mem[0]
	S += 41 < new_TX0_mem0
	S += new_TX0_mem0 <= new_TX0

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	new_TX0_mem1 += alt(MUL_mem)
	S += (new_TX_t1*MUL[0])-1 < new_TX0_mem1*MUL_mem[0]
	S += new_TX0_mem1 <= new_TX0

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	new_TX0_w += alt(INPUT_mem_w)
	S += new_TX0-1 <= new_TX0_w

	new_TX1 = S.Task('new_TX1', length=1, delay_cost=1)
	new_TX1 += alt(ADD)

	S += 15<new_TX1

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	new_TX1_mem0 += alt(MUL_mem)
	S += (new_TX_t4*MUL[0])-1 < new_TX1_mem0*MUL_mem[0]
	S += new_TX1_mem0 <= new_TX1

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	new_TX1_mem1 += alt(ADD_mem)
	S += (new_TX_t5*ADD[0])-1 < new_TX1_mem1*ADD_mem[0]
	S += (new_TX_t5*ADD[1])-1 < new_TX1_mem1*ADD_mem[1]
	S += (new_TX_t5*ADD[2])-1 < new_TX1_mem1*ADD_mem[2]
	S += (new_TX_t5*ADD[3])-1 < new_TX1_mem1*ADD_mem[3]
	S += new_TX1_mem1 <= new_TX1

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	new_TX1_w += alt(INPUT_mem_w)
	S += new_TX1-1 <= new_TX1_w

	new_TY0 = S.Task('new_TY0', length=1, delay_cost=1)
	new_TY0 += alt(ADD)

	S += 18<new_TY0

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += alt(ADD_mem)
	S += (t170*ADD[0])-1 < new_TY0_mem0*ADD_mem[0]
	S += (t170*ADD[1])-1 < new_TY0_mem0*ADD_mem[1]
	S += (t170*ADD[2])-1 < new_TY0_mem0*ADD_mem[2]
	S += (t170*ADD[3])-1 < new_TY0_mem0*ADD_mem[3]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += ADD_mem[1]
	S += 37 < new_TY0_mem1
	S += new_TY0_mem1 <= new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(INPUT_mem_w)
	S += new_TY0-1 <= new_TY0_w

	new_TY1 = S.Task('new_TY1', length=1, delay_cost=1)
	new_TY1 += alt(ADD)

	S += 18<new_TY1

	new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
	new_TY1_mem0 += alt(ADD_mem)
	S += (t171*ADD[0])-1 < new_TY1_mem0*ADD_mem[0]
	S += (t171*ADD[1])-1 < new_TY1_mem0*ADD_mem[1]
	S += (t171*ADD[2])-1 < new_TY1_mem0*ADD_mem[2]
	S += (t171*ADD[3])-1 < new_TY1_mem0*ADD_mem[3]
	S += new_TY1_mem0 <= new_TY1

	new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
	new_TY1_mem1 += ADD_mem[0]
	S += 37 < new_TY1_mem1
	S += new_TY1_mem1 <= new_TY1

	new_TY1_w = S.Task('new_TY1_w', length=1, delay_cost=1)
	new_TY1_w += alt(INPUT_mem_w)
	S += new_TY1-1 <= new_TY1_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls12-1150/scheduling/PDBL_mul1_add4/PDBL_2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

