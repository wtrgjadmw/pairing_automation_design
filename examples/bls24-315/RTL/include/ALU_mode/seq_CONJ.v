case (state)
0: begin
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd11;
	ram_input_raddr2 <= `RAM_ZERO;
	state <= state + 1;
end
1: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd12;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd11;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
2: begin
	add3_opr1 <= ram_input_out1; add3_opr2 <= ram_input_out2; issub3 <= 1;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd13;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd12;
	wdata_s1 <= `ADD3;
	state <= state + 1;
end
3: begin
	add2_opr1 <= ram_input_out1; add2_opr2 <= ram_input_out2; issub2 <= 1;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd1;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd13;
	wdata_s1 <= `ADD2;
	state <= state + 1;
end
4: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd0;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd1;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
5: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd15;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd0;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
6: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 1;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd16;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd15;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
7: begin
	add2_opr1 <= ram_input_out1; add2_opr2 <= ram_input_out2; issub2 <= 1;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd14;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd16;
	wdata_s1 <= `ADD2;
	state <= state + 1;
end
8: begin
	add3_opr1 <= ram_input_out1; add3_opr2 <= ram_input_out2; issub3 <= 1;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd17;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd14;
	wdata_s1 <= `ADD3;
	state <= state + 1;
end
9: begin
	add1_opr1 <= ram_input_out1; add1_opr2 <= ram_input_out2; issub1 <= 1;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd18;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd17;
	wdata_s1 <= `ADD1;
	state <= state + 1;
end
10: begin
	add3_opr1 <= ram_input_out1; add3_opr2 <= ram_input_out2; issub3 <= 1;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd19;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd18;
	wdata_s1 <= `ADD3;
	state <= state + 1;
end
11: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 1;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd20;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd19;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
12: begin
	add1_opr1 <= ram_input_out1; add1_opr2 <= ram_input_out2; issub1 <= 1;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd21;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd20;
	wdata_s1 <= `ADD1;
	state <= state + 1;
end
13: begin
	add1_opr1 <= ram_input_out1; add1_opr2 <= ram_input_out2; issub1 <= 1;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd2;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd21;
	wdata_s1 <= `ADD1;
	state <= state + 1;
end
14: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd22;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd2;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
15: begin
	add2_opr1 <= ram_input_out1; add2_opr2 <= ram_input_out2; issub2 <= 1;
	ram_input_raddr1 <= `RAM_ZERO;
	ram_input_raddr2 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd23;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd22;
	wdata_s1 <= `ADD2;
	state <= state + 1;
end
16: begin
	add1_opr1 <= ram_input_out1; add1_opr2 <= ram_input_out2; issub1 <= 1;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd4;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd23;
	wdata_s1 <= `ADD1;
	state <= state + 1;
end
17: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd3;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd4;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
18: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd6;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd3;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
19: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd5;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd6;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
20: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd9;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd5;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
21: begin
	add0_opr1 <= ram_input_out1; add0_opr2 <= ram_input_out2; issub0 <= 0;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd7;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd9;
	wdata_s1 <= `ADD0;
	state <= state + 1;
end
22: begin
	add2_opr1 <= ram_input_out1; add2_opr2 <= ram_input_out2; issub2 <= 0;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd8;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd7;
	wdata_s1 <= `ADD2;
	state <= state + 1;
end
23: begin
	add1_opr1 <= ram_input_out1; add1_opr2 <= ram_input_out2; issub1 <= 0;
	ram_input_raddr1 <= inst_addr_opr1 + `RAM_ADDR_SIZE'd10;
	ram_input_raddr2 <= `RAM_ZERO;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd8;
	wdata_s1 <= `ADD1;
	state <= state + 1;
end
24: begin
	add3_opr1 <= ram_input_out1; add3_opr2 <= ram_input_out2; issub3 <= 0;
	w1_n_reg <= 0;
	waddr1_reg <= ret_addr + `RAM_ADDR_SIZE'd10;
	wdata_s1 <= `ADD3;
	state <= state + 1;
end
25: begin
	w1_n_reg <= 1;
	state <= 0;
end
endcase
