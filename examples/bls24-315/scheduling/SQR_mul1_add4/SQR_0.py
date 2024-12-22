from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 135
	S = Scenario("SQR_0", horizon=horizon)

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

	# new tasks
	c_a1_0_y1__y1_0 = S.Task('c_a1_0_y1__y1_0', length=1, delay_cost=1)
	c_a1_0_y1__y1_0 += alt(ADD)

	c_a1_0_y1__y1_0_mem0 = S.Task('c_a1_0_y1__y1_0_mem0', length=1, delay_cost=1)
	c_a1_0_y1__y1_0_mem0 += INPUT_mem_r
	S += c_a1_0_y1__y1_0_mem0 <= c_a1_0_y1__y1_0

	c_t0001 = S.Task('c_t0001', length=1, delay_cost=1)
	c_t0001 += alt(ADD)

	c_t0001_mem0 = S.Task('c_t0001_mem0', length=1, delay_cost=1)
	c_t0001_mem0 += INPUT_mem_r
	S += c_t0001_mem0 <= c_t0001

	c_t0001_mem1 = S.Task('c_t0001_mem1', length=1, delay_cost=1)
	c_t0001_mem1 += INPUT_mem_r
	S += c_t0001_mem1 <= c_t0001

	c_t0010 = S.Task('c_t0010', length=1, delay_cost=1)
	c_t0010 += alt(ADD)

	c_t0010_mem0 = S.Task('c_t0010_mem0', length=1, delay_cost=1)
	c_t0010_mem0 += INPUT_mem_r
	S += c_t0010_mem0 <= c_t0010

	c_t0010_mem1 = S.Task('c_t0010_mem1', length=1, delay_cost=1)
	c_t0010_mem1 += INPUT_mem_r
	S += c_t0010_mem1 <= c_t0010

	c_t0011 = S.Task('c_t0011', length=1, delay_cost=1)
	c_t0011 += alt(ADD)

	c_t0011_mem0 = S.Task('c_t0011_mem0', length=1, delay_cost=1)
	c_t0011_mem0 += INPUT_mem_r
	S += c_t0011_mem0 <= c_t0011

	c_t0011_mem1 = S.Task('c_t0011_mem1', length=1, delay_cost=1)
	c_t0011_mem1 += INPUT_mem_r
	S += c_t0011_mem1 <= c_t0011

	c_t0100 = S.Task('c_t0100', length=1, delay_cost=1)
	c_t0100 += alt(ADD)

	c_t0100_mem0 = S.Task('c_t0100_mem0', length=1, delay_cost=1)
	c_t0100_mem0 += INPUT_mem_r
	S += c_t0100_mem0 <= c_t0100

	c_t0100_mem1 = S.Task('c_t0100_mem1', length=1, delay_cost=1)
	c_t0100_mem1 += INPUT_mem_r
	S += c_t0100_mem1 <= c_t0100

	c_t0101 = S.Task('c_t0101', length=1, delay_cost=1)
	c_t0101 += alt(ADD)

	c_t0101_mem0 = S.Task('c_t0101_mem0', length=1, delay_cost=1)
	c_t0101_mem0 += INPUT_mem_r
	S += c_t0101_mem0 <= c_t0101

	c_t0101_mem1 = S.Task('c_t0101_mem1', length=1, delay_cost=1)
	c_t0101_mem1 += INPUT_mem_r
	S += c_t0101_mem1 <= c_t0101

	c_t0110 = S.Task('c_t0110', length=1, delay_cost=1)
	c_t0110 += alt(ADD)

	c_t0110_mem0 = S.Task('c_t0110_mem0', length=1, delay_cost=1)
	c_t0110_mem0 += INPUT_mem_r
	S += c_t0110_mem0 <= c_t0110

	c_t0110_mem1 = S.Task('c_t0110_mem1', length=1, delay_cost=1)
	c_t0110_mem1 += INPUT_mem_r
	S += c_t0110_mem1 <= c_t0110

	c_t0111 = S.Task('c_t0111', length=1, delay_cost=1)
	c_t0111 += alt(ADD)

	c_t0111_mem0 = S.Task('c_t0111_mem0', length=1, delay_cost=1)
	c_t0111_mem0 += INPUT_mem_r
	S += c_t0111_mem0 <= c_t0111

	c_t0111_mem1 = S.Task('c_t0111_mem1', length=1, delay_cost=1)
	c_t0111_mem1 += INPUT_mem_r
	S += c_t0111_mem1 <= c_t0111

	c_t0200 = S.Task('c_t0200', length=1, delay_cost=1)
	c_t0200 += alt(ADD)

	c_t0200_mem0 = S.Task('c_t0200_mem0', length=1, delay_cost=1)
	c_t0200_mem0 += INPUT_mem_r
	S += c_t0200_mem0 <= c_t0200

	c_t0200_mem1 = S.Task('c_t0200_mem1', length=1, delay_cost=1)
	c_t0200_mem1 += INPUT_mem_r
	S += c_t0200_mem1 <= c_t0200

	c_t0201 = S.Task('c_t0201', length=1, delay_cost=1)
	c_t0201 += alt(ADD)

	c_t0201_mem0 = S.Task('c_t0201_mem0', length=1, delay_cost=1)
	c_t0201_mem0 += INPUT_mem_r
	S += c_t0201_mem0 <= c_t0201

	c_t0201_mem1 = S.Task('c_t0201_mem1', length=1, delay_cost=1)
	c_t0201_mem1 += INPUT_mem_r
	S += c_t0201_mem1 <= c_t0201

	c_t0210 = S.Task('c_t0210', length=1, delay_cost=1)
	c_t0210 += alt(ADD)

	c_t0210_mem0 = S.Task('c_t0210_mem0', length=1, delay_cost=1)
	c_t0210_mem0 += INPUT_mem_r
	S += c_t0210_mem0 <= c_t0210

	c_t0210_mem1 = S.Task('c_t0210_mem1', length=1, delay_cost=1)
	c_t0210_mem1 += INPUT_mem_r
	S += c_t0210_mem1 <= c_t0210

	c_t0211 = S.Task('c_t0211', length=1, delay_cost=1)
	c_t0211 += alt(ADD)

	c_t0211_mem0 = S.Task('c_t0211_mem0', length=1, delay_cost=1)
	c_t0211_mem0 += INPUT_mem_r
	S += c_t0211_mem0 <= c_t0211

	c_t0211_mem1 = S.Task('c_t0211_mem1', length=1, delay_cost=1)
	c_t0211_mem1 += INPUT_mem_r
	S += c_t0211_mem1 <= c_t0211

	c_t1000 = S.Task('c_t1000', length=1, delay_cost=1)
	c_t1000 += alt(ADD)

	c_t1000_mem0 = S.Task('c_t1000_mem0', length=1, delay_cost=1)
	c_t1000_mem0 += INPUT_mem_r
	S += c_t1000_mem0 <= c_t1000

	c_t1000_mem1 = S.Task('c_t1000_mem1', length=1, delay_cost=1)
	c_t1000_mem1 += INPUT_mem_r
	S += c_t1000_mem1 <= c_t1000

	c_t1001 = S.Task('c_t1001', length=1, delay_cost=1)
	c_t1001 += alt(ADD)

	c_t1001_mem0 = S.Task('c_t1001_mem0', length=1, delay_cost=1)
	c_t1001_mem0 += INPUT_mem_r
	S += c_t1001_mem0 <= c_t1001

	c_t1001_mem1 = S.Task('c_t1001_mem1', length=1, delay_cost=1)
	c_t1001_mem1 += INPUT_mem_r
	S += c_t1001_mem1 <= c_t1001

	c_t1010 = S.Task('c_t1010', length=1, delay_cost=1)
	c_t1010 += alt(ADD)

	c_t1010_mem0 = S.Task('c_t1010_mem0', length=1, delay_cost=1)
	c_t1010_mem0 += INPUT_mem_r
	S += c_t1010_mem0 <= c_t1010

	c_t1010_mem1 = S.Task('c_t1010_mem1', length=1, delay_cost=1)
	c_t1010_mem1 += INPUT_mem_r
	S += c_t1010_mem1 <= c_t1010

	c_t1011 = S.Task('c_t1011', length=1, delay_cost=1)
	c_t1011 += alt(ADD)

	c_t1011_mem0 = S.Task('c_t1011_mem0', length=1, delay_cost=1)
	c_t1011_mem0 += INPUT_mem_r
	S += c_t1011_mem0 <= c_t1011

	c_t1011_mem1 = S.Task('c_t1011_mem1', length=1, delay_cost=1)
	c_t1011_mem1 += INPUT_mem_r
	S += c_t1011_mem1 <= c_t1011

	c_t1100 = S.Task('c_t1100', length=1, delay_cost=1)
	c_t1100 += alt(ADD)

	c_t1100_mem0 = S.Task('c_t1100_mem0', length=1, delay_cost=1)
	c_t1100_mem0 += INPUT_mem_r
	S += c_t1100_mem0 <= c_t1100

	c_t1100_mem1 = S.Task('c_t1100_mem1', length=1, delay_cost=1)
	c_t1100_mem1 += INPUT_mem_r
	S += c_t1100_mem1 <= c_t1100

	c_t1101 = S.Task('c_t1101', length=1, delay_cost=1)
	c_t1101 += alt(ADD)

	c_t1101_mem0 = S.Task('c_t1101_mem0', length=1, delay_cost=1)
	c_t1101_mem0 += INPUT_mem_r
	S += c_t1101_mem0 <= c_t1101

	c_t1101_mem1 = S.Task('c_t1101_mem1', length=1, delay_cost=1)
	c_t1101_mem1 += INPUT_mem_r
	S += c_t1101_mem1 <= c_t1101

	c_t1110 = S.Task('c_t1110', length=1, delay_cost=1)
	c_t1110 += alt(ADD)

	c_t1110_mem0 = S.Task('c_t1110_mem0', length=1, delay_cost=1)
	c_t1110_mem0 += INPUT_mem_r
	S += c_t1110_mem0 <= c_t1110

	c_t1110_mem1 = S.Task('c_t1110_mem1', length=1, delay_cost=1)
	c_t1110_mem1 += INPUT_mem_r
	S += c_t1110_mem1 <= c_t1110

	c_t1111 = S.Task('c_t1111', length=1, delay_cost=1)
	c_t1111 += alt(ADD)

	c_t1111_mem0 = S.Task('c_t1111_mem0', length=1, delay_cost=1)
	c_t1111_mem0 += INPUT_mem_r
	S += c_t1111_mem0 <= c_t1111

	c_t1111_mem1 = S.Task('c_t1111_mem1', length=1, delay_cost=1)
	c_t1111_mem1 += INPUT_mem_r
	S += c_t1111_mem1 <= c_t1111

	c_t1200 = S.Task('c_t1200', length=1, delay_cost=1)
	c_t1200 += alt(ADD)

	c_t1200_mem0 = S.Task('c_t1200_mem0', length=1, delay_cost=1)
	c_t1200_mem0 += INPUT_mem_r
	S += c_t1200_mem0 <= c_t1200

	c_t1200_mem1 = S.Task('c_t1200_mem1', length=1, delay_cost=1)
	c_t1200_mem1 += INPUT_mem_r
	S += c_t1200_mem1 <= c_t1200

	c_t1201 = S.Task('c_t1201', length=1, delay_cost=1)
	c_t1201 += alt(ADD)

	c_t1201_mem0 = S.Task('c_t1201_mem0', length=1, delay_cost=1)
	c_t1201_mem0 += INPUT_mem_r
	S += c_t1201_mem0 <= c_t1201

	c_t1201_mem1 = S.Task('c_t1201_mem1', length=1, delay_cost=1)
	c_t1201_mem1 += INPUT_mem_r
	S += c_t1201_mem1 <= c_t1201

	c_t1210 = S.Task('c_t1210', length=1, delay_cost=1)
	c_t1210 += alt(ADD)

	c_t1210_mem0 = S.Task('c_t1210_mem0', length=1, delay_cost=1)
	c_t1210_mem0 += INPUT_mem_r
	S += c_t1210_mem0 <= c_t1210

	c_t1210_mem1 = S.Task('c_t1210_mem1', length=1, delay_cost=1)
	c_t1210_mem1 += INPUT_mem_r
	S += c_t1210_mem1 <= c_t1210

	c_t1211 = S.Task('c_t1211', length=1, delay_cost=1)
	c_t1211 += alt(ADD)

	c_t1211_mem0 = S.Task('c_t1211_mem0', length=1, delay_cost=1)
	c_t1211_mem0 += INPUT_mem_r
	S += c_t1211_mem0 <= c_t1211

	c_t1211_mem1 = S.Task('c_t1211_mem1', length=1, delay_cost=1)
	c_t1211_mem1 += INPUT_mem_r
	S += c_t1211_mem1 <= c_t1211

	c_t3_t0_t0_t0_in = S.Task('c_t3_t0_t0_t0_in', length=1, delay_cost=1)
	c_t3_t0_t0_t0_in += alt(MUL_in)
	c_t3_t0_t0_t0 = S.Task('c_t3_t0_t0_t0', length=7, delay_cost=1)
	c_t3_t0_t0_t0 += alt(MUL)
	S += c_t3_t0_t0_t0>=c_t3_t0_t0_t0_in

	c_t3_t0_t0_t0_mem0 = S.Task('c_t3_t0_t0_t0_mem0', length=1, delay_cost=1)
	c_t3_t0_t0_t0_mem0 += INPUT_mem_r
	S += c_t3_t0_t0_t0_mem0 <= c_t3_t0_t0_t0

	c_t3_t0_t0_t0_mem1 = S.Task('c_t3_t0_t0_t0_mem1', length=1, delay_cost=1)
	c_t3_t0_t0_t0_mem1 += INPUT_mem_r
	S += c_t3_t0_t0_t0_mem1 <= c_t3_t0_t0_t0

	c_t3_t0_t0_t1_in = S.Task('c_t3_t0_t0_t1_in', length=1, delay_cost=1)
	c_t3_t0_t0_t1_in += alt(MUL_in)
	c_t3_t0_t0_t1 = S.Task('c_t3_t0_t0_t1', length=7, delay_cost=1)
	c_t3_t0_t0_t1 += alt(MUL)
	S += c_t3_t0_t0_t1>=c_t3_t0_t0_t1_in

	c_t3_t0_t0_t1_mem0 = S.Task('c_t3_t0_t0_t1_mem0', length=1, delay_cost=1)
	c_t3_t0_t0_t1_mem0 += INPUT_mem_r
	S += c_t3_t0_t0_t1_mem0 <= c_t3_t0_t0_t1

	c_t3_t0_t0_t1_mem1 = S.Task('c_t3_t0_t0_t1_mem1', length=1, delay_cost=1)
	c_t3_t0_t0_t1_mem1 += INPUT_mem_r
	S += c_t3_t0_t0_t1_mem1 <= c_t3_t0_t0_t1

	c_t3_t0_t0_t2 = S.Task('c_t3_t0_t0_t2', length=1, delay_cost=1)
	c_t3_t0_t0_t2 += alt(ADD)

	c_t3_t0_t0_t2_mem0 = S.Task('c_t3_t0_t0_t2_mem0', length=1, delay_cost=1)
	c_t3_t0_t0_t2_mem0 += INPUT_mem_r
	S += c_t3_t0_t0_t2_mem0 <= c_t3_t0_t0_t2

	c_t3_t0_t0_t2_mem1 = S.Task('c_t3_t0_t0_t2_mem1', length=1, delay_cost=1)
	c_t3_t0_t0_t2_mem1 += INPUT_mem_r
	S += c_t3_t0_t0_t2_mem1 <= c_t3_t0_t0_t2

	c_t3_t0_t0_t3 = S.Task('c_t3_t0_t0_t3', length=1, delay_cost=1)
	c_t3_t0_t0_t3 += alt(ADD)

	c_t3_t0_t0_t3_mem0 = S.Task('c_t3_t0_t0_t3_mem0', length=1, delay_cost=1)
	c_t3_t0_t0_t3_mem0 += INPUT_mem_r
	S += c_t3_t0_t0_t3_mem0 <= c_t3_t0_t0_t3

	c_t3_t0_t0_t3_mem1 = S.Task('c_t3_t0_t0_t3_mem1', length=1, delay_cost=1)
	c_t3_t0_t0_t3_mem1 += INPUT_mem_r
	S += c_t3_t0_t0_t3_mem1 <= c_t3_t0_t0_t3

	c_t3_t0_t1_t0_in = S.Task('c_t3_t0_t1_t0_in', length=1, delay_cost=1)
	c_t3_t0_t1_t0_in += alt(MUL_in)
	c_t3_t0_t1_t0 = S.Task('c_t3_t0_t1_t0', length=7, delay_cost=1)
	c_t3_t0_t1_t0 += alt(MUL)
	S += c_t3_t0_t1_t0>=c_t3_t0_t1_t0_in

	c_t3_t0_t1_t0_mem0 = S.Task('c_t3_t0_t1_t0_mem0', length=1, delay_cost=1)
	c_t3_t0_t1_t0_mem0 += INPUT_mem_r
	S += c_t3_t0_t1_t0_mem0 <= c_t3_t0_t1_t0

	c_t3_t0_t1_t0_mem1 = S.Task('c_t3_t0_t1_t0_mem1', length=1, delay_cost=1)
	c_t3_t0_t1_t0_mem1 += INPUT_mem_r
	S += c_t3_t0_t1_t0_mem1 <= c_t3_t0_t1_t0

	c_t3_t0_t1_t1_in = S.Task('c_t3_t0_t1_t1_in', length=1, delay_cost=1)
	c_t3_t0_t1_t1_in += alt(MUL_in)
	c_t3_t0_t1_t1 = S.Task('c_t3_t0_t1_t1', length=7, delay_cost=1)
	c_t3_t0_t1_t1 += alt(MUL)
	S += c_t3_t0_t1_t1>=c_t3_t0_t1_t1_in

	c_t3_t0_t1_t1_mem0 = S.Task('c_t3_t0_t1_t1_mem0', length=1, delay_cost=1)
	c_t3_t0_t1_t1_mem0 += INPUT_mem_r
	S += c_t3_t0_t1_t1_mem0 <= c_t3_t0_t1_t1

	c_t3_t0_t1_t1_mem1 = S.Task('c_t3_t0_t1_t1_mem1', length=1, delay_cost=1)
	c_t3_t0_t1_t1_mem1 += INPUT_mem_r
	S += c_t3_t0_t1_t1_mem1 <= c_t3_t0_t1_t1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/SQR_mul1_add4/SQR_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

