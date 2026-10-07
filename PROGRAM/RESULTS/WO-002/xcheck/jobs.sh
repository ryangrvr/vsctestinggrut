#!/bin/bash
D=/tmp/claude-0/-home-user-vsctestinggrut/1a09ed24-aca1-5a3e-824d-0bafde87a0b5/scratchpad/wo002_xcheck
cd $D
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
( python3 $D/pass1.py trap_0.06 400 ; python3 $D/pass1.py ghx4_384 400 ) > log_a.txt 2>&1 &
( python3 $D/pass1.py trap_0.08 400 ; python3 $D/pass1.py trap_0.08 200 ; python3 $D/pass1.py ghx4_96 400 dop853 ) > log_b.txt 2>&1 &
( python3 $D/pass1.py ghx4_3072 400 ; python3 $D/pass1.py ghx4_768 400 ) > log_c.txt 2>&1 &
( python3 $D/pass1.py freud_192_3072 400 ; python3 $D/pass1.py ghx4_1536 400 ; python3 $D/pass1.py ghx4_96 400 ; python3 $D/pass1.py ghx4_192 400 ) > log_d.txt 2>&1 &
wait
echo ALLDONE
