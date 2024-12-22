from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 121
	S = Scenario("FROB_0", horizon=horizon)

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
	c_f101_t0_in = S.Task('c_f101_t0_in', length=1, delay_cost=1)
	c_f101_t0_in += alt(MUL_in)
	c_f101_t0 = S.Task('c_f101_t0', length=7, delay_cost=1)
	c_f101_t0 += alt(MUL)
	S += c_f101_t0>=c_f101_t0_in

	c_f101_t0_mem0 = S.Task('c_f101_t0_mem0', length=1, delay_cost=1)
	c_f101_t0_mem0 += INPUT_mem_r
	S += c_f101_t0_mem0 <= c_f101_t0

	c_f101_t0_mem1 = S.Task('c_f101_t0_mem1', length=1, delay_cost=1)
	c_f101_t0_mem1 += INPUT_mem_r
	S += c_f101_t0_mem1 <= c_f101_t0

	c_f101_t1_in = S.Task('c_f101_t1_in', length=1, delay_cost=1)
	c_f101_t1_in += alt(MUL_in)
	c_f101_t1 = S.Task('c_f101_t1', length=7, delay_cost=1)
	c_f101_t1 += alt(MUL)
	S += c_f101_t1>=c_f101_t1_in

	c_f101_t1_mem0 = S.Task('c_f101_t1_mem0', length=1, delay_cost=1)
	c_f101_t1_mem0 += INPUT_mem_r
	S += c_f101_t1_mem0 <= c_f101_t1

	c_f101_t1_mem1 = S.Task('c_f101_t1_mem1', length=1, delay_cost=1)
	c_f101_t1_mem1 += INPUT_mem_r
	S += c_f101_t1_mem1 <= c_f101_t1

	c_f101_t2 = S.Task('c_f101_t2', length=1, delay_cost=1)
	c_f101_t2 += alt(ADD)

	c_f101_t2_mem0 = S.Task('c_f101_t2_mem0', length=1, delay_cost=1)
	c_f101_t2_mem0 += INPUT_mem_r
	S += c_f101_t2_mem0 <= c_f101_t2

	c_f101_t2_mem1 = S.Task('c_f101_t2_mem1', length=1, delay_cost=1)
	c_f101_t2_mem1 += INPUT_mem_r
	S += c_f101_t2_mem1 <= c_f101_t2

	c_f101_t3 = S.Task('c_f101_t3', length=1, delay_cost=1)
	c_f101_t3 += alt(ADD)

	c_f101_t3_mem0 = S.Task('c_f101_t3_mem0', length=1, delay_cost=1)
	c_f101_t3_mem0 += INPUT_mem_r
	S += c_f101_t3_mem0 <= c_f101_t3

	c_f101_t3_mem1 = S.Task('c_f101_t3_mem1', length=1, delay_cost=1)
	c_f101_t3_mem1 += INPUT_mem_r
	S += c_f101_t3_mem1 <= c_f101_t3

	c_f011_t0_in = S.Task('c_f011_t0_in', length=1, delay_cost=1)
	c_f011_t0_in += alt(MUL_in)
	c_f011_t0 = S.Task('c_f011_t0', length=7, delay_cost=1)
	c_f011_t0 += alt(MUL)
	S += c_f011_t0>=c_f011_t0_in

	c_f011_t0_mem0 = S.Task('c_f011_t0_mem0', length=1, delay_cost=1)
	c_f011_t0_mem0 += INPUT_mem_r
	S += c_f011_t0_mem0 <= c_f011_t0

	c_f011_t0_mem1 = S.Task('c_f011_t0_mem1', length=1, delay_cost=1)
	c_f011_t0_mem1 += INPUT_mem_r
	S += c_f011_t0_mem1 <= c_f011_t0

	c_f011_t1_in = S.Task('c_f011_t1_in', length=1, delay_cost=1)
	c_f011_t1_in += alt(MUL_in)
	c_f011_t1 = S.Task('c_f011_t1', length=7, delay_cost=1)
	c_f011_t1 += alt(MUL)
	S += c_f011_t1>=c_f011_t1_in

	c_f011_t1_mem0 = S.Task('c_f011_t1_mem0', length=1, delay_cost=1)
	c_f011_t1_mem0 += INPUT_mem_r
	S += c_f011_t1_mem0 <= c_f011_t1

	c_f011_t1_mem1 = S.Task('c_f011_t1_mem1', length=1, delay_cost=1)
	c_f011_t1_mem1 += INPUT_mem_r
	S += c_f011_t1_mem1 <= c_f011_t1

	c_f011_t2 = S.Task('c_f011_t2', length=1, delay_cost=1)
	c_f011_t2 += alt(ADD)

	c_f011_t2_mem0 = S.Task('c_f011_t2_mem0', length=1, delay_cost=1)
	c_f011_t2_mem0 += INPUT_mem_r
	S += c_f011_t2_mem0 <= c_f011_t2

	c_f011_t2_mem1 = S.Task('c_f011_t2_mem1', length=1, delay_cost=1)
	c_f011_t2_mem1 += INPUT_mem_r
	S += c_f011_t2_mem1 <= c_f011_t2

	c_f011_t3 = S.Task('c_f011_t3', length=1, delay_cost=1)
	c_f011_t3 += alt(ADD)

	c_f011_t3_mem0 = S.Task('c_f011_t3_mem0', length=1, delay_cost=1)
	c_f011_t3_mem0 += INPUT_mem_r
	S += c_f011_t3_mem0 <= c_f011_t3

	c_f011_t3_mem1 = S.Task('c_f011_t3_mem1', length=1, delay_cost=1)
	c_f011_t3_mem1 += INPUT_mem_r
	S += c_f011_t3_mem1 <= c_f011_t3

	c_f111_t0_in = S.Task('c_f111_t0_in', length=1, delay_cost=1)
	c_f111_t0_in += alt(MUL_in)
	c_f111_t0 = S.Task('c_f111_t0', length=7, delay_cost=1)
	c_f111_t0 += alt(MUL)
	S += c_f111_t0>=c_f111_t0_in

	c_f111_t0_mem0 = S.Task('c_f111_t0_mem0', length=1, delay_cost=1)
	c_f111_t0_mem0 += INPUT_mem_r
	S += c_f111_t0_mem0 <= c_f111_t0

	c_f111_t0_mem1 = S.Task('c_f111_t0_mem1', length=1, delay_cost=1)
	c_f111_t0_mem1 += INPUT_mem_r
	S += c_f111_t0_mem1 <= c_f111_t0

	c_f111_t1_in = S.Task('c_f111_t1_in', length=1, delay_cost=1)
	c_f111_t1_in += alt(MUL_in)
	c_f111_t1 = S.Task('c_f111_t1', length=7, delay_cost=1)
	c_f111_t1 += alt(MUL)
	S += c_f111_t1>=c_f111_t1_in

	c_f111_t1_mem0 = S.Task('c_f111_t1_mem0', length=1, delay_cost=1)
	c_f111_t1_mem0 += INPUT_mem_r
	S += c_f111_t1_mem0 <= c_f111_t1

	c_f111_t1_mem1 = S.Task('c_f111_t1_mem1', length=1, delay_cost=1)
	c_f111_t1_mem1 += INPUT_mem_r
	S += c_f111_t1_mem1 <= c_f111_t1

	c_f111_t2 = S.Task('c_f111_t2', length=1, delay_cost=1)
	c_f111_t2 += alt(ADD)

	c_f111_t2_mem0 = S.Task('c_f111_t2_mem0', length=1, delay_cost=1)
	c_f111_t2_mem0 += INPUT_mem_r
	S += c_f111_t2_mem0 <= c_f111_t2

	c_f111_t2_mem1 = S.Task('c_f111_t2_mem1', length=1, delay_cost=1)
	c_f111_t2_mem1 += INPUT_mem_r
	S += c_f111_t2_mem1 <= c_f111_t2

	c_f111_t3 = S.Task('c_f111_t3', length=1, delay_cost=1)
	c_f111_t3 += alt(ADD)

	c_f111_t3_mem0 = S.Task('c_f111_t3_mem0', length=1, delay_cost=1)
	c_f111_t3_mem0 += INPUT_mem_r
	S += c_f111_t3_mem0 <= c_f111_t3

	c_f111_t3_mem1 = S.Task('c_f111_t3_mem1', length=1, delay_cost=1)
	c_f111_t3_mem1 += INPUT_mem_r
	S += c_f111_t3_mem1 <= c_f111_t3

	c_f021_t0_in = S.Task('c_f021_t0_in', length=1, delay_cost=1)
	c_f021_t0_in += alt(MUL_in)
	c_f021_t0 = S.Task('c_f021_t0', length=7, delay_cost=1)
	c_f021_t0 += alt(MUL)
	S += c_f021_t0>=c_f021_t0_in

	c_f021_t0_mem0 = S.Task('c_f021_t0_mem0', length=1, delay_cost=1)
	c_f021_t0_mem0 += INPUT_mem_r
	S += c_f021_t0_mem0 <= c_f021_t0

	c_f021_t0_mem1 = S.Task('c_f021_t0_mem1', length=1, delay_cost=1)
	c_f021_t0_mem1 += INPUT_mem_r
	S += c_f021_t0_mem1 <= c_f021_t0

	c_f021_t1_in = S.Task('c_f021_t1_in', length=1, delay_cost=1)
	c_f021_t1_in += alt(MUL_in)
	c_f021_t1 = S.Task('c_f021_t1', length=7, delay_cost=1)
	c_f021_t1 += alt(MUL)
	S += c_f021_t1>=c_f021_t1_in

	c_f021_t1_mem0 = S.Task('c_f021_t1_mem0', length=1, delay_cost=1)
	c_f021_t1_mem0 += INPUT_mem_r
	S += c_f021_t1_mem0 <= c_f021_t1

	c_f021_t1_mem1 = S.Task('c_f021_t1_mem1', length=1, delay_cost=1)
	c_f021_t1_mem1 += INPUT_mem_r
	S += c_f021_t1_mem1 <= c_f021_t1

	c_f021_t2 = S.Task('c_f021_t2', length=1, delay_cost=1)
	c_f021_t2 += alt(ADD)

	c_f021_t2_mem0 = S.Task('c_f021_t2_mem0', length=1, delay_cost=1)
	c_f021_t2_mem0 += INPUT_mem_r
	S += c_f021_t2_mem0 <= c_f021_t2

	c_f021_t2_mem1 = S.Task('c_f021_t2_mem1', length=1, delay_cost=1)
	c_f021_t2_mem1 += INPUT_mem_r
	S += c_f021_t2_mem1 <= c_f021_t2

	c_f021_t3 = S.Task('c_f021_t3', length=1, delay_cost=1)
	c_f021_t3 += alt(ADD)

	c_f021_t3_mem0 = S.Task('c_f021_t3_mem0', length=1, delay_cost=1)
	c_f021_t3_mem0 += INPUT_mem_r
	S += c_f021_t3_mem0 <= c_f021_t3

	c_f021_t3_mem1 = S.Task('c_f021_t3_mem1', length=1, delay_cost=1)
	c_f021_t3_mem1 += INPUT_mem_r
	S += c_f021_t3_mem1 <= c_f021_t3

	c_f121_t0_in = S.Task('c_f121_t0_in', length=1, delay_cost=1)
	c_f121_t0_in += alt(MUL_in)
	c_f121_t0 = S.Task('c_f121_t0', length=7, delay_cost=1)
	c_f121_t0 += alt(MUL)
	S += c_f121_t0>=c_f121_t0_in

	c_f121_t0_mem0 = S.Task('c_f121_t0_mem0', length=1, delay_cost=1)
	c_f121_t0_mem0 += INPUT_mem_r
	S += c_f121_t0_mem0 <= c_f121_t0

	c_f121_t0_mem1 = S.Task('c_f121_t0_mem1', length=1, delay_cost=1)
	c_f121_t0_mem1 += INPUT_mem_r
	S += c_f121_t0_mem1 <= c_f121_t0

	c_f121_t1_in = S.Task('c_f121_t1_in', length=1, delay_cost=1)
	c_f121_t1_in += alt(MUL_in)
	c_f121_t1 = S.Task('c_f121_t1', length=7, delay_cost=1)
	c_f121_t1 += alt(MUL)
	S += c_f121_t1>=c_f121_t1_in

	c_f121_t1_mem0 = S.Task('c_f121_t1_mem0', length=1, delay_cost=1)
	c_f121_t1_mem0 += INPUT_mem_r
	S += c_f121_t1_mem0 <= c_f121_t1

	c_f121_t1_mem1 = S.Task('c_f121_t1_mem1', length=1, delay_cost=1)
	c_f121_t1_mem1 += INPUT_mem_r
	S += c_f121_t1_mem1 <= c_f121_t1

	c_f121_t2 = S.Task('c_f121_t2', length=1, delay_cost=1)
	c_f121_t2 += alt(ADD)

	c_f121_t2_mem0 = S.Task('c_f121_t2_mem0', length=1, delay_cost=1)
	c_f121_t2_mem0 += INPUT_mem_r
	S += c_f121_t2_mem0 <= c_f121_t2

	c_f121_t2_mem1 = S.Task('c_f121_t2_mem1', length=1, delay_cost=1)
	c_f121_t2_mem1 += INPUT_mem_r
	S += c_f121_t2_mem1 <= c_f121_t2

	c_f121_t3 = S.Task('c_f121_t3', length=1, delay_cost=1)
	c_f121_t3 += alt(ADD)

	c_f121_t3_mem0 = S.Task('c_f121_t3_mem0', length=1, delay_cost=1)
	c_f121_t3_mem0 += INPUT_mem_r
	S += c_f121_t3_mem0 <= c_f121_t3

	c_f121_t3_mem1 = S.Task('c_f121_t3_mem1', length=1, delay_cost=1)
	c_f121_t3_mem1 += INPUT_mem_r
	S += c_f121_t3_mem1 <= c_f121_t3

	c001_t0_in = S.Task('c001_t0_in', length=1, delay_cost=1)
	c001_t0_in += alt(MUL_in)
	c001_t0 = S.Task('c001_t0', length=7, delay_cost=1)
	c001_t0 += alt(MUL)
	S += c001_t0>=c001_t0_in

	c001_t0_mem0 = S.Task('c001_t0_mem0', length=1, delay_cost=1)
	c001_t0_mem0 += INPUT_mem_r
	S += c001_t0_mem0 <= c001_t0

	c001_t0_mem1 = S.Task('c001_t0_mem1', length=1, delay_cost=1)
	c001_t0_mem1 += INPUT_mem_r
	S += c001_t0_mem1 <= c001_t0

	c001_t1_in = S.Task('c001_t1_in', length=1, delay_cost=1)
	c001_t1_in += alt(MUL_in)
	c001_t1 = S.Task('c001_t1', length=7, delay_cost=1)
	c001_t1 += alt(MUL)
	S += c001_t1>=c001_t1_in

	c001_t1_mem0 = S.Task('c001_t1_mem0', length=1, delay_cost=1)
	c001_t1_mem0 += INPUT_mem_r
	S += c001_t1_mem0 <= c001_t1

	c001_t1_mem1 = S.Task('c001_t1_mem1', length=1, delay_cost=1)
	c001_t1_mem1 += INPUT_mem_r
	S += c001_t1_mem1 <= c001_t1

	c001_t2 = S.Task('c001_t2', length=1, delay_cost=1)
	c001_t2 += alt(ADD)

	c001_t2_mem0 = S.Task('c001_t2_mem0', length=1, delay_cost=1)
	c001_t2_mem0 += INPUT_mem_r
	S += c001_t2_mem0 <= c001_t2

	c001_t2_mem1 = S.Task('c001_t2_mem1', length=1, delay_cost=1)
	c001_t2_mem1 += INPUT_mem_r
	S += c001_t2_mem1 <= c001_t2

	c001_t3 = S.Task('c001_t3', length=1, delay_cost=1)
	c001_t3 += alt(ADD)

	c001_t3_mem0 = S.Task('c001_t3_mem0', length=1, delay_cost=1)
	c001_t3_mem0 += INPUT_mem_r
	S += c001_t3_mem0 <= c001_t3

	c001_t3_mem1 = S.Task('c001_t3_mem1', length=1, delay_cost=1)
	c001_t3_mem1 += INPUT_mem_r
	S += c001_t3_mem1 <= c001_t3

	c10_t0_t0_in = S.Task('c10_t0_t0_in', length=1, delay_cost=1)
	c10_t0_t0_in += alt(MUL_in)
	c10_t0_t0 = S.Task('c10_t0_t0', length=7, delay_cost=1)
	c10_t0_t0 += alt(MUL)
	S += c10_t0_t0>=c10_t0_t0_in

	c10_t0_t0_mem0 = S.Task('c10_t0_t0_mem0', length=1, delay_cost=1)
	c10_t0_t0_mem0 += INPUT_mem_r
	S += c10_t0_t0_mem0 <= c10_t0_t0

	c10_t0_t0_mem1 = S.Task('c10_t0_t0_mem1', length=1, delay_cost=1)
	c10_t0_t0_mem1 += INPUT_mem_r
	S += c10_t0_t0_mem1 <= c10_t0_t0

	c10_t0_t1_in = S.Task('c10_t0_t1_in', length=1, delay_cost=1)
	c10_t0_t1_in += alt(MUL_in)
	c10_t0_t1 = S.Task('c10_t0_t1', length=7, delay_cost=1)
	c10_t0_t1 += alt(MUL)
	S += c10_t0_t1>=c10_t0_t1_in

	c10_t0_t1_mem0 = S.Task('c10_t0_t1_mem0', length=1, delay_cost=1)
	c10_t0_t1_mem0 += INPUT_mem_r
	S += c10_t0_t1_mem0 <= c10_t0_t1

	c10_t0_t1_mem1 = S.Task('c10_t0_t1_mem1', length=1, delay_cost=1)
	c10_t0_t1_mem1 += INPUT_mem_r
	S += c10_t0_t1_mem1 <= c10_t0_t1

	c10_t0_t2 = S.Task('c10_t0_t2', length=1, delay_cost=1)
	c10_t0_t2 += alt(ADD)

	c10_t0_t2_mem0 = S.Task('c10_t0_t2_mem0', length=1, delay_cost=1)
	c10_t0_t2_mem0 += INPUT_mem_r
	S += c10_t0_t2_mem0 <= c10_t0_t2

	c10_t0_t2_mem1 = S.Task('c10_t0_t2_mem1', length=1, delay_cost=1)
	c10_t0_t2_mem1 += INPUT_mem_r
	S += c10_t0_t2_mem1 <= c10_t0_t2

	c10_t0_t3 = S.Task('c10_t0_t3', length=1, delay_cost=1)
	c10_t0_t3 += alt(ADD)

	c10_t0_t3_mem0 = S.Task('c10_t0_t3_mem0', length=1, delay_cost=1)
	c10_t0_t3_mem0 += INPUT_mem_r
	S += c10_t0_t3_mem0 <= c10_t0_t3

	c10_t0_t3_mem1 = S.Task('c10_t0_t3_mem1', length=1, delay_cost=1)
	c10_t0_t3_mem1 += INPUT_mem_r
	S += c10_t0_t3_mem1 <= c10_t0_t3

	c10_t1_t3 = S.Task('c10_t1_t3', length=1, delay_cost=1)
	c10_t1_t3 += alt(ADD)

	c10_t1_t3_mem0 = S.Task('c10_t1_t3_mem0', length=1, delay_cost=1)
	c10_t1_t3_mem0 += INPUT_mem_r
	S += c10_t1_t3_mem0 <= c10_t1_t3

	c10_t1_t3_mem1 = S.Task('c10_t1_t3_mem1', length=1, delay_cost=1)
	c10_t1_t3_mem1 += INPUT_mem_r
	S += c10_t1_t3_mem1 <= c10_t1_t3

	c10_t30 = S.Task('c10_t30', length=1, delay_cost=1)
	c10_t30 += alt(ADD)

	c10_t30_mem0 = S.Task('c10_t30_mem0', length=1, delay_cost=1)
	c10_t30_mem0 += INPUT_mem_r
	S += c10_t30_mem0 <= c10_t30

	c10_t30_mem1 = S.Task('c10_t30_mem1', length=1, delay_cost=1)
	c10_t30_mem1 += INPUT_mem_r
	S += c10_t30_mem1 <= c10_t30

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/FROB_mul1_add4/FROB_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

