from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 175
	S = Scenario("SQR_3", horizon=horizon)

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

	c_t3_t2_t1_t0_in = S.Task('c_t3_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t2_t1_t0_in >= 30
	c_t3_t2_t1_t0_in += MUL_in[0]

	c_t3_t2_t1_t0_mem0 = S.Task('c_t3_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t1_t0_mem0 >= 30
	c_t3_t2_t1_t0_mem0 += INPUT_mem_r

	c_t3_t2_t1_t0_mem1 = S.Task('c_t3_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t1_t0_mem1 >= 30
	c_t3_t2_t1_t0_mem1 += INPUT_mem_r

	c_t3_t2_t0_t1_in = S.Task('c_t3_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t2_t0_t1_in >= 31
	c_t3_t2_t0_t1_in += MUL_in[0]

	c_t3_t2_t0_t1_mem0 = S.Task('c_t3_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t0_t1_mem0 >= 31
	c_t3_t2_t0_t1_mem0 += INPUT_mem_r

	c_t3_t2_t0_t1_mem1 = S.Task('c_t3_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t0_t1_mem1 >= 31
	c_t3_t2_t0_t1_mem1 += INPUT_mem_r

	c_t3_t2_t1_t0 = S.Task('c_t3_t2_t1_t0', length=7, delay_cost=1)
	S += c_t3_t2_t1_t0 >= 31
	c_t3_t2_t1_t0 += MUL[0]

	c_t3_t2_t0_t1 = S.Task('c_t3_t2_t0_t1', length=7, delay_cost=1)
	S += c_t3_t2_t0_t1 >= 32
	c_t3_t2_t0_t1 += MUL[0]

	c_t3_t2_t1_t1_in = S.Task('c_t3_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t2_t1_t1_in >= 32
	c_t3_t2_t1_t1_in += MUL_in[0]

	c_t3_t2_t1_t1_mem0 = S.Task('c_t3_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t1_t1_mem0 >= 32
	c_t3_t2_t1_t1_mem0 += INPUT_mem_r

	c_t3_t2_t1_t1_mem1 = S.Task('c_t3_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t1_t1_mem1 >= 32
	c_t3_t2_t1_t1_mem1 += INPUT_mem_r

	c_t3_t2_t0_t0_in = S.Task('c_t3_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t2_t0_t0_in >= 33
	c_t3_t2_t0_t0_in += MUL_in[0]

	c_t3_t2_t0_t0_mem0 = S.Task('c_t3_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t0_t0_mem0 >= 33
	c_t3_t2_t0_t0_mem0 += INPUT_mem_r

	c_t3_t2_t0_t0_mem1 = S.Task('c_t3_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t0_t0_mem1 >= 33
	c_t3_t2_t0_t0_mem1 += INPUT_mem_r

	c_t3_t2_t1_t1 = S.Task('c_t3_t2_t1_t1', length=7, delay_cost=1)
	S += c_t3_t2_t1_t1 >= 33
	c_t3_t2_t1_t1 += MUL[0]

	c_t3_t1_t1_t1_in = S.Task('c_t3_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_t1_in >= 34
	c_t3_t1_t1_t1_in += MUL_in[0]

	c_t3_t1_t1_t1_mem0 = S.Task('c_t3_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_t1_mem0 >= 34
	c_t3_t1_t1_t1_mem0 += INPUT_mem_r

	c_t3_t1_t1_t1_mem1 = S.Task('c_t3_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_t1_mem1 >= 34
	c_t3_t1_t1_t1_mem1 += INPUT_mem_r

	c_t3_t2_t0_t0 = S.Task('c_t3_t2_t0_t0', length=7, delay_cost=1)
	S += c_t3_t2_t0_t0 >= 34
	c_t3_t2_t0_t0 += MUL[0]

	c_t3_t1_t1_t0_in = S.Task('c_t3_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_t0_in >= 35
	c_t3_t1_t1_t0_in += MUL_in[0]

	c_t3_t1_t1_t0_mem0 = S.Task('c_t3_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_t0_mem0 >= 35
	c_t3_t1_t1_t0_mem0 += INPUT_mem_r

	c_t3_t1_t1_t0_mem1 = S.Task('c_t3_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_t0_mem1 >= 35
	c_t3_t1_t1_t0_mem1 += INPUT_mem_r

	c_t3_t1_t1_t1 = S.Task('c_t3_t1_t1_t1', length=7, delay_cost=1)
	S += c_t3_t1_t1_t1 >= 35
	c_t3_t1_t1_t1 += MUL[0]

	c_t3_t1_t0_t1_in = S.Task('c_t3_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_t1_in >= 36
	c_t3_t1_t0_t1_in += MUL_in[0]

	c_t3_t1_t0_t1_mem0 = S.Task('c_t3_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_t1_mem0 >= 36
	c_t3_t1_t0_t1_mem0 += INPUT_mem_r

	c_t3_t1_t0_t1_mem1 = S.Task('c_t3_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_t1_mem1 >= 36
	c_t3_t1_t0_t1_mem1 += INPUT_mem_r

	c_t3_t1_t1_t0 = S.Task('c_t3_t1_t1_t0', length=7, delay_cost=1)
	S += c_t3_t1_t1_t0 >= 36
	c_t3_t1_t1_t0 += MUL[0]

	c_t3_t1_t0_t0_in = S.Task('c_t3_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_t0_in >= 37
	c_t3_t1_t0_t0_in += MUL_in[0]

	c_t3_t1_t0_t0_mem0 = S.Task('c_t3_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_t0_mem0 >= 37
	c_t3_t1_t0_t0_mem0 += INPUT_mem_r

	c_t3_t1_t0_t0_mem1 = S.Task('c_t3_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_t0_mem1 >= 37
	c_t3_t1_t0_t0_mem1 += INPUT_mem_r

	c_t3_t1_t0_t1 = S.Task('c_t3_t1_t0_t1', length=7, delay_cost=1)
	S += c_t3_t1_t0_t1 >= 37
	c_t3_t1_t0_t1 += MUL[0]

	c_t3_t1_t0_t0 = S.Task('c_t3_t1_t0_t0', length=7, delay_cost=1)
	S += c_t3_t1_t0_t0 >= 38
	c_t3_t1_t0_t0 += MUL[0]

	c_t3_t2_t30_mem0 = S.Task('c_t3_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t30_mem0 >= 38
	c_t3_t2_t30_mem0 += INPUT_mem_r

	c_t3_t2_t30_mem1 = S.Task('c_t3_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t30_mem1 >= 38
	c_t3_t2_t30_mem1 += INPUT_mem_r

	c_t3_t0_t1_t3_mem0 = S.Task('c_t3_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_t3_mem0 >= 39
	c_t3_t0_t1_t3_mem0 += INPUT_mem_r

	c_t3_t0_t1_t3_mem1 = S.Task('c_t3_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_t3_mem1 >= 39
	c_t3_t0_t1_t3_mem1 += INPUT_mem_r

	c_t3_t2_t30 = S.Task('c_t3_t2_t30', length=1, delay_cost=1)
	S += c_t3_t2_t30 >= 39
	c_t3_t2_t30 += ADD[2]

	c_t3_t0_t1_t3 = S.Task('c_t3_t0_t1_t3', length=1, delay_cost=1)
	S += c_t3_t0_t1_t3 >= 40
	c_t3_t0_t1_t3 += ADD[0]

	c_t3_t1_t0_t2_mem0 = S.Task('c_t3_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_t2_mem0 >= 40
	c_t3_t1_t0_t2_mem0 += INPUT_mem_r

	c_t3_t1_t0_t2_mem1 = S.Task('c_t3_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_t2_mem1 >= 40
	c_t3_t1_t0_t2_mem1 += INPUT_mem_r

	c_t3_t1_t0_t2 = S.Task('c_t3_t1_t0_t2', length=1, delay_cost=1)
	S += c_t3_t1_t0_t2 >= 41
	c_t3_t1_t0_t2 += ADD[3]

	c_t3_t2_t1_t3_mem0 = S.Task('c_t3_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t1_t3_mem0 >= 41
	c_t3_t2_t1_t3_mem0 += INPUT_mem_r

	c_t3_t2_t1_t3_mem1 = S.Task('c_t3_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t1_t3_mem1 >= 41
	c_t3_t2_t1_t3_mem1 += INPUT_mem_r

	c_t3_t2_t0_t3_mem0 = S.Task('c_t3_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t0_t3_mem0 >= 42
	c_t3_t2_t0_t3_mem0 += INPUT_mem_r

	c_t3_t2_t0_t3_mem1 = S.Task('c_t3_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t0_t3_mem1 >= 42
	c_t3_t2_t0_t3_mem1 += INPUT_mem_r

	c_t3_t2_t1_t3 = S.Task('c_t3_t2_t1_t3', length=1, delay_cost=1)
	S += c_t3_t2_t1_t3 >= 42
	c_t3_t2_t1_t3 += ADD[0]

	c_t3_t0_t31_mem0 = S.Task('c_t3_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t31_mem0 >= 43
	c_t3_t0_t31_mem0 += INPUT_mem_r

	c_t3_t0_t31_mem1 = S.Task('c_t3_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t31_mem1 >= 43
	c_t3_t0_t31_mem1 += INPUT_mem_r

	c_t3_t2_t0_t3 = S.Task('c_t3_t2_t0_t3', length=1, delay_cost=1)
	S += c_t3_t2_t0_t3 >= 43
	c_t3_t2_t0_t3 += ADD[0]

	c_t3_t0_t20_mem0 = S.Task('c_t3_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t20_mem0 >= 44
	c_t3_t0_t20_mem0 += INPUT_mem_r

	c_t3_t0_t20_mem1 = S.Task('c_t3_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t20_mem1 >= 44
	c_t3_t0_t20_mem1 += INPUT_mem_r

	c_t3_t0_t31 = S.Task('c_t3_t0_t31', length=1, delay_cost=1)
	S += c_t3_t0_t31 >= 44
	c_t3_t0_t31 += ADD[1]

	c_t3_t0_t20 = S.Task('c_t3_t0_t20', length=1, delay_cost=1)
	S += c_t3_t0_t20 >= 45
	c_t3_t0_t20 += ADD[2]

	c_t3_t0_t21_mem0 = S.Task('c_t3_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t21_mem0 >= 45
	c_t3_t0_t21_mem0 += INPUT_mem_r

	c_t3_t0_t21_mem1 = S.Task('c_t3_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t21_mem1 >= 45
	c_t3_t0_t21_mem1 += INPUT_mem_r

	c_t3_t0_t21 = S.Task('c_t3_t0_t21', length=1, delay_cost=1)
	S += c_t3_t0_t21 >= 46
	c_t3_t0_t21 += ADD[3]

	c_t3_t0_t30_mem0 = S.Task('c_t3_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t30_mem0 >= 46
	c_t3_t0_t30_mem0 += INPUT_mem_r

	c_t3_t0_t30_mem1 = S.Task('c_t3_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t30_mem1 >= 46
	c_t3_t0_t30_mem1 += INPUT_mem_r

	c_t3_t0_t30 = S.Task('c_t3_t0_t30', length=1, delay_cost=1)
	S += c_t3_t0_t30 >= 47
	c_t3_t0_t30 += ADD[3]

	c_t3_t2_t21_mem0 = S.Task('c_t3_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t21_mem0 >= 47
	c_t3_t2_t21_mem0 += INPUT_mem_r

	c_t3_t2_t21_mem1 = S.Task('c_t3_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t21_mem1 >= 47
	c_t3_t2_t21_mem1 += INPUT_mem_r

	c_t3_t2_t0_t2_mem0 = S.Task('c_t3_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t0_t2_mem0 >= 48
	c_t3_t2_t0_t2_mem0 += INPUT_mem_r

	c_t3_t2_t0_t2_mem1 = S.Task('c_t3_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t0_t2_mem1 >= 48
	c_t3_t2_t0_t2_mem1 += INPUT_mem_r

	c_t3_t2_t21 = S.Task('c_t3_t2_t21', length=1, delay_cost=1)
	S += c_t3_t2_t21 >= 48
	c_t3_t2_t21 += ADD[0]

	c_t3_t2_t0_t2 = S.Task('c_t3_t2_t0_t2', length=1, delay_cost=1)
	S += c_t3_t2_t0_t2 >= 49
	c_t3_t2_t0_t2 += ADD[1]

	c_t3_t2_t20_mem0 = S.Task('c_t3_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t20_mem0 >= 49
	c_t3_t2_t20_mem0 += INPUT_mem_r

	c_t3_t2_t20_mem1 = S.Task('c_t3_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t20_mem1 >= 49
	c_t3_t2_t20_mem1 += INPUT_mem_r

	c_t3_t2_t1_t2_mem0 = S.Task('c_t3_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t1_t2_mem0 >= 50
	c_t3_t2_t1_t2_mem0 += INPUT_mem_r

	c_t3_t2_t1_t2_mem1 = S.Task('c_t3_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t1_t2_mem1 >= 50
	c_t3_t2_t1_t2_mem1 += INPUT_mem_r

	c_t3_t2_t20 = S.Task('c_t3_t2_t20', length=1, delay_cost=1)
	S += c_t3_t2_t20 >= 50
	c_t3_t2_t20 += ADD[3]

	c_t3_t2_t1_t2 = S.Task('c_t3_t2_t1_t2', length=1, delay_cost=1)
	S += c_t3_t2_t1_t2 >= 51
	c_t3_t2_t1_t2 += ADD[1]

	c_t3_t2_t31_mem0 = S.Task('c_t3_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t31_mem0 >= 51
	c_t3_t2_t31_mem0 += INPUT_mem_r

	c_t3_t2_t31_mem1 = S.Task('c_t3_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t31_mem1 >= 51
	c_t3_t2_t31_mem1 += INPUT_mem_r

	c_t3_t1_t31_mem0 = S.Task('c_t3_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t31_mem0 >= 52
	c_t3_t1_t31_mem0 += INPUT_mem_r

	c_t3_t1_t31_mem1 = S.Task('c_t3_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t31_mem1 >= 52
	c_t3_t1_t31_mem1 += INPUT_mem_r

	c_t3_t2_t31 = S.Task('c_t3_t2_t31', length=1, delay_cost=1)
	S += c_t3_t2_t31 >= 52
	c_t3_t2_t31 += ADD[0]

	c_t3_t1_t30_mem0 = S.Task('c_t3_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t30_mem0 >= 53
	c_t3_t1_t30_mem0 += INPUT_mem_r

	c_t3_t1_t30_mem1 = S.Task('c_t3_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t30_mem1 >= 53
	c_t3_t1_t30_mem1 += INPUT_mem_r

	c_t3_t1_t31 = S.Task('c_t3_t1_t31', length=1, delay_cost=1)
	S += c_t3_t1_t31 >= 53
	c_t3_t1_t31 += ADD[2]

	c_t3_t1_t21_mem0 = S.Task('c_t3_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t21_mem0 >= 54
	c_t3_t1_t21_mem0 += INPUT_mem_r

	c_t3_t1_t21_mem1 = S.Task('c_t3_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t21_mem1 >= 54
	c_t3_t1_t21_mem1 += INPUT_mem_r

	c_t3_t1_t30 = S.Task('c_t3_t1_t30', length=1, delay_cost=1)
	S += c_t3_t1_t30 >= 54
	c_t3_t1_t30 += ADD[0]

	c_t3_t1_t20_mem0 = S.Task('c_t3_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t20_mem0 >= 55
	c_t3_t1_t20_mem0 += INPUT_mem_r

	c_t3_t1_t20_mem1 = S.Task('c_t3_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t20_mem1 >= 55
	c_t3_t1_t20_mem1 += INPUT_mem_r

	c_t3_t1_t21 = S.Task('c_t3_t1_t21', length=1, delay_cost=1)
	S += c_t3_t1_t21 >= 55
	c_t3_t1_t21 += ADD[0]

	c_t3_t0_t1_t2_mem0 = S.Task('c_t3_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_t2_mem0 >= 56
	c_t3_t0_t1_t2_mem0 += INPUT_mem_r

	c_t3_t0_t1_t2_mem1 = S.Task('c_t3_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_t2_mem1 >= 56
	c_t3_t0_t1_t2_mem1 += INPUT_mem_r

	c_t3_t1_t20 = S.Task('c_t3_t1_t20', length=1, delay_cost=1)
	S += c_t3_t1_t20 >= 56
	c_t3_t1_t20 += ADD[0]

	c_t3_t0_t1_t2 = S.Task('c_t3_t0_t1_t2', length=1, delay_cost=1)
	S += c_t3_t0_t1_t2 >= 57
	c_t3_t0_t1_t2 += ADD[0]

	c_t3_t1_t1_t3_mem0 = S.Task('c_t3_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_t3_mem0 >= 57
	c_t3_t1_t1_t3_mem0 += INPUT_mem_r

	c_t3_t1_t1_t3_mem1 = S.Task('c_t3_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_t3_mem1 >= 57
	c_t3_t1_t1_t3_mem1 += INPUT_mem_r

	c_t3_t1_t1_t2_mem0 = S.Task('c_t3_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_t2_mem0 >= 58
	c_t3_t1_t1_t2_mem0 += INPUT_mem_r

	c_t3_t1_t1_t2_mem1 = S.Task('c_t3_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_t2_mem1 >= 58
	c_t3_t1_t1_t2_mem1 += INPUT_mem_r

	c_t3_t1_t1_t3 = S.Task('c_t3_t1_t1_t3', length=1, delay_cost=1)
	S += c_t3_t1_t1_t3 >= 58
	c_t3_t1_t1_t3 += ADD[0]

	c_t3_t1_t0_t3_mem0 = S.Task('c_t3_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_t3_mem0 >= 59
	c_t3_t1_t0_t3_mem0 += INPUT_mem_r

	c_t3_t1_t0_t3_mem1 = S.Task('c_t3_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_t3_mem1 >= 59
	c_t3_t1_t0_t3_mem1 += INPUT_mem_r

	c_t3_t1_t1_t2 = S.Task('c_t3_t1_t1_t2', length=1, delay_cost=1)
	S += c_t3_t1_t1_t2 >= 59
	c_t3_t1_t1_t2 += ADD[0]

	c_t3_t1_t0_t3 = S.Task('c_t3_t1_t0_t3', length=1, delay_cost=1)
	S += c_t3_t1_t0_t3 >= 60
	c_t3_t1_t0_t3 += ADD[0]

	c_t3_t3101_mem0 = S.Task('c_t3_t3101_mem0', length=1, delay_cost=1)
	S += c_t3_t3101_mem0 >= 60
	c_t3_t3101_mem0 += INPUT_mem_r

	c_t3_t3101_mem1 = S.Task('c_t3_t3101_mem1', length=1, delay_cost=1)
	S += c_t3_t3101_mem1 >= 60
	c_t3_t3101_mem1 += INPUT_mem_r

	c_t3_t3101 = S.Task('c_t3_t3101', length=1, delay_cost=1)
	S += c_t3_t3101 >= 61
	c_t3_t3101 += ADD[0]

	c_t3_t3110_mem0 = S.Task('c_t3_t3110_mem0', length=1, delay_cost=1)
	S += c_t3_t3110_mem0 >= 61
	c_t3_t3110_mem0 += INPUT_mem_r

	c_t3_t3110_mem1 = S.Task('c_t3_t3110_mem1', length=1, delay_cost=1)
	S += c_t3_t3110_mem1 >= 61
	c_t3_t3110_mem1 += INPUT_mem_r

	c_t3_t3110 = S.Task('c_t3_t3110', length=1, delay_cost=1)
	S += c_t3_t3110 >= 62
	c_t3_t3110 += ADD[0]

	c_t3_t3111_mem0 = S.Task('c_t3_t3111_mem0', length=1, delay_cost=1)
	S += c_t3_t3111_mem0 >= 62
	c_t3_t3111_mem0 += INPUT_mem_r

	c_t3_t3111_mem1 = S.Task('c_t3_t3111_mem1', length=1, delay_cost=1)
	S += c_t3_t3111_mem1 >= 62
	c_t3_t3111_mem1 += INPUT_mem_r

	c_t3_t3111 = S.Task('c_t3_t3111', length=1, delay_cost=1)
	S += c_t3_t3111 >= 63
	c_t3_t3111 += ADD[2]

	c_t3_t4000_mem0 = S.Task('c_t3_t4000_mem0', length=1, delay_cost=1)
	S += c_t3_t4000_mem0 >= 63
	c_t3_t4000_mem0 += INPUT_mem_r

	c_t3_t4000_mem1 = S.Task('c_t3_t4000_mem1', length=1, delay_cost=1)
	S += c_t3_t4000_mem1 >= 63
	c_t3_t4000_mem1 += INPUT_mem_r

	c_t3_t4000 = S.Task('c_t3_t4000', length=1, delay_cost=1)
	S += c_t3_t4000 >= 64
	c_t3_t4000 += ADD[0]

	c_t3_t4001_mem0 = S.Task('c_t3_t4001_mem0', length=1, delay_cost=1)
	S += c_t3_t4001_mem0 >= 64
	c_t3_t4001_mem0 += INPUT_mem_r

	c_t3_t4001_mem1 = S.Task('c_t3_t4001_mem1', length=1, delay_cost=1)
	S += c_t3_t4001_mem1 >= 64
	c_t3_t4001_mem1 += INPUT_mem_r

	c_t3_t4001 = S.Task('c_t3_t4001', length=1, delay_cost=1)
	S += c_t3_t4001 >= 65
	c_t3_t4001 += ADD[0]

	c_t3_t4010_mem0 = S.Task('c_t3_t4010_mem0', length=1, delay_cost=1)
	S += c_t3_t4010_mem0 >= 65
	c_t3_t4010_mem0 += INPUT_mem_r

	c_t3_t4010_mem1 = S.Task('c_t3_t4010_mem1', length=1, delay_cost=1)
	S += c_t3_t4010_mem1 >= 65
	c_t3_t4010_mem1 += INPUT_mem_r

	c_t3_t4010 = S.Task('c_t3_t4010', length=1, delay_cost=1)
	S += c_t3_t4010 >= 66
	c_t3_t4010 += ADD[0]

	c_t3_t4011_mem0 = S.Task('c_t3_t4011_mem0', length=1, delay_cost=1)
	S += c_t3_t4011_mem0 >= 66
	c_t3_t4011_mem0 += INPUT_mem_r

	c_t3_t4011_mem1 = S.Task('c_t3_t4011_mem1', length=1, delay_cost=1)
	S += c_t3_t4011_mem1 >= 66
	c_t3_t4011_mem1 += INPUT_mem_r

	c_t3_t4011 = S.Task('c_t3_t4011', length=1, delay_cost=1)
	S += c_t3_t4011 >= 67
	c_t3_t4011 += ADD[0]

	c_t3_t4100_mem0 = S.Task('c_t3_t4100_mem0', length=1, delay_cost=1)
	S += c_t3_t4100_mem0 >= 67
	c_t3_t4100_mem0 += INPUT_mem_r

	c_t3_t4100_mem1 = S.Task('c_t3_t4100_mem1', length=1, delay_cost=1)
	S += c_t3_t4100_mem1 >= 67
	c_t3_t4100_mem1 += INPUT_mem_r

	c_t3_t4100 = S.Task('c_t3_t4100', length=1, delay_cost=1)
	S += c_t3_t4100 >= 68
	c_t3_t4100 += ADD[0]

	c_t3_t4101_mem0 = S.Task('c_t3_t4101_mem0', length=1, delay_cost=1)
	S += c_t3_t4101_mem0 >= 68
	c_t3_t4101_mem0 += INPUT_mem_r

	c_t3_t4101_mem1 = S.Task('c_t3_t4101_mem1', length=1, delay_cost=1)
	S += c_t3_t4101_mem1 >= 68
	c_t3_t4101_mem1 += INPUT_mem_r

	c_t3_t4101 = S.Task('c_t3_t4101', length=1, delay_cost=1)
	S += c_t3_t4101 >= 69
	c_t3_t4101 += ADD[0]

	c_t3_t4110_mem0 = S.Task('c_t3_t4110_mem0', length=1, delay_cost=1)
	S += c_t3_t4110_mem0 >= 69
	c_t3_t4110_mem0 += INPUT_mem_r

	c_t3_t4110_mem1 = S.Task('c_t3_t4110_mem1', length=1, delay_cost=1)
	S += c_t3_t4110_mem1 >= 69
	c_t3_t4110_mem1 += INPUT_mem_r

	c_t3_t4110 = S.Task('c_t3_t4110', length=1, delay_cost=1)
	S += c_t3_t4110 >= 70
	c_t3_t4110 += ADD[0]

	c_t3_t4111_mem0 = S.Task('c_t3_t4111_mem0', length=1, delay_cost=1)
	S += c_t3_t4111_mem0 >= 70
	c_t3_t4111_mem0 += INPUT_mem_r

	c_t3_t4111_mem1 = S.Task('c_t3_t4111_mem1', length=1, delay_cost=1)
	S += c_t3_t4111_mem1 >= 70
	c_t3_t4111_mem1 += INPUT_mem_r

	c_t3_t3000_mem0 = S.Task('c_t3_t3000_mem0', length=1, delay_cost=1)
	S += c_t3_t3000_mem0 >= 71
	c_t3_t3000_mem0 += INPUT_mem_r

	c_t3_t3000_mem1 = S.Task('c_t3_t3000_mem1', length=1, delay_cost=1)
	S += c_t3_t3000_mem1 >= 71
	c_t3_t3000_mem1 += INPUT_mem_r

	c_t3_t4111 = S.Task('c_t3_t4111', length=1, delay_cost=1)
	S += c_t3_t4111 >= 71
	c_t3_t4111 += ADD[0]

	c_t3_t3000 = S.Task('c_t3_t3000', length=1, delay_cost=1)
	S += c_t3_t3000 >= 72
	c_t3_t3000 += ADD[0]

	c_t3_t5000_mem0 = S.Task('c_t3_t5000_mem0', length=1, delay_cost=1)
	S += c_t3_t5000_mem0 >= 72
	c_t3_t5000_mem0 += INPUT_mem_r

	c_t3_t5000_mem1 = S.Task('c_t3_t5000_mem1', length=1, delay_cost=1)
	S += c_t3_t5000_mem1 >= 72
	c_t3_t5000_mem1 += INPUT_mem_r

	c_t3_t5000 = S.Task('c_t3_t5000', length=1, delay_cost=1)
	S += c_t3_t5000 >= 73
	c_t3_t5000 += ADD[1]

	c_t3_t5001_mem0 = S.Task('c_t3_t5001_mem0', length=1, delay_cost=1)
	S += c_t3_t5001_mem0 >= 73
	c_t3_t5001_mem0 += INPUT_mem_r

	c_t3_t5001_mem1 = S.Task('c_t3_t5001_mem1', length=1, delay_cost=1)
	S += c_t3_t5001_mem1 >= 73
	c_t3_t5001_mem1 += INPUT_mem_r

	c_t3_t5001 = S.Task('c_t3_t5001', length=1, delay_cost=1)
	S += c_t3_t5001 >= 74
	c_t3_t5001 += ADD[1]

	c_t3_t5010_mem0 = S.Task('c_t3_t5010_mem0', length=1, delay_cost=1)
	S += c_t3_t5010_mem0 >= 74
	c_t3_t5010_mem0 += INPUT_mem_r

	c_t3_t5010_mem1 = S.Task('c_t3_t5010_mem1', length=1, delay_cost=1)
	S += c_t3_t5010_mem1 >= 74
	c_t3_t5010_mem1 += INPUT_mem_r

	c_t3_t5010 = S.Task('c_t3_t5010', length=1, delay_cost=1)
	S += c_t3_t5010 >= 75
	c_t3_t5010 += ADD[0]

	c_t3_t5011_mem0 = S.Task('c_t3_t5011_mem0', length=1, delay_cost=1)
	S += c_t3_t5011_mem0 >= 75
	c_t3_t5011_mem0 += INPUT_mem_r

	c_t3_t5011_mem1 = S.Task('c_t3_t5011_mem1', length=1, delay_cost=1)
	S += c_t3_t5011_mem1 >= 75
	c_t3_t5011_mem1 += INPUT_mem_r

	c_t3_t5011 = S.Task('c_t3_t5011', length=1, delay_cost=1)
	S += c_t3_t5011 >= 76
	c_t3_t5011 += ADD[0]

	c_t3_t5100_mem0 = S.Task('c_t3_t5100_mem0', length=1, delay_cost=1)
	S += c_t3_t5100_mem0 >= 76
	c_t3_t5100_mem0 += INPUT_mem_r

	c_t3_t5100_mem1 = S.Task('c_t3_t5100_mem1', length=1, delay_cost=1)
	S += c_t3_t5100_mem1 >= 76
	c_t3_t5100_mem1 += INPUT_mem_r

	c_t3_t5100 = S.Task('c_t3_t5100', length=1, delay_cost=1)
	S += c_t3_t5100 >= 77
	c_t3_t5100 += ADD[0]

	c_t3_t5101_mem0 = S.Task('c_t3_t5101_mem0', length=1, delay_cost=1)
	S += c_t3_t5101_mem0 >= 77
	c_t3_t5101_mem0 += INPUT_mem_r

	c_t3_t5101_mem1 = S.Task('c_t3_t5101_mem1', length=1, delay_cost=1)
	S += c_t3_t5101_mem1 >= 77
	c_t3_t5101_mem1 += INPUT_mem_r

	c_t3_t5101 = S.Task('c_t3_t5101', length=1, delay_cost=1)
	S += c_t3_t5101 >= 78
	c_t3_t5101 += ADD[0]

	c_t3_t5110_mem0 = S.Task('c_t3_t5110_mem0', length=1, delay_cost=1)
	S += c_t3_t5110_mem0 >= 78
	c_t3_t5110_mem0 += INPUT_mem_r

	c_t3_t5110_mem1 = S.Task('c_t3_t5110_mem1', length=1, delay_cost=1)
	S += c_t3_t5110_mem1 >= 78
	c_t3_t5110_mem1 += INPUT_mem_r

	c_t3_t5110 = S.Task('c_t3_t5110', length=1, delay_cost=1)
	S += c_t3_t5110 >= 79
	c_t3_t5110 += ADD[0]

	c_t3_t5111_mem0 = S.Task('c_t3_t5111_mem0', length=1, delay_cost=1)
	S += c_t3_t5111_mem0 >= 79
	c_t3_t5111_mem0 += INPUT_mem_r

	c_t3_t5111_mem1 = S.Task('c_t3_t5111_mem1', length=1, delay_cost=1)
	S += c_t3_t5111_mem1 >= 79
	c_t3_t5111_mem1 += INPUT_mem_r

	c_t3_t3001_mem0 = S.Task('c_t3_t3001_mem0', length=1, delay_cost=1)
	S += c_t3_t3001_mem0 >= 80
	c_t3_t3001_mem0 += INPUT_mem_r

	c_t3_t3001_mem1 = S.Task('c_t3_t3001_mem1', length=1, delay_cost=1)
	S += c_t3_t3001_mem1 >= 80
	c_t3_t3001_mem1 += INPUT_mem_r

	c_t3_t5111 = S.Task('c_t3_t5111', length=1, delay_cost=1)
	S += c_t3_t5111 >= 80
	c_t3_t5111 += ADD[0]

	c_t3_t3001 = S.Task('c_t3_t3001', length=1, delay_cost=1)
	S += c_t3_t3001 >= 81
	c_t3_t3001 += ADD[0]

	c_t3_t3010_mem0 = S.Task('c_t3_t3010_mem0', length=1, delay_cost=1)
	S += c_t3_t3010_mem0 >= 81
	c_t3_t3010_mem0 += INPUT_mem_r

	c_t3_t3010_mem1 = S.Task('c_t3_t3010_mem1', length=1, delay_cost=1)
	S += c_t3_t3010_mem1 >= 81
	c_t3_t3010_mem1 += INPUT_mem_r

	c_t3_t3010 = S.Task('c_t3_t3010', length=1, delay_cost=1)
	S += c_t3_t3010 >= 82
	c_t3_t3010 += ADD[0]

	c_t3_t3011_mem0 = S.Task('c_t3_t3011_mem0', length=1, delay_cost=1)
	S += c_t3_t3011_mem0 >= 82
	c_t3_t3011_mem0 += INPUT_mem_r

	c_t3_t3011_mem1 = S.Task('c_t3_t3011_mem1', length=1, delay_cost=1)
	S += c_t3_t3011_mem1 >= 82
	c_t3_t3011_mem1 += INPUT_mem_r

	c_t3_t3011 = S.Task('c_t3_t3011', length=1, delay_cost=1)
	S += c_t3_t3011 >= 83
	c_t3_t3011 += ADD[3]

	c_t3_t3100_mem0 = S.Task('c_t3_t3100_mem0', length=1, delay_cost=1)
	S += c_t3_t3100_mem0 >= 83
	c_t3_t3100_mem0 += INPUT_mem_r

	c_t3_t3100_mem1 = S.Task('c_t3_t3100_mem1', length=1, delay_cost=1)
	S += c_t3_t3100_mem1 >= 83
	c_t3_t3100_mem1 += INPUT_mem_r

	c_t3_t3100 = S.Task('c_t3_t3100', length=1, delay_cost=1)
	S += c_t3_t3100 >= 84
	c_t3_t3100 += ADD[3]


	# new tasks
	c_a1_0_y1__y1_1 = S.Task('c_a1_0_y1__y1_1', length=1, delay_cost=1)
	c_a1_0_y1__y1_1 += alt(ADD)

	c_a1_0_y1__y1_1_mem0 = S.Task('c_a1_0_y1__y1_1_mem0', length=1, delay_cost=1)
	c_a1_0_y1__y1_1_mem0 += ADD_mem[3]
	S += 30 < c_a1_0_y1__y1_1_mem0
	S += c_a1_0_y1__y1_1_mem0 <= c_a1_0_y1__y1_1

	c_a1_0_y1__y1_1_mem1 = S.Task('c_a1_0_y1__y1_1_mem1', length=1, delay_cost=1)
	c_a1_0_y1__y1_1_mem1 += INPUT_mem_r
	S += c_a1_0_y1__y1_1_mem1 <= c_a1_0_y1__y1_1

	c_t2_t0_t0_t1_in = S.Task('c_t2_t0_t0_t1_in', length=1, delay_cost=1)
	c_t2_t0_t0_t1_in += alt(MUL_in)
	c_t2_t0_t0_t1 = S.Task('c_t2_t0_t0_t1', length=7, delay_cost=1)
	c_t2_t0_t0_t1 += alt(MUL)
	S += c_t2_t0_t0_t1>=c_t2_t0_t0_t1_in

	c_t2_t0_t0_t1_mem0 = S.Task('c_t2_t0_t0_t1_mem0', length=1, delay_cost=1)
	c_t2_t0_t0_t1_mem0 += ADD_mem[3]
	S += 5 < c_t2_t0_t0_t1_mem0
	S += c_t2_t0_t0_t1_mem0 <= c_t2_t0_t0_t1

	c_t2_t0_t0_t1_mem1 = S.Task('c_t2_t0_t0_t1_mem1', length=1, delay_cost=1)
	c_t2_t0_t0_t1_mem1 += ADD_mem[1]
	S += 15 < c_t2_t0_t0_t1_mem1
	S += c_t2_t0_t0_t1_mem1 <= c_t2_t0_t0_t1

	c_t2_t0_t0_t3 = S.Task('c_t2_t0_t0_t3', length=1, delay_cost=1)
	c_t2_t0_t0_t3 += alt(ADD)

	c_t2_t0_t0_t3_mem0 = S.Task('c_t2_t0_t0_t3_mem0', length=1, delay_cost=1)
	c_t2_t0_t0_t3_mem0 += ADD_mem[0]
	S += 21 < c_t2_t0_t0_t3_mem0
	S += c_t2_t0_t0_t3_mem0 <= c_t2_t0_t0_t3

	c_t2_t0_t0_t3_mem1 = S.Task('c_t2_t0_t0_t3_mem1', length=1, delay_cost=1)
	c_t2_t0_t0_t3_mem1 += ADD_mem[1]
	S += 15 < c_t2_t0_t0_t3_mem1
	S += c_t2_t0_t0_t3_mem1 <= c_t2_t0_t0_t3

	c_t2_t0_t1_t0_in = S.Task('c_t2_t0_t1_t0_in', length=1, delay_cost=1)
	c_t2_t0_t1_t0_in += alt(MUL_in)
	c_t2_t0_t1_t0 = S.Task('c_t2_t0_t1_t0', length=7, delay_cost=1)
	c_t2_t0_t1_t0 += alt(MUL)
	S += c_t2_t0_t1_t0>=c_t2_t0_t1_t0_in

	c_t2_t0_t1_t0_mem0 = S.Task('c_t2_t0_t1_t0_mem0', length=1, delay_cost=1)
	c_t2_t0_t1_t0_mem0 += ADD_mem[1]
	S += 28 < c_t2_t0_t1_t0_mem0
	S += c_t2_t0_t1_t0_mem0 <= c_t2_t0_t1_t0

	c_t2_t0_t1_t0_mem1 = S.Task('c_t2_t0_t1_t0_mem1', length=1, delay_cost=1)
	c_t2_t0_t1_t0_mem1 += ADD_mem[0]
	S += 14 < c_t2_t0_t1_t0_mem1
	S += c_t2_t0_t1_t0_mem1 <= c_t2_t0_t1_t0

	c_t2_t0_t1_t1_in = S.Task('c_t2_t0_t1_t1_in', length=1, delay_cost=1)
	c_t2_t0_t1_t1_in += alt(MUL_in)
	c_t2_t0_t1_t1 = S.Task('c_t2_t0_t1_t1', length=7, delay_cost=1)
	c_t2_t0_t1_t1 += alt(MUL)
	S += c_t2_t0_t1_t1>=c_t2_t0_t1_t1_in

	c_t2_t0_t1_t1_mem0 = S.Task('c_t2_t0_t1_t1_mem0', length=1, delay_cost=1)
	c_t2_t0_t1_t1_mem0 += ADD_mem[3]
	S += 29 < c_t2_t0_t1_t1_mem0
	S += c_t2_t0_t1_t1_mem0 <= c_t2_t0_t1_t1

	c_t2_t0_t1_t1_mem1 = S.Task('c_t2_t0_t1_t1_mem1', length=1, delay_cost=1)
	c_t2_t0_t1_t1_mem1 += ADD_mem[3]
	S += 11 < c_t2_t0_t1_t1_mem1
	S += c_t2_t0_t1_t1_mem1 <= c_t2_t0_t1_t1

	c_t2_t0_t1_t2 = S.Task('c_t2_t0_t1_t2', length=1, delay_cost=1)
	c_t2_t0_t1_t2 += alt(ADD)

	c_t2_t0_t1_t2_mem0 = S.Task('c_t2_t0_t1_t2_mem0', length=1, delay_cost=1)
	c_t2_t0_t1_t2_mem0 += ADD_mem[1]
	S += 28 < c_t2_t0_t1_t2_mem0
	S += c_t2_t0_t1_t2_mem0 <= c_t2_t0_t1_t2

	c_t2_t0_t1_t2_mem1 = S.Task('c_t2_t0_t1_t2_mem1', length=1, delay_cost=1)
	c_t2_t0_t1_t2_mem1 += ADD_mem[3]
	S += 29 < c_t2_t0_t1_t2_mem1
	S += c_t2_t0_t1_t2_mem1 <= c_t2_t0_t1_t2

	c_t2_t0_t1_t3 = S.Task('c_t2_t0_t1_t3', length=1, delay_cost=1)
	c_t2_t0_t1_t3 += alt(ADD)

	c_t2_t0_t1_t3_mem0 = S.Task('c_t2_t0_t1_t3_mem0', length=1, delay_cost=1)
	c_t2_t0_t1_t3_mem0 += ADD_mem[0]
	S += 14 < c_t2_t0_t1_t3_mem0
	S += c_t2_t0_t1_t3_mem0 <= c_t2_t0_t1_t3

	c_t2_t0_t1_t3_mem1 = S.Task('c_t2_t0_t1_t3_mem1', length=1, delay_cost=1)
	c_t2_t0_t1_t3_mem1 += ADD_mem[3]
	S += 11 < c_t2_t0_t1_t3_mem1
	S += c_t2_t0_t1_t3_mem1 <= c_t2_t0_t1_t3

	c_t2_t0_t21 = S.Task('c_t2_t0_t21', length=1, delay_cost=1)
	c_t2_t0_t21 += alt(ADD)

	c_t2_t0_t21_mem0 = S.Task('c_t2_t0_t21_mem0', length=1, delay_cost=1)
	c_t2_t0_t21_mem0 += ADD_mem[3]
	S += 5 < c_t2_t0_t21_mem0
	S += c_t2_t0_t21_mem0 <= c_t2_t0_t21

	c_t2_t0_t21_mem1 = S.Task('c_t2_t0_t21_mem1', length=1, delay_cost=1)
	c_t2_t0_t21_mem1 += ADD_mem[3]
	S += 29 < c_t2_t0_t21_mem1
	S += c_t2_t0_t21_mem1 <= c_t2_t0_t21

	c_t2_t0_t30 = S.Task('c_t2_t0_t30', length=1, delay_cost=1)
	c_t2_t0_t30 += alt(ADD)

	c_t2_t0_t30_mem0 = S.Task('c_t2_t0_t30_mem0', length=1, delay_cost=1)
	c_t2_t0_t30_mem0 += ADD_mem[0]
	S += 21 < c_t2_t0_t30_mem0
	S += c_t2_t0_t30_mem0 <= c_t2_t0_t30

	c_t2_t0_t30_mem1 = S.Task('c_t2_t0_t30_mem1', length=1, delay_cost=1)
	c_t2_t0_t30_mem1 += ADD_mem[0]
	S += 14 < c_t2_t0_t30_mem1
	S += c_t2_t0_t30_mem1 <= c_t2_t0_t30

	c_t2_t0_t31 = S.Task('c_t2_t0_t31', length=1, delay_cost=1)
	c_t2_t0_t31 += alt(ADD)

	c_t2_t0_t31_mem0 = S.Task('c_t2_t0_t31_mem0', length=1, delay_cost=1)
	c_t2_t0_t31_mem0 += ADD_mem[1]
	S += 15 < c_t2_t0_t31_mem0
	S += c_t2_t0_t31_mem0 <= c_t2_t0_t31

	c_t2_t0_t31_mem1 = S.Task('c_t2_t0_t31_mem1', length=1, delay_cost=1)
	c_t2_t0_t31_mem1 += ADD_mem[3]
	S += 11 < c_t2_t0_t31_mem1
	S += c_t2_t0_t31_mem1 <= c_t2_t0_t31

	c_t2_t1_t0_t0_in = S.Task('c_t2_t1_t0_t0_in', length=1, delay_cost=1)
	c_t2_t1_t0_t0_in += alt(MUL_in)
	c_t2_t1_t0_t0 = S.Task('c_t2_t1_t0_t0', length=7, delay_cost=1)
	c_t2_t1_t0_t0 += alt(MUL)
	S += c_t2_t1_t0_t0>=c_t2_t1_t0_t0_in

	c_t2_t1_t0_t0_mem0 = S.Task('c_t2_t1_t0_t0_mem0', length=1, delay_cost=1)
	c_t2_t1_t0_t0_mem0 += ADD_mem[1]
	S += 6 < c_t2_t1_t0_t0_mem0
	S += c_t2_t1_t0_t0_mem0 <= c_t2_t1_t0_t0

	c_t2_t1_t0_t0_mem1 = S.Task('c_t2_t1_t0_t0_mem1', length=1, delay_cost=1)
	c_t2_t1_t0_t0_mem1 += ADD_mem[2]
	S += 12 < c_t2_t1_t0_t0_mem1
	S += c_t2_t1_t0_t0_mem1 <= c_t2_t1_t0_t0

	c_t2_t1_t0_t1_in = S.Task('c_t2_t1_t0_t1_in', length=1, delay_cost=1)
	c_t2_t1_t0_t1_in += alt(MUL_in)
	c_t2_t1_t0_t1 = S.Task('c_t2_t1_t0_t1', length=7, delay_cost=1)
	c_t2_t1_t0_t1 += alt(MUL)
	S += c_t2_t1_t0_t1>=c_t2_t1_t0_t1_in

	c_t2_t1_t0_t1_mem0 = S.Task('c_t2_t1_t0_t1_mem0', length=1, delay_cost=1)
	c_t2_t1_t0_t1_mem0 += ADD_mem[1]
	S += 27 < c_t2_t1_t0_t1_mem0
	S += c_t2_t1_t0_t1_mem0 <= c_t2_t1_t0_t1

	c_t2_t1_t0_t1_mem1 = S.Task('c_t2_t1_t0_t1_mem1', length=1, delay_cost=1)
	c_t2_t1_t0_t1_mem1 += ADD_mem[0]
	S += 16 < c_t2_t1_t0_t1_mem1
	S += c_t2_t1_t0_t1_mem1 <= c_t2_t1_t0_t1

	c_t2_t1_t0_t2 = S.Task('c_t2_t1_t0_t2', length=1, delay_cost=1)
	c_t2_t1_t0_t2 += alt(ADD)

	c_t2_t1_t0_t2_mem0 = S.Task('c_t2_t1_t0_t2_mem0', length=1, delay_cost=1)
	c_t2_t1_t0_t2_mem0 += ADD_mem[1]
	S += 6 < c_t2_t1_t0_t2_mem0
	S += c_t2_t1_t0_t2_mem0 <= c_t2_t1_t0_t2

	c_t2_t1_t0_t2_mem1 = S.Task('c_t2_t1_t0_t2_mem1', length=1, delay_cost=1)
	c_t2_t1_t0_t2_mem1 += ADD_mem[1]
	S += 27 < c_t2_t1_t0_t2_mem1
	S += c_t2_t1_t0_t2_mem1 <= c_t2_t1_t0_t2

	c_t2_t1_t0_t3 = S.Task('c_t2_t1_t0_t3', length=1, delay_cost=1)
	c_t2_t1_t0_t3 += alt(ADD)

	c_t2_t1_t0_t3_mem0 = S.Task('c_t2_t1_t0_t3_mem0', length=1, delay_cost=1)
	c_t2_t1_t0_t3_mem0 += ADD_mem[2]
	S += 12 < c_t2_t1_t0_t3_mem0
	S += c_t2_t1_t0_t3_mem0 <= c_t2_t1_t0_t3

	c_t2_t1_t0_t3_mem1 = S.Task('c_t2_t1_t0_t3_mem1', length=1, delay_cost=1)
	c_t2_t1_t0_t3_mem1 += ADD_mem[0]
	S += 16 < c_t2_t1_t0_t3_mem1
	S += c_t2_t1_t0_t3_mem1 <= c_t2_t1_t0_t3

	c_t2_t1_t1_t0_in = S.Task('c_t2_t1_t1_t0_in', length=1, delay_cost=1)
	c_t2_t1_t1_t0_in += alt(MUL_in)
	c_t2_t1_t1_t0 = S.Task('c_t2_t1_t1_t0', length=7, delay_cost=1)
	c_t2_t1_t1_t0 += alt(MUL)
	S += c_t2_t1_t1_t0>=c_t2_t1_t1_t0_in

	c_t2_t1_t1_t0_mem0 = S.Task('c_t2_t1_t1_t0_mem0', length=1, delay_cost=1)
	c_t2_t1_t1_t0_mem0 += ADD_mem[3]
	S += 10 < c_t2_t1_t1_t0_mem0
	S += c_t2_t1_t1_t0_mem0 <= c_t2_t1_t1_t0

	c_t2_t1_t1_t0_mem1 = S.Task('c_t2_t1_t1_t0_mem1', length=1, delay_cost=1)
	c_t2_t1_t1_t0_mem1 += ADD_mem[3]
	S += 7 < c_t2_t1_t1_t0_mem1
	S += c_t2_t1_t1_t0_mem1 <= c_t2_t1_t1_t0

	c_t2_t1_t1_t1_in = S.Task('c_t2_t1_t1_t1_in', length=1, delay_cost=1)
	c_t2_t1_t1_t1_in += alt(MUL_in)
	c_t2_t1_t1_t1 = S.Task('c_t2_t1_t1_t1', length=7, delay_cost=1)
	c_t2_t1_t1_t1 += alt(MUL)
	S += c_t2_t1_t1_t1>=c_t2_t1_t1_t1_in

	c_t2_t1_t1_t1_mem0 = S.Task('c_t2_t1_t1_t1_mem0', length=1, delay_cost=1)
	c_t2_t1_t1_t1_mem0 += ADD_mem[2]
	S += 22 < c_t2_t1_t1_t1_mem0
	S += c_t2_t1_t1_t1_mem0 <= c_t2_t1_t1_t1

	c_t2_t1_t1_t1_mem1 = S.Task('c_t2_t1_t1_t1_mem1', length=1, delay_cost=1)
	c_t2_t1_t1_t1_mem1 += ADD_mem[3]
	S += 9 < c_t2_t1_t1_t1_mem1
	S += c_t2_t1_t1_t1_mem1 <= c_t2_t1_t1_t1

	c_t2_t1_t1_t2 = S.Task('c_t2_t1_t1_t2', length=1, delay_cost=1)
	c_t2_t1_t1_t2 += alt(ADD)

	c_t2_t1_t1_t2_mem0 = S.Task('c_t2_t1_t1_t2_mem0', length=1, delay_cost=1)
	c_t2_t1_t1_t2_mem0 += ADD_mem[3]
	S += 10 < c_t2_t1_t1_t2_mem0
	S += c_t2_t1_t1_t2_mem0 <= c_t2_t1_t1_t2

	c_t2_t1_t1_t2_mem1 = S.Task('c_t2_t1_t1_t2_mem1', length=1, delay_cost=1)
	c_t2_t1_t1_t2_mem1 += ADD_mem[2]
	S += 22 < c_t2_t1_t1_t2_mem1
	S += c_t2_t1_t1_t2_mem1 <= c_t2_t1_t1_t2

	c_t2_t1_t1_t3 = S.Task('c_t2_t1_t1_t3', length=1, delay_cost=1)
	c_t2_t1_t1_t3 += alt(ADD)

	c_t2_t1_t1_t3_mem0 = S.Task('c_t2_t1_t1_t3_mem0', length=1, delay_cost=1)
	c_t2_t1_t1_t3_mem0 += ADD_mem[3]
	S += 7 < c_t2_t1_t1_t3_mem0
	S += c_t2_t1_t1_t3_mem0 <= c_t2_t1_t1_t3

	c_t2_t1_t1_t3_mem1 = S.Task('c_t2_t1_t1_t3_mem1', length=1, delay_cost=1)
	c_t2_t1_t1_t3_mem1 += ADD_mem[3]
	S += 9 < c_t2_t1_t1_t3_mem1
	S += c_t2_t1_t1_t3_mem1 <= c_t2_t1_t1_t3

	c_t2_t1_t20 = S.Task('c_t2_t1_t20', length=1, delay_cost=1)
	c_t2_t1_t20 += alt(ADD)

	c_t2_t1_t20_mem0 = S.Task('c_t2_t1_t20_mem0', length=1, delay_cost=1)
	c_t2_t1_t20_mem0 += ADD_mem[1]
	S += 6 < c_t2_t1_t20_mem0
	S += c_t2_t1_t20_mem0 <= c_t2_t1_t20

	c_t2_t1_t20_mem1 = S.Task('c_t2_t1_t20_mem1', length=1, delay_cost=1)
	c_t2_t1_t20_mem1 += ADD_mem[3]
	S += 10 < c_t2_t1_t20_mem1
	S += c_t2_t1_t20_mem1 <= c_t2_t1_t20

	c_t2_t1_t21 = S.Task('c_t2_t1_t21', length=1, delay_cost=1)
	c_t2_t1_t21 += alt(ADD)

	c_t2_t1_t21_mem0 = S.Task('c_t2_t1_t21_mem0', length=1, delay_cost=1)
	c_t2_t1_t21_mem0 += ADD_mem[1]
	S += 27 < c_t2_t1_t21_mem0
	S += c_t2_t1_t21_mem0 <= c_t2_t1_t21

	c_t2_t1_t21_mem1 = S.Task('c_t2_t1_t21_mem1', length=1, delay_cost=1)
	c_t2_t1_t21_mem1 += ADD_mem[2]
	S += 22 < c_t2_t1_t21_mem1
	S += c_t2_t1_t21_mem1 <= c_t2_t1_t21

	c_t2_t1_t30 = S.Task('c_t2_t1_t30', length=1, delay_cost=1)
	c_t2_t1_t30 += alt(ADD)

	c_t2_t1_t30_mem0 = S.Task('c_t2_t1_t30_mem0', length=1, delay_cost=1)
	c_t2_t1_t30_mem0 += ADD_mem[2]
	S += 12 < c_t2_t1_t30_mem0
	S += c_t2_t1_t30_mem0 <= c_t2_t1_t30

	c_t2_t1_t30_mem1 = S.Task('c_t2_t1_t30_mem1', length=1, delay_cost=1)
	c_t2_t1_t30_mem1 += ADD_mem[3]
	S += 7 < c_t2_t1_t30_mem1
	S += c_t2_t1_t30_mem1 <= c_t2_t1_t30

	c_t2_t1_t31 = S.Task('c_t2_t1_t31', length=1, delay_cost=1)
	c_t2_t1_t31 += alt(ADD)

	c_t2_t1_t31_mem0 = S.Task('c_t2_t1_t31_mem0', length=1, delay_cost=1)
	c_t2_t1_t31_mem0 += ADD_mem[0]
	S += 16 < c_t2_t1_t31_mem0
	S += c_t2_t1_t31_mem0 <= c_t2_t1_t31

	c_t2_t1_t31_mem1 = S.Task('c_t2_t1_t31_mem1', length=1, delay_cost=1)
	c_t2_t1_t31_mem1 += ADD_mem[3]
	S += 9 < c_t2_t1_t31_mem1
	S += c_t2_t1_t31_mem1 <= c_t2_t1_t31

	c_t2_t2_t0_t0_in = S.Task('c_t2_t2_t0_t0_in', length=1, delay_cost=1)
	c_t2_t2_t0_t0_in += alt(MUL_in)
	c_t2_t2_t0_t0 = S.Task('c_t2_t2_t0_t0', length=7, delay_cost=1)
	c_t2_t2_t0_t0 += alt(MUL)
	S += c_t2_t2_t0_t0>=c_t2_t2_t0_t0_in

	c_t2_t2_t0_t0_mem0 = S.Task('c_t2_t2_t0_t0_mem0', length=1, delay_cost=1)
	c_t2_t2_t0_t0_mem0 += ADD_mem[3]
	S += 20 < c_t2_t2_t0_t0_mem0
	S += c_t2_t2_t0_t0_mem0 <= c_t2_t2_t0_t0

	c_t2_t2_t0_t0_mem1 = S.Task('c_t2_t2_t0_t0_mem1', length=1, delay_cost=1)
	c_t2_t2_t0_t0_mem1 += ADD_mem[2]
	S += 26 < c_t2_t2_t0_t0_mem1
	S += c_t2_t2_t0_t0_mem1 <= c_t2_t2_t0_t0

	c_t2_t2_t0_t1_in = S.Task('c_t2_t2_t0_t1_in', length=1, delay_cost=1)
	c_t2_t2_t0_t1_in += alt(MUL_in)
	c_t2_t2_t0_t1 = S.Task('c_t2_t2_t0_t1', length=7, delay_cost=1)
	c_t2_t2_t0_t1 += alt(MUL)
	S += c_t2_t2_t0_t1>=c_t2_t2_t0_t1_in

	c_t2_t2_t0_t1_mem0 = S.Task('c_t2_t2_t0_t1_mem0', length=1, delay_cost=1)
	c_t2_t2_t0_t1_mem0 += ADD_mem[2]
	S += 23 < c_t2_t2_t0_t1_mem0
	S += c_t2_t2_t0_t1_mem0 <= c_t2_t2_t0_t1

	c_t2_t2_t0_t1_mem1 = S.Task('c_t2_t2_t0_t1_mem1', length=1, delay_cost=1)
	c_t2_t2_t0_t1_mem1 += ADD_mem[2]
	S += 19 < c_t2_t2_t0_t1_mem1
	S += c_t2_t2_t0_t1_mem1 <= c_t2_t2_t0_t1

	c_t2_t2_t0_t2 = S.Task('c_t2_t2_t0_t2', length=1, delay_cost=1)
	c_t2_t2_t0_t2 += alt(ADD)

	c_t2_t2_t0_t2_mem0 = S.Task('c_t2_t2_t0_t2_mem0', length=1, delay_cost=1)
	c_t2_t2_t0_t2_mem0 += ADD_mem[3]
	S += 20 < c_t2_t2_t0_t2_mem0
	S += c_t2_t2_t0_t2_mem0 <= c_t2_t2_t0_t2

	c_t2_t2_t0_t2_mem1 = S.Task('c_t2_t2_t0_t2_mem1', length=1, delay_cost=1)
	c_t2_t2_t0_t2_mem1 += ADD_mem[2]
	S += 23 < c_t2_t2_t0_t2_mem1
	S += c_t2_t2_t0_t2_mem1 <= c_t2_t2_t0_t2

	c_t2_t2_t0_t3 = S.Task('c_t2_t2_t0_t3', length=1, delay_cost=1)
	c_t2_t2_t0_t3 += alt(ADD)

	c_t2_t2_t0_t3_mem0 = S.Task('c_t2_t2_t0_t3_mem0', length=1, delay_cost=1)
	c_t2_t2_t0_t3_mem0 += ADD_mem[2]
	S += 26 < c_t2_t2_t0_t3_mem0
	S += c_t2_t2_t0_t3_mem0 <= c_t2_t2_t0_t3

	c_t2_t2_t0_t3_mem1 = S.Task('c_t2_t2_t0_t3_mem1', length=1, delay_cost=1)
	c_t2_t2_t0_t3_mem1 += ADD_mem[2]
	S += 19 < c_t2_t2_t0_t3_mem1
	S += c_t2_t2_t0_t3_mem1 <= c_t2_t2_t0_t3

	c_t2_t2_t1_t0_in = S.Task('c_t2_t2_t1_t0_in', length=1, delay_cost=1)
	c_t2_t2_t1_t0_in += alt(MUL_in)
	c_t2_t2_t1_t0 = S.Task('c_t2_t2_t1_t0', length=7, delay_cost=1)
	c_t2_t2_t1_t0 += alt(MUL)
	S += c_t2_t2_t1_t0>=c_t2_t2_t1_t0_in

	c_t2_t2_t1_t0_mem0 = S.Task('c_t2_t2_t1_t0_mem0', length=1, delay_cost=1)
	c_t2_t2_t1_t0_mem0 += ADD_mem[2]
	S += 18 < c_t2_t2_t1_t0_mem0
	S += c_t2_t2_t1_t0_mem0 <= c_t2_t2_t1_t0

	c_t2_t2_t1_t0_mem1 = S.Task('c_t2_t2_t1_t0_mem1', length=1, delay_cost=1)
	c_t2_t2_t1_t0_mem1 += ADD_mem[1]
	S += 24 < c_t2_t2_t1_t0_mem1
	S += c_t2_t2_t1_t0_mem1 <= c_t2_t2_t1_t0

	c_t2_t2_t1_t1_in = S.Task('c_t2_t2_t1_t1_in', length=1, delay_cost=1)
	c_t2_t2_t1_t1_in += alt(MUL_in)
	c_t2_t2_t1_t1 = S.Task('c_t2_t2_t1_t1', length=7, delay_cost=1)
	c_t2_t2_t1_t1 += alt(MUL)
	S += c_t2_t2_t1_t1>=c_t2_t2_t1_t1_in

	c_t2_t2_t1_t1_mem0 = S.Task('c_t2_t2_t1_t1_mem0', length=1, delay_cost=1)
	c_t2_t2_t1_t1_mem0 += ADD_mem[0]
	S += 13 < c_t2_t2_t1_t1_mem0
	S += c_t2_t2_t1_t1_mem0 <= c_t2_t2_t1_t1

	c_t2_t2_t1_t1_mem1 = S.Task('c_t2_t2_t1_t1_mem1', length=1, delay_cost=1)
	c_t2_t2_t1_t1_mem1 += ADD_mem[0]
	S += 17 < c_t2_t2_t1_t1_mem1
	S += c_t2_t2_t1_t1_mem1 <= c_t2_t2_t1_t1

	c_t2_t2_t1_t2 = S.Task('c_t2_t2_t1_t2', length=1, delay_cost=1)
	c_t2_t2_t1_t2 += alt(ADD)

	c_t2_t2_t1_t2_mem0 = S.Task('c_t2_t2_t1_t2_mem0', length=1, delay_cost=1)
	c_t2_t2_t1_t2_mem0 += ADD_mem[2]
	S += 18 < c_t2_t2_t1_t2_mem0
	S += c_t2_t2_t1_t2_mem0 <= c_t2_t2_t1_t2

	c_t2_t2_t1_t2_mem1 = S.Task('c_t2_t2_t1_t2_mem1', length=1, delay_cost=1)
	c_t2_t2_t1_t2_mem1 += ADD_mem[0]
	S += 13 < c_t2_t2_t1_t2_mem1
	S += c_t2_t2_t1_t2_mem1 <= c_t2_t2_t1_t2

	c_t2_t2_t1_t3 = S.Task('c_t2_t2_t1_t3', length=1, delay_cost=1)
	c_t2_t2_t1_t3 += alt(ADD)

	c_t2_t2_t1_t3_mem0 = S.Task('c_t2_t2_t1_t3_mem0', length=1, delay_cost=1)
	c_t2_t2_t1_t3_mem0 += ADD_mem[1]
	S += 24 < c_t2_t2_t1_t3_mem0
	S += c_t2_t2_t1_t3_mem0 <= c_t2_t2_t1_t3

	c_t2_t2_t1_t3_mem1 = S.Task('c_t2_t2_t1_t3_mem1', length=1, delay_cost=1)
	c_t2_t2_t1_t3_mem1 += ADD_mem[0]
	S += 17 < c_t2_t2_t1_t3_mem1
	S += c_t2_t2_t1_t3_mem1 <= c_t2_t2_t1_t3

	c_t2_t2_t20 = S.Task('c_t2_t2_t20', length=1, delay_cost=1)
	c_t2_t2_t20 += alt(ADD)

	c_t2_t2_t20_mem0 = S.Task('c_t2_t2_t20_mem0', length=1, delay_cost=1)
	c_t2_t2_t20_mem0 += ADD_mem[3]
	S += 20 < c_t2_t2_t20_mem0
	S += c_t2_t2_t20_mem0 <= c_t2_t2_t20

	c_t2_t2_t20_mem1 = S.Task('c_t2_t2_t20_mem1', length=1, delay_cost=1)
	c_t2_t2_t20_mem1 += ADD_mem[2]
	S += 18 < c_t2_t2_t20_mem1
	S += c_t2_t2_t20_mem1 <= c_t2_t2_t20

	c_t2_t2_t21 = S.Task('c_t2_t2_t21', length=1, delay_cost=1)
	c_t2_t2_t21 += alt(ADD)

	c_t2_t2_t21_mem0 = S.Task('c_t2_t2_t21_mem0', length=1, delay_cost=1)
	c_t2_t2_t21_mem0 += ADD_mem[2]
	S += 23 < c_t2_t2_t21_mem0
	S += c_t2_t2_t21_mem0 <= c_t2_t2_t21

	c_t2_t2_t21_mem1 = S.Task('c_t2_t2_t21_mem1', length=1, delay_cost=1)
	c_t2_t2_t21_mem1 += ADD_mem[0]
	S += 13 < c_t2_t2_t21_mem1
	S += c_t2_t2_t21_mem1 <= c_t2_t2_t21

	c_t2_t2_t30 = S.Task('c_t2_t2_t30', length=1, delay_cost=1)
	c_t2_t2_t30 += alt(ADD)

	c_t2_t2_t30_mem0 = S.Task('c_t2_t2_t30_mem0', length=1, delay_cost=1)
	c_t2_t2_t30_mem0 += ADD_mem[2]
	S += 26 < c_t2_t2_t30_mem0
	S += c_t2_t2_t30_mem0 <= c_t2_t2_t30

	c_t2_t2_t30_mem1 = S.Task('c_t2_t2_t30_mem1', length=1, delay_cost=1)
	c_t2_t2_t30_mem1 += ADD_mem[1]
	S += 24 < c_t2_t2_t30_mem1
	S += c_t2_t2_t30_mem1 <= c_t2_t2_t30

	c_t2_t2_t31 = S.Task('c_t2_t2_t31', length=1, delay_cost=1)
	c_t2_t2_t31 += alt(ADD)

	c_t2_t2_t31_mem0 = S.Task('c_t2_t2_t31_mem0', length=1, delay_cost=1)
	c_t2_t2_t31_mem0 += ADD_mem[2]
	S += 19 < c_t2_t2_t31_mem0
	S += c_t2_t2_t31_mem0 <= c_t2_t2_t31

	c_t2_t2_t31_mem1 = S.Task('c_t2_t2_t31_mem1', length=1, delay_cost=1)
	c_t2_t2_t31_mem1 += ADD_mem[0]
	S += 17 < c_t2_t2_t31_mem1
	S += c_t2_t2_t31_mem1 <= c_t2_t2_t31

	c_t2_t3001 = S.Task('c_t2_t3001', length=1, delay_cost=1)
	c_t2_t3001 += alt(ADD)

	c_t2_t3001_mem0 = S.Task('c_t2_t3001_mem0', length=1, delay_cost=1)
	c_t2_t3001_mem0 += ADD_mem[3]
	S += 5 < c_t2_t3001_mem0
	S += c_t2_t3001_mem0 <= c_t2_t3001

	c_t2_t3001_mem1 = S.Task('c_t2_t3001_mem1', length=1, delay_cost=1)
	c_t2_t3001_mem1 += ADD_mem[1]
	S += 27 < c_t2_t3001_mem1
	S += c_t2_t3001_mem1 <= c_t2_t3001

	c_t2_t3010 = S.Task('c_t2_t3010', length=1, delay_cost=1)
	c_t2_t3010 += alt(ADD)

	c_t2_t3010_mem0 = S.Task('c_t2_t3010_mem0', length=1, delay_cost=1)
	c_t2_t3010_mem0 += ADD_mem[1]
	S += 28 < c_t2_t3010_mem0
	S += c_t2_t3010_mem0 <= c_t2_t3010

	c_t2_t3010_mem1 = S.Task('c_t2_t3010_mem1', length=1, delay_cost=1)
	c_t2_t3010_mem1 += ADD_mem[3]
	S += 10 < c_t2_t3010_mem1
	S += c_t2_t3010_mem1 <= c_t2_t3010

	c_t2_t3011 = S.Task('c_t2_t3011', length=1, delay_cost=1)
	c_t2_t3011 += alt(ADD)

	c_t2_t3011_mem0 = S.Task('c_t2_t3011_mem0', length=1, delay_cost=1)
	c_t2_t3011_mem0 += ADD_mem[3]
	S += 29 < c_t2_t3011_mem0
	S += c_t2_t3011_mem0 <= c_t2_t3011

	c_t2_t3011_mem1 = S.Task('c_t2_t3011_mem1', length=1, delay_cost=1)
	c_t2_t3011_mem1 += ADD_mem[2]
	S += 22 < c_t2_t3011_mem1
	S += c_t2_t3011_mem1 <= c_t2_t3011

	c_t2_t3100 = S.Task('c_t2_t3100', length=1, delay_cost=1)
	c_t2_t3100 += alt(ADD)

	c_t2_t3100_mem0 = S.Task('c_t2_t3100_mem0', length=1, delay_cost=1)
	c_t2_t3100_mem0 += ADD_mem[0]
	S += 21 < c_t2_t3100_mem0
	S += c_t2_t3100_mem0 <= c_t2_t3100

	c_t2_t3100_mem1 = S.Task('c_t2_t3100_mem1', length=1, delay_cost=1)
	c_t2_t3100_mem1 += ADD_mem[2]
	S += 12 < c_t2_t3100_mem1
	S += c_t2_t3100_mem1 <= c_t2_t3100

	c_t2_t3101 = S.Task('c_t2_t3101', length=1, delay_cost=1)
	c_t2_t3101 += alt(ADD)

	c_t2_t3101_mem0 = S.Task('c_t2_t3101_mem0', length=1, delay_cost=1)
	c_t2_t3101_mem0 += ADD_mem[1]
	S += 15 < c_t2_t3101_mem0
	S += c_t2_t3101_mem0 <= c_t2_t3101

	c_t2_t3101_mem1 = S.Task('c_t2_t3101_mem1', length=1, delay_cost=1)
	c_t2_t3101_mem1 += ADD_mem[0]
	S += 16 < c_t2_t3101_mem1
	S += c_t2_t3101_mem1 <= c_t2_t3101

	c_t2_t3110 = S.Task('c_t2_t3110', length=1, delay_cost=1)
	c_t2_t3110 += alt(ADD)

	c_t2_t3110_mem0 = S.Task('c_t2_t3110_mem0', length=1, delay_cost=1)
	c_t2_t3110_mem0 += ADD_mem[0]
	S += 14 < c_t2_t3110_mem0
	S += c_t2_t3110_mem0 <= c_t2_t3110

	c_t2_t3110_mem1 = S.Task('c_t2_t3110_mem1', length=1, delay_cost=1)
	c_t2_t3110_mem1 += ADD_mem[3]
	S += 7 < c_t2_t3110_mem1
	S += c_t2_t3110_mem1 <= c_t2_t3110

	c_t2_t3111 = S.Task('c_t2_t3111', length=1, delay_cost=1)
	c_t2_t3111 += alt(ADD)

	c_t2_t3111_mem0 = S.Task('c_t2_t3111_mem0', length=1, delay_cost=1)
	c_t2_t3111_mem0 += ADD_mem[3]
	S += 11 < c_t2_t3111_mem0
	S += c_t2_t3111_mem0 <= c_t2_t3111

	c_t2_t3111_mem1 = S.Task('c_t2_t3111_mem1', length=1, delay_cost=1)
	c_t2_t3111_mem1 += ADD_mem[3]
	S += 9 < c_t2_t3111_mem1
	S += c_t2_t3111_mem1 <= c_t2_t3111

	c_t2_t4000 = S.Task('c_t2_t4000', length=1, delay_cost=1)
	c_t2_t4000 += alt(ADD)

	c_t2_t4000_mem0 = S.Task('c_t2_t4000_mem0', length=1, delay_cost=1)
	c_t2_t4000_mem0 += ADD_mem[1]
	S += 6 < c_t2_t4000_mem0
	S += c_t2_t4000_mem0 <= c_t2_t4000

	c_t2_t4000_mem1 = S.Task('c_t2_t4000_mem1', length=1, delay_cost=1)
	c_t2_t4000_mem1 += ADD_mem[3]
	S += 20 < c_t2_t4000_mem1
	S += c_t2_t4000_mem1 <= c_t2_t4000

	c_t2_t4001 = S.Task('c_t2_t4001', length=1, delay_cost=1)
	c_t2_t4001 += alt(ADD)

	c_t2_t4001_mem0 = S.Task('c_t2_t4001_mem0', length=1, delay_cost=1)
	c_t2_t4001_mem0 += ADD_mem[1]
	S += 27 < c_t2_t4001_mem0
	S += c_t2_t4001_mem0 <= c_t2_t4001

	c_t2_t4001_mem1 = S.Task('c_t2_t4001_mem1', length=1, delay_cost=1)
	c_t2_t4001_mem1 += ADD_mem[2]
	S += 23 < c_t2_t4001_mem1
	S += c_t2_t4001_mem1 <= c_t2_t4001

	c_t2_t4010 = S.Task('c_t2_t4010', length=1, delay_cost=1)
	c_t2_t4010 += alt(ADD)

	c_t2_t4010_mem0 = S.Task('c_t2_t4010_mem0', length=1, delay_cost=1)
	c_t2_t4010_mem0 += ADD_mem[3]
	S += 10 < c_t2_t4010_mem0
	S += c_t2_t4010_mem0 <= c_t2_t4010

	c_t2_t4010_mem1 = S.Task('c_t2_t4010_mem1', length=1, delay_cost=1)
	c_t2_t4010_mem1 += ADD_mem[2]
	S += 18 < c_t2_t4010_mem1
	S += c_t2_t4010_mem1 <= c_t2_t4010

	c_t2_t4011 = S.Task('c_t2_t4011', length=1, delay_cost=1)
	c_t2_t4011 += alt(ADD)

	c_t2_t4011_mem0 = S.Task('c_t2_t4011_mem0', length=1, delay_cost=1)
	c_t2_t4011_mem0 += ADD_mem[2]
	S += 22 < c_t2_t4011_mem0
	S += c_t2_t4011_mem0 <= c_t2_t4011

	c_t2_t4011_mem1 = S.Task('c_t2_t4011_mem1', length=1, delay_cost=1)
	c_t2_t4011_mem1 += ADD_mem[0]
	S += 13 < c_t2_t4011_mem1
	S += c_t2_t4011_mem1 <= c_t2_t4011

	c_t2_t4100 = S.Task('c_t2_t4100', length=1, delay_cost=1)
	c_t2_t4100 += alt(ADD)

	c_t2_t4100_mem0 = S.Task('c_t2_t4100_mem0', length=1, delay_cost=1)
	c_t2_t4100_mem0 += ADD_mem[2]
	S += 12 < c_t2_t4100_mem0
	S += c_t2_t4100_mem0 <= c_t2_t4100

	c_t2_t4100_mem1 = S.Task('c_t2_t4100_mem1', length=1, delay_cost=1)
	c_t2_t4100_mem1 += ADD_mem[2]
	S += 26 < c_t2_t4100_mem1
	S += c_t2_t4100_mem1 <= c_t2_t4100

	c_t2_t4101 = S.Task('c_t2_t4101', length=1, delay_cost=1)
	c_t2_t4101 += alt(ADD)

	c_t2_t4101_mem0 = S.Task('c_t2_t4101_mem0', length=1, delay_cost=1)
	c_t2_t4101_mem0 += ADD_mem[0]
	S += 16 < c_t2_t4101_mem0
	S += c_t2_t4101_mem0 <= c_t2_t4101

	c_t2_t4101_mem1 = S.Task('c_t2_t4101_mem1', length=1, delay_cost=1)
	c_t2_t4101_mem1 += ADD_mem[2]
	S += 19 < c_t2_t4101_mem1
	S += c_t2_t4101_mem1 <= c_t2_t4101

	c_t2_t4110 = S.Task('c_t2_t4110', length=1, delay_cost=1)
	c_t2_t4110 += alt(ADD)

	c_t2_t4110_mem0 = S.Task('c_t2_t4110_mem0', length=1, delay_cost=1)
	c_t2_t4110_mem0 += ADD_mem[3]
	S += 7 < c_t2_t4110_mem0
	S += c_t2_t4110_mem0 <= c_t2_t4110

	c_t2_t4110_mem1 = S.Task('c_t2_t4110_mem1', length=1, delay_cost=1)
	c_t2_t4110_mem1 += ADD_mem[1]
	S += 24 < c_t2_t4110_mem1
	S += c_t2_t4110_mem1 <= c_t2_t4110

	c_t2_t4111 = S.Task('c_t2_t4111', length=1, delay_cost=1)
	c_t2_t4111 += alt(ADD)

	c_t2_t4111_mem0 = S.Task('c_t2_t4111_mem0', length=1, delay_cost=1)
	c_t2_t4111_mem0 += ADD_mem[3]
	S += 9 < c_t2_t4111_mem0
	S += c_t2_t4111_mem0 <= c_t2_t4111

	c_t2_t4111_mem1 = S.Task('c_t2_t4111_mem1', length=1, delay_cost=1)
	c_t2_t4111_mem1 += ADD_mem[0]
	S += 17 < c_t2_t4111_mem1
	S += c_t2_t4111_mem1 <= c_t2_t4111

	c_t2_t5001 = S.Task('c_t2_t5001', length=1, delay_cost=1)
	c_t2_t5001 += alt(ADD)

	c_t2_t5001_mem0 = S.Task('c_t2_t5001_mem0', length=1, delay_cost=1)
	c_t2_t5001_mem0 += ADD_mem[2]
	S += 23 < c_t2_t5001_mem0
	S += c_t2_t5001_mem0 <= c_t2_t5001

	c_t2_t5001_mem1 = S.Task('c_t2_t5001_mem1', length=1, delay_cost=1)
	c_t2_t5001_mem1 += ADD_mem[3]
	S += 5 < c_t2_t5001_mem1
	S += c_t2_t5001_mem1 <= c_t2_t5001

	c_t2_t5010 = S.Task('c_t2_t5010', length=1, delay_cost=1)
	c_t2_t5010 += alt(ADD)

	c_t2_t5010_mem0 = S.Task('c_t2_t5010_mem0', length=1, delay_cost=1)
	c_t2_t5010_mem0 += ADD_mem[2]
	S += 18 < c_t2_t5010_mem0
	S += c_t2_t5010_mem0 <= c_t2_t5010

	c_t2_t5010_mem1 = S.Task('c_t2_t5010_mem1', length=1, delay_cost=1)
	c_t2_t5010_mem1 += ADD_mem[1]
	S += 28 < c_t2_t5010_mem1
	S += c_t2_t5010_mem1 <= c_t2_t5010

	c_t2_t5011 = S.Task('c_t2_t5011', length=1, delay_cost=1)
	c_t2_t5011 += alt(ADD)

	c_t2_t5011_mem0 = S.Task('c_t2_t5011_mem0', length=1, delay_cost=1)
	c_t2_t5011_mem0 += ADD_mem[0]
	S += 13 < c_t2_t5011_mem0
	S += c_t2_t5011_mem0 <= c_t2_t5011

	c_t2_t5011_mem1 = S.Task('c_t2_t5011_mem1', length=1, delay_cost=1)
	c_t2_t5011_mem1 += ADD_mem[3]
	S += 29 < c_t2_t5011_mem1
	S += c_t2_t5011_mem1 <= c_t2_t5011

	c_t2_t5100 = S.Task('c_t2_t5100', length=1, delay_cost=1)
	c_t2_t5100 += alt(ADD)

	c_t2_t5100_mem0 = S.Task('c_t2_t5100_mem0', length=1, delay_cost=1)
	c_t2_t5100_mem0 += ADD_mem[2]
	S += 26 < c_t2_t5100_mem0
	S += c_t2_t5100_mem0 <= c_t2_t5100

	c_t2_t5100_mem1 = S.Task('c_t2_t5100_mem1', length=1, delay_cost=1)
	c_t2_t5100_mem1 += ADD_mem[0]
	S += 21 < c_t2_t5100_mem1
	S += c_t2_t5100_mem1 <= c_t2_t5100

	c_t2_t5101 = S.Task('c_t2_t5101', length=1, delay_cost=1)
	c_t2_t5101 += alt(ADD)

	c_t2_t5101_mem0 = S.Task('c_t2_t5101_mem0', length=1, delay_cost=1)
	c_t2_t5101_mem0 += ADD_mem[2]
	S += 19 < c_t2_t5101_mem0
	S += c_t2_t5101_mem0 <= c_t2_t5101

	c_t2_t5101_mem1 = S.Task('c_t2_t5101_mem1', length=1, delay_cost=1)
	c_t2_t5101_mem1 += ADD_mem[1]
	S += 15 < c_t2_t5101_mem1
	S += c_t2_t5101_mem1 <= c_t2_t5101

	c_t2_t5110 = S.Task('c_t2_t5110', length=1, delay_cost=1)
	c_t2_t5110 += alt(ADD)

	c_t2_t5110_mem0 = S.Task('c_t2_t5110_mem0', length=1, delay_cost=1)
	c_t2_t5110_mem0 += ADD_mem[1]
	S += 24 < c_t2_t5110_mem0
	S += c_t2_t5110_mem0 <= c_t2_t5110

	c_t2_t5110_mem1 = S.Task('c_t2_t5110_mem1', length=1, delay_cost=1)
	c_t2_t5110_mem1 += ADD_mem[0]
	S += 14 < c_t2_t5110_mem1
	S += c_t2_t5110_mem1 <= c_t2_t5110

	c_t2_t5111 = S.Task('c_t2_t5111', length=1, delay_cost=1)
	c_t2_t5111 += alt(ADD)

	c_t2_t5111_mem0 = S.Task('c_t2_t5111_mem0', length=1, delay_cost=1)
	c_t2_t5111_mem0 += ADD_mem[0]
	S += 17 < c_t2_t5111_mem0
	S += c_t2_t5111_mem0 <= c_t2_t5111

	c_t2_t5111_mem1 = S.Task('c_t2_t5111_mem1', length=1, delay_cost=1)
	c_t2_t5111_mem1 += ADD_mem[3]
	S += 11 < c_t2_t5111_mem1
	S += c_t2_t5111_mem1 <= c_t2_t5111

	c_t3_t0_t0_t4_in = S.Task('c_t3_t0_t0_t4_in', length=1, delay_cost=1)
	c_t3_t0_t0_t4_in += alt(MUL_in)
	c_t3_t0_t0_t4 = S.Task('c_t3_t0_t0_t4', length=7, delay_cost=1)
	c_t3_t0_t0_t4 += alt(MUL)
	S += c_t3_t0_t0_t4>=c_t3_t0_t0_t4_in

	c_t3_t0_t0_t4_mem0 = S.Task('c_t3_t0_t0_t4_mem0', length=1, delay_cost=1)
	c_t3_t0_t0_t4_mem0 += ADD_mem[3]
	S += 8 < c_t3_t0_t0_t4_mem0
	S += c_t3_t0_t0_t4_mem0 <= c_t3_t0_t0_t4

	c_t3_t0_t0_t4_mem1 = S.Task('c_t3_t0_t0_t4_mem1', length=1, delay_cost=1)
	c_t3_t0_t0_t4_mem1 += ADD_mem[2]
	S += 25 < c_t3_t0_t0_t4_mem1
	S += c_t3_t0_t0_t4_mem1 <= c_t3_t0_t0_t4

	c_t3_t0_t0_s00 = S.Task('c_t3_t0_t0_s00', length=1, delay_cost=1)
	c_t3_t0_t0_s00 += alt(ADD)

	c_t3_t0_t0_s00_mem0 = S.Task('c_t3_t0_t0_s00_mem0', length=1, delay_cost=1)
	c_t3_t0_t0_s00_mem0 += MUL_mem[0]
	S += 10 < c_t3_t0_t0_s00_mem0
	S += c_t3_t0_t0_s00_mem0 <= c_t3_t0_t0_s00

	c_t3_t0_t0_t5 = S.Task('c_t3_t0_t0_t5', length=1, delay_cost=1)
	c_t3_t0_t0_t5 += alt(ADD)

	c_t3_t0_t0_t5_mem0 = S.Task('c_t3_t0_t0_t5_mem0', length=1, delay_cost=1)
	c_t3_t0_t0_t5_mem0 += MUL_mem[0]
	S += 8 < c_t3_t0_t0_t5_mem0
	S += c_t3_t0_t0_t5_mem0 <= c_t3_t0_t0_t5

	c_t3_t0_t0_t5_mem1 = S.Task('c_t3_t0_t0_t5_mem1', length=1, delay_cost=1)
	c_t3_t0_t0_t5_mem1 += MUL_mem[0]
	S += 10 < c_t3_t0_t0_t5_mem1
	S += c_t3_t0_t0_t5_mem1 <= c_t3_t0_t0_t5

	c_t3_t0_t1_t4_in = S.Task('c_t3_t0_t1_t4_in', length=1, delay_cost=1)
	c_t3_t0_t1_t4_in += alt(MUL_in)
	c_t3_t0_t1_t4 = S.Task('c_t3_t0_t1_t4', length=7, delay_cost=1)
	c_t3_t0_t1_t4 += alt(MUL)
	S += c_t3_t0_t1_t4>=c_t3_t0_t1_t4_in

	c_t3_t0_t1_t4_mem0 = S.Task('c_t3_t0_t1_t4_mem0', length=1, delay_cost=1)
	c_t3_t0_t1_t4_mem0 += ADD_mem[0]
	S += 57 < c_t3_t0_t1_t4_mem0
	S += c_t3_t0_t1_t4_mem0 <= c_t3_t0_t1_t4

	c_t3_t0_t1_t4_mem1 = S.Task('c_t3_t0_t1_t4_mem1', length=1, delay_cost=1)
	c_t3_t0_t1_t4_mem1 += ADD_mem[0]
	S += 40 < c_t3_t0_t1_t4_mem1
	S += c_t3_t0_t1_t4_mem1 <= c_t3_t0_t1_t4

	c_t3_t0_t1_s00 = S.Task('c_t3_t0_t1_s00', length=1, delay_cost=1)
	c_t3_t0_t1_s00 += alt(ADD)

	c_t3_t0_t1_s00_mem0 = S.Task('c_t3_t0_t1_s00_mem0', length=1, delay_cost=1)
	c_t3_t0_t1_s00_mem0 += MUL_mem[0]
	S += 7 < c_t3_t0_t1_s00_mem0
	S += c_t3_t0_t1_s00_mem0 <= c_t3_t0_t1_s00

	c_t3_t0_t1_t5 = S.Task('c_t3_t0_t1_t5', length=1, delay_cost=1)
	c_t3_t0_t1_t5 += alt(ADD)

	c_t3_t0_t1_t5_mem0 = S.Task('c_t3_t0_t1_t5_mem0', length=1, delay_cost=1)
	c_t3_t0_t1_t5_mem0 += MUL_mem[0]
	S += 9 < c_t3_t0_t1_t5_mem0
	S += c_t3_t0_t1_t5_mem0 <= c_t3_t0_t1_t5

	c_t3_t0_t1_t5_mem1 = S.Task('c_t3_t0_t1_t5_mem1', length=1, delay_cost=1)
	c_t3_t0_t1_t5_mem1 += MUL_mem[0]
	S += 7 < c_t3_t0_t1_t5_mem1
	S += c_t3_t0_t1_t5_mem1 <= c_t3_t0_t1_t5

	c_t3_t0_t4_t0_in = S.Task('c_t3_t0_t4_t0_in', length=1, delay_cost=1)
	c_t3_t0_t4_t0_in += alt(MUL_in)
	c_t3_t0_t4_t0 = S.Task('c_t3_t0_t4_t0', length=7, delay_cost=1)
	c_t3_t0_t4_t0 += alt(MUL)
	S += c_t3_t0_t4_t0>=c_t3_t0_t4_t0_in

	c_t3_t0_t4_t0_mem0 = S.Task('c_t3_t0_t4_t0_mem0', length=1, delay_cost=1)
	c_t3_t0_t4_t0_mem0 += ADD_mem[2]
	S += 45 < c_t3_t0_t4_t0_mem0
	S += c_t3_t0_t4_t0_mem0 <= c_t3_t0_t4_t0

	c_t3_t0_t4_t0_mem1 = S.Task('c_t3_t0_t4_t0_mem1', length=1, delay_cost=1)
	c_t3_t0_t4_t0_mem1 += ADD_mem[3]
	S += 47 < c_t3_t0_t4_t0_mem1
	S += c_t3_t0_t4_t0_mem1 <= c_t3_t0_t4_t0

	c_t3_t0_t4_t1_in = S.Task('c_t3_t0_t4_t1_in', length=1, delay_cost=1)
	c_t3_t0_t4_t1_in += alt(MUL_in)
	c_t3_t0_t4_t1 = S.Task('c_t3_t0_t4_t1', length=7, delay_cost=1)
	c_t3_t0_t4_t1 += alt(MUL)
	S += c_t3_t0_t4_t1>=c_t3_t0_t4_t1_in

	c_t3_t0_t4_t1_mem0 = S.Task('c_t3_t0_t4_t1_mem0', length=1, delay_cost=1)
	c_t3_t0_t4_t1_mem0 += ADD_mem[3]
	S += 46 < c_t3_t0_t4_t1_mem0
	S += c_t3_t0_t4_t1_mem0 <= c_t3_t0_t4_t1

	c_t3_t0_t4_t1_mem1 = S.Task('c_t3_t0_t4_t1_mem1', length=1, delay_cost=1)
	c_t3_t0_t4_t1_mem1 += ADD_mem[1]
	S += 44 < c_t3_t0_t4_t1_mem1
	S += c_t3_t0_t4_t1_mem1 <= c_t3_t0_t4_t1

	c_t3_t0_t4_t2 = S.Task('c_t3_t0_t4_t2', length=1, delay_cost=1)
	c_t3_t0_t4_t2 += alt(ADD)

	c_t3_t0_t4_t2_mem0 = S.Task('c_t3_t0_t4_t2_mem0', length=1, delay_cost=1)
	c_t3_t0_t4_t2_mem0 += ADD_mem[2]
	S += 45 < c_t3_t0_t4_t2_mem0
	S += c_t3_t0_t4_t2_mem0 <= c_t3_t0_t4_t2

	c_t3_t0_t4_t2_mem1 = S.Task('c_t3_t0_t4_t2_mem1', length=1, delay_cost=1)
	c_t3_t0_t4_t2_mem1 += ADD_mem[3]
	S += 46 < c_t3_t0_t4_t2_mem1
	S += c_t3_t0_t4_t2_mem1 <= c_t3_t0_t4_t2

	c_t3_t0_t4_t3 = S.Task('c_t3_t0_t4_t3', length=1, delay_cost=1)
	c_t3_t0_t4_t3 += alt(ADD)

	c_t3_t0_t4_t3_mem0 = S.Task('c_t3_t0_t4_t3_mem0', length=1, delay_cost=1)
	c_t3_t0_t4_t3_mem0 += ADD_mem[3]
	S += 47 < c_t3_t0_t4_t3_mem0
	S += c_t3_t0_t4_t3_mem0 <= c_t3_t0_t4_t3

	c_t3_t0_t4_t3_mem1 = S.Task('c_t3_t0_t4_t3_mem1', length=1, delay_cost=1)
	c_t3_t0_t4_t3_mem1 += ADD_mem[1]
	S += 44 < c_t3_t0_t4_t3_mem1
	S += c_t3_t0_t4_t3_mem1 <= c_t3_t0_t4_t3

	c_t3_t1_t0_t4_in = S.Task('c_t3_t1_t0_t4_in', length=1, delay_cost=1)
	c_t3_t1_t0_t4_in += alt(MUL_in)
	c_t3_t1_t0_t4 = S.Task('c_t3_t1_t0_t4', length=7, delay_cost=1)
	c_t3_t1_t0_t4 += alt(MUL)
	S += c_t3_t1_t0_t4>=c_t3_t1_t0_t4_in

	c_t3_t1_t0_t4_mem0 = S.Task('c_t3_t1_t0_t4_mem0', length=1, delay_cost=1)
	c_t3_t1_t0_t4_mem0 += ADD_mem[3]
	S += 41 < c_t3_t1_t0_t4_mem0
	S += c_t3_t1_t0_t4_mem0 <= c_t3_t1_t0_t4

	c_t3_t1_t0_t4_mem1 = S.Task('c_t3_t1_t0_t4_mem1', length=1, delay_cost=1)
	c_t3_t1_t0_t4_mem1 += ADD_mem[0]
	S += 60 < c_t3_t1_t0_t4_mem1
	S += c_t3_t1_t0_t4_mem1 <= c_t3_t1_t0_t4

	c_t3_t1_t0_s00 = S.Task('c_t3_t1_t0_s00', length=1, delay_cost=1)
	c_t3_t1_t0_s00 += alt(ADD)

	c_t3_t1_t0_s00_mem0 = S.Task('c_t3_t1_t0_s00_mem0', length=1, delay_cost=1)
	c_t3_t1_t0_s00_mem0 += MUL_mem[0]
	S += 43 < c_t3_t1_t0_s00_mem0
	S += c_t3_t1_t0_s00_mem0 <= c_t3_t1_t0_s00

	c_t3_t1_t0_t5 = S.Task('c_t3_t1_t0_t5', length=1, delay_cost=1)
	c_t3_t1_t0_t5 += alt(ADD)

	c_t3_t1_t0_t5_mem0 = S.Task('c_t3_t1_t0_t5_mem0', length=1, delay_cost=1)
	c_t3_t1_t0_t5_mem0 += MUL_mem[0]
	S += 44 < c_t3_t1_t0_t5_mem0
	S += c_t3_t1_t0_t5_mem0 <= c_t3_t1_t0_t5

	c_t3_t1_t0_t5_mem1 = S.Task('c_t3_t1_t0_t5_mem1', length=1, delay_cost=1)
	c_t3_t1_t0_t5_mem1 += MUL_mem[0]
	S += 43 < c_t3_t1_t0_t5_mem1
	S += c_t3_t1_t0_t5_mem1 <= c_t3_t1_t0_t5

	c_t3_t1_t1_t4_in = S.Task('c_t3_t1_t1_t4_in', length=1, delay_cost=1)
	c_t3_t1_t1_t4_in += alt(MUL_in)
	c_t3_t1_t1_t4 = S.Task('c_t3_t1_t1_t4', length=7, delay_cost=1)
	c_t3_t1_t1_t4 += alt(MUL)
	S += c_t3_t1_t1_t4>=c_t3_t1_t1_t4_in

	c_t3_t1_t1_t4_mem0 = S.Task('c_t3_t1_t1_t4_mem0', length=1, delay_cost=1)
	c_t3_t1_t1_t4_mem0 += ADD_mem[0]
	S += 59 < c_t3_t1_t1_t4_mem0
	S += c_t3_t1_t1_t4_mem0 <= c_t3_t1_t1_t4

	c_t3_t1_t1_t4_mem1 = S.Task('c_t3_t1_t1_t4_mem1', length=1, delay_cost=1)
	c_t3_t1_t1_t4_mem1 += ADD_mem[0]
	S += 58 < c_t3_t1_t1_t4_mem1
	S += c_t3_t1_t1_t4_mem1 <= c_t3_t1_t1_t4

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/SQR_mul1_add4/SQR_3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

