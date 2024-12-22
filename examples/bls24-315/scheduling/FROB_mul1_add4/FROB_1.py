from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 121
	S = Scenario("FROB_1", horizon=horizon)

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
	c_f111_t1_in = S.Task('c_f111_t1_in', length=1, delay_cost=1)
	S += c_f111_t1_in >= 0
	c_f111_t1_in += MUL_in[0]

	c_f111_t1_mem0 = S.Task('c_f111_t1_mem0', length=1, delay_cost=1)
	S += c_f111_t1_mem0 >= 0
	c_f111_t1_mem0 += INPUT_mem_r

	c_f111_t1_mem1 = S.Task('c_f111_t1_mem1', length=1, delay_cost=1)
	S += c_f111_t1_mem1 >= 0
	c_f111_t1_mem1 += INPUT_mem_r

	c_f111_t1 = S.Task('c_f111_t1', length=7, delay_cost=1)
	S += c_f111_t1 >= 1
	c_f111_t1 += MUL[0]

	c_f121_t0_in = S.Task('c_f121_t0_in', length=1, delay_cost=1)
	S += c_f121_t0_in >= 1
	c_f121_t0_in += MUL_in[0]

	c_f121_t0_mem0 = S.Task('c_f121_t0_mem0', length=1, delay_cost=1)
	S += c_f121_t0_mem0 >= 1
	c_f121_t0_mem0 += INPUT_mem_r

	c_f121_t0_mem1 = S.Task('c_f121_t0_mem1', length=1, delay_cost=1)
	S += c_f121_t0_mem1 >= 1
	c_f121_t0_mem1 += INPUT_mem_r

	c_f011_t0_in = S.Task('c_f011_t0_in', length=1, delay_cost=1)
	S += c_f011_t0_in >= 2
	c_f011_t0_in += MUL_in[0]

	c_f011_t0_mem0 = S.Task('c_f011_t0_mem0', length=1, delay_cost=1)
	S += c_f011_t0_mem0 >= 2
	c_f011_t0_mem0 += INPUT_mem_r

	c_f011_t0_mem1 = S.Task('c_f011_t0_mem1', length=1, delay_cost=1)
	S += c_f011_t0_mem1 >= 2
	c_f011_t0_mem1 += INPUT_mem_r

	c_f121_t0 = S.Task('c_f121_t0', length=7, delay_cost=1)
	S += c_f121_t0 >= 2
	c_f121_t0 += MUL[0]

	c10_t0_t1_in = S.Task('c10_t0_t1_in', length=1, delay_cost=1)
	S += c10_t0_t1_in >= 3
	c10_t0_t1_in += MUL_in[0]

	c10_t0_t1_mem0 = S.Task('c10_t0_t1_mem0', length=1, delay_cost=1)
	S += c10_t0_t1_mem0 >= 3
	c10_t0_t1_mem0 += INPUT_mem_r

	c10_t0_t1_mem1 = S.Task('c10_t0_t1_mem1', length=1, delay_cost=1)
	S += c10_t0_t1_mem1 >= 3
	c10_t0_t1_mem1 += INPUT_mem_r

	c_f011_t0 = S.Task('c_f011_t0', length=7, delay_cost=1)
	S += c_f011_t0 >= 3
	c_f011_t0 += MUL[0]

	c10_t0_t1 = S.Task('c10_t0_t1', length=7, delay_cost=1)
	S += c10_t0_t1 >= 4
	c10_t0_t1 += MUL[0]

	c_f011_t1_in = S.Task('c_f011_t1_in', length=1, delay_cost=1)
	S += c_f011_t1_in >= 4
	c_f011_t1_in += MUL_in[0]

	c_f011_t1_mem0 = S.Task('c_f011_t1_mem0', length=1, delay_cost=1)
	S += c_f011_t1_mem0 >= 4
	c_f011_t1_mem0 += INPUT_mem_r

	c_f011_t1_mem1 = S.Task('c_f011_t1_mem1', length=1, delay_cost=1)
	S += c_f011_t1_mem1 >= 4
	c_f011_t1_mem1 += INPUT_mem_r

	c10_t0_t0_in = S.Task('c10_t0_t0_in', length=1, delay_cost=1)
	S += c10_t0_t0_in >= 5
	c10_t0_t0_in += MUL_in[0]

	c10_t0_t0_mem0 = S.Task('c10_t0_t0_mem0', length=1, delay_cost=1)
	S += c10_t0_t0_mem0 >= 5
	c10_t0_t0_mem0 += INPUT_mem_r

	c10_t0_t0_mem1 = S.Task('c10_t0_t0_mem1', length=1, delay_cost=1)
	S += c10_t0_t0_mem1 >= 5
	c10_t0_t0_mem1 += INPUT_mem_r

	c_f011_t1 = S.Task('c_f011_t1', length=7, delay_cost=1)
	S += c_f011_t1 >= 5
	c_f011_t1 += MUL[0]

	c10_t0_t0 = S.Task('c10_t0_t0', length=7, delay_cost=1)
	S += c10_t0_t0 >= 6
	c10_t0_t0 += MUL[0]

	c_f101_t1_in = S.Task('c_f101_t1_in', length=1, delay_cost=1)
	S += c_f101_t1_in >= 6
	c_f101_t1_in += MUL_in[0]

	c_f101_t1_mem0 = S.Task('c_f101_t1_mem0', length=1, delay_cost=1)
	S += c_f101_t1_mem0 >= 6
	c_f101_t1_mem0 += INPUT_mem_r

	c_f101_t1_mem1 = S.Task('c_f101_t1_mem1', length=1, delay_cost=1)
	S += c_f101_t1_mem1 >= 6
	c_f101_t1_mem1 += INPUT_mem_r

	c001_t0_in = S.Task('c001_t0_in', length=1, delay_cost=1)
	S += c001_t0_in >= 7
	c001_t0_in += MUL_in[0]

	c001_t0_mem0 = S.Task('c001_t0_mem0', length=1, delay_cost=1)
	S += c001_t0_mem0 >= 7
	c001_t0_mem0 += INPUT_mem_r

	c001_t0_mem1 = S.Task('c001_t0_mem1', length=1, delay_cost=1)
	S += c001_t0_mem1 >= 7
	c001_t0_mem1 += INPUT_mem_r

	c_f101_t1 = S.Task('c_f101_t1', length=7, delay_cost=1)
	S += c_f101_t1 >= 7
	c_f101_t1 += MUL[0]

	c001_t0 = S.Task('c001_t0', length=7, delay_cost=1)
	S += c001_t0 >= 8
	c001_t0 += MUL[0]

	c_f021_t0_in = S.Task('c_f021_t0_in', length=1, delay_cost=1)
	S += c_f021_t0_in >= 8
	c_f021_t0_in += MUL_in[0]

	c_f021_t0_mem0 = S.Task('c_f021_t0_mem0', length=1, delay_cost=1)
	S += c_f021_t0_mem0 >= 8
	c_f021_t0_mem0 += INPUT_mem_r

	c_f021_t0_mem1 = S.Task('c_f021_t0_mem1', length=1, delay_cost=1)
	S += c_f021_t0_mem1 >= 8
	c_f021_t0_mem1 += INPUT_mem_r

	c_f021_t0 = S.Task('c_f021_t0', length=7, delay_cost=1)
	S += c_f021_t0 >= 9
	c_f021_t0 += MUL[0]

	c_f121_t1_in = S.Task('c_f121_t1_in', length=1, delay_cost=1)
	S += c_f121_t1_in >= 9
	c_f121_t1_in += MUL_in[0]

	c_f121_t1_mem0 = S.Task('c_f121_t1_mem0', length=1, delay_cost=1)
	S += c_f121_t1_mem0 >= 9
	c_f121_t1_mem0 += INPUT_mem_r

	c_f121_t1_mem1 = S.Task('c_f121_t1_mem1', length=1, delay_cost=1)
	S += c_f121_t1_mem1 >= 9
	c_f121_t1_mem1 += INPUT_mem_r

	c_f111_t0_in = S.Task('c_f111_t0_in', length=1, delay_cost=1)
	S += c_f111_t0_in >= 10
	c_f111_t0_in += MUL_in[0]

	c_f111_t0_mem0 = S.Task('c_f111_t0_mem0', length=1, delay_cost=1)
	S += c_f111_t0_mem0 >= 10
	c_f111_t0_mem0 += INPUT_mem_r

	c_f111_t0_mem1 = S.Task('c_f111_t0_mem1', length=1, delay_cost=1)
	S += c_f111_t0_mem1 >= 10
	c_f111_t0_mem1 += INPUT_mem_r

	c_f121_t1 = S.Task('c_f121_t1', length=7, delay_cost=1)
	S += c_f121_t1 >= 10
	c_f121_t1 += MUL[0]

	c_f101_t0_in = S.Task('c_f101_t0_in', length=1, delay_cost=1)
	S += c_f101_t0_in >= 11
	c_f101_t0_in += MUL_in[0]

	c_f101_t0_mem0 = S.Task('c_f101_t0_mem0', length=1, delay_cost=1)
	S += c_f101_t0_mem0 >= 11
	c_f101_t0_mem0 += INPUT_mem_r

	c_f101_t0_mem1 = S.Task('c_f101_t0_mem1', length=1, delay_cost=1)
	S += c_f101_t0_mem1 >= 11
	c_f101_t0_mem1 += INPUT_mem_r

	c_f111_t0 = S.Task('c_f111_t0', length=7, delay_cost=1)
	S += c_f111_t0 >= 11
	c_f111_t0 += MUL[0]

	c_f021_t1_in = S.Task('c_f021_t1_in', length=1, delay_cost=1)
	S += c_f021_t1_in >= 12
	c_f021_t1_in += MUL_in[0]

	c_f021_t1_mem0 = S.Task('c_f021_t1_mem0', length=1, delay_cost=1)
	S += c_f021_t1_mem0 >= 12
	c_f021_t1_mem0 += INPUT_mem_r

	c_f021_t1_mem1 = S.Task('c_f021_t1_mem1', length=1, delay_cost=1)
	S += c_f021_t1_mem1 >= 12
	c_f021_t1_mem1 += INPUT_mem_r

	c_f101_t0 = S.Task('c_f101_t0', length=7, delay_cost=1)
	S += c_f101_t0 >= 12
	c_f101_t0 += MUL[0]

	c001_t1_in = S.Task('c001_t1_in', length=1, delay_cost=1)
	S += c001_t1_in >= 13
	c001_t1_in += MUL_in[0]

	c001_t1_mem0 = S.Task('c001_t1_mem0', length=1, delay_cost=1)
	S += c001_t1_mem0 >= 13
	c001_t1_mem0 += INPUT_mem_r

	c001_t1_mem1 = S.Task('c001_t1_mem1', length=1, delay_cost=1)
	S += c001_t1_mem1 >= 13
	c001_t1_mem1 += INPUT_mem_r

	c_f021_t1 = S.Task('c_f021_t1', length=7, delay_cost=1)
	S += c_f021_t1 >= 13
	c_f021_t1 += MUL[0]

	c001_t1 = S.Task('c001_t1', length=7, delay_cost=1)
	S += c001_t1 >= 14
	c001_t1 += MUL[0]

	c10_t30_mem0 = S.Task('c10_t30_mem0', length=1, delay_cost=1)
	S += c10_t30_mem0 >= 14
	c10_t30_mem0 += INPUT_mem_r

	c10_t30_mem1 = S.Task('c10_t30_mem1', length=1, delay_cost=1)
	S += c10_t30_mem1 >= 14
	c10_t30_mem1 += INPUT_mem_r

	c10_t30 = S.Task('c10_t30', length=1, delay_cost=1)
	S += c10_t30 >= 15
	c10_t30 += ADD[1]

	c_f101_t2_mem0 = S.Task('c_f101_t2_mem0', length=1, delay_cost=1)
	S += c_f101_t2_mem0 >= 15
	c_f101_t2_mem0 += INPUT_mem_r

	c_f101_t2_mem1 = S.Task('c_f101_t2_mem1', length=1, delay_cost=1)
	S += c_f101_t2_mem1 >= 15
	c_f101_t2_mem1 += INPUT_mem_r

	c_f021_t2_mem0 = S.Task('c_f021_t2_mem0', length=1, delay_cost=1)
	S += c_f021_t2_mem0 >= 16
	c_f021_t2_mem0 += INPUT_mem_r

	c_f021_t2_mem1 = S.Task('c_f021_t2_mem1', length=1, delay_cost=1)
	S += c_f021_t2_mem1 >= 16
	c_f021_t2_mem1 += INPUT_mem_r

	c_f101_t2 = S.Task('c_f101_t2', length=1, delay_cost=1)
	S += c_f101_t2 >= 16
	c_f101_t2 += ADD[0]

	c_f011_t3_mem0 = S.Task('c_f011_t3_mem0', length=1, delay_cost=1)
	S += c_f011_t3_mem0 >= 17
	c_f011_t3_mem0 += INPUT_mem_r

	c_f011_t3_mem1 = S.Task('c_f011_t3_mem1', length=1, delay_cost=1)
	S += c_f011_t3_mem1 >= 17
	c_f011_t3_mem1 += INPUT_mem_r

	c_f021_t2 = S.Task('c_f021_t2', length=1, delay_cost=1)
	S += c_f021_t2 >= 17
	c_f021_t2 += ADD[0]

	c10_t1_t3_mem0 = S.Task('c10_t1_t3_mem0', length=1, delay_cost=1)
	S += c10_t1_t3_mem0 >= 18
	c10_t1_t3_mem0 += INPUT_mem_r

	c10_t1_t3_mem1 = S.Task('c10_t1_t3_mem1', length=1, delay_cost=1)
	S += c10_t1_t3_mem1 >= 18
	c10_t1_t3_mem1 += INPUT_mem_r

	c_f011_t3 = S.Task('c_f011_t3', length=1, delay_cost=1)
	S += c_f011_t3 >= 18
	c_f011_t3 += ADD[0]

	c10_t1_t3 = S.Task('c10_t1_t3', length=1, delay_cost=1)
	S += c10_t1_t3 >= 19
	c10_t1_t3 += ADD[0]

	c_f021_t3_mem0 = S.Task('c_f021_t3_mem0', length=1, delay_cost=1)
	S += c_f021_t3_mem0 >= 19
	c_f021_t3_mem0 += INPUT_mem_r

	c_f021_t3_mem1 = S.Task('c_f021_t3_mem1', length=1, delay_cost=1)
	S += c_f021_t3_mem1 >= 19
	c_f021_t3_mem1 += INPUT_mem_r

	c_f021_t3 = S.Task('c_f021_t3', length=1, delay_cost=1)
	S += c_f021_t3 >= 20
	c_f021_t3 += ADD[0]

	c_f111_t3_mem0 = S.Task('c_f111_t3_mem0', length=1, delay_cost=1)
	S += c_f111_t3_mem0 >= 20
	c_f111_t3_mem0 += INPUT_mem_r

	c_f111_t3_mem1 = S.Task('c_f111_t3_mem1', length=1, delay_cost=1)
	S += c_f111_t3_mem1 >= 20
	c_f111_t3_mem1 += INPUT_mem_r

	c_f011_t2_mem0 = S.Task('c_f011_t2_mem0', length=1, delay_cost=1)
	S += c_f011_t2_mem0 >= 21
	c_f011_t2_mem0 += INPUT_mem_r

	c_f011_t2_mem1 = S.Task('c_f011_t2_mem1', length=1, delay_cost=1)
	S += c_f011_t2_mem1 >= 21
	c_f011_t2_mem1 += INPUT_mem_r

	c_f111_t3 = S.Task('c_f111_t3', length=1, delay_cost=1)
	S += c_f111_t3 >= 21
	c_f111_t3 += ADD[3]

	c_f011_t2 = S.Task('c_f011_t2', length=1, delay_cost=1)
	S += c_f011_t2 >= 22
	c_f011_t2 += ADD[3]

	c_f111_t2_mem0 = S.Task('c_f111_t2_mem0', length=1, delay_cost=1)
	S += c_f111_t2_mem0 >= 22
	c_f111_t2_mem0 += INPUT_mem_r

	c_f111_t2_mem1 = S.Task('c_f111_t2_mem1', length=1, delay_cost=1)
	S += c_f111_t2_mem1 >= 22
	c_f111_t2_mem1 += INPUT_mem_r

	c10_t0_t3_mem0 = S.Task('c10_t0_t3_mem0', length=1, delay_cost=1)
	S += c10_t0_t3_mem0 >= 23
	c10_t0_t3_mem0 += INPUT_mem_r

	c10_t0_t3_mem1 = S.Task('c10_t0_t3_mem1', length=1, delay_cost=1)
	S += c10_t0_t3_mem1 >= 23
	c10_t0_t3_mem1 += INPUT_mem_r

	c_f111_t2 = S.Task('c_f111_t2', length=1, delay_cost=1)
	S += c_f111_t2 >= 23
	c_f111_t2 += ADD[3]

	c10_t0_t3 = S.Task('c10_t0_t3', length=1, delay_cost=1)
	S += c10_t0_t3 >= 24
	c10_t0_t3 += ADD[0]

	c_f101_t3_mem0 = S.Task('c_f101_t3_mem0', length=1, delay_cost=1)
	S += c_f101_t3_mem0 >= 24
	c_f101_t3_mem0 += INPUT_mem_r

	c_f101_t3_mem1 = S.Task('c_f101_t3_mem1', length=1, delay_cost=1)
	S += c_f101_t3_mem1 >= 24
	c_f101_t3_mem1 += INPUT_mem_r

	c10_t0_t2_mem0 = S.Task('c10_t0_t2_mem0', length=1, delay_cost=1)
	S += c10_t0_t2_mem0 >= 25
	c10_t0_t2_mem0 += INPUT_mem_r

	c10_t0_t2_mem1 = S.Task('c10_t0_t2_mem1', length=1, delay_cost=1)
	S += c10_t0_t2_mem1 >= 25
	c10_t0_t2_mem1 += INPUT_mem_r

	c_f101_t3 = S.Task('c_f101_t3', length=1, delay_cost=1)
	S += c_f101_t3 >= 25
	c_f101_t3 += ADD[2]

	c001_t3_mem0 = S.Task('c001_t3_mem0', length=1, delay_cost=1)
	S += c001_t3_mem0 >= 26
	c001_t3_mem0 += INPUT_mem_r

	c001_t3_mem1 = S.Task('c001_t3_mem1', length=1, delay_cost=1)
	S += c001_t3_mem1 >= 26
	c001_t3_mem1 += INPUT_mem_r

	c10_t0_t2 = S.Task('c10_t0_t2', length=1, delay_cost=1)
	S += c10_t0_t2 >= 26
	c10_t0_t2 += ADD[0]

	c001_t2_mem0 = S.Task('c001_t2_mem0', length=1, delay_cost=1)
	S += c001_t2_mem0 >= 27
	c001_t2_mem0 += INPUT_mem_r

	c001_t2_mem1 = S.Task('c001_t2_mem1', length=1, delay_cost=1)
	S += c001_t2_mem1 >= 27
	c001_t2_mem1 += INPUT_mem_r

	c001_t3 = S.Task('c001_t3', length=1, delay_cost=1)
	S += c001_t3 >= 27
	c001_t3 += ADD[2]

	c001_t2 = S.Task('c001_t2', length=1, delay_cost=1)
	S += c001_t2 >= 28
	c001_t2 += ADD[1]

	c_f121_t3_mem0 = S.Task('c_f121_t3_mem0', length=1, delay_cost=1)
	S += c_f121_t3_mem0 >= 28
	c_f121_t3_mem0 += INPUT_mem_r

	c_f121_t3_mem1 = S.Task('c_f121_t3_mem1', length=1, delay_cost=1)
	S += c_f121_t3_mem1 >= 28
	c_f121_t3_mem1 += INPUT_mem_r

	c_f121_t2_mem0 = S.Task('c_f121_t2_mem0', length=1, delay_cost=1)
	S += c_f121_t2_mem0 >= 29
	c_f121_t2_mem0 += INPUT_mem_r

	c_f121_t2_mem1 = S.Task('c_f121_t2_mem1', length=1, delay_cost=1)
	S += c_f121_t2_mem1 >= 29
	c_f121_t2_mem1 += INPUT_mem_r

	c_f121_t3 = S.Task('c_f121_t3', length=1, delay_cost=1)
	S += c_f121_t3 >= 29
	c_f121_t3 += ADD[1]

	c_f121_t2 = S.Task('c_f121_t2', length=1, delay_cost=1)
	S += c_f121_t2 >= 30
	c_f121_t2 += ADD[3]


	# new tasks
	c10_t31 = S.Task('c10_t31', length=1, delay_cost=1)
	c10_t31 += alt(ADD)

	c10_t31_mem0 = S.Task('c10_t31_mem0', length=1, delay_cost=1)
	c10_t31_mem0 += INPUT_mem_r
	S += c10_t31_mem0 <= c10_t31

	c10_t31_mem1 = S.Task('c10_t31_mem1', length=1, delay_cost=1)
	c10_t31_mem1 += INPUT_mem_r
	S += c10_t31_mem1 <= c10_t31

	c01_t0_t0_in = S.Task('c01_t0_t0_in', length=1, delay_cost=1)
	c01_t0_t0_in += alt(MUL_in)
	c01_t0_t0 = S.Task('c01_t0_t0', length=7, delay_cost=1)
	c01_t0_t0 += alt(MUL)
	S += c01_t0_t0>=c01_t0_t0_in

	c01_t0_t0_mem0 = S.Task('c01_t0_t0_mem0', length=1, delay_cost=1)
	c01_t0_t0_mem0 += INPUT_mem_r
	S += c01_t0_t0_mem0 <= c01_t0_t0

	c01_t0_t0_mem1 = S.Task('c01_t0_t0_mem1', length=1, delay_cost=1)
	c01_t0_t0_mem1 += INPUT_mem_r
	S += c01_t0_t0_mem1 <= c01_t0_t0

	c01_t0_t1_in = S.Task('c01_t0_t1_in', length=1, delay_cost=1)
	c01_t0_t1_in += alt(MUL_in)
	c01_t0_t1 = S.Task('c01_t0_t1', length=7, delay_cost=1)
	c01_t0_t1 += alt(MUL)
	S += c01_t0_t1>=c01_t0_t1_in

	c01_t0_t1_mem0 = S.Task('c01_t0_t1_mem0', length=1, delay_cost=1)
	c01_t0_t1_mem0 += INPUT_mem_r
	S += c01_t0_t1_mem0 <= c01_t0_t1

	c01_t0_t1_mem1 = S.Task('c01_t0_t1_mem1', length=1, delay_cost=1)
	c01_t0_t1_mem1 += INPUT_mem_r
	S += c01_t0_t1_mem1 <= c01_t0_t1

	c01_t0_t2 = S.Task('c01_t0_t2', length=1, delay_cost=1)
	c01_t0_t2 += alt(ADD)

	c01_t0_t2_mem0 = S.Task('c01_t0_t2_mem0', length=1, delay_cost=1)
	c01_t0_t2_mem0 += INPUT_mem_r
	S += c01_t0_t2_mem0 <= c01_t0_t2

	c01_t0_t2_mem1 = S.Task('c01_t0_t2_mem1', length=1, delay_cost=1)
	c01_t0_t2_mem1 += INPUT_mem_r
	S += c01_t0_t2_mem1 <= c01_t0_t2

	c01_t0_t3 = S.Task('c01_t0_t3', length=1, delay_cost=1)
	c01_t0_t3 += alt(ADD)

	c01_t0_t3_mem0 = S.Task('c01_t0_t3_mem0', length=1, delay_cost=1)
	c01_t0_t3_mem0 += INPUT_mem_r
	S += c01_t0_t3_mem0 <= c01_t0_t3

	c01_t0_t3_mem1 = S.Task('c01_t0_t3_mem1', length=1, delay_cost=1)
	c01_t0_t3_mem1 += INPUT_mem_r
	S += c01_t0_t3_mem1 <= c01_t0_t3

	c01_t1_t3 = S.Task('c01_t1_t3', length=1, delay_cost=1)
	c01_t1_t3 += alt(ADD)

	c01_t1_t3_mem0 = S.Task('c01_t1_t3_mem0', length=1, delay_cost=1)
	c01_t1_t3_mem0 += INPUT_mem_r
	S += c01_t1_t3_mem0 <= c01_t1_t3

	c01_t1_t3_mem1 = S.Task('c01_t1_t3_mem1', length=1, delay_cost=1)
	c01_t1_t3_mem1 += INPUT_mem_r
	S += c01_t1_t3_mem1 <= c01_t1_t3

	c01_t30 = S.Task('c01_t30', length=1, delay_cost=1)
	c01_t30 += alt(ADD)

	c01_t30_mem0 = S.Task('c01_t30_mem0', length=1, delay_cost=1)
	c01_t30_mem0 += INPUT_mem_r
	S += c01_t30_mem0 <= c01_t30

	c01_t30_mem1 = S.Task('c01_t30_mem1', length=1, delay_cost=1)
	c01_t30_mem1 += INPUT_mem_r
	S += c01_t30_mem1 <= c01_t30

	c01_t31 = S.Task('c01_t31', length=1, delay_cost=1)
	c01_t31 += alt(ADD)

	c01_t31_mem0 = S.Task('c01_t31_mem0', length=1, delay_cost=1)
	c01_t31_mem0 += INPUT_mem_r
	S += c01_t31_mem0 <= c01_t31

	c01_t31_mem1 = S.Task('c01_t31_mem1', length=1, delay_cost=1)
	c01_t31_mem1 += INPUT_mem_r
	S += c01_t31_mem1 <= c01_t31

	c11_t0_t0_in = S.Task('c11_t0_t0_in', length=1, delay_cost=1)
	c11_t0_t0_in += alt(MUL_in)
	c11_t0_t0 = S.Task('c11_t0_t0', length=7, delay_cost=1)
	c11_t0_t0 += alt(MUL)
	S += c11_t0_t0>=c11_t0_t0_in

	c11_t0_t0_mem0 = S.Task('c11_t0_t0_mem0', length=1, delay_cost=1)
	c11_t0_t0_mem0 += INPUT_mem_r
	S += c11_t0_t0_mem0 <= c11_t0_t0

	c11_t0_t0_mem1 = S.Task('c11_t0_t0_mem1', length=1, delay_cost=1)
	c11_t0_t0_mem1 += INPUT_mem_r
	S += c11_t0_t0_mem1 <= c11_t0_t0

	c11_t0_t1_in = S.Task('c11_t0_t1_in', length=1, delay_cost=1)
	c11_t0_t1_in += alt(MUL_in)
	c11_t0_t1 = S.Task('c11_t0_t1', length=7, delay_cost=1)
	c11_t0_t1 += alt(MUL)
	S += c11_t0_t1>=c11_t0_t1_in

	c11_t0_t1_mem0 = S.Task('c11_t0_t1_mem0', length=1, delay_cost=1)
	c11_t0_t1_mem0 += INPUT_mem_r
	S += c11_t0_t1_mem0 <= c11_t0_t1

	c11_t0_t1_mem1 = S.Task('c11_t0_t1_mem1', length=1, delay_cost=1)
	c11_t0_t1_mem1 += INPUT_mem_r
	S += c11_t0_t1_mem1 <= c11_t0_t1

	c11_t0_t2 = S.Task('c11_t0_t2', length=1, delay_cost=1)
	c11_t0_t2 += alt(ADD)

	c11_t0_t2_mem0 = S.Task('c11_t0_t2_mem0', length=1, delay_cost=1)
	c11_t0_t2_mem0 += INPUT_mem_r
	S += c11_t0_t2_mem0 <= c11_t0_t2

	c11_t0_t2_mem1 = S.Task('c11_t0_t2_mem1', length=1, delay_cost=1)
	c11_t0_t2_mem1 += INPUT_mem_r
	S += c11_t0_t2_mem1 <= c11_t0_t2

	c11_t0_t3 = S.Task('c11_t0_t3', length=1, delay_cost=1)
	c11_t0_t3 += alt(ADD)

	c11_t0_t3_mem0 = S.Task('c11_t0_t3_mem0', length=1, delay_cost=1)
	c11_t0_t3_mem0 += INPUT_mem_r
	S += c11_t0_t3_mem0 <= c11_t0_t3

	c11_t0_t3_mem1 = S.Task('c11_t0_t3_mem1', length=1, delay_cost=1)
	c11_t0_t3_mem1 += INPUT_mem_r
	S += c11_t0_t3_mem1 <= c11_t0_t3

	c11_t1_t3 = S.Task('c11_t1_t3', length=1, delay_cost=1)
	c11_t1_t3 += alt(ADD)

	c11_t1_t3_mem0 = S.Task('c11_t1_t3_mem0', length=1, delay_cost=1)
	c11_t1_t3_mem0 += INPUT_mem_r
	S += c11_t1_t3_mem0 <= c11_t1_t3

	c11_t1_t3_mem1 = S.Task('c11_t1_t3_mem1', length=1, delay_cost=1)
	c11_t1_t3_mem1 += INPUT_mem_r
	S += c11_t1_t3_mem1 <= c11_t1_t3

	c11_t30 = S.Task('c11_t30', length=1, delay_cost=1)
	c11_t30 += alt(ADD)

	c11_t30_mem0 = S.Task('c11_t30_mem0', length=1, delay_cost=1)
	c11_t30_mem0 += INPUT_mem_r
	S += c11_t30_mem0 <= c11_t30

	c11_t30_mem1 = S.Task('c11_t30_mem1', length=1, delay_cost=1)
	c11_t30_mem1 += INPUT_mem_r
	S += c11_t30_mem1 <= c11_t30

	c11_t31 = S.Task('c11_t31', length=1, delay_cost=1)
	c11_t31 += alt(ADD)

	c11_t31_mem0 = S.Task('c11_t31_mem0', length=1, delay_cost=1)
	c11_t31_mem0 += INPUT_mem_r
	S += c11_t31_mem0 <= c11_t31

	c11_t31_mem1 = S.Task('c11_t31_mem1', length=1, delay_cost=1)
	c11_t31_mem1 += INPUT_mem_r
	S += c11_t31_mem1 <= c11_t31

	c02_t0_t0_in = S.Task('c02_t0_t0_in', length=1, delay_cost=1)
	c02_t0_t0_in += alt(MUL_in)
	c02_t0_t0 = S.Task('c02_t0_t0', length=7, delay_cost=1)
	c02_t0_t0 += alt(MUL)
	S += c02_t0_t0>=c02_t0_t0_in

	c02_t0_t0_mem0 = S.Task('c02_t0_t0_mem0', length=1, delay_cost=1)
	c02_t0_t0_mem0 += INPUT_mem_r
	S += c02_t0_t0_mem0 <= c02_t0_t0

	c02_t0_t0_mem1 = S.Task('c02_t0_t0_mem1', length=1, delay_cost=1)
	c02_t0_t0_mem1 += INPUT_mem_r
	S += c02_t0_t0_mem1 <= c02_t0_t0

	c02_t0_t1_in = S.Task('c02_t0_t1_in', length=1, delay_cost=1)
	c02_t0_t1_in += alt(MUL_in)
	c02_t0_t1 = S.Task('c02_t0_t1', length=7, delay_cost=1)
	c02_t0_t1 += alt(MUL)
	S += c02_t0_t1>=c02_t0_t1_in

	c02_t0_t1_mem0 = S.Task('c02_t0_t1_mem0', length=1, delay_cost=1)
	c02_t0_t1_mem0 += INPUT_mem_r
	S += c02_t0_t1_mem0 <= c02_t0_t1

	c02_t0_t1_mem1 = S.Task('c02_t0_t1_mem1', length=1, delay_cost=1)
	c02_t0_t1_mem1 += INPUT_mem_r
	S += c02_t0_t1_mem1 <= c02_t0_t1

	c02_t0_t2 = S.Task('c02_t0_t2', length=1, delay_cost=1)
	c02_t0_t2 += alt(ADD)

	c02_t0_t2_mem0 = S.Task('c02_t0_t2_mem0', length=1, delay_cost=1)
	c02_t0_t2_mem0 += INPUT_mem_r
	S += c02_t0_t2_mem0 <= c02_t0_t2

	c02_t0_t2_mem1 = S.Task('c02_t0_t2_mem1', length=1, delay_cost=1)
	c02_t0_t2_mem1 += INPUT_mem_r
	S += c02_t0_t2_mem1 <= c02_t0_t2

	c02_t0_t3 = S.Task('c02_t0_t3', length=1, delay_cost=1)
	c02_t0_t3 += alt(ADD)

	c02_t0_t3_mem0 = S.Task('c02_t0_t3_mem0', length=1, delay_cost=1)
	c02_t0_t3_mem0 += INPUT_mem_r
	S += c02_t0_t3_mem0 <= c02_t0_t3

	c02_t0_t3_mem1 = S.Task('c02_t0_t3_mem1', length=1, delay_cost=1)
	c02_t0_t3_mem1 += INPUT_mem_r
	S += c02_t0_t3_mem1 <= c02_t0_t3

	c02_t1_t3 = S.Task('c02_t1_t3', length=1, delay_cost=1)
	c02_t1_t3 += alt(ADD)

	c02_t1_t3_mem0 = S.Task('c02_t1_t3_mem0', length=1, delay_cost=1)
	c02_t1_t3_mem0 += INPUT_mem_r
	S += c02_t1_t3_mem0 <= c02_t1_t3

	c02_t1_t3_mem1 = S.Task('c02_t1_t3_mem1', length=1, delay_cost=1)
	c02_t1_t3_mem1 += INPUT_mem_r
	S += c02_t1_t3_mem1 <= c02_t1_t3

	c02_t30 = S.Task('c02_t30', length=1, delay_cost=1)
	c02_t30 += alt(ADD)

	c02_t30_mem0 = S.Task('c02_t30_mem0', length=1, delay_cost=1)
	c02_t30_mem0 += INPUT_mem_r
	S += c02_t30_mem0 <= c02_t30

	c02_t30_mem1 = S.Task('c02_t30_mem1', length=1, delay_cost=1)
	c02_t30_mem1 += INPUT_mem_r
	S += c02_t30_mem1 <= c02_t30

	c02_t31 = S.Task('c02_t31', length=1, delay_cost=1)
	c02_t31 += alt(ADD)

	c02_t31_mem0 = S.Task('c02_t31_mem0', length=1, delay_cost=1)
	c02_t31_mem0 += INPUT_mem_r
	S += c02_t31_mem0 <= c02_t31

	c02_t31_mem1 = S.Task('c02_t31_mem1', length=1, delay_cost=1)
	c02_t31_mem1 += INPUT_mem_r
	S += c02_t31_mem1 <= c02_t31

	c12_t0_t0_in = S.Task('c12_t0_t0_in', length=1, delay_cost=1)
	c12_t0_t0_in += alt(MUL_in)
	c12_t0_t0 = S.Task('c12_t0_t0', length=7, delay_cost=1)
	c12_t0_t0 += alt(MUL)
	S += c12_t0_t0>=c12_t0_t0_in

	c12_t0_t0_mem0 = S.Task('c12_t0_t0_mem0', length=1, delay_cost=1)
	c12_t0_t0_mem0 += INPUT_mem_r
	S += c12_t0_t0_mem0 <= c12_t0_t0

	c12_t0_t0_mem1 = S.Task('c12_t0_t0_mem1', length=1, delay_cost=1)
	c12_t0_t0_mem1 += INPUT_mem_r
	S += c12_t0_t0_mem1 <= c12_t0_t0

	c12_t0_t1_in = S.Task('c12_t0_t1_in', length=1, delay_cost=1)
	c12_t0_t1_in += alt(MUL_in)
	c12_t0_t1 = S.Task('c12_t0_t1', length=7, delay_cost=1)
	c12_t0_t1 += alt(MUL)
	S += c12_t0_t1>=c12_t0_t1_in

	c12_t0_t1_mem0 = S.Task('c12_t0_t1_mem0', length=1, delay_cost=1)
	c12_t0_t1_mem0 += INPUT_mem_r
	S += c12_t0_t1_mem0 <= c12_t0_t1

	c12_t0_t1_mem1 = S.Task('c12_t0_t1_mem1', length=1, delay_cost=1)
	c12_t0_t1_mem1 += INPUT_mem_r
	S += c12_t0_t1_mem1 <= c12_t0_t1

	c12_t0_t2 = S.Task('c12_t0_t2', length=1, delay_cost=1)
	c12_t0_t2 += alt(ADD)

	c12_t0_t2_mem0 = S.Task('c12_t0_t2_mem0', length=1, delay_cost=1)
	c12_t0_t2_mem0 += INPUT_mem_r
	S += c12_t0_t2_mem0 <= c12_t0_t2

	c12_t0_t2_mem1 = S.Task('c12_t0_t2_mem1', length=1, delay_cost=1)
	c12_t0_t2_mem1 += INPUT_mem_r
	S += c12_t0_t2_mem1 <= c12_t0_t2

	c12_t0_t3 = S.Task('c12_t0_t3', length=1, delay_cost=1)
	c12_t0_t3 += alt(ADD)

	c12_t0_t3_mem0 = S.Task('c12_t0_t3_mem0', length=1, delay_cost=1)
	c12_t0_t3_mem0 += INPUT_mem_r
	S += c12_t0_t3_mem0 <= c12_t0_t3

	c12_t0_t3_mem1 = S.Task('c12_t0_t3_mem1', length=1, delay_cost=1)
	c12_t0_t3_mem1 += INPUT_mem_r
	S += c12_t0_t3_mem1 <= c12_t0_t3

	c12_t1_t3 = S.Task('c12_t1_t3', length=1, delay_cost=1)
	c12_t1_t3 += alt(ADD)

	c12_t1_t3_mem0 = S.Task('c12_t1_t3_mem0', length=1, delay_cost=1)
	c12_t1_t3_mem0 += INPUT_mem_r
	S += c12_t1_t3_mem0 <= c12_t1_t3

	c12_t1_t3_mem1 = S.Task('c12_t1_t3_mem1', length=1, delay_cost=1)
	c12_t1_t3_mem1 += INPUT_mem_r
	S += c12_t1_t3_mem1 <= c12_t1_t3

	c12_t30 = S.Task('c12_t30', length=1, delay_cost=1)
	c12_t30 += alt(ADD)

	c12_t30_mem0 = S.Task('c12_t30_mem0', length=1, delay_cost=1)
	c12_t30_mem0 += INPUT_mem_r
	S += c12_t30_mem0 <= c12_t30

	c12_t30_mem1 = S.Task('c12_t30_mem1', length=1, delay_cost=1)
	c12_t30_mem1 += INPUT_mem_r
	S += c12_t30_mem1 <= c12_t30

	c12_t31 = S.Task('c12_t31', length=1, delay_cost=1)
	c12_t31 += alt(ADD)

	c12_t31_mem0 = S.Task('c12_t31_mem0', length=1, delay_cost=1)
	c12_t31_mem0 += INPUT_mem_r
	S += c12_t31_mem0 <= c12_t31

	c12_t31_mem1 = S.Task('c12_t31_mem1', length=1, delay_cost=1)
	c12_t31_mem1 += INPUT_mem_r
	S += c12_t31_mem1 <= c12_t31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/FROB_mul1_add4/FROB_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

