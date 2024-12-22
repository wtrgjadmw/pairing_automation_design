from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 131
	S = Scenario("SQR012345_0", horizon=horizon)

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
	t0_a1__y1_0 = S.Task('t0_a1__y1_0', length=1, delay_cost=1)
	t0_a1__y1_0 += alt(ADD)

	t0_a1__y1_0_mem0 = S.Task('t0_a1__y1_0_mem0', length=1, delay_cost=1)
	t0_a1__y1_0_mem0 += INPUT_mem_r
	S += t0_a1__y1_0_mem0 <= t0_a1__y1_0

	t0_t01 = S.Task('t0_t01', length=1, delay_cost=1)
	t0_t01 += alt(ADD)

	t0_t01_mem0 = S.Task('t0_t01_mem0', length=1, delay_cost=1)
	t0_t01_mem0 += INPUT_mem_r
	S += t0_t01_mem0 <= t0_t01

	t0_t01_mem1 = S.Task('t0_t01_mem1', length=1, delay_cost=1)
	t0_t01_mem1 += INPUT_mem_r
	S += t0_t01_mem1 <= t0_t01

	t0_t10 = S.Task('t0_t10', length=1, delay_cost=1)
	t0_t10 += alt(ADD)

	t0_t10_mem0 = S.Task('t0_t10_mem0', length=1, delay_cost=1)
	t0_t10_mem0 += INPUT_mem_r
	S += t0_t10_mem0 <= t0_t10

	t0_t10_mem1 = S.Task('t0_t10_mem1', length=1, delay_cost=1)
	t0_t10_mem1 += INPUT_mem_r
	S += t0_t10_mem1 <= t0_t10

	t0_t11 = S.Task('t0_t11', length=1, delay_cost=1)
	t0_t11 += alt(ADD)

	t0_t11_mem0 = S.Task('t0_t11_mem0', length=1, delay_cost=1)
	t0_t11_mem0 += INPUT_mem_r
	S += t0_t11_mem0 <= t0_t11

	t0_t11_mem1 = S.Task('t0_t11_mem1', length=1, delay_cost=1)
	t0_t11_mem1 += INPUT_mem_r
	S += t0_t11_mem1 <= t0_t11

	t0_t3_t0_in = S.Task('t0_t3_t0_in', length=1, delay_cost=1)
	t0_t3_t0_in += alt(MUL_in)
	t0_t3_t0 = S.Task('t0_t3_t0', length=7, delay_cost=1)
	t0_t3_t0 += alt(MUL)
	S += t0_t3_t0>=t0_t3_t0_in

	t0_t3_t0_mem0 = S.Task('t0_t3_t0_mem0', length=1, delay_cost=1)
	t0_t3_t0_mem0 += INPUT_mem_r
	S += t0_t3_t0_mem0 <= t0_t3_t0

	t0_t3_t0_mem1 = S.Task('t0_t3_t0_mem1', length=1, delay_cost=1)
	t0_t3_t0_mem1 += INPUT_mem_r
	S += t0_t3_t0_mem1 <= t0_t3_t0

	t0_t3_t1_in = S.Task('t0_t3_t1_in', length=1, delay_cost=1)
	t0_t3_t1_in += alt(MUL_in)
	t0_t3_t1 = S.Task('t0_t3_t1', length=7, delay_cost=1)
	t0_t3_t1 += alt(MUL)
	S += t0_t3_t1>=t0_t3_t1_in

	t0_t3_t1_mem0 = S.Task('t0_t3_t1_mem0', length=1, delay_cost=1)
	t0_t3_t1_mem0 += INPUT_mem_r
	S += t0_t3_t1_mem0 <= t0_t3_t1

	t0_t3_t1_mem1 = S.Task('t0_t3_t1_mem1', length=1, delay_cost=1)
	t0_t3_t1_mem1 += INPUT_mem_r
	S += t0_t3_t1_mem1 <= t0_t3_t1

	t0_t3_t2 = S.Task('t0_t3_t2', length=1, delay_cost=1)
	t0_t3_t2 += alt(ADD)

	t0_t3_t2_mem0 = S.Task('t0_t3_t2_mem0', length=1, delay_cost=1)
	t0_t3_t2_mem0 += INPUT_mem_r
	S += t0_t3_t2_mem0 <= t0_t3_t2

	t0_t3_t2_mem1 = S.Task('t0_t3_t2_mem1', length=1, delay_cost=1)
	t0_t3_t2_mem1 += INPUT_mem_r
	S += t0_t3_t2_mem1 <= t0_t3_t2

	t0_t3_t3 = S.Task('t0_t3_t3', length=1, delay_cost=1)
	t0_t3_t3 += alt(ADD)

	t0_t3_t3_mem0 = S.Task('t0_t3_t3_mem0', length=1, delay_cost=1)
	t0_t3_t3_mem0 += INPUT_mem_r
	S += t0_t3_t3_mem0 <= t0_t3_t3

	t0_t3_t3_mem1 = S.Task('t0_t3_t3_mem1', length=1, delay_cost=1)
	t0_t3_t3_mem1 += INPUT_mem_r
	S += t0_t3_t3_mem1 <= t0_t3_t3

	t100 = S.Task('t100', length=1, delay_cost=1)
	t100 += alt(ADD)

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	t100_mem0 += INPUT_mem_r
	S += t100_mem0 <= t100

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	t100_mem1 += INPUT_mem_r
	S += t100_mem1 <= t100

	t101 = S.Task('t101', length=1, delay_cost=1)
	t101 += alt(ADD)

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	t101_mem0 += INPUT_mem_r
	S += t101_mem0 <= t101

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	t101_mem1 += INPUT_mem_r
	S += t101_mem1 <= t101

	t110 = S.Task('t110', length=1, delay_cost=1)
	t110 += alt(ADD)

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	t110_mem0 += INPUT_mem_r
	S += t110_mem0 <= t110

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	t110_mem1 += INPUT_mem_r
	S += t110_mem1 <= t110

	t111 = S.Task('t111', length=1, delay_cost=1)
	t111 += alt(ADD)

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	t111_mem0 += INPUT_mem_r
	S += t111_mem0 <= t111

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	t111_mem1 += INPUT_mem_r
	S += t111_mem1 <= t111

	t3_t0_t0_in = S.Task('t3_t0_t0_in', length=1, delay_cost=1)
	t3_t0_t0_in += alt(MUL_in)
	t3_t0_t0 = S.Task('t3_t0_t0', length=7, delay_cost=1)
	t3_t0_t0 += alt(MUL)
	S += t3_t0_t0>=t3_t0_t0_in

	t3_t0_t0_mem0 = S.Task('t3_t0_t0_mem0', length=1, delay_cost=1)
	t3_t0_t0_mem0 += INPUT_mem_r
	S += t3_t0_t0_mem0 <= t3_t0_t0

	t3_t0_t0_mem1 = S.Task('t3_t0_t0_mem1', length=1, delay_cost=1)
	t3_t0_t0_mem1 += INPUT_mem_r
	S += t3_t0_t0_mem1 <= t3_t0_t0

	t3_t0_t1_in = S.Task('t3_t0_t1_in', length=1, delay_cost=1)
	t3_t0_t1_in += alt(MUL_in)
	t3_t0_t1 = S.Task('t3_t0_t1', length=7, delay_cost=1)
	t3_t0_t1 += alt(MUL)
	S += t3_t0_t1>=t3_t0_t1_in

	t3_t0_t1_mem0 = S.Task('t3_t0_t1_mem0', length=1, delay_cost=1)
	t3_t0_t1_mem0 += INPUT_mem_r
	S += t3_t0_t1_mem0 <= t3_t0_t1

	t3_t0_t1_mem1 = S.Task('t3_t0_t1_mem1', length=1, delay_cost=1)
	t3_t0_t1_mem1 += INPUT_mem_r
	S += t3_t0_t1_mem1 <= t3_t0_t1

	t3_t0_t2 = S.Task('t3_t0_t2', length=1, delay_cost=1)
	t3_t0_t2 += alt(ADD)

	t3_t0_t2_mem0 = S.Task('t3_t0_t2_mem0', length=1, delay_cost=1)
	t3_t0_t2_mem0 += INPUT_mem_r
	S += t3_t0_t2_mem0 <= t3_t0_t2

	t3_t0_t2_mem1 = S.Task('t3_t0_t2_mem1', length=1, delay_cost=1)
	t3_t0_t2_mem1 += INPUT_mem_r
	S += t3_t0_t2_mem1 <= t3_t0_t2

	t3_t0_t3 = S.Task('t3_t0_t3', length=1, delay_cost=1)
	t3_t0_t3 += alt(ADD)

	t3_t0_t3_mem0 = S.Task('t3_t0_t3_mem0', length=1, delay_cost=1)
	t3_t0_t3_mem0 += INPUT_mem_r
	S += t3_t0_t3_mem0 <= t3_t0_t3

	t3_t0_t3_mem1 = S.Task('t3_t0_t3_mem1', length=1, delay_cost=1)
	t3_t0_t3_mem1 += INPUT_mem_r
	S += t3_t0_t3_mem1 <= t3_t0_t3

	t3_t1_t0_in = S.Task('t3_t1_t0_in', length=1, delay_cost=1)
	t3_t1_t0_in += alt(MUL_in)
	t3_t1_t0 = S.Task('t3_t1_t0', length=7, delay_cost=1)
	t3_t1_t0 += alt(MUL)
	S += t3_t1_t0>=t3_t1_t0_in

	t3_t1_t0_mem0 = S.Task('t3_t1_t0_mem0', length=1, delay_cost=1)
	t3_t1_t0_mem0 += INPUT_mem_r
	S += t3_t1_t0_mem0 <= t3_t1_t0

	t3_t1_t0_mem1 = S.Task('t3_t1_t0_mem1', length=1, delay_cost=1)
	t3_t1_t0_mem1 += INPUT_mem_r
	S += t3_t1_t0_mem1 <= t3_t1_t0

	t3_t1_t1_in = S.Task('t3_t1_t1_in', length=1, delay_cost=1)
	t3_t1_t1_in += alt(MUL_in)
	t3_t1_t1 = S.Task('t3_t1_t1', length=7, delay_cost=1)
	t3_t1_t1 += alt(MUL)
	S += t3_t1_t1>=t3_t1_t1_in

	t3_t1_t1_mem0 = S.Task('t3_t1_t1_mem0', length=1, delay_cost=1)
	t3_t1_t1_mem0 += INPUT_mem_r
	S += t3_t1_t1_mem0 <= t3_t1_t1

	t3_t1_t1_mem1 = S.Task('t3_t1_t1_mem1', length=1, delay_cost=1)
	t3_t1_t1_mem1 += INPUT_mem_r
	S += t3_t1_t1_mem1 <= t3_t1_t1

	t3_t1_t2 = S.Task('t3_t1_t2', length=1, delay_cost=1)
	t3_t1_t2 += alt(ADD)

	t3_t1_t2_mem0 = S.Task('t3_t1_t2_mem0', length=1, delay_cost=1)
	t3_t1_t2_mem0 += INPUT_mem_r
	S += t3_t1_t2_mem0 <= t3_t1_t2

	t3_t1_t2_mem1 = S.Task('t3_t1_t2_mem1', length=1, delay_cost=1)
	t3_t1_t2_mem1 += INPUT_mem_r
	S += t3_t1_t2_mem1 <= t3_t1_t2

	t3_t1_t3 = S.Task('t3_t1_t3', length=1, delay_cost=1)
	t3_t1_t3 += alt(ADD)

	t3_t1_t3_mem0 = S.Task('t3_t1_t3_mem0', length=1, delay_cost=1)
	t3_t1_t3_mem0 += INPUT_mem_r
	S += t3_t1_t3_mem0 <= t3_t1_t3

	t3_t1_t3_mem1 = S.Task('t3_t1_t3_mem1', length=1, delay_cost=1)
	t3_t1_t3_mem1 += INPUT_mem_r
	S += t3_t1_t3_mem1 <= t3_t1_t3

	t3_t20 = S.Task('t3_t20', length=1, delay_cost=1)
	t3_t20 += alt(ADD)

	t3_t20_mem0 = S.Task('t3_t20_mem0', length=1, delay_cost=1)
	t3_t20_mem0 += INPUT_mem_r
	S += t3_t20_mem0 <= t3_t20

	t3_t20_mem1 = S.Task('t3_t20_mem1', length=1, delay_cost=1)
	t3_t20_mem1 += INPUT_mem_r
	S += t3_t20_mem1 <= t3_t20

	t3_t21 = S.Task('t3_t21', length=1, delay_cost=1)
	t3_t21 += alt(ADD)

	t3_t21_mem0 = S.Task('t3_t21_mem0', length=1, delay_cost=1)
	t3_t21_mem0 += INPUT_mem_r
	S += t3_t21_mem0 <= t3_t21

	t3_t21_mem1 = S.Task('t3_t21_mem1', length=1, delay_cost=1)
	t3_t21_mem1 += INPUT_mem_r
	S += t3_t21_mem1 <= t3_t21

	t3_t30 = S.Task('t3_t30', length=1, delay_cost=1)
	t3_t30 += alt(ADD)

	t3_t30_mem0 = S.Task('t3_t30_mem0', length=1, delay_cost=1)
	t3_t30_mem0 += INPUT_mem_r
	S += t3_t30_mem0 <= t3_t30

	t3_t30_mem1 = S.Task('t3_t30_mem1', length=1, delay_cost=1)
	t3_t30_mem1 += INPUT_mem_r
	S += t3_t30_mem1 <= t3_t30

	t3_t31 = S.Task('t3_t31', length=1, delay_cost=1)
	t3_t31 += alt(ADD)

	t3_t31_mem0 = S.Task('t3_t31_mem0', length=1, delay_cost=1)
	t3_t31_mem0 += INPUT_mem_r
	S += t3_t31_mem0 <= t3_t31

	t3_t31_mem1 = S.Task('t3_t31_mem1', length=1, delay_cost=1)
	t3_t31_mem1 += INPUT_mem_r
	S += t3_t31_mem1 <= t3_t31

	t4_a1__y1_0 = S.Task('t4_a1__y1_0', length=1, delay_cost=1)
	t4_a1__y1_0 += alt(ADD)

	t4_a1__y1_0_mem0 = S.Task('t4_a1__y1_0_mem0', length=1, delay_cost=1)
	t4_a1__y1_0_mem0 += INPUT_mem_r
	S += t4_a1__y1_0_mem0 <= t4_a1__y1_0

	t4_t01 = S.Task('t4_t01', length=1, delay_cost=1)
	t4_t01 += alt(ADD)

	t4_t01_mem0 = S.Task('t4_t01_mem0', length=1, delay_cost=1)
	t4_t01_mem0 += INPUT_mem_r
	S += t4_t01_mem0 <= t4_t01

	t4_t01_mem1 = S.Task('t4_t01_mem1', length=1, delay_cost=1)
	t4_t01_mem1 += INPUT_mem_r
	S += t4_t01_mem1 <= t4_t01

	t4_t10 = S.Task('t4_t10', length=1, delay_cost=1)
	t4_t10 += alt(ADD)

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	t4_t10_mem0 += INPUT_mem_r
	S += t4_t10_mem0 <= t4_t10

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	t4_t10_mem1 += INPUT_mem_r
	S += t4_t10_mem1 <= t4_t10

	t4_t11 = S.Task('t4_t11', length=1, delay_cost=1)
	t4_t11 += alt(ADD)

	t4_t11_mem0 = S.Task('t4_t11_mem0', length=1, delay_cost=1)
	t4_t11_mem0 += INPUT_mem_r
	S += t4_t11_mem0 <= t4_t11

	t4_t11_mem1 = S.Task('t4_t11_mem1', length=1, delay_cost=1)
	t4_t11_mem1 += INPUT_mem_r
	S += t4_t11_mem1 <= t4_t11

	t4_t3_t0_in = S.Task('t4_t3_t0_in', length=1, delay_cost=1)
	t4_t3_t0_in += alt(MUL_in)
	t4_t3_t0 = S.Task('t4_t3_t0', length=7, delay_cost=1)
	t4_t3_t0 += alt(MUL)
	S += t4_t3_t0>=t4_t3_t0_in

	t4_t3_t0_mem0 = S.Task('t4_t3_t0_mem0', length=1, delay_cost=1)
	t4_t3_t0_mem0 += INPUT_mem_r
	S += t4_t3_t0_mem0 <= t4_t3_t0

	t4_t3_t0_mem1 = S.Task('t4_t3_t0_mem1', length=1, delay_cost=1)
	t4_t3_t0_mem1 += INPUT_mem_r
	S += t4_t3_t0_mem1 <= t4_t3_t0

	t4_t3_t1_in = S.Task('t4_t3_t1_in', length=1, delay_cost=1)
	t4_t3_t1_in += alt(MUL_in)
	t4_t3_t1 = S.Task('t4_t3_t1', length=7, delay_cost=1)
	t4_t3_t1 += alt(MUL)
	S += t4_t3_t1>=t4_t3_t1_in

	t4_t3_t1_mem0 = S.Task('t4_t3_t1_mem0', length=1, delay_cost=1)
	t4_t3_t1_mem0 += INPUT_mem_r
	S += t4_t3_t1_mem0 <= t4_t3_t1

	t4_t3_t1_mem1 = S.Task('t4_t3_t1_mem1', length=1, delay_cost=1)
	t4_t3_t1_mem1 += INPUT_mem_r
	S += t4_t3_t1_mem1 <= t4_t3_t1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/SQR012345_mul1_add4/SQR012345_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

