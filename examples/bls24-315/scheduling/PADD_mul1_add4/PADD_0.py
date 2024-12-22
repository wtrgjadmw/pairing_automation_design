from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("PADD_0", horizon=horizon)

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
	t0_t0_t0_in = S.Task('t0_t0_t0_in', length=1, delay_cost=1)
	t0_t0_t0_in += alt(MUL_in)
	t0_t0_t0 = S.Task('t0_t0_t0', length=7, delay_cost=1)
	t0_t0_t0 += alt(MUL)
	S += t0_t0_t0>=t0_t0_t0_in

	t0_t0_t0_mem0 = S.Task('t0_t0_t0_mem0', length=1, delay_cost=1)
	t0_t0_t0_mem0 += INPUT_mem_r
	S += t0_t0_t0_mem0 <= t0_t0_t0

	t0_t0_t0_mem1 = S.Task('t0_t0_t0_mem1', length=1, delay_cost=1)
	t0_t0_t0_mem1 += INPUT_mem_r
	S += t0_t0_t0_mem1 <= t0_t0_t0

	t0_t0_t1_in = S.Task('t0_t0_t1_in', length=1, delay_cost=1)
	t0_t0_t1_in += alt(MUL_in)
	t0_t0_t1 = S.Task('t0_t0_t1', length=7, delay_cost=1)
	t0_t0_t1 += alt(MUL)
	S += t0_t0_t1>=t0_t0_t1_in

	t0_t0_t1_mem0 = S.Task('t0_t0_t1_mem0', length=1, delay_cost=1)
	t0_t0_t1_mem0 += INPUT_mem_r
	S += t0_t0_t1_mem0 <= t0_t0_t1

	t0_t0_t1_mem1 = S.Task('t0_t0_t1_mem1', length=1, delay_cost=1)
	t0_t0_t1_mem1 += INPUT_mem_r
	S += t0_t0_t1_mem1 <= t0_t0_t1

	t0_t0_t2 = S.Task('t0_t0_t2', length=1, delay_cost=1)
	t0_t0_t2 += alt(ADD)

	t0_t0_t2_mem0 = S.Task('t0_t0_t2_mem0', length=1, delay_cost=1)
	t0_t0_t2_mem0 += INPUT_mem_r
	S += t0_t0_t2_mem0 <= t0_t0_t2

	t0_t0_t2_mem1 = S.Task('t0_t0_t2_mem1', length=1, delay_cost=1)
	t0_t0_t2_mem1 += INPUT_mem_r
	S += t0_t0_t2_mem1 <= t0_t0_t2

	t0_t0_t3 = S.Task('t0_t0_t3', length=1, delay_cost=1)
	t0_t0_t3 += alt(ADD)

	t0_t0_t3_mem0 = S.Task('t0_t0_t3_mem0', length=1, delay_cost=1)
	t0_t0_t3_mem0 += INPUT_mem_r
	S += t0_t0_t3_mem0 <= t0_t0_t3

	t0_t0_t3_mem1 = S.Task('t0_t0_t3_mem1', length=1, delay_cost=1)
	t0_t0_t3_mem1 += INPUT_mem_r
	S += t0_t0_t3_mem1 <= t0_t0_t3

	t0_t1_t0_in = S.Task('t0_t1_t0_in', length=1, delay_cost=1)
	t0_t1_t0_in += alt(MUL_in)
	t0_t1_t0 = S.Task('t0_t1_t0', length=7, delay_cost=1)
	t0_t1_t0 += alt(MUL)
	S += t0_t1_t0>=t0_t1_t0_in

	t0_t1_t0_mem0 = S.Task('t0_t1_t0_mem0', length=1, delay_cost=1)
	t0_t1_t0_mem0 += INPUT_mem_r
	S += t0_t1_t0_mem0 <= t0_t1_t0

	t0_t1_t0_mem1 = S.Task('t0_t1_t0_mem1', length=1, delay_cost=1)
	t0_t1_t0_mem1 += INPUT_mem_r
	S += t0_t1_t0_mem1 <= t0_t1_t0

	t0_t1_t1_in = S.Task('t0_t1_t1_in', length=1, delay_cost=1)
	t0_t1_t1_in += alt(MUL_in)
	t0_t1_t1 = S.Task('t0_t1_t1', length=7, delay_cost=1)
	t0_t1_t1 += alt(MUL)
	S += t0_t1_t1>=t0_t1_t1_in

	t0_t1_t1_mem0 = S.Task('t0_t1_t1_mem0', length=1, delay_cost=1)
	t0_t1_t1_mem0 += INPUT_mem_r
	S += t0_t1_t1_mem0 <= t0_t1_t1

	t0_t1_t1_mem1 = S.Task('t0_t1_t1_mem1', length=1, delay_cost=1)
	t0_t1_t1_mem1 += INPUT_mem_r
	S += t0_t1_t1_mem1 <= t0_t1_t1

	t0_t1_t2 = S.Task('t0_t1_t2', length=1, delay_cost=1)
	t0_t1_t2 += alt(ADD)

	t0_t1_t2_mem0 = S.Task('t0_t1_t2_mem0', length=1, delay_cost=1)
	t0_t1_t2_mem0 += INPUT_mem_r
	S += t0_t1_t2_mem0 <= t0_t1_t2

	t0_t1_t2_mem1 = S.Task('t0_t1_t2_mem1', length=1, delay_cost=1)
	t0_t1_t2_mem1 += INPUT_mem_r
	S += t0_t1_t2_mem1 <= t0_t1_t2

	t0_t1_t3 = S.Task('t0_t1_t3', length=1, delay_cost=1)
	t0_t1_t3 += alt(ADD)

	t0_t1_t3_mem0 = S.Task('t0_t1_t3_mem0', length=1, delay_cost=1)
	t0_t1_t3_mem0 += INPUT_mem_r
	S += t0_t1_t3_mem0 <= t0_t1_t3

	t0_t1_t3_mem1 = S.Task('t0_t1_t3_mem1', length=1, delay_cost=1)
	t0_t1_t3_mem1 += INPUT_mem_r
	S += t0_t1_t3_mem1 <= t0_t1_t3

	t0_t20 = S.Task('t0_t20', length=1, delay_cost=1)
	t0_t20 += alt(ADD)

	t0_t20_mem0 = S.Task('t0_t20_mem0', length=1, delay_cost=1)
	t0_t20_mem0 += INPUT_mem_r
	S += t0_t20_mem0 <= t0_t20

	t0_t20_mem1 = S.Task('t0_t20_mem1', length=1, delay_cost=1)
	t0_t20_mem1 += INPUT_mem_r
	S += t0_t20_mem1 <= t0_t20

	t0_t21 = S.Task('t0_t21', length=1, delay_cost=1)
	t0_t21 += alt(ADD)

	t0_t21_mem0 = S.Task('t0_t21_mem0', length=1, delay_cost=1)
	t0_t21_mem0 += INPUT_mem_r
	S += t0_t21_mem0 <= t0_t21

	t0_t21_mem1 = S.Task('t0_t21_mem1', length=1, delay_cost=1)
	t0_t21_mem1 += INPUT_mem_r
	S += t0_t21_mem1 <= t0_t21

	t0_t30 = S.Task('t0_t30', length=1, delay_cost=1)
	t0_t30 += alt(ADD)

	t0_t30_mem0 = S.Task('t0_t30_mem0', length=1, delay_cost=1)
	t0_t30_mem0 += INPUT_mem_r
	S += t0_t30_mem0 <= t0_t30

	t0_t30_mem1 = S.Task('t0_t30_mem1', length=1, delay_cost=1)
	t0_t30_mem1 += INPUT_mem_r
	S += t0_t30_mem1 <= t0_t30

	t0_t31 = S.Task('t0_t31', length=1, delay_cost=1)
	t0_t31 += alt(ADD)

	t0_t31_mem0 = S.Task('t0_t31_mem0', length=1, delay_cost=1)
	t0_t31_mem0 += INPUT_mem_r
	S += t0_t31_mem0 <= t0_t31

	t0_t31_mem1 = S.Task('t0_t31_mem1', length=1, delay_cost=1)
	t0_t31_mem1 += INPUT_mem_r
	S += t0_t31_mem1 <= t0_t31

	t2_t0_t0_in = S.Task('t2_t0_t0_in', length=1, delay_cost=1)
	t2_t0_t0_in += alt(MUL_in)
	t2_t0_t0 = S.Task('t2_t0_t0', length=7, delay_cost=1)
	t2_t0_t0 += alt(MUL)
	S += t2_t0_t0>=t2_t0_t0_in

	t2_t0_t0_mem0 = S.Task('t2_t0_t0_mem0', length=1, delay_cost=1)
	t2_t0_t0_mem0 += INPUT_mem_r
	S += t2_t0_t0_mem0 <= t2_t0_t0

	t2_t0_t0_mem1 = S.Task('t2_t0_t0_mem1', length=1, delay_cost=1)
	t2_t0_t0_mem1 += INPUT_mem_r
	S += t2_t0_t0_mem1 <= t2_t0_t0

	t2_t0_t1_in = S.Task('t2_t0_t1_in', length=1, delay_cost=1)
	t2_t0_t1_in += alt(MUL_in)
	t2_t0_t1 = S.Task('t2_t0_t1', length=7, delay_cost=1)
	t2_t0_t1 += alt(MUL)
	S += t2_t0_t1>=t2_t0_t1_in

	t2_t0_t1_mem0 = S.Task('t2_t0_t1_mem0', length=1, delay_cost=1)
	t2_t0_t1_mem0 += INPUT_mem_r
	S += t2_t0_t1_mem0 <= t2_t0_t1

	t2_t0_t1_mem1 = S.Task('t2_t0_t1_mem1', length=1, delay_cost=1)
	t2_t0_t1_mem1 += INPUT_mem_r
	S += t2_t0_t1_mem1 <= t2_t0_t1

	t2_t0_t2 = S.Task('t2_t0_t2', length=1, delay_cost=1)
	t2_t0_t2 += alt(ADD)

	t2_t0_t2_mem0 = S.Task('t2_t0_t2_mem0', length=1, delay_cost=1)
	t2_t0_t2_mem0 += INPUT_mem_r
	S += t2_t0_t2_mem0 <= t2_t0_t2

	t2_t0_t2_mem1 = S.Task('t2_t0_t2_mem1', length=1, delay_cost=1)
	t2_t0_t2_mem1 += INPUT_mem_r
	S += t2_t0_t2_mem1 <= t2_t0_t2

	t2_t0_t3 = S.Task('t2_t0_t3', length=1, delay_cost=1)
	t2_t0_t3 += alt(ADD)

	t2_t0_t3_mem0 = S.Task('t2_t0_t3_mem0', length=1, delay_cost=1)
	t2_t0_t3_mem0 += INPUT_mem_r
	S += t2_t0_t3_mem0 <= t2_t0_t3

	t2_t0_t3_mem1 = S.Task('t2_t0_t3_mem1', length=1, delay_cost=1)
	t2_t0_t3_mem1 += INPUT_mem_r
	S += t2_t0_t3_mem1 <= t2_t0_t3

	t2_t1_t0_in = S.Task('t2_t1_t0_in', length=1, delay_cost=1)
	t2_t1_t0_in += alt(MUL_in)
	t2_t1_t0 = S.Task('t2_t1_t0', length=7, delay_cost=1)
	t2_t1_t0 += alt(MUL)
	S += t2_t1_t0>=t2_t1_t0_in

	t2_t1_t0_mem0 = S.Task('t2_t1_t0_mem0', length=1, delay_cost=1)
	t2_t1_t0_mem0 += INPUT_mem_r
	S += t2_t1_t0_mem0 <= t2_t1_t0

	t2_t1_t0_mem1 = S.Task('t2_t1_t0_mem1', length=1, delay_cost=1)
	t2_t1_t0_mem1 += INPUT_mem_r
	S += t2_t1_t0_mem1 <= t2_t1_t0

	t2_t1_t1_in = S.Task('t2_t1_t1_in', length=1, delay_cost=1)
	t2_t1_t1_in += alt(MUL_in)
	t2_t1_t1 = S.Task('t2_t1_t1', length=7, delay_cost=1)
	t2_t1_t1 += alt(MUL)
	S += t2_t1_t1>=t2_t1_t1_in

	t2_t1_t1_mem0 = S.Task('t2_t1_t1_mem0', length=1, delay_cost=1)
	t2_t1_t1_mem0 += INPUT_mem_r
	S += t2_t1_t1_mem0 <= t2_t1_t1

	t2_t1_t1_mem1 = S.Task('t2_t1_t1_mem1', length=1, delay_cost=1)
	t2_t1_t1_mem1 += INPUT_mem_r
	S += t2_t1_t1_mem1 <= t2_t1_t1

	t2_t1_t2 = S.Task('t2_t1_t2', length=1, delay_cost=1)
	t2_t1_t2 += alt(ADD)

	t2_t1_t2_mem0 = S.Task('t2_t1_t2_mem0', length=1, delay_cost=1)
	t2_t1_t2_mem0 += INPUT_mem_r
	S += t2_t1_t2_mem0 <= t2_t1_t2

	t2_t1_t2_mem1 = S.Task('t2_t1_t2_mem1', length=1, delay_cost=1)
	t2_t1_t2_mem1 += INPUT_mem_r
	S += t2_t1_t2_mem1 <= t2_t1_t2

	t2_t1_t3 = S.Task('t2_t1_t3', length=1, delay_cost=1)
	t2_t1_t3 += alt(ADD)

	t2_t1_t3_mem0 = S.Task('t2_t1_t3_mem0', length=1, delay_cost=1)
	t2_t1_t3_mem0 += INPUT_mem_r
	S += t2_t1_t3_mem0 <= t2_t1_t3

	t2_t1_t3_mem1 = S.Task('t2_t1_t3_mem1', length=1, delay_cost=1)
	t2_t1_t3_mem1 += INPUT_mem_r
	S += t2_t1_t3_mem1 <= t2_t1_t3

	t2_t20 = S.Task('t2_t20', length=1, delay_cost=1)
	t2_t20 += alt(ADD)

	t2_t20_mem0 = S.Task('t2_t20_mem0', length=1, delay_cost=1)
	t2_t20_mem0 += INPUT_mem_r
	S += t2_t20_mem0 <= t2_t20

	t2_t20_mem1 = S.Task('t2_t20_mem1', length=1, delay_cost=1)
	t2_t20_mem1 += INPUT_mem_r
	S += t2_t20_mem1 <= t2_t20

	t2_t21 = S.Task('t2_t21', length=1, delay_cost=1)
	t2_t21 += alt(ADD)

	t2_t21_mem0 = S.Task('t2_t21_mem0', length=1, delay_cost=1)
	t2_t21_mem0 += INPUT_mem_r
	S += t2_t21_mem0 <= t2_t21

	t2_t21_mem1 = S.Task('t2_t21_mem1', length=1, delay_cost=1)
	t2_t21_mem1 += INPUT_mem_r
	S += t2_t21_mem1 <= t2_t21

	t2_t30 = S.Task('t2_t30', length=1, delay_cost=1)
	t2_t30 += alt(ADD)

	t2_t30_mem0 = S.Task('t2_t30_mem0', length=1, delay_cost=1)
	t2_t30_mem0 += INPUT_mem_r
	S += t2_t30_mem0 <= t2_t30

	t2_t30_mem1 = S.Task('t2_t30_mem1', length=1, delay_cost=1)
	t2_t30_mem1 += INPUT_mem_r
	S += t2_t30_mem1 <= t2_t30

	t2_t31 = S.Task('t2_t31', length=1, delay_cost=1)
	t2_t31 += alt(ADD)

	t2_t31_mem0 = S.Task('t2_t31_mem0', length=1, delay_cost=1)
	t2_t31_mem0 += INPUT_mem_r
	S += t2_t31_mem0 <= t2_t31

	t2_t31_mem1 = S.Task('t2_t31_mem1', length=1, delay_cost=1)
	t2_t31_mem1 += INPUT_mem_r
	S += t2_t31_mem1 <= t2_t31

	t7_t0_t2 = S.Task('t7_t0_t2', length=1, delay_cost=1)
	t7_t0_t2 += alt(ADD)

	t7_t0_t2_mem0 = S.Task('t7_t0_t2_mem0', length=1, delay_cost=1)
	t7_t0_t2_mem0 += INPUT_mem_r
	S += t7_t0_t2_mem0 <= t7_t0_t2

	t7_t0_t2_mem1 = S.Task('t7_t0_t2_mem1', length=1, delay_cost=1)
	t7_t0_t2_mem1 += INPUT_mem_r
	S += t7_t0_t2_mem1 <= t7_t0_t2

	t7_t1_t2 = S.Task('t7_t1_t2', length=1, delay_cost=1)
	t7_t1_t2 += alt(ADD)

	t7_t1_t2_mem0 = S.Task('t7_t1_t2_mem0', length=1, delay_cost=1)
	t7_t1_t2_mem0 += INPUT_mem_r
	S += t7_t1_t2_mem0 <= t7_t1_t2

	t7_t1_t2_mem1 = S.Task('t7_t1_t2_mem1', length=1, delay_cost=1)
	t7_t1_t2_mem1 += INPUT_mem_r
	S += t7_t1_t2_mem1 <= t7_t1_t2

	t7_t20 = S.Task('t7_t20', length=1, delay_cost=1)
	t7_t20 += alt(ADD)

	t7_t20_mem0 = S.Task('t7_t20_mem0', length=1, delay_cost=1)
	t7_t20_mem0 += INPUT_mem_r
	S += t7_t20_mem0 <= t7_t20

	t7_t20_mem1 = S.Task('t7_t20_mem1', length=1, delay_cost=1)
	t7_t20_mem1 += INPUT_mem_r
	S += t7_t20_mem1 <= t7_t20

	t7_t21 = S.Task('t7_t21', length=1, delay_cost=1)
	t7_t21 += alt(ADD)

	t7_t21_mem0 = S.Task('t7_t21_mem0', length=1, delay_cost=1)
	t7_t21_mem0 += INPUT_mem_r
	S += t7_t21_mem0 <= t7_t21

	t7_t21_mem1 = S.Task('t7_t21_mem1', length=1, delay_cost=1)
	t7_t21_mem1 += INPUT_mem_r
	S += t7_t21_mem1 <= t7_t21

	t9_t0_t2 = S.Task('t9_t0_t2', length=1, delay_cost=1)
	t9_t0_t2 += alt(ADD)

	t9_t0_t2_mem0 = S.Task('t9_t0_t2_mem0', length=1, delay_cost=1)
	t9_t0_t2_mem0 += INPUT_mem_r
	S += t9_t0_t2_mem0 <= t9_t0_t2

	t9_t0_t2_mem1 = S.Task('t9_t0_t2_mem1', length=1, delay_cost=1)
	t9_t0_t2_mem1 += INPUT_mem_r
	S += t9_t0_t2_mem1 <= t9_t0_t2

	t9_t1_t2 = S.Task('t9_t1_t2', length=1, delay_cost=1)
	t9_t1_t2 += alt(ADD)

	t9_t1_t2_mem0 = S.Task('t9_t1_t2_mem0', length=1, delay_cost=1)
	t9_t1_t2_mem0 += INPUT_mem_r
	S += t9_t1_t2_mem0 <= t9_t1_t2

	t9_t1_t2_mem1 = S.Task('t9_t1_t2_mem1', length=1, delay_cost=1)
	t9_t1_t2_mem1 += INPUT_mem_r
	S += t9_t1_t2_mem1 <= t9_t1_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/pairing_automation_design/bls24-315/scheduling/PADD_mul1_add4/PADD_0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=True, fig_size=(cycles*0.25+3, 5), show_task_labels=False)

	return solution

