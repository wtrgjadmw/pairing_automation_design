// for wrapper -------------------------------------------------------------------------------------------------

// modes for the wrapper
`define I_INPUTMODE_SIZE    2
`define REF_RESULT                       2'd0
`define INPUT_COORD_CORE                 2'd1
`define EXEC_CORE                        2'd2
`define INPUT_CMD_CORE                   2'd3

// modes for the calculation core -------------------------------------------------------------------------------------------------
`define MODE_SIZE 'd4

// `define MODE_PDBL_FIRST 4'b0000
`define MODE_PDBL 4'b0001
`define MODE_PADD 4'b0010
`define MODE_PMINUS 4'b0011
`define MODE_SQUARE 4'b0100
`define MODE_SPARSE_MUL 4'b0101
`define MODE_CONJ 4'b0110
`define MODE_MUL 4'b0111
`define MODE_FROB 4'b1000
`define MODE_INV 4'b1001
`define MODE_MUL_CONJ 4'b1010
`define MODE_SQR012345 4'b1011

// for command buffer -----------------------------------------------------------------------------
// modes for the core 
`define CMD_SIZE   `MODE_SIZE + `RAM_ADDR_SIZE * 3

`define CMD_INSTTYPE 'd1
`define inst_ML 'b0
`define inst_FE 'b1
// for RAM -----------------------------------------------------------------------------

`define RAM_DEPTH 176
`define RAM_ADDR_SIZE 8


`define RAM_PX	    `RAM_ADDR_SIZE'd0
`define RAM_PY_	    `RAM_ADDR_SIZE'd1
`define RAM_BT00	`RAM_ADDR_SIZE'd2
`define RAM_BT01	`RAM_ADDR_SIZE'd3
`define RAM_BT10	`RAM_ADDR_SIZE'd4
`define RAM_BT11	`RAM_ADDR_SIZE'd5
`define RAM_PX_	    `RAM_ADDR_SIZE'd6
`define RAM_PY      `RAM_ADDR_SIZE'd7
`define RAM_QX00	`RAM_ADDR_SIZE'd8
`define RAM_QX01	`RAM_ADDR_SIZE'd9
`define RAM_QX10	`RAM_ADDR_SIZE'd10
`define RAM_QX11	`RAM_ADDR_SIZE'd11
`define RAM_QY00	`RAM_ADDR_SIZE'd12
`define RAM_QY01	`RAM_ADDR_SIZE'd13
`define RAM_QY10	`RAM_ADDR_SIZE'd14
`define RAM_QY11	`RAM_ADDR_SIZE'd15
`define RAM_QY_00	`RAM_ADDR_SIZE'd16
`define RAM_QY_01	`RAM_ADDR_SIZE'd17
`define RAM_QY_10	`RAM_ADDR_SIZE'd18
`define RAM_QY_11	`RAM_ADDR_SIZE'd19
`define RAM_TX00	`RAM_ADDR_SIZE'd20
`define RAM_TX01	`RAM_ADDR_SIZE'd21
`define RAM_TX10	`RAM_ADDR_SIZE'd22
`define RAM_TX11	`RAM_ADDR_SIZE'd23
`define RAM_TY00	`RAM_ADDR_SIZE'd24
`define RAM_TY01	`RAM_ADDR_SIZE'd25
`define RAM_TY10	`RAM_ADDR_SIZE'd26
`define RAM_TY11	`RAM_ADDR_SIZE'd27
`define RAM_TZ00	`RAM_ADDR_SIZE'd28
`define RAM_TZ01	`RAM_ADDR_SIZE'd29
`define RAM_TZ10	`RAM_ADDR_SIZE'd30
`define RAM_TZ11	`RAM_ADDR_SIZE'd31

`define RAM_XI100	`RAM_ADDR_SIZE'd32
`define RAM_XI101	`RAM_ADDR_SIZE'd33
`define RAM_XI110	`RAM_ADDR_SIZE'd34
`define RAM_XI111	`RAM_ADDR_SIZE'd35
`define RAM_XI200	`RAM_ADDR_SIZE'd36
`define RAM_XI201	`RAM_ADDR_SIZE'd37
`define RAM_XI210	`RAM_ADDR_SIZE'd38
`define RAM_XI211	`RAM_ADDR_SIZE'd39
`define RAM_XI300	`RAM_ADDR_SIZE'd40
`define RAM_XI301	`RAM_ADDR_SIZE'd41
`define RAM_XI310	`RAM_ADDR_SIZE'd42
`define RAM_XI311	`RAM_ADDR_SIZE'd43
`define RAM_XI400	`RAM_ADDR_SIZE'd44
`define RAM_XI401	`RAM_ADDR_SIZE'd45
`define RAM_XI410	`RAM_ADDR_SIZE'd46
`define RAM_XI411	`RAM_ADDR_SIZE'd47
`define RAM_XI500	`RAM_ADDR_SIZE'd48
`define RAM_XI501	`RAM_ADDR_SIZE'd49
`define RAM_XI510	`RAM_ADDR_SIZE'd50
`define RAM_XI511	`RAM_ADDR_SIZE'd51
`define RAM_K0	    `RAM_ADDR_SIZE'd52
`define RAM_K1	    `RAM_ADDR_SIZE'd53
`define RAM_ZERO	`RAM_ADDR_SIZE'd54
`define RAM_ONE	    `RAM_ADDR_SIZE'd55

`define RAM_A	`RAM_ADDR_SIZE'd56
`define RAM_B	`RAM_ADDR_SIZE'd80
`define RAM_C	`RAM_ADDR_SIZE'd104
`define RAM_E	`RAM_ADDR_SIZE'd128
`define RAM_F	`RAM_ADDR_SIZE'd152

// constants --------------------------------------------------------
`define WORD_SIZE 'd315
`define CHAR 315'h4c23a02b586d650d3f7498be97c5eafdec1d01aa27a1ae0421ee5da52bde5026fe802ff40300001
`define CHAR_INV 315'h66866b2867e3f8e4ecbe935ddb76276784a516bb53badfb34b4e2083df7de42702ff9ff402fffff
`define INVERSION_INITIAL_VALUE 315'h4a89339dbb88f584cdc7efb424164aee429744453d17ea32649a3243db1ec21efdb674ce8ce84a8
`define CHAR_3X 317'he46ae08209482f27be5dca3bc751c0f9c45704fe76e50a0c65cb18ef839af074fb808fdc0900003

// parameters for twisted curve (Ep4)
`define BT00 315'h0
`define BT01 315'h0
`define BT10 315'h0
`define BT11 315'h1b6aaeceed058d79360736f0e7f298b0c0557689ba60633c07d48bc3a7a974f54e6c59d5d94ec4f
// // constants independent from elliptic curve
`define ZERO 315'd0
`define ONE 315'h33dc5fd4a7929af2c08b6741683a150213e2fe55d85e51fbde11a25ad421afd9017fd00bfcfffff

// Frobenius pre-calculated coefficients
`define K0 315'h268027b827eafe1a67c8b8f84b6e191a048b47d5dae2b4999ebd1f532b4b99db7cb22dd3cd9385f
`define K1 315'h0
`define XI100 315'he9ddbd0f2a73e68ba9005fad90b4cadc9ced8f8aa1a09ccd86debe153fee68582a04bf1d715dd0
`define XI101 315'h0
`define XI110 315'h0
`define XI111 315'h0
`define XI200 315'h32a810c48f9d76996c3a6f67a5c5d9b504b962a4461a383d58dc196d24a3452ea7cc64d12c1aa4b
`define XI201 315'h0
`define XI210 315'h0
`define XI211 315'h0
`define XI300 315'h1003d602fab25291041a241d228f88d1f6f0378b9a8e85a8441a19b222472a7d40d80f0bb2fdf21
`define XI301 315'h0
`define XI310 315'h0
`define XI311 315'h0
`define XI400 315'h2c50373a9b434782eb9ae5932780a945df71cf5bbd711e8c6b295f1f72fa4358e007213f095b523
`define XI401 315'h0
`define XI410 315'h0
`define XI411 315'h0
`define XI500 315'h259552f078324ddb9c640341a1ba9cf16557ee31e3926838db9cfc2fad9f107c7c6c2174964c75a
`define XI501 315'h0
`define XI510 315'h0
`define XI511 315'h0
`define CMD_MEMDEPTH_ML 102
`define CMD_MEMSIZE_ML 7

`define CMD_MEMDEPTH_FE 353
`define CMD_MEMSIZE_FE 9

`define CMD_MEMSIZE 9
