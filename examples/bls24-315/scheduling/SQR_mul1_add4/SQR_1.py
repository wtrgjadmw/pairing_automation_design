from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 135
	S = Scenario("SQR_1", horizon=horizon)

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
	c_t3_t0_t1_t1_in = S.Task('c_t3_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_t1_in >= 0
	c_t3_t0_t1_t1_in += MUL_in[0]

	c_t3_t0_t1_t1_mem0 = S.Task('c_t3_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_t1_mem0 >= 0
	c_t3_t0_t1_t1_mem0 += INPUT_mem_r

	c_t3_t0_t1_t1_mem1 = S.Task('c_t3_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_t1_mem1 >= 0
	c_t3_t0_t1_t1_mem1 += INPUT_mem_r

	c_t3_t0_t0_t0_in = S.Task('c_t3_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_t0_in >= 1
	c_t3_t0_t0_t0_in += MUL_in[0]

	c_t3_t0_t0_t0_mem0 = S.Task('c_t3_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_t0_mem0 >= 1
	c_t3_t0_t0_t0_mem0 += INPUT_mem_r

	c_t3_t0_t0_t0_mem1 = S.Task('c_t3_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_t0_mem1 >= 1
	c_t3_t0_t0_t0_mem1 += INPUT_mem_r

	c_t3_t0_t1_t1 = S.Task('c_t3_t0_t1_t1', length=7, delay_cost=1)
	S += c_t3_t0_t1_t1 >= 1
	c_t3_t0_t1_t1 += MUL[0]

	c_t3_t0_t0_t0 = S.Task('c_t3_t0_t0_t0', length=7, delay_cost=1)
	S += c_t3_t0_t0_t0 >= 2
	c_t3_t0_t0_t0 += MUL[0]

	c_t3_t0_t1_t0_in = S.Task('c_t3_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_t0_in >= 2
	c_t3_t0_t1_t0_in += MUL_in[0]

	c_t3_t0_t1_t0_mem0 = S.Task('c_t3_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_t0_mem0 >= 2
	c_t3_t0_t1_t0_mem0 += INPUT_mem_r

	c_t3_t0_t1_t0_mem1 = S.Task('c_t3_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_t0_mem1 >= 2
	c_t3_t0_t1_t0_mem1 += INPUT_mem_r

	c_t3_t0_t0_t1_in = S.Task('c_t3_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_t1_in >= 3
	c_t3_t0_t0_t1_in += MUL_in[0]

	c_t3_t0_t0_t1_mem0 = S.Task('c_t3_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_t1_mem0 >= 3
	c_t3_t0_t0_t1_mem0 += INPUT_mem_r

	c_t3_t0_t0_t1_mem1 = S.Task('c_t3_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_t1_mem1 >= 3
	c_t3_t0_t0_t1_mem1 += INPUT_mem_r

	c_t3_t0_t1_t0 = S.Task('c_t3_t0_t1_t0', length=7, delay_cost=1)
	S += c_t3_t0_t1_t0 >= 3
	c_t3_t0_t1_t0 += MUL[0]

	c_t0001_mem0 = S.Task('c_t0001_mem0', length=1, delay_cost=1)
	S += c_t0001_mem0 >= 4
	c_t0001_mem0 += INPUT_mem_r

	c_t0001_mem1 = S.Task('c_t0001_mem1', length=1, delay_cost=1)
	S += c_t0001_mem1 >= 4
	c_t0001_mem1 += INPUT_mem_r

	c_t3_t0_t0_t1 = S.Task('c_t3_t0_t0_t1', length=7, delay_cost=1)
	S += c_t3_t0_t0_t1 >= 4
	c_t3_t0_t0_t1 += MUL[0]

	c_t0001 = S.Task('c_t0001', length=1, delay_cost=1)
	S += c_t0001 >= 5
	c_t0001 += ADD[3]

	c_t0100_mem0 = S.Task('c_t0100_mem0', length=1, delay_cost=1)
	S += c_t0100_mem0 >= 5
	c_t0100_mem0 += INPUT_mem_r

	c_t0100_mem1 = S.Task('c_t0100_mem1', length=1, delay_cost=1)
	S += c_t0100_mem1 >= 5
	c_t0100_mem1 += INPUT_mem_r

	c_t0100 = S.Task('c_t0100', length=1, delay_cost=1)
	S += c_t0100 >= 6
	c_t0100 += ADD[1]

	c_t1110_mem0 = S.Task('c_t1110_mem0', length=1, delay_cost=1)
	S += c_t1110_mem0 >= 6
	c_t1110_mem0 += INPUT_mem_r

	c_t1110_mem1 = S.Task('c_t1110_mem1', length=1, delay_cost=1)
	S += c_t1110_mem1 >= 6
	c_t1110_mem1 += INPUT_mem_r

	c_t1110 = S.Task('c_t1110', length=1, delay_cost=1)
	S += c_t1110 >= 7
	c_t1110 += ADD[3]

	c_t3_t0_t0_t2_mem0 = S.Task('c_t3_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_t2_mem0 >= 7
	c_t3_t0_t0_t2_mem0 += INPUT_mem_r

	c_t3_t0_t0_t2_mem1 = S.Task('c_t3_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_t2_mem1 >= 7
	c_t3_t0_t0_t2_mem1 += INPUT_mem_r

	c_t1111_mem0 = S.Task('c_t1111_mem0', length=1, delay_cost=1)
	S += c_t1111_mem0 >= 8
	c_t1111_mem0 += INPUT_mem_r

	c_t1111_mem1 = S.Task('c_t1111_mem1', length=1, delay_cost=1)
	S += c_t1111_mem1 >= 8
	c_t1111_mem1 += INPUT_mem_r

	c_t3_t0_t0_t2 = S.Task('c_t3_t0_t0_t2', length=1, delay_cost=1)
	S += c_t3_t0_t0_t2 >= 8
	c_t3_t0_t0_t2 += ADD[3]

	c_t0110_mem0 = S.Task('c_t0110_mem0', length=1, delay_cost=1)
	S += c_t0110_mem0 >= 9
	c_t0110_mem0 += INPUT_mem_r

	c_t0110_mem1 = S.Task('c_t0110_mem1', length=1, delay_cost=1)
	S += c_t0110_mem1 >= 9
	c_t0110_mem1 += INPUT_mem_r

	c_t1111 = S.Task('c_t1111', length=1, delay_cost=1)
	S += c_t1111 >= 9
	c_t1111 += ADD[3]

	c_t0110 = S.Task('c_t0110', length=1, delay_cost=1)
	S += c_t0110 >= 10
	c_t0110 += ADD[3]

	c_t1011_mem0 = S.Task('c_t1011_mem0', length=1, delay_cost=1)
	S += c_t1011_mem0 >= 10
	c_t1011_mem0 += INPUT_mem_r

	c_t1011_mem1 = S.Task('c_t1011_mem1', length=1, delay_cost=1)
	S += c_t1011_mem1 >= 10
	c_t1011_mem1 += INPUT_mem_r

	c_t1011 = S.Task('c_t1011', length=1, delay_cost=1)
	S += c_t1011 >= 11
	c_t1011 += ADD[3]

	c_t1100_mem0 = S.Task('c_t1100_mem0', length=1, delay_cost=1)
	S += c_t1100_mem0 >= 11
	c_t1100_mem0 += INPUT_mem_r

	c_t1100_mem1 = S.Task('c_t1100_mem1', length=1, delay_cost=1)
	S += c_t1100_mem1 >= 11
	c_t1100_mem1 += INPUT_mem_r

	c_t0211_mem0 = S.Task('c_t0211_mem0', length=1, delay_cost=1)
	S += c_t0211_mem0 >= 12
	c_t0211_mem0 += INPUT_mem_r

	c_t0211_mem1 = S.Task('c_t0211_mem1', length=1, delay_cost=1)
	S += c_t0211_mem1 >= 12
	c_t0211_mem1 += INPUT_mem_r

	c_t1100 = S.Task('c_t1100', length=1, delay_cost=1)
	S += c_t1100 >= 12
	c_t1100 += ADD[2]

	c_t0211 = S.Task('c_t0211', length=1, delay_cost=1)
	S += c_t0211 >= 13
	c_t0211 += ADD[0]

	c_t1010_mem0 = S.Task('c_t1010_mem0', length=1, delay_cost=1)
	S += c_t1010_mem0 >= 13
	c_t1010_mem0 += INPUT_mem_r

	c_t1010_mem1 = S.Task('c_t1010_mem1', length=1, delay_cost=1)
	S += c_t1010_mem1 >= 13
	c_t1010_mem1 += INPUT_mem_r

	c_t1001_mem0 = S.Task('c_t1001_mem0', length=1, delay_cost=1)
	S += c_t1001_mem0 >= 14
	c_t1001_mem0 += INPUT_mem_r

	c_t1001_mem1 = S.Task('c_t1001_mem1', length=1, delay_cost=1)
	S += c_t1001_mem1 >= 14
	c_t1001_mem1 += INPUT_mem_r

	c_t1010 = S.Task('c_t1010', length=1, delay_cost=1)
	S += c_t1010 >= 14
	c_t1010 += ADD[0]

	c_t1001 = S.Task('c_t1001', length=1, delay_cost=1)
	S += c_t1001 >= 15
	c_t1001 += ADD[1]

	c_t1101_mem0 = S.Task('c_t1101_mem0', length=1, delay_cost=1)
	S += c_t1101_mem0 >= 15
	c_t1101_mem0 += INPUT_mem_r

	c_t1101_mem1 = S.Task('c_t1101_mem1', length=1, delay_cost=1)
	S += c_t1101_mem1 >= 15
	c_t1101_mem1 += INPUT_mem_r

	c_t1101 = S.Task('c_t1101', length=1, delay_cost=1)
	S += c_t1101 >= 16
	c_t1101 += ADD[0]

	c_t1211_mem0 = S.Task('c_t1211_mem0', length=1, delay_cost=1)
	S += c_t1211_mem0 >= 16
	c_t1211_mem0 += INPUT_mem_r

	c_t1211_mem1 = S.Task('c_t1211_mem1', length=1, delay_cost=1)
	S += c_t1211_mem1 >= 16
	c_t1211_mem1 += INPUT_mem_r

	c_t0210_mem0 = S.Task('c_t0210_mem0', length=1, delay_cost=1)
	S += c_t0210_mem0 >= 17
	c_t0210_mem0 += INPUT_mem_r

	c_t0210_mem1 = S.Task('c_t0210_mem1', length=1, delay_cost=1)
	S += c_t0210_mem1 >= 17
	c_t0210_mem1 += INPUT_mem_r

	c_t1211 = S.Task('c_t1211', length=1, delay_cost=1)
	S += c_t1211 >= 17
	c_t1211 += ADD[0]

	c_t0210 = S.Task('c_t0210', length=1, delay_cost=1)
	S += c_t0210 >= 18
	c_t0210 += ADD[2]

	c_t1201_mem0 = S.Task('c_t1201_mem0', length=1, delay_cost=1)
	S += c_t1201_mem0 >= 18
	c_t1201_mem0 += INPUT_mem_r

	c_t1201_mem1 = S.Task('c_t1201_mem1', length=1, delay_cost=1)
	S += c_t1201_mem1 >= 18
	c_t1201_mem1 += INPUT_mem_r

	c_t0200_mem0 = S.Task('c_t0200_mem0', length=1, delay_cost=1)
	S += c_t0200_mem0 >= 19
	c_t0200_mem0 += INPUT_mem_r

	c_t0200_mem1 = S.Task('c_t0200_mem1', length=1, delay_cost=1)
	S += c_t0200_mem1 >= 19
	c_t0200_mem1 += INPUT_mem_r

	c_t1201 = S.Task('c_t1201', length=1, delay_cost=1)
	S += c_t1201 >= 19
	c_t1201 += ADD[2]

	c_t0200 = S.Task('c_t0200', length=1, delay_cost=1)
	S += c_t0200 >= 20
	c_t0200 += ADD[3]

	c_t1000_mem0 = S.Task('c_t1000_mem0', length=1, delay_cost=1)
	S += c_t1000_mem0 >= 20
	c_t1000_mem0 += INPUT_mem_r

	c_t1000_mem1 = S.Task('c_t1000_mem1', length=1, delay_cost=1)
	S += c_t1000_mem1 >= 20
	c_t1000_mem1 += INPUT_mem_r

	c_t0111_mem0 = S.Task('c_t0111_mem0', length=1, delay_cost=1)
	S += c_t0111_mem0 >= 21
	c_t0111_mem0 += INPUT_mem_r

	c_t0111_mem1 = S.Task('c_t0111_mem1', length=1, delay_cost=1)
	S += c_t0111_mem1 >= 21
	c_t0111_mem1 += INPUT_mem_r

	c_t1000 = S.Task('c_t1000', length=1, delay_cost=1)
	S += c_t1000 >= 21
	c_t1000 += ADD[0]

	c_t0111 = S.Task('c_t0111', length=1, delay_cost=1)
	S += c_t0111 >= 22
	c_t0111 += ADD[2]

	c_t0201_mem0 = S.Task('c_t0201_mem0', length=1, delay_cost=1)
	S += c_t0201_mem0 >= 22
	c_t0201_mem0 += INPUT_mem_r

	c_t0201_mem1 = S.Task('c_t0201_mem1', length=1, delay_cost=1)
	S += c_t0201_mem1 >= 22
	c_t0201_mem1 += INPUT_mem_r

	c_t0201 = S.Task('c_t0201', length=1, delay_cost=1)
	S += c_t0201 >= 23
	c_t0201 += ADD[2]

	c_t1210_mem0 = S.Task('c_t1210_mem0', length=1, delay_cost=1)
	S += c_t1210_mem0 >= 23
	c_t1210_mem0 += INPUT_mem_r

	c_t1210_mem1 = S.Task('c_t1210_mem1', length=1, delay_cost=1)
	S += c_t1210_mem1 >= 23
	c_t1210_mem1 += INPUT_mem_r

	c_t1210 = S.Task('c_t1210', length=1, delay_cost=1)
	S += c_t1210 >= 24
	c_t1210 += ADD[1]

	c_t3_t0_t0_t3_mem0 = S.Task('c_t3_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_t3_mem0 >= 24
	c_t3_t0_t0_t3_mem0 += INPUT_mem_r

	c_t3_t0_t0_t3_mem1 = S.Task('c_t3_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_t3_mem1 >= 24
	c_t3_t0_t0_t3_mem1 += INPUT_mem_r

	c_t1200_mem0 = S.Task('c_t1200_mem0', length=1, delay_cost=1)
	S += c_t1200_mem0 >= 25
	c_t1200_mem0 += INPUT_mem_r

	c_t1200_mem1 = S.Task('c_t1200_mem1', length=1, delay_cost=1)
	S += c_t1200_mem1 >= 25
	c_t1200_mem1 += INPUT_mem_r

	c_t3_t0_t0_t3 = S.Task('c_t3_t0_t0_t3', length=1, delay_cost=1)
	S += c_t3_t0_t0_t3 >= 25
	c_t3_t0_t0_t3 += ADD[2]

	c_t0101_mem0 = S.Task('c_t0101_mem0', length=1, delay_cost=1)
	S += c_t0101_mem0 >= 26
	c_t0101_mem0 += INPUT_mem_r

	c_t0101_mem1 = S.Task('c_t0101_mem1', length=1, delay_cost=1)
	S += c_t0101_mem1 >= 26
	c_t0101_mem1 += INPUT_mem_r

	c_t1200 = S.Task('c_t1200', length=1, delay_cost=1)
	S += c_t1200 >= 26
	c_t1200 += ADD[2]

	c_t0010_mem0 = S.Task('c_t0010_mem0', length=1, delay_cost=1)
	S += c_t0010_mem0 >= 27
	c_t0010_mem0 += INPUT_mem_r

	c_t0010_mem1 = S.Task('c_t0010_mem1', length=1, delay_cost=1)
	S += c_t0010_mem1 >= 27
	c_t0010_mem1 += INPUT_mem_r

	c_t0101 = S.Task('c_t0101', length=1, delay_cost=1)
	S += c_t0101 >= 27
	c_t0101 += ADD[1]

	c_t0010 = S.Task('c_t0010', length=1, delay_cost=1)
	S += c_t0010 >= 28
	c_t0010 += ADD[1]

	c_t0011_mem0 = S.Task('c_t0011_mem0', length=1, delay_cost=1)
	S += c_t0011_mem0 >= 28
	c_t0011_mem0 += INPUT_mem_r

	c_t0011_mem1 = S.Task('c_t0011_mem1', length=1, delay_cost=1)
	S += c_t0011_mem1 >= 28
	c_t0011_mem1 += INPUT_mem_r

	c_a1_0_y1__y1_0_mem0 = S.Task('c_a1_0_y1__y1_0_mem0', length=1, delay_cost=1)
	S += c_a1_0_y1__y1_0_mem0 >= 29
	c_a1_0_y1__y1_0_mem0 += INPUT_mem_r

	c_t0011 = S.Task('c_t0011', length=1, delay_cost=1)
	S += c_t0011 >= 29
	c_t0011 += ADD[3]

	c_a1_0_y1__y1_0 = S.Task('c_a1_0_y1__y1_0', length=1, delay_cost=1)
	S += c_a1_0_y1__y1_0 >= 30
	c_a1_0_y1__y1_0 += ADD[3]


	# new tasks
	c_t3_t0_t1_t2 = S.Task('c_t3_t0_t1_t2', length=1, delay_cost=1)
	c_t3_t0_t1_t2 += alt(ADD)

	c_t3_t0_t1_t2_mem0 = S.Task('c_t3_t0_t1_t2_mem0', length=1, delay_cost=1)
	c_t3_t0_t1_t2_mem0 += INPUT_mem_r
	S += c_t3_t0_t1_t2_mem0 <= c_t3_t0_t1_t2

	c_t3_t0_t1_t2_mem1 = S.Task('c_t3_t0_t1_t2_mem1', length=1, delay_cost=1)
	c_t3_t0_t1_t2_mem1 += INPUT_mem_r
	S += c_t3_t0_t1_t2_mem1 <= c_t3_t0_t1_t2

	c_t3_t0_t1_t3 = S.Task('c_t3_t0_t1_t3', length=1, delay_cost=1)
	c_t3_t0_t1_t3 += alt(ADD)

	c_t3_t0_t1_t3_mem0 = S.Task('c_t3_t0_t1_t3_mem0', length=1, delay_cost=1)
	c_t3_t0_t1_t3_mem0 += INPUT_mem_r
	S += c_t3_t0_t1_t3_mem0 <= c_t3_t0_t1_t3

	c_t3_t0_t1_t3_mem1 = S.Task('c_t3_t0_t1_t3_mem1', length=1, delay_cost=1)
	c_t3_t0_t1_t3_mem1 += INPUT_mem_r
	S += c_t3_t0_t1_t3_mem1 <= c_t3_t0_t1_t3

	c_t3_t0_t20 = S.Task('c_t3_t0_t20', length=1, delay_cost=1)
	c_t3_t0_t20 += alt(ADD)

	c_t3_t0_t20_mem0 = S.Task('c_t3_t0_t20_mem0', length=1, delay_cost=1)
	c_t3_t0_t20_mem0 += INPUT_mem_r
	S += c_t3_t0_t20_mem0 <= c_t3_t0_t20

	c_t3_t0_t20_mem1 = S.Task('c_t3_t0_t20_mem1', length=1, delay_cost=1)
	c_t3_t0_t20_mem1 += INPUT_mem_r
	S += c_t3_t0_t20_mem1 <= c_t3_t0_t20

	c_t3_t0_t21 = S.Task('c_t3_t0_t21', length=1, delay_cost=1)
	c_t3_t0_t21 += alt(ADD)

	c_t3_t0_t21_mem0 = S.Task('c_t3_t0_t21_mem0', length=1, delay_cost=1)
	c_t3_t0_t21_mem0 += INPUT_mem_r
	S += c_t3_t0_t21_mem0 <= c_t3_t0_t21

	c_t3_t0_t21_mem1 = S.Task('c_t3_t0_t21_mem1', length=1, delay_cost=1)
	c_t3_t0_t21_mem1 += INPUT_mem_r
	S += c_t3_t0_t21_mem1 <= c_t3_t0_t21

	c_t3_t0_t30 = S.Task('c_t3_t0_t30', length=1, delay_cost=1)
	c_t3_t0_t30 += alt(ADD)

	c_t3_t0_t30_mem0 = S.Task('c_t3_t0_t30_mem0', length=1, delay_cost=1)
	c_t3_t0_t30_mem0 += INPUT_mem_r
	S += c_t3_t0_t30_mem0 <= c_t3_t0_t30

	c_t3_t0_t30_mem1 = S.Task('c_t3_t0_t30_mem1', length=1, delay_cost=1)
	c_t3_t0_t30_mem1 += INPUT_mem_r
	S += c_t3_t0_t30_mem1 <= c_t3_t0_t30

	c_t3_t0_t31 = S.Task('c_t3_t0_t31', length=1, delay_cost=1)
	c_t3_t0_t31 += alt(ADD)

	c_t3_t0_t31_mem0 = S.Task('c_t3_t0_t31_mem0', length=1, delay_cost=1)
	c_t3_t0_t31_mem0 += INPUT_mem_r
	S += c_t3_t0_t31_mem0 <= c_t3_t0_t31

	c_t3_t0_t31_mem1 = S.Task('c_t3_t0_t31_mem1', length=1, delay_cost=1)
	c_t3_t0_t31_mem1 += INPUT_mem_r
	S += c_t3_t0_t31_mem1 <= c_t3_t0_t31

	c_t3_t1_t0_t0_in = S.Task('c_t3_t1_t0_t0_in', length=1, delay_cost=1)
	c_t3_t1_t0_t0_in += alt(MUL_in)
	c_t3_t1_t0_t0 = S.Task('c_t3_t1_t0_t0', length=7, delay_cost=1)
	c_t3_t1_t0_t0 += alt(MUL)
	S += c_t3_t1_t0_t0>=c_t3_t1_t0_t0_in

	c_t3_t1_t0_t0_mem0 = S.Task('c_t3_t1_t0_t0_mem0', length=1, delay_cost=1)
	c_t3_t1_t0_t0_mem0 += INPUT_mem_r
	S += c_t3_t1_t0_t0_mem0 <= c_t3_t1_t0_t0

	c_t3_t1_t0_t0_mem1 = S.Task('c_t3_t1_t0_t0_mem1', length=1, delay_cost=1)
	c_t3_t1_t0_t0_mem1 += INPUT_mem_r
	S += c_t3_t1_t0_t0_mem1 <= c_t3_t1_t0_t0

	c_t3_t1_t0_t1_in = S.Task('c_t3_t1_t0_t1_in', length=1, delay_cost=1)
	c_t3_t1_t0_t1_in += alt(MUL_in)
	c_t3_t1_t0_t1 = S.Task('c_t3_t1_t0_t1', length=7, delay_cost=1)
	c_t3_t1_t0_t1 += alt(MUL)
	S += c_t3_t1_t0_t1>=c_t3_t1_t0_t1_in

	c_t3_t1_t0_t1_mem0 = S.Task('c_t3_t1_t0_t1_mem0', length=1, delay_cost=1)
	c_t3_t1_t0_t1_mem0 += INPUT_mem_r
	S += c_t3_t1_t0_t1_mem0 <= c_t3_t1_t0_t1

	c_t3_t1_t0_t1_mem1 = S.Task('c_t3_t1_t0_t1_mem1', length=1, delay_cost=1)
	c_t3_t1_t0_t1_mem1 += INPUT_mem_r
	S += c_t3_t1_t0_t1_mem1 <= c_t3_t1_t0_t1

	c_t3_t1_t0_t2 = S.Task('c_t3_t1_t0_t2', length=1, delay_cost=1)
	c_t3_t1_t0_t2 += alt(ADD)

	c_t3_t1_t0_t2_mem0 = S.Task('c_t3_t1_t0_t2_mem0', length=1, delay_cost=1)
	c_t3_t1_t0_t2_mem0 += INPUT_mem_r
	S += c_t3_t1_t0_t2_mem0 <= c_t3_t1_t0_t2

	c_t3_t1_t0_t2_mem1 = S.Task('c_t3_t1_t0_t2_mem1', length=1, delay_cost=1)
	c_t3_t1_t0_t2_mem1 += INPUT_mem_r
	S += c_t3_t1_t0_t2_mem1 <= c_t3_t1_t0_t2

	c_t3_t1_t0_t3 = S.Task('c_t3_t1_t0_t3', length=1, delay_cost=1)
	c_t3_t1_t0_t3 += alt(ADD)

	c_t3_t1_t0_t3_mem0 = S.Task('c_t3_t1_t0_t3_mem0', length=1, delay_cost=1)
	c_t3_t1_t0_t3_mem0 += INPUT_mem_r
	S += c_t3_t1_t0_t3_mem0 <= c_t3_t1_t0_t3

	c_t3_t1_t0_t3_mem1 = S.Task('c_t3_t1_t0_t3_mem1', length=1, delay_cost=1)
	c_t3_t1_t0_t3_mem1 += INPUT_mem_r
	S += c_t3_t1_t0_t3_mem1 <= c_t3_t1_t0_t3

	c_t3_t1_t1_t0_in = S.Task('c_t3_t1_t1_t0_in', length=1, delay_cost=1)
	c_t3_t1_t1_t0_in += alt(MUL_in)
	c_t3_t1_t1_t0 = S.Task('c_t3_t1_t1_t0', length=7, delay_cost=1)
	c_t3_t1_t1_t0 += alt(MUL)
	S += c_t3_t1_t1_t0>=c_t3_t1_t1_t0_in

	c_t3_t1_t1_t0_mem0 = S.Task('c_t3_t1_t1_t0_mem0', length=1, delay_cost=1)
	c_t3_t1_t1_t0_mem0 += INPUT_mem_r
	S += c_t3_t1_t1_t0_mem0 <= c_t3_t1_t1_t0

	c_t3_t1_t1_t0_mem1 = S.Task('c_t3_t1_t1_t0_mem1', length=1, delay_cost=1)
	c_t3_t1_t1_t0_mem1 += INPUT_mem_r
	S += c_t3_t1_t1_t0_mem1 <= c_t3_t1_t1_t0

	c_t3_t1_t1_t1_in = S.Task('c_t3_t1_t1_t1_in', length=1, delay_cost=1)
	c_t3_t1_t1_t1_in += alt(MUL_in)
	c_t3_t1_t1_t1 = S.Task('c_t3_t1_t1_t1', length=7, delay_cost=1)
	c_t3_t1_t1_t1 += alt(MUL)
	S += c_t3_t1_t1_t1>=c_t3_t1_t1_t1_in

	c_t3_t1_t1_t1_mem0 = S.Task('c_t3_t1_t1_t1_mem0', length=1, delay_cost=1)
	c_t3_t1_t1_t1_mem0 += INPUT_mem_r
	S += c_t3_t1_t1_t1_mem0 <= c_t3_t1_t1_t1

	c_t3_t1_t1_t1_mem1 = S.Task('c_t3_t1_t1_t1_mem1', length=1, delay_cost=1)
	c_t3_t1_t1_t1_mem1 += INPUT_mem_r
	S += c_t3_t1_t1_t1_mem1 <= c_t3_t1_t1_t1

	c_t3_t1_t1_t2 = S.Task('c_t3_t1_t1_t2', length=1, delay_cost=1)
	c_t3_t1_t1_t2 += alt(ADD)

	c_t3_t1_t1_t2_mem0 = S.Task('c_t3_t1_t1_t2_mem0', length=1, delay_cost=1)
	c_t3_t1_t1_t2_mem0 += INPUT_mem_r
	S += c_t3_t1_t1_t2_mem0 <= c_t3_t1_t1_t2

	c_t3_t1_t1_t2_mem1 = S.Task('c_t3_t1_t1_t2_mem1', length=1, delay_cost=1)
	c_t3_t1_t1_t2_mem1 += INPUT_mem_r
	S += c_t3_t1_t1_t2_mem1 <= c_t3_t1_t1_t2

	c_t3_t1_t1_t3 = S.Task('c_t3_t1_t1_t3', length=1, delay_cost=1)
	c_t3_t1_t1_t3 += alt(ADD)

	c_t3_t1_t1_t3_mem0 = S.Task('c_t3_t1_t1_t3_mem0', length=1, delay_cost=1)
	c_t3_t1_t1_t3_mem0 += INPUT_mem_r
	S += c_t3_t1_t1_t3_mem0 <= c_t3_t1_t1_t3

	c_t3_t1_t1_t3_mem1 = S.Task('c_t3_t1_t1_t3_mem1', length=1, delay_cost=1)
	c_t3_t1_t1_t3_mem1 += INPUT_mem_r
	S += c_t3_t1_t1_t3_mem1 <= c_t3_t1_t1_t3

	c_t3_t1_t20 = S.Task('c_t3_t1_t20', length=1, delay_cost=1)
	c_t3_t1_t20 += alt(ADD)

	c_t3_t1_t20_mem0 = S.Task('c_t3_t1_t20_mem0', length=1, delay_cost=1)
	c_t3_t1_t20_mem0 += INPUT_mem_r
	S += c_t3_t1_t20_mem0 <= c_t3_t1_t20

	c_t3_t1_t20_mem1 = S.Task('c_t3_t1_t20_mem1', length=1, delay_cost=1)
	c_t3_t1_t20_mem1 += INPUT_mem_r
	S += c_t3_t1_t20_mem1 <= c_t3_t1_t20

	c_t3_t1_t21 = S.Task('c_t3_t1_t21', length=1, delay_cost=1)
	c_t3_t1_t21 += alt(ADD)

	c_t3_t1_t21_mem0 = S.Task('c_t3_t1_t21_mem0', length=1, delay_cost=1)
	c_t3_t1_t21_mem0 += INPUT_mem_r
	S += c_t3_t1_t21_mem0 <= c_t3_t1_t21

	c_t3_t1_t21_mem1 = S.Task('c_t3_t1_t21_mem1', length=1, delay_cost=1)
	c_t3_t1_t21_mem1 += INPUT_mem_r
	S += c_t3_t1_t21_mem1 <= c_t3_t1_t21

	c_t3_t1_t30 = S.Task('c_t3_t1_t30', length=1, delay_cost=1)
	c_t3_t1_t30 += alt(ADD)

	c_t3_t1_t30_mem0 = S.Task('c_t3_t1_t30_mem0', length=1, delay_cost=1)
	c_t3_t1_t30_mem0 += INPUT_mem_r
	S += c_t3_t1_t30_mem0 <= c_t3_t1_t30

	c_t3_t1_t30_mem1 = S.Task('c_t3_t1_t30_mem1', length=1, delay_cost=1)
	c_t3_t1_t30_mem1 += INPUT_mem_r
	S += c_t3_t1_t30_mem1 <= c_t3_t1_t30

	c_t3_t1_t31 = S.Task('c_t3_t1_t31', length=1, delay_cost=1)
	c_t3_t1_t31 += alt(ADD)

	c_t3_t1_t31_mem0 = S.Task('c_t3_t1_t31_mem0', length=1, delay_cost=1)
	c_t3_t1_t31_mem0 += INPUT_mem_r
	S += c_t3_t1_t31_mem0 <= c_t3_t1_t31

	c_t3_t1_t31_mem1 = S.Task('c_t3_t1_t31_mem1', length=1, delay_cost=1)
	c_t3_t1_t31_mem1 += INPUT_mem_r
	S += c_t3_t1_t31_mem1 <= c_t3_t1_t31

	c_t3_t2_t0_t0_in = S.Task('c_t3_t2_t0_t0_in', length=1, delay_cost=1)
	c_t3_t2_t0_t0_in += alt(MUL_in)
	c_t3_t2_t0_t0 = S.Task('c_t3_t2_t0_t0', length=7, delay_cost=1)
	c_t3_t2_t0_t0 += alt(MUL)
	S += c_t3_t2_t0_t0>=c_t3_t2_t0_t0_in

	c_t3_t2_t0_t0_mem0 = S.Task('c_t3_t2_t0_t0_mem0', length=1, delay_cost=1)
	c_t3_t2_t0_t0_mem0 += INPUT_mem_r
	S += c_t3_t2_t0_t0_mem0 <= c_t3_t2_t0_t0

	c_t3_t2_t0_t0_mem1 = S.Task('c_t3_t2_t0_t0_mem1', length=1, delay_cost=1)
	c_t3_t2_t0_t0_mem1 += INPUT_mem_r
	S += c_t3_t2_t0_t0_mem1 <= c_t3_t2_t0_t0

	c_t3_t2_t0_t1_in = S.Task('c_t3_t2_t0_t1_in', length=1, delay_cost=1)
	c_t3_t2_t0_t1_in += alt(MUL_in)
	c_t3_t2_t0_t1 = S.Task('c_t3_t2_t0_t1', length=7, delay_cost=1)
	c_t3_t2_t0_t1 += alt(MUL)
	S += c_t3_t2_t0_t1>=c_t3_t2_t0_t1_in

	c_t3_t2_t0_t1_mem0 = S.Task('c_t3_t2_t0_t1_mem0', length=1, delay_cost=1)
	c_t3_t2_t0_t1_mem0 += INPUT_mem_r
	S += c_t3_t2_t0_t1_mem0 <= c_t3_t2_t0_t1

	c_t3_t2_t0_t1_mem1 = S.Task('c_t3_t2_t0_t1_mem1', length=1, delay_cost=1)
	c_t3_t2_t0_t1_mem1 += INPUT_mem_r
	S += c_t3_t2_t0_t1_mem1 <= c_t3_t2_t0_t1

	c_t3_t2_t0_t2 = S.Task('c_t3_t2_t0_t2', length=1, delay_cost=1)
	c_t3_t2_t0_t2 += alt(ADD)

	c_t3_t2_t0_t2_mem0 = S.Task('c_t3_t2_t0_t2_mem0', length=1, delay_cost=1)
	c_t3_t2_t0_t2_mem0 += INPUT_mem_r
	S += c_t3_t2_t0_t2_mem0 <= c_t3_t2_t0_t2

	c_t3_t2_t0_t2_mem1 = S.Task('c_t3_t2_t0_t2_mem1', length=1, delay_cost=1)
	c_t3_t2_t0_t2_mem1 += INPUT_mem_r
	S += c_t3_t2_t0_t2_mem1 <= c_t3_t2_t0_t2

	c_t3_t2_t0_t3 = S.Task('c_t3_t2_t0_t3', length=1, delay_cost=1)
	c_t3_t2_t0_t3 += alt(ADD)

	c_t3_t2_t0_t3_mem0 = S.Task('c_t3_t2_t0_t3_mem0', length=1, delay_cost=1)
	c_t3_t2_t0_t3_mem0 += INPUT_mem_r
	S += c_t3_t2_t0_t3_mem0 <= c_t3_t2_t0_t3

	c_t3_t2_t0_t3_mem1 = S.Task('c_t3_t2_t0_t3_mem1', length=1, delay_cost=1)
	c_t3_t2_t0_t3_mem1 += INPUT_mem_r
	S += c_t3_t2_t0_t3_mem1 <= c_t3_t2_t0_t3

	c_t3_t2_t1_t0_in = S.Task('c_t3_t2_t1_t0_in', length=1, delay_cost=1)
	c_t3_t2_t1_t0_in += alt(MUL_in)
	c_t3_t2_t1_t0 = S.Task('c_t3_t2_t1_t0', length=7, delay_cost=1)
	c_t3_t2_t1_t0 += alt(MUL)
	S += c_t3_t2_t1_t0>=c_t3_t2_t1_t0_in

	c_t3_t2_t1_t0_mem0 = S.Task('c_t3_t2_t1_t0_mem0', length=1, delay_cost=1)
	c_t3_t2_t1_t0_mem0 += INPUT_mem_r
	S += c_t3_t2_t1_t0_mem0 <= c_t3_t2_t1_t0

	c_t3_t2_t1_t0_mem1 = S.Task('c_t3_t2_t1_t0_mem1', length=1, delay_cost=1)
	c_t3_t2_t1_t0_mem1 += INPUT_mem_r
	S += c_t3_t2_t1_t0_mem1 <= c_t3_t2_t1_t0

	c_t3_t2_t1_t1_in = S.Task('c_t3_t2_t1_t1_in', length=1, delay_cost=1)
	c_t3_t2_t1_t1_in += alt(MUL_in)
	c_t3_t2_t1_t1 = S.Task('c_t3_t2_t1_t1', length=7, delay_cost=1)
	c_t3_t2_t1_t1 += alt(MUL)
	S += c_t3_t2_t1_t1>=c_t3_t2_t1_t1_in

	c_t3_t2_t1_t1_mem0 = S.Task('c_t3_t2_t1_t1_mem0', length=1, delay_cost=1)
	c_t3_t2_t1_t1_mem0 += INPUT_mem_r
	S += c_t3_t2_t1_t1_mem0 <= c_t3_t2_t1_t1

	c_t3_t2_t1_t1_mem1 = S.Task('c_t3_t2_t1_t1_mem1', length=1, delay_cost=1)
	c_t3_t2_t1_t1_mem1 += INPUT_mem_r
	S += c_t3_t2_t1_t1_mem1 <= c_t3_t2_t1_t1

	c_t3_t2_t1_t2 = S.Task('c_t3_t2_t1_t2', length=1, delay_cost=1)
	c_t3_t2_t1_t2 += alt(ADD)

	c_t3_t2_t1_t2_mem0 = S.Task('c_t3_t2_t1_t2_mem0', length=1, delay_cost=1)
	c_t3_t2_t1_t2_mem0 += INPUT_mem_r
	S += c_t3_t2_t1_t2_mem0 <= c_t3_t2_t1_t2

	c_t3_t2_t1_t2_mem1 = S.Task('c_t3_t2_t1_t2_mem1', length=1, delay_cost=1)
	c_t3_t2_t1_t2_mem1 += INPUT_mem_r
	S += c_t3_t2_t1_t2_mem1 <= c_t3_t2_t1_t2

	c_t3_t2_t1_t3 = S.Task('c_t3_t2_t1_t3', length=1, delay_cost=1)
	c_t3_t2_t1_t3 += alt(ADD)

	c_t3_t2_t1_t3_mem0 = S.Task('c_t3_t2_t1_t3_mem0', length=1, delay_cost=1)
	c_t3_t2_t1_t3_mem0 += INPUT_mem_r
	S += c_t3_t2_t1_t3_mem0 <= c_t3_t2_t1_t3

	c_t3_t2_t1_t3_mem1 = S.Task('c_t3_t2_t1_t3_mem1', length=1, delay_cost=1)
	c_t3_t2_t1_t3_mem1 += INPUT_mem_r
	S += c_t3_t2_t1_t3_mem1 <= c_t3_t2_t1_t3

	c_t3_t2_t20 = S.Task('c_t3_t2_t20', length=1, delay_cost=1)
	c_t3_t2_t20 += alt(ADD)

	c_t3_t2_t20_mem0 = S.Task('c_t3_t2_t20_mem0', length=1, delay_cost=1)
	c_t3_t2_t20_mem0 += INPUT_mem_r
	S += c_t3_t2_t20_mem0 <= c_t3_t2_t20

	c_t3_t2_t20_mem1 = S.Task('c_t3_t2_t20_mem1', length=1, delay_cost=1)
	c_t3_t2_t20_mem1 += INPUT_mem_r
	S += c_t3_t2_t20_mem1 <= c_t3_t2_t20

	c_t3_t2_t21 = S.Task('c_t3_t2_t21', length=1, delay_cost=1)
	c_t3_t2_t21 += alt(ADD)

	c_t3_t2_t21_mem0 = S.Task('c_t3_t2_t21_mem0', length=1, delay_cost=1)
	c_t3_t2_t21_mem0 += INPUT_mem_r
	S += c_t3_t2_t21_mem0 <= c_t3_t2_t21

	c_t3_t2_t21_mem1 = S.Task('c_t3_t2_t21_mem1', length=1, delay_cost=1)
	c_t3_t2_t21_mem1 += INPUT_mem_r
	S += c_t3_t2_t21_mem1 <= c_t3_t2_t21

	c_t3_t2_t30 = S.Task('c_t3_t2_t30', length=1, delay_cost=1)
	c_t3_t2_t30 += alt(ADD)

	c_t3_t2_t30_mem0 = S.Task('c_t3_t2_t30_mem0', length=1, delay_cost=1)
	c_t3_t2_t30_mem0 += INPUT_mem_r
	S += c_t3_t2_t30_mem0 <= c_t3_t2_t30

	c_t3_t2_t30_mem1 = S.Task('c_t3_t2_t30_mem1', length=1, delay_cost=1)
	c_t3_t2_t30_mem1 += INPUT_mem_r
	S += c_t3_t2_t30_mem1 <= c_t3_t2_t30

	c_t3_t2_t31 = S.Task('c_t3_t2_t31', length=1, delay_cost=1)
	c_t3_t2_t31 += alt(ADD)

	c_t3_t2_t31_mem0 = S.Task('c_t3_t2_t31_mem0', length=1, delay_cost=1)
	c_t3_t2_t31_mem0 += INPUT_mem_r
	S += c_t3_t2_t31_mem0 <= c_t3_t2_t31

	c_t3_t2_t31_mem1 = S.Task('c_t3_t2_t31_mem1', length=1, delay_cost=1)
	c_t3_t2_t31_mem1 += INPUT_mem_r
	S += c_t3_t2_t31_mem1 <= c_t3_t2_t31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/SQR_mul1_add4/SQR_1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

