`define MM_RAM_DEPTH 64
`define ADD0_RAM_DEPTH 64
`define ADD1_RAM_DEPTH 64
`define ADD2_RAM_DEPTH 64
`define ADD3_RAM_DEPTH 64

`define MM_RAM_SIZE 6
`define ADD0_RAM_SIZE 6
`define ADD1_RAM_SIZE 6
`define ADD2_RAM_SIZE 6
`define ADD3_RAM_SIZE 6

`define OPR_NUM_SIZE    3  // log(5)
`define MM0     0
`define ADD0    1
`define ADD1    2
`define ADD2    3
`define ADD3    4
`define CALC_STATE_SIZE 9
`define CALC_CONJ_STATE_SIZE `CALC_STATE_SIZE'd26
`define CALC_FROB_STATE_SIZE `CALC_STATE_SIZE'd101
`define CALC_MUL_STATE_SIZE `CALC_STATE_SIZE'd241
`define CALC_PADD_STATE_SIZE `CALC_STATE_SIZE'd162
`define CALC_PDBL_STATE_SIZE `CALC_STATE_SIZE'd123
`define CALC_SPARSE_STATE_SIZE `CALC_STATE_SIZE'd172
`define CALC_SQR012345_STATE_SIZE `CALC_STATE_SIZE'd117
`define CALC_INV_STATE_SIZE `CALC_STATE_SIZE'd485
`define CALC_PMINUS_STATE_SIZE `CALC_STATE_SIZE'd162
`define CALC_MUL_CONJ_STATE_SIZE `CALC_STATE_SIZE'd241
`define CALC_SQR_STATE_SIZE `CALC_STATE_SIZE'd157